import copy
from antlr4 import *
from tupy.langLexer import langLexer
from tupy.langParser import langParser
import tupy.evalVisitor
import tupy.functionVisitor
import tupy.CallStack
import tupy.Context
import tupy.JSONPrinter
import tupy.Variable
import tupy.Instance
import tupy.Builtins
import tupy.errorHelper
import logging
import sys
import bisect

FORMAT = "=> %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
logger = logging.getLogger(__name__)

from enum import Enum
from tupy.Type import Type
from io import StringIO

class FlowEvent(Enum):
    STEP = 0
    BREAK = 1
    CONTINUE = 2
    RETURN = 3

def exception_handler(exception_type, exception, traceback, debug_hook=sys.excepthook): # pragma: no cover
    if len(exception.args) > 1:
        print("[{0}] {1} - Linha {2}".format(exception_type.__name__, exception.args[0], exception.args[1]))
    else: 
        print("[{0}] {1}".format(exception_type.__name__, exception))

class Interpreter(object):
    isDebug = False
    outStream = StringIO()
    iterationLimit = 1000
    classContextDepth = 7777777
    instContextDepth = 7777777 #9999999

    @classmethod
    def initialize(cls):
        cls.visitor = tupy.evalVisitor.evalVisitor()
        cls.callStack = tupy.CallStack.CallStack()
        cls.flow = FlowEvent.STEP
        cls.lastEvent = FlowEvent.STEP
        cls.returnData = None
        cls.outStream = StringIO()
        cls.traceOut = None
        cls.traceBars = []

    @classmethod
    def interpret(cls, input, rule="r", trace=False, printTokens=False):
        logger.debug("Input is {0}".format(str(input)))
        if (input[-1] != '\n'):
            input = input + "\n"
            print("")
        cls.outStream.close()
        cls.initialize()

        if (trace):
            cls.traceOut = tupy.JSONPrinter.JSONPrinter(input)
        if (cls.isDebug):
            logging.getLogger().setLevel(logging.DEBUG)
        else:
            sys.excepthook = exception_handler

        try:
            tupy.Builtins.initialize()
            lexer = langLexer(InputStream(input))
            lexer.removeErrorListeners()
            lexer.addErrorListener(TupyErrorListener.INSTANCE)
            stream = CommonTokenStream(lexer)

            if printTokens:
                symbolicNames = lexer.symbolicNames + ["INDENT", "DEDENT"]

                for token in lexer.getAllTokens():
                    if (token.type != Token.EOF):
                        logger.info("{0:<15} {1:>15}".format(symbolicNames[token.type], cls.format_token(token)))

                lexer = langLexer(InputStream(input))
                lexer.removeErrorListeners()
                lexer.addErrorListener(TupyErrorListener.INSTANCE)
                stream = CommonTokenStream(lexer)

            parser = langParser(stream)
            parser.removeErrorListeners()
            parser.addErrorListener(TupyErrorListener.INSTANCE)
            parser._errHandler = TupyErrorStrategy()
            #parser.setTrace(True)
            treenode = getattr(parser, rule)
            tree = treenode()
            cls.visitor.setParser(parser)
            funcscanner = tupy.functionVisitor.functionVisitor(parser, cls.callStack.top())
            logger.debug("Using rule " + rule)
            funcvisit = getattr(funcscanner, "visit" + rule[0].upper() + rule[1:])
            funcvisit(tree)
            #logger.debug(tree.toStringTree())
            visit = getattr(cls.visitor, "visit" + rule[0].upper() + rule[1:])
            #logger.debug(visit)
        
            ret_visit = visit(tree)
        except tupy.errorHelper.TupyError as e:
            cls.trace(e.args[1], exception=e.args[0])
            if (cls.traceOut is None):
                raise e
            else:
                ret = cls.traceOut.dump()
                print(ret)
                return ret

        if (cls.traceOut is None):
            return ret_visit
        else:
            ret = cls.traceOut.dump()
            print(ret)
            return ret

    @classmethod
    def executeBlock(cls, function, callArgs):
        # We evaluate all literals once beforehand, otherwise we can end up
        # making function calls twice unnecessarily if the literal has CALL trailers.
        instArgs = [literal.get() for literal in callArgs]

        (codeIndex, _depth, argumentList, returnType, isBuiltIn, isConstructor) = function.get(instArgs)
        logger.debug("codeIndex = {0}; argList = {1}; return = {2}; isBuiltin = {3}; isConstructor = {4}".format(
                codeIndex, argumentList, returnType, isBuiltIn, isConstructor))
        argNames = [a.name for a in argumentList]
        argTypes = [a.type for a in argumentList]
        argClassNames = [a.className for a in argumentList]
        argDimensions = [a.arrayDimensions for a in argumentList]
        argValues = copy.copy(callArgs)
        for a in argumentList[len(callArgs):]:
            argValues.append(a.defaultValue)

        try:
            argPassage = [ ( (cls.getDepth(argValues[ind].name), argValues[ind].trailers)
                              if (a.passByRef) else (-1, []) ) 
                                for ind, a in enumerate(argumentList) ]
        except Exception:
            # We can only access "name" in argValues above if it's a Symbol.
            # Otherwise we are thrown an Exception.
            raise SyntaxError("Referência inválida!")

        # Variadic handling
        if len(argTypes)>0 and argTypes[-1] == Type.TUPLE:
            # The last argument is just a tuple packing all the extra args
            # The fixed arguments are all the ones before it (thus we subtract 1 from len)
            fixedCount = len(argTypes)-1
            if (len(callArgs) > fixedCount):
                extraInsts = instArgs[fixedCount:]
                argValues = argValues[:fixedCount]
                memExtraArgs = [memAlloc(inst) for inst in extraInsts]
                packed = tupy.Variable.Literal(tupy.Instance.Instance(Type.TUPLE, tuple(memExtraArgs)))
                argValues.append(packed)
            else:
                # This is to prevent extraArgs from having Nones which cause
                # errors when instantiating, and come from the appending of defaultValues
                # from the argumentList. (variadic args won't have them so None ends up
                # being added to argValues)
                packed = tupy.Variable.Literal(tupy.Instance.Instance(Type.TUPLE, tuple()))
                argValues[-1] = packed
        
        finalArgs = list(zip(argNames, argTypes, argDimensions, argPassage, argClassNames, argValues))
        logger.debug("GONNA EXECUTE A CODE BLOCK {0}".format(finalArgs))
        if (isBuiltIn):
            logger.debug("CodeIndex is {0}".format(codeIndex))
            builtInFunc = getattr(tupy.Builtins, codeIndex)
            return builtInFunc(*argValues)
        else:
            codeBlock = cls.retrieveCodeTree(codeIndex)
            if (isConstructor):
                classInstance = cls.newClassInstance(function.name)
                cls.callStack.push(classInstance.value)
                cls.visitor.visitBlock(codeBlock, finalArgs, returnType, funcName="Construtor de {0}".format(function.name))
                cls.callStack.pop()
                return classInstance
            else:
                return cls.visitor.visitBlock(codeBlock, finalArgs, returnType, funcName="Função {0}".format(function.name))

    @classmethod
    def getDepth(cls, name):
        return cls.callStack.top().locals.declaredDepth[name]

    @classmethod
    def getClassContext(cls, name):
        return cls.callStack.top().classes[name]

    @classmethod
    def getClassLineage(cls, name):
        return cls.callStack.top().classLineage[name]

    @classmethod
    def areClassNamesCompatible(cls, lhs, rhs):
        return lhs in cls.getClassLineage(rhs)

    @classmethod
    def putClassContext(cls, name, context, lineage):
        cls.callStack.top().classes[name] = context
        cls.callStack.top().classLineage[name] = lineage

    @classmethod
    def isValidClass(cls, name):
        logger.debug(cls.callStack.top().classes)
        return name in cls.callStack.top().classes

    @classmethod
    def newClassInstance(cls, name):
        objContext = tupy.Context.Context(cls.instContextDepth, True, struct=name,
                                          funcName="Instância de {0}".format(name))
        try:
            classContext = cls.getClassContext(name)
            objContext.locals = copy.deepcopy(classContext.locals)
            objContext.locals.context = objContext
            logger.debug("Now my locals are {0}".format(objContext.locals))
            objContext.functions = copy.copy(classContext.functions)
            objContext.classes = copy.copy(classContext.classes)
        except KeyError as exc:
            raise NameError("Classe {0} não existe!".format(name)) from exc
        return tupy.tupy.Instance.Instance(Type.STRUCT, objContext, className=name)

    @classmethod
    def loadSymbol(cls, name):
        if cls.callStack.top().locals.hasKey(name):
            return cls.callStack.top().locals.get(name)
        else:
            raise NameError(name+" não está definido!")

    @classmethod
    def storeSymbol(cls, name, instance, trailerList):
        logger.debug("Storing "+name+" as "+str(instance)+" with trailers "+str(trailerList))
        # logger.debug("CallStack: {0}".format(cls.callStack.items))
        return cls.callStack.top().locals.put(name, instance, trailerList)

    @classmethod
    def declareSymbol(cls, name, datatype, subscriptList, className):
        logger.debug("Declaring "+name+" as "+str(datatype)+" with subscripts "+str(subscriptList))
        return cls.callStack.top().locals.declare(name, datatype, subscriptList, className)

    @classmethod
    def referenceSymbol(cls, name, memoryCell, trailerList = None):
        if (trailerList is None): trailerList = []
        if not trailerList:
            logger.debug("Setting "+name+" to reference "+str(memoryCell))
            cls.callStack.top().locals.ref(name, memoryCell)
            return True
        else:
            logger.debug("Setting {0}{1} to reference {2}".format(name, trailerList, str(memoryCell)))
            inst = cls.loadSymbol(name)
            (ret, parent_triple) = tupy.Variable.Variable.retrieveWithTrailers(inst, trailerList)
            (parent, trailer, depth) = parent_triple
            if (depth == -2): # A TT.MEMBER is referencing memoryCell
                memberDepth = parent.value.locals.declaredDepth[trailer]
                parent.value.locals.data[(trailer, memberDepth)] = memoryCell
                return True
            elif (depth == -1): # A TT.CALL is referencing memoryCell
                raise SyntaxError("Não é possível atribuir uma referência a uma chamada de função!")
            else: # A TT.SUBSCRIPT is referencing memoryCell
                if (trailer.isSingle):
                    if parent.type == Type.STRING:
                        raise SyntaxError("Não é possível atribuir uma referência a um caracter de uma string!")
                    else:
                        parent.value[trailer.begin] = memoryCell
                        return True
                else:
                    raise SyntaxError("Não é possível atribuir uma referência a um intervalo de array!")

    @classmethod
    def getDeepMemoryCell(cls, inst, trailers):
        (ret, parent_triple) = tupy.Variable.Variable.retrieveWithTrailers(inst, trailers)
        (parent, trailer, depth) = parent_triple
        if (depth == -2): # Get cell for a TT.MEMBER
            memberDepth = parent.value.locals.declaredDepth[trailer]
            return parent.value.locals.data[(trailer, memberDepth)]
        elif (depth == -1): # Get cell for a TT.CALL
            raise InvalidMemoryAccessException("<Function call>")
        else: # Get cell for a TT.SUBSCRIPT
            if (trailer.isSingle):
                if parent.type == Type.STRING:
                    raise InvalidMemoryAccessException("<Character>")
                else:
                    return parent.value[trailer.begin]
            else:
                raise InvalidMemoryAccessException("<Range-subscripted array>")

    @classmethod
    def getMemoryCell(cls, name, depth):
        return cls.callStack.top().locals.data[(name, depth)]

    @classmethod
    def retrieveCodeTree(cls, functionIndex):
        logger.debug("RETRIEVIN CODE TREE FROM CONTEXT {0}".format(cls.callStack.top().functions))
        return cls.callStack.top().functions[functionIndex]

    @classmethod
    def pushFrame(cls, returnable=False, breakable=False, returnType=None, funcName=None):
        logger.debug("Pushing frame, cloning top:\n{0}".format(str(cls.callStack.top())))
        newContext = tupy.Context.Context(cls.callStack.size(), returnable, breakable, funcName, returnType)
        newContext.inheritSymbolTable(cls.callStack.top())
        # newContext.locals.context = newContext
        cls.pushContext(newContext)

    @classmethod
    def pushContext(cls, context):
         # Code trees don't need deep copying
        context.functions = copy.copy(cls.callStack.top().functions)
        # context.refMappings = copy.copy(cls.callStack.top().refMappings)
        context.classes = copy.copy(cls.callStack.top().classes)
        context.classLineage = copy.deepcopy(cls.callStack.top().classLineage)

        cls.callStack.push(context)

    @classmethod
    def popFrame(cls):
        prev = cls.callStack.pop()
        logger.debug("Dropped context:\n{0}".format(str(prev)))

        # Only merge if dropped context is not a class context
        if (prev.structName is None):
            # logger.debug("Top before merge:\n{0}".format(str(cls.callStack.top())))
            cls.callStack.top().locals.merge(prev.locals)
            # cls.callStack.top().mergeRefMappings(prev.refMappings)
            # logger.debug("Top after merge:\n{0}".format(str(cls.callStack.top())))

        return prev

    @classmethod
    def doStep(cls):
        cls.lastEvent = cls.flow
        cls.flow = FlowEvent.STEP

    @classmethod
    def doBreak(cls):
        cls.lastEvent = cls.flow
        cls.flow = FlowEvent.BREAK

    @classmethod
    def doContinue(cls):
        cls.lastEvent = cls.flow
        cls.flow = FlowEvent.CONTINUE

    # Is true for function contexts and the global context only
    @classmethod
    def canReturn(cls):
        return cls.callStack.top().returnable

    # Is true for for/while loops, function contexts and the global context
    @classmethod
    def canBreak(cls):
        return cls.callStack.top().breakable

    @classmethod
    def getReturnType(cls):
        return cls.callStack.top().returnType

    @classmethod
    def doReturn(cls, data):
        cls.lastEvent = cls.flow
        cls.flow = FlowEvent.RETURN
        cls.returnData = data #testOrExpressionList (tuple of Instance)

    @classmethod
    def output(cls, string):
        logger.debug("STDOUT>>>>>>>>>>>>>>>>>>>>>>>>>>>{0}".format(string))
        if cls.traceOut is None:
            print(string)
        cls.outStream.write(string)
        cls.outStream.write("\n")

    @classmethod
    def trace(cls, line, returnData=None, exception=None):
        if cls.traceOut is not None:
            if (exception or cls.should_print(line)):
                cls.traceOut.trace(line, returnData, exception)

    @classmethod
    def format_token(cls, token):
        return token.text.replace('\n', '\\n').replace('\r', '\\r').replace('\t', '\\t')

    @classmethod
    def should_print(cls, line):
        if len(cls.traceBars) == 0: return True
        else: return cls.find_next_tracebar(line)%2 == len(cls.traceBars)%2

    @classmethod
    def find_next_tracebar(cls, line):
        # Find leftmost value greater than 'line' in traceBars
        # returns len(traceBars) if no match
        ind = bisect.bisect_right(cls.traceBars, line)
        return ind

