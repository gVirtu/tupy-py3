import sys
import copy
from antlr4 import *
from langLexer import langLexer
from langParser import langParser
from evalVisitor import evalVisitor
from CallStack import CallStack
from Context import Context

class Interpreter(object):
    visitor = evalVisitor()
    callStack = CallStack()

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
        #print(tree.toStringTree())
        print("Using rule " + rule)
        visit = getattr(cls.visitor, "visit" + rule[0].upper() + rule[1:])
        #print(visit)
        return visit(tree)

    @classmethod
    def loadSymbol(cls, name):
        if cls.callStack.top().locals.hasKey(name):
            return cls.callStack.top().locals.get(name)
        else:
            raise NameError(name+" is not defined!")

    @classmethod
    def storeSymbol(cls, name, instance, trailerList):
        print("Storing "+name+" as "+str(instance))
        return cls.callStack.top().locals.put(name, instance, trailerList)

    @classmethod
    def declareSymbol(cls, name, datatype, subscriptList):
        print("Declaring "+name+" as "+str(datatype))
        return cls.callStack.top().locals.declare(name, datatype, subscriptList)

    @classmethod
    def pushFrame(cls):
        newContext = copy.deepcopy(cls.callStack.top())
        newContext.setDepth(cls.callStack.size())
        cls.callStack.push(newContext)

    @classmethod
    def popFrame(cls):
        prev = cls.callStack.pop()
        print("Dropped context:\n{0}".format(str(prev)))
        print("Top before:\n{0}".format(str(cls.callStack.top())))
        cls.callStack.top().locals.merge(prev.locals)
        print("Top after:\n{0}".format(str(cls.callStack.top())))
        return prev

def main(argv):
    if len(argv)>1:
        input = argv[1]
    else:
        input = sys.stdin.read()
    return Interpreter.interpret(input)

if __name__ == '__main__':
    main(sys.argv)