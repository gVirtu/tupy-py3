import sys
import copy
from antlr4 import *
from langLexer import langLexer
from langParser import langParser
from evalVisitor import evalVisitor
from functionVisitor import functionVisitor
from CallStack import CallStack
from Context import Context
from enum import Enum
from Type import Type
from io import StringIO
import Variable
import Instance
import Builtins
import logging

FORMAT = "=> %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
logger = logging.getLogger(__name__)

class FlowEvent(Enum):
    STEP = 0
    BREAK = 1
    CONTINUE = 2
    RETURN = 3

class Interpreter(object):
    outStream = StringIO()
    iterationLimit = 1000
    classContextDepth = 9999999

    @classmethod
    def initialize(cls):
        cls.visitor = evalVisitor()
        cls.callStack = CallStack()
        cls.flow = FlowEvent.STEP
        cls.lastEvent = FlowEvent.STEP
        cls.returnData = None
        cls.outStream = StringIO()

    @classmethod
    def interpret(cls, input, rule="r"):
        cls.outStream.close()
        cls.initialize()
        Builtins.initialize()
        lexer = langLexer(InputStream(input))
        stream = CommonTokenStream(lexer)
        parser = langParser(stream)
        #parser.setTrace(True)
        treenode = getattr(parser, rule)
        tree = treenode()
        cls.visitor.setParser(parser)
        funcscanner = functionVisitor(parser, cls.callStack.top())
        logger.debug("Using rule " + rule)
        funcvisit = getattr(funcscanner, "visit" + rule[0].upper() + rule[1:])
        funcvisit(tree)
        #logger.debug(tree.toStringTree())
        visit = getattr(cls.visitor, "visit" + rule[0].upper() + rule[1:])
        #logger.debug(visit)
        return visit(tree)

    @classmethod
    def executeBlock(cls, function, callArgs):
        (codeIndex, argumentList, returnType, isBuiltIn, isConstructor) = function.get(callArgs)
        logger.debug("codeIndex = {0}; argList = {1}; return = {2}; isBuiltin = {3}; isConstructor = {4}".format(
                codeIndex, argumentList, returnType, isBuiltIn, isConstructor))
        argNames = [a.name for a in argumentList]
        argTypes = [a.type for a in argumentList]
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
            raise SyntaxError("Invalid reference!")

        # Variadic handling
        if len(argTypes)>0 and argTypes[-1] == Type.TUPLE:
            # The last argument is just a tuple packing all the extra args
            # The fixed arguments are all the ones before it (thus we subtract 1 from len)
            fixedCount = len(argTypes)-1
            if (len(callArgs) > fixedCount):
                extraArgs = argValues[fixedCount:]
                argValues = argValues[:fixedCount]
                memExtraArgs = [memAlloc(literal.get()) for literal in extraArgs]
                packed = Variable.Literal(Instance.Instance(Type.TUPLE, tuple(memExtraArgs)))
                argValues.append(packed)
            else:
                # This is to prevent extraArgs from having Nones which cause
                # errors when instantiating, and come from the appending of defaultValues
                # from the argumentList. (variadic args won't have them so None ends up
                # being added to argValues)
                packed = Variable.Literal(Instance.Instance(Type.TUPLE, tuple()))
                argValues[-1] = packed
        
        finalArgs = list(zip(argNames, argTypes, argDimensions, argPassage, argValues))
        logger.debug("GONNA EXECUTE A CODE BLOCK {0}".format(finalArgs))
        if (isBuiltIn):
            logger.debug("CodeIndex is {0}".format(codeIndex))
            builtInFunc = getattr(Builtins, codeIndex)
            return builtInFunc(*argValues)
        else:
            codeBlock = cls.retrieveCodeTree(codeIndex)
            if (isConstructor):
                classInstance = cls.newClassInstance(function.name)
                cls.callStack.push(classInstance.value)
                cls.visitor.visitBlock(codeBlock, finalArgs, returnType)
                cls.callStack.pop()
                return classInstance
            else:
                return cls.visitor.visitBlock(codeBlock, finalArgs, returnType)

    @classmethod
    def getDepth(cls, name):
        return cls.callStack.top().locals.declaredDepth[name]

    @classmethod
    def getClassContext(cls, name):
        return cls.callStack.top().classes[name]

    @classmethod
    def putClassContext(cls, name, context):
        cls.callStack.top().classes[name] = context;

    @classmethod
    def isValidClass(cls, name):
        logger.debug(cls.callStack.top().classes)
        return name in cls.callStack.top().classes

    @classmethod
    def newClassInstance(cls, name):
        objContext = Context(cls.classContextDepth, True, struct=name)
        try:
            classContext = cls.getClassContext(name)
            objContext.locals = copy.deepcopy(classContext.locals)
            objContext.locals.context = objContext
            logger.debug("Now my locals are {0}".format(objContext.locals))
            objContext.functions = copy.copy(classContext.functions)
            objContext.classes = copy.copy(classContext.classes)
        except e:
            raise TypeError("Class {0} does not exist!".format(name))
        return Instance.Instance(Type.STRUCT, objContext, className=name)

    @classmethod
    def loadSymbol(cls, name):
        if cls.callStack.top().locals.hasKey(name):
            return cls.callStack.top().locals.get(name)
        else:
            raise NameError(name+" is not defined!")

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
            (ret, parent_triple) = Variable.Variable.retrieveWithTrailers(inst, trailerList)
            (parent, trailer, depth) = parent_triple
            if (depth == -2): # A TT.MEMBER is referencing memoryCell
                memberDepth = parent.value.locals.declaredDepth[trailer]
                parent.value.locals.data[(trailer, memberDepth)] = memoryCell
                return True
            elif (depth == -1): # A TT.CALL is referencing memoryCell
                raise SyntaxError("Cannot assign a reference to function call!")
            else: # A TT.SUBSCRIPT is referencing memoryCell
                if (trailer.isSingle):
                    if parent.type == Type.STRING:
                        raise SyntaxError("Cannot assign a reference to a string's character!")
                    else:
                        parent.value[trailer.begin] = memoryCell
                        return True
                else:
                    raise SyntaxError("Cannot assign a reference to a range-subscripted array!")

    @classmethod
    def getDeepMemoryCell(cls, inst, trailers):
        (ret, parent_triple) = Variable.Variable.retrieveWithTrailers(inst, trailers)
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
    def clearRefs(cls, name):
         srcDepth = cls.getDepth(name)
         entry = (name, srcDepth)
         if entry in cls.callStack.top().refMappings:
            data = cls.callStack.top().refMappings[entry]
            deletionList = []
            for (ref, depth), (trailers, sourceTrailers, isReferrer) in data.items():
                if (isReferrer):
                    deletionList.append( (ref, depth) )
            
            for linkedEntry in deletionList:
                cls.callStack.top().refMappings[entry].pop(linkedEntry, None)
                if linkedEntry in cls.callStack.top().refMappings:
                    cls.callStack.top().refMappings[linkedEntry].pop(entry, None)
                     

    @classmethod
    def mapRefParam(cls, name, ref, depth, trailers, sourceTrailers = None, isReferrer = True):
        if sourceTrailers is None: sourceTrailers = []
        srcDepth = cls.getDepth(name)
        entry = (name, srcDepth)
        if entry not in cls.callStack.top().refMappings:
            cls.callStack.top().refMappings[entry] = {}

        refEntry = (ref, depth)
        refData = (trailers, sourceTrailers, isReferrer)
        cls.callStack.top().refMappings[entry][refEntry] = refData
        logger.debug("New REFMAPPING in {1}. Currently = {0}".format(str(cls.callStack.top().refMappings), str(cls.callStack.top())))

    @classmethod
    def retrieveCodeTree(cls, functionIndex):
        logger.debug("RETRIEVIN CODE TREE FROM CONTEXT {0}".format(cls.callStack.top().functions))
        return cls.callStack.top().functions[functionIndex]

    @classmethod
    def pushFrame(cls, returnable=False, breakable=False, returnType=None):
        logger.debug("Pushing frame, cloning top:\n{0}".format(str(cls.callStack.top())))
        newContext = Context(cls.callStack.size(), returnable, breakable, returnType)
        newContext.inheritSymbolTable(cls.callStack.top())
        # newContext.locals.context = newContext
        cls.pushContext(newContext)

    @classmethod
    def pushContext(cls, context):
         # Code trees don't need deep copying
        context.functions = copy.copy(cls.callStack.top().functions)
        # context.refMappings = copy.copy(cls.callStack.top().refMappings)
        context.classes = copy.copy(cls.callStack.top().classes)

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
        logger.info("STDOUT>>>>>>>>>>>>>>>>>>>>>>>>>>>{0}".format(string))
        cls.outStream.write(string)
        cls.outStream.write("\n")

# Memory access functions
# TODO: Memory Cell class
#       Garbage collection when popping context

class MemoryCell(object):
    def __init__(self, inst):
        self.data = inst

    def __repr__(self):
        return "■MEMORYCELL■" #"■{0}■".format(self.data)

class InvalidMemoryAccessException(Exception):
    pass

def memAlloc(data):
    return MemoryCell(data)

def memRead(cell):
    return cell.data

def memWrite(cell, data):
    cell.data = data

#========================

def main(argv):
    if len(argv)>1:
        input = argv[1]
    else:
        input = sys.stdin.read()
    return Interpreter.interpret(input)

if __name__ == '__main__':
    main(sys.argv)
