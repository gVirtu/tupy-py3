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
import Variable
import Instance

class FlowEvent(Enum):
    STEP = 0
    BREAK = 1
    CONTINUE = 2
    RETURN = 3

class Interpreter(object):
    visitor = evalVisitor()
    callStack = CallStack()
    flow = FlowEvent.STEP
    lastEvent = FlowEvent.STEP
    returnData = None

    @classmethod
    def interpret(cls, input, rule="r"):
        cls.callStack = CallStack()
        lexer = langLexer(InputStream(input))
        stream = CommonTokenStream(lexer)
        parser = langParser(stream)
        treenode = getattr(parser, rule)
        tree = treenode()
        cls.visitor = evalVisitor()
        cls.visitor.setParser(parser)
        funcscanner = functionVisitor(parser)
        print("Using rule " + rule)
        funcvisit = getattr(funcscanner, "visit" + rule[0].upper() + rule[1:])
        funcvisit(tree)
        #print(tree.toStringTree())
        visit = getattr(cls.visitor, "visit" + rule[0].upper() + rule[1:])
        #print(visit)
        return visit(tree)

    @classmethod
    def executeBlock(cls, function, callArgs):
        (codeIndex, argumentList, returnType) = function.get(callArgs)
        print("codeIndex = {0}; argList = {1}; return = {2}".format(codeIndex, argumentList, returnType))
        codeBlock = cls.retrieveCodeTree(codeIndex)
        argNames = [a.name for a in argumentList]
        argTypes = [a.type for a in argumentList]
        argValues = copy.copy(callArgs)
        for a in argumentList[len(callArgs):]:
            argValues.append(a.defaultValue)

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
        
        finalArgs = list(zip(argNames, argTypes, argValues))
        print("GONNA EXECUTE A CODE BLOCK {0}".format(finalArgs))
        return cls.visitor.visitBlock(codeBlock, finalArgs)

    @classmethod
    def loadSymbol(cls, name):
        if cls.callStack.top().locals.hasKey(name):
            return cls.callStack.top().locals.get(name)
        else:
            raise NameError(name+" is not defined!")

    @classmethod
    def storeSymbol(cls, name, instance, trailerList):
        print("Storing "+name+" as "+str(instance)+" with trailers "+str(trailerList))
        return cls.callStack.top().locals.put(name, instance, trailerList)

    @classmethod
    def declareSymbol(cls, name, datatype, subscriptList):
        print("Declaring "+name+" as "+str(datatype)+" with subscripts "+str(subscriptList))
        return cls.callStack.top().locals.declare(name, datatype, subscriptList)

    @classmethod
    def defineFunction(cls, name, returntype, argumentList, codeTree):
        print("Declaring function "+name+" that returns "+str(returntype)+" with arguments "+str(argumentList))
        return cls.callStack.top().locals.defineFunction(name, returntype, argumentList, codeTree)

    @classmethod
    def registerCodeTree(cls, codeTree):
        funcIndex = len(cls.callStack.top().functions)
        cls.callStack.top().functions.append(codeTree)
        return funcIndex

    @classmethod
    def retrieveCodeTree(cls, functionIndex):
        return cls.callStack.top().functions[functionIndex]

    @classmethod
    def pushFrame(cls, returnable=False):
        print("Pushing frame, cloning top:\n{0}".format(str(cls.callStack.top())))
        newContext = Context(cls.callStack.size(), returnable)
        #import pdb; pdb.set_trace()
        # hack: Deepcopy would leak to the Context reference
        cls.callStack.top().locals.context = None 
        newContext.locals = copy.deepcopy(cls.callStack.top().locals)
        cls.callStack.top().locals.context = cls.callStack.top()

        newContext.locals.context = newContext
        # Code trees don't need deep copying
        newContext.functions = copy.copy(cls.callStack.top().functions)
        cls.callStack.push(newContext)

    @classmethod
    def popFrame(cls):
        prev = cls.callStack.pop()
        print("Dropped context:\n{0}".format(str(prev)))
        print("Top before merge:\n{0}".format(str(cls.callStack.top())))
        cls.callStack.top().locals.merge(prev.locals)
        print("Top after merge:\n{0}".format(str(cls.callStack.top())))
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

    @classmethod
    def doReturn(cls, data):
        cls.lastEvent = cls.flow
        cls.flow = FlowEvent.RETURN
        cls.returnData = data #testOrExpressionList (tuple of Instance)


def main(argv):
    if len(argv)>1:
        input = argv[1]
    else:
        input = sys.stdin.read()
    return Interpreter.interpret(input)

if __name__ == '__main__':
    main(sys.argv)