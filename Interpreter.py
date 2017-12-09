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

class FlowEvent(Enum):
    STEP = 0
    BREAK = 1
    CONTINUE = 2
    RETURN = 3

class Interpreter(object):
    outStream = StringIO()
    iterationLimit = 1000

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
        treenode = getattr(parser, rule)
        tree = treenode()
        cls.visitor.setParser(parser)
        funcscanner = functionVisitor(parser, cls.callStack.top())
        print("Using rule " + rule)
        funcvisit = getattr(funcscanner, "visit" + rule[0].upper() + rule[1:])
        funcvisit(tree)
        #print(tree.toStringTree())
        visit = getattr(cls.visitor, "visit" + rule[0].upper() + rule[1:])
        #print(visit)
        return visit(tree)

    @classmethod
    def executeBlock(cls, function, callArgs):
        (codeIndex, argumentList, returnType, isBuiltIn, isConstructor) = function.get(callArgs)
        print("codeIndex = {0}; argList = {1}; return = {2}; isBuiltin = {3}; isConstructor = {4}".format(
                codeIndex, argumentList, returnType, isBuiltIn, isConstructor))
        argNames = [a.name for a in argumentList]
        argTypes = [a.type for a in argumentList]
        argDimensions = [a.arrayDimensions for a in argumentList]
        argValues = copy.copy(callArgs)
        for a in argumentList[len(callArgs):]:
            argValues.append(a.defaultValue)

        try:
            argPassage = [ ( cls.getDepth(argValues[ind].name) if (a.passByRef) else -1 ) 
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
                packed = Variable.Literal(Instance.Instance(Type.TUPLE, tuple(extraArgs)))
                argValues.append(packed)
            else:
                # This is to prevent extraArgs from having Nones which cause
                # errors when instantiating, and come from the appending of defaultValues
                # from the argumentList. (variadic args won't have them so None ends up
                # being added to argValues)
                packed = Variable.Literal(Instance.Instance(Type.TUPLE, tuple()))
                argValues[-1] = packed
        
        finalArgs = list(zip(argNames, argTypes, argDimensions, argPassage, argValues))
        print("GONNA EXECUTE A CODE BLOCK {0}".format(finalArgs))
        if (isBuiltIn):
            print("CodeIndex is {0}".format(codeIndex))
            builtInFunc = getattr(Builtins, codeIndex)
            return builtInFunc(*argValues)
        else:
            codeBlock = cls.retrieveCodeTree(codeIndex)
            if (isConstructor):
                classInstance = cls.newClassInstance(function.name)
                cls.callStack.push(classInstance.value)
                cls.visitor.visitBlock(codeBlock, finalArgs, returnType)
                cls.callStack.pop()
                return classInstance;
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
        print(cls.callStack.top().classes)
        return name in cls.callStack.top().classes

    @classmethod
    def newClassInstance(cls, name):
        objContext = Context(0, True, struct=name)
        try:
            classContext = cls.getClassContext(name)
            objContext.locals = copy.deepcopy(classContext.locals)
            objContext.locals.context = objContext
            print("Now my locals are {0}".format(objContext.locals))
            objContext.functions = copy.copy(classContext.functions)
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
    def storeSymbol(cls, name, instance, trailerList, isReference=False):
        print("Storing "+name+" as "+str(instance)+" with trailers "+str(trailerList))
        return cls.callStack.top().locals.put(name, instance, trailerList, isReference)

    @classmethod
    def declareSymbol(cls, name, datatype, subscriptList, className):
        print("Declaring "+name+" as "+str(datatype)+" with subscripts "+str(subscriptList))
        return cls.callStack.top().locals.declare(name, datatype, subscriptList, className)

    @classmethod
    def mapRefParam(cls, name, ref, depth):
        cls.callStack.top().refMappings[name] = (ref, depth)

    @classmethod
    def retrieveCodeTree(cls, functionIndex):
        print("RETRIEVIN CODE TREE FROM CONTEXT {0}".format(cls.callStack.top().functions))
        return cls.callStack.top().functions[functionIndex]

    @classmethod
    def pushFrame(cls, returnable=False, breakable=False, returnType=None):
        print("Pushing frame, cloning top:\n{0}".format(str(cls.callStack.top())))
        newContext = Context(cls.callStack.size(), returnable, breakable, returnType)
        newContext.inheritSymbolTable(cls.callStack.top())
        # newContext.locals.context = newContext
        cls.pushContext(newContext)

    @classmethod
    def pushContext(cls, context):
         # Code trees don't need deep copying
        context.functions = copy.copy(cls.callStack.top().functions)
        context.classes = copy.copy(cls.callStack.top().classes)

        cls.callStack.push(context)

    @classmethod
    def popFrame(cls):
        prev = cls.callStack.pop()
        print("Dropped context:\n{0}".format(str(prev)))

        # Only merge if dropped context is not a class context
        if (prev.structName is None):
            print("Top before merge:\n{0}".format(str(cls.callStack.top())))
            cls.callStack.top().locals.merge(prev.locals)
            print("Top after merge:\n{0}".format(str(cls.callStack.top())))
        # Iterate through mapped pass-by-reference symbol names
        # and hand over their values to their referenced symbols
        #for name, ref in prev.refMappings.items():
        #    print("REFMAPPING {0} TO {1}...".format(name, ref))
        #    inst = prev.locals.get(name)
        #    cls.callStack.top().locals.put(ref, inst, [])

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
        print(string)
        cls.outStream.write(string)
        cls.outStream.write("\n")


def main(argv):
    if len(argv)>1:
        input = argv[1]
    else:
        input = sys.stdin.read()
    return Interpreter.interpret(input)

if __name__ == '__main__':
    main(sys.argv)