# Memory access functions

class MemoryCell(object):
    def __init__(self, inst):
        self.data = inst

    def __repr__(self):
        return "■{0}".format(self.data)

class InvalidMemoryAccessException(Exception):
    pass

def memAlloc(data):
    return MemoryCell(data)

def memRead(cell):
    return cell.data

def memWrite(cell, data):
    cell.data = data

# Custom Error Listener

class TupyErrorListener(error.ErrorListener.ErrorListener):
    INSTANCE = None

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        tupy.errorHelper.parseError(msg, line)

TupyErrorListener.INSTANCE = TupyErrorListener()

# Custom Error Strategy

class TupyErrorStrategy(error.ErrorStrategy.DefaultErrorStrategy):
    def recover(self, recognizer:Parser, e:RecognitionException):
        context = recognizer._ctx
        while context is not None:
            context.exception = e
            context = context.parentCtx

        msg = "Falha inesperada de sintaxe!" if (e.message is None) else e.message
        recognizer.notifyErrorListeners(msg, recognizer.getCurrentToken(), e)

    # Make sure we don't attempt to recover inline; if the parser
    #  successfully recovers, it won't throw an exception.
    #
    def recoverInline(self, recognizer:Parser):
        self.recover(recognizer, error.Errors.InputMismatchException(recognizer))

    # Make sure we don't attempt to recover from problems in subrules.#
    def sync(self, recognizer:Parser):
        pass
        