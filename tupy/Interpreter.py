import copy
from antlr4 import *
from tupy.langLexer import langLexer
from tupy.langParser import langParser
import tupy.evalVisitor
import tupy.functionVisitor
import tupy.CallStack
import tupy.Stack
import tupy.Context
import tupy.JSONPrinter
import tupy.Variable
import tupy.Instance
import tupy.Builtins
import tupy.errorHelper
import logging
import sys
import bisect
import io

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
        cls.inStream = sys.stdin
        cls.bufferedLine = ""
        cls.bufferedLineTokens = []
        cls.bufferedLineIndices = []
        cls.outStream = StringIO()
        cls.traceOut = None
        cls.traceBars = []
        cls.singleTraceSkip = False

    @classmethod
    def interpret(cls, input, rule="r", trace=False, printTokens=False, stdin=None):
        logger.debug("Input is {0}".format(str(input)))
        if (input[-1] != '\n'):
            input = input + "\n"
            print("")
        cls.outStream.close()
        cls.initialize()

        if (isinstance(stdin, str)):
            cls.inStream = io.StringIO(stdin)

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
    def executeBlock(cls, function, callArgs, classContextsPushed):
        # Make sure we will perform the evaluations within the correct context
        # Example scenario that would break without this:
        #   tipo Teste:
        #       Func(inteiro x):
        #           <...>
        #
        #   Teste T <- Teste()
        #
        #   Helper(inteiro a):
        #       T.Func(a)       <<- this line would push T's context to the top,
        #                           in which we don't know what is 'a'

        stackBuffer = tupy.Stack.Stack()
        for _ in range(classContextsPushed):
            stackBuffer.push(cls.callStack.pop())

        # We evaluate all literals once beforehand, otherwise we can end up
        # making function calls twice unnecessarily if the literal has CALL trailers.
        instArgs = [literal.get() for literal in callArgs]

        for _ in range(classContextsPushed):
            cls.callStack.push(stackBuffer.pop())

        (codeIndex, _depth, argumentList, returnType, isBuiltIn, isConstructor) = function.get(instArgs)
        logger.debug("codeIndex = {0}; argList = {1}; return = {2}; isBuiltin = {3}; isConstructor = {4}".format(
                codeIndex, argumentList, returnType, isBuiltIn, isConstructor))
        argNames = [a.name for a in argumentList]
        argTypes = [a.type for a in argumentList]
        if len(argTypes)>0 and argTypes[-1] == Type.TUPLE:
            isVariadic = True
            # The last argument is just a tuple packing all the extra args
            # The fixed arguments are all the ones before it (thus we subtract 1 from len)
            fixedCount = len(argTypes)-1
        else:
            isVariadic = False
            fixedCount = len(argTypes)

        argClassNames = [a.className for a in argumentList]
        argIsInvisible = [a.invisible for a in argumentList]
        argDimensions = [a.arrayDimensions for a in argumentList]
        argValues = copy.copy(instArgs)
        try:
            argPassage = [ ((cls.getDepth(a.name), a.name, a.trailers)
                              if (argumentList[ind].passByRef) else (-1, "", []) ) 
                              for ind, a in enumerate(callArgs[:fixedCount]) ]

            for a in argumentList[len(callArgs):fixedCount]:
                argValues.append(a.defaultValue.get())
                argPassage.append((cls.getDepth(a.defaultValue.name), a.defaultValue.name, a.defaultValue.trailers)
                                  if (a.passByRef) else (-1, "", []) )

        except AttributeError as e:
            # We can only access "name" in argValues above if it's a Symbol.
            # Otherwise we are thrown an Exception.
            raise SyntaxError("Referência inválida!")

        # Validations

        for i, inst in enumerate(argValues[:fixedCount]):
            if inst.array_dimensions != argDimensions[i]:
                if argDimensions[i] == 0:
                    raise TypeError("A função {0} não esperava uma lista como argumento!".format(function.name))
                elif inst.roottype == Type.ARRAY:
                    inst.array_dimensions = argDimensions[i]
                else:
                    raise TypeError("A função {0} esperava uma lista de {1} dimensões!".format(function.name, argDimensions[i]))

            if inst.type == Type.STRUCT: # then inst.value contains a Context
                if not tupy.Interpreter.Interpreter.areClassNamesCompatible(argClassNames[i], inst.value.structName):
                    raise TypeError("A função {0} esperava um objeto do tipo {1} como argumento! (Foi passado {2})".format(function.name, argClassNames[i], inst.value.structName))

        # Variadic handling
        if isVariadic:
            # Currently argPassage only goes up to fixedCount
            # This append is to prevent it from limiting the finalArgs zip
            argPassage.append( (-1, "", []) )

            if (len(callArgs) > fixedCount):
                argValues = argValues[:fixedCount]
                # Pass by value (evaluated args in tuple)
                if not argumentList[-1].passByRef:
                    extraInsts = instArgs[fixedCount:]
                # Pass by reference
                else:
                    symbols = callArgs[fixedCount:]
                    if not all([isinstance(symbol, tupy.Variable.Symbol) for symbol in symbols]):
                        raise SyntaxError("Referência inválida!")
                    extraInsts = [tupy.Instance.Instance(Type.REFERENCE, symbol) 
                                    for symbol in symbols]
                memExtraArgs = [memAlloc(inst) for inst in extraInsts]
                packed = tupy.Instance.Instance(Type.TUPLE, tuple(memExtraArgs))
            else:
                # This is to prevent extraArgs from having Nones which cause
                # errors when instantiating, and come from the appending of defaultValues
                # from the argumentList. (variadic args won't have them so None ends up
                # being added to argValues)
                packed = tupy.Instance.Instance(Type.TUPLE, tuple())
            
            argValues.append(packed)
        
        finalArgs = list(zip(argNames, argTypes, argDimensions, argPassage, argIsInvisible, argClassNames, argValues))
        logger.debug("GONNA EXECUTE A CODE BLOCK {0}".format(finalArgs))
        if (isBuiltIn):
            logger.debug("CodeIndex is {0}".format(codeIndex))
            builtInFunc = getattr(tupy.Builtins, codeIndex)
            passValues = [argValues[i] if argPassage[i][0] == -1 \
                                       else tupy.Instance.Instance(Type.REFERENCE, callArgs[i]) \
                                       for i in range(len(argValues))]
            return builtInFunc(*passValues)
        else:
            codeBlock = cls.retrieveCodeTree(codeIndex)
            if (isConstructor):
                classInstance = cls.newClassInstance(function.name)
                cls.callStack.push(classInstance.value)
                cls.visitor.visitBlock(codeBlock, finalArgs, returnType, funcName="Construtor de {0}".format(function.name))
                cls.callStack.pop()
                logger.debug("Constructed {0}".format(classInstance))
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
        return cls.callStack.top().classLineage.get(name, [])

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
            #objContext.locals = copy.deepcopy(classContext.locals)
            objContext.inheritSymbolTable(classContext)
            # Class attributes need to be copied otherwise all instances will share the same data
            for (local_name, depth) in objContext.locals.data.keys():
                if (depth == cls.classContextDepth and objContext.locals.datatype[local_name] != Type.FUNCTION):
                    classAttribute = copy.deepcopy(objContext.locals.data[(local_name, depth)])
                    objContext.locals.data[(local_name, depth)] = classAttribute
            #objContext.locals.context = objContext
            logger.debug("Now my locals are {0}".format(objContext.locals.print_all_locals()))
            objContext.functions = copy.copy(classContext.functions)
            objContext.classes = copy.copy(classContext.classes)
            objContext.classLineage = copy.deepcopy(classContext.classLineage)
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
    def declareSymbol(cls, name, datatype, subscriptList, className, isInvisible):
        logger.debug("Declaring "+name+" as "+str(datatype)+" with subscripts "+str(subscriptList))
        return cls.callStack.top().locals.declare(name, datatype, subscriptList, className, isInvisible)

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
        logger.debug("RETRIEVIN CODE TREE {0} FROM CONTEXT {1}".format(functionIndex, cls.callStack.top().functions))
        return cls.callStack.top().functions[functionIndex]

    @classmethod
    def pushFrame(cls, returnable=False, breakable=False, returnType=None, funcName=None):
        logger.debug("Pushing frame, cloning top:\n{0}".format(str(cls.callStack.top())))
        newContext = tupy.Context.Context(cls.callStack.size(), returnable, breakable, funcName, returnType)
        # newContext.locals.context = newContext
        cls.pushContext(newContext)

    @classmethod
    def pushContext(cls, context):
         # Code trees don't need deep copying
        context.functions = copy.copy(cls.callStack.top().functions)
        context.inheritSymbolTable(cls.callStack.top())
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
    def inputSingle(cls):
        if not len(cls.bufferedLineTokens):
            cls.bufferLine()
        cls.bufferedLineIndices.pop()
        if not len(cls.bufferedLineIndices):
            cls.bufferedLine = ""
        return cls.bufferedLineTokens.pop()

    @classmethod
    def inputLine(cls):
        if not len(cls.bufferedLine):
            cls.bufferLine()
        sliceStart = 0
        if len(cls.bufferedLineIndices):
            sliceStart = cls.bufferedLineIndices.pop()
        ret = cls.bufferedLine[sliceStart:]
        cls.bufferedLine = ""
        cls.bufferedLineTokens = []
        cls.bufferedLineIndices = []
        return ret

    @classmethod
    def bufferLine(cls):
        cls.bufferedLine = cls.inStream.readline()
        lineTokens = cls.bufferedLine.split()
        lineIndices = []
        sliceStart = 0
        for token in lineTokens:
            sliceStart = cls.bufferedLine.find(token, sliceStart)
            lineIndices.append(sliceStart)
            sliceStart = sliceStart + 1
        cls.bufferedLineIndices = list(reversed(lineIndices))
        cls.bufferedLineTokens = list(reversed(lineTokens)) # make popping easier

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
        if cls.singleTraceSkip: return False
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
    def __init__(self, inst, invisible):
        self.data = inst
        self.invisible = invisible

    def __repr__(self):
        return "■{0}".format(self.data)

class InvalidMemoryAccessException(Exception):
    pass

def memAlloc(data, invisible=False):
    return MemoryCell(data, invisible)

def memRealloc(cell, data, invisible=False):
    cell.data = data
    cell.invisible = invisible

def memRead(cell):
    return cell.data

def memWrite(cell, data):
    cell.data.type = data.type #Specifically for NULL -> TYPE
    cell.data.value = data.value
    cell.data.update_size()

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
        