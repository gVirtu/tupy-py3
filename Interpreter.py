import sys
from antlr4 import *
from langLexer import langLexer
from langParser import langParser
from evalVisitor import evalVisitor
from CallStack import CallStack

class Interpreter(object):
    visitor = evalVisitor()
    callStack = CallStack()

    @classmethod
    def interpret(cls, input, rule="r"):
        lexer = langLexer(InputStream(input))
        stream = CommonTokenStream(lexer)
        parser = langParser(stream)
        treenode = getattr(parser, rule)
        tree = treenode()
        cls.visitor.setParser(parser)
        print(tree.toStringTree())
        print("Using rule " + rule)
        visit = getattr(cls.visitor, "visit" + rule[0].upper() + rule[1:])
        print(visit)
        return visit(tree)

    @classmethod
    def loadSymbol(cls, name):
        return cls.callStack.top().locals.get(name)

    @classmethod
    def storeSymbol(cls, name, instance):
        print("Storing "+name+" as "+str(instance))
        return cls.callStack.top().locals.put(name, instance)

def main(argv):
    if len(argv)>1:
        input = argv[1]
    else:
        input = sys.stdin.read()
    return Interpreter.interpret(input)

if __name__ == '__main__':
    main(sys.argv)