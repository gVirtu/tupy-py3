import sys
from antlr4 import InputStream, CommonTokenStream
from langLexer import langLexer
from langParser import langParser
from evalVisitor import evalVisitor
from pprint import pprint

'''def handleExpression(expr): 
    adding = True
    value = 0
    for child in expr.getChildren():
        if isinstance(child, TerminalNode):
            adding = child.getText() == "+"
        else:
            multValue = handleMultiply(child)
            if adding:
                value += multValue
            else:
                value -= multValue
    print("Parsed expression %s has value %s" % (expr.getText(), value))

def handleMultiply(expr):
    multiplying = True
    value = 1
    for child in expr.getChildren():
        if isinstance(child, TerminalNode):
            multiplying = child.getText() == "*"
        else:
            if multiplying:
                value *= int(child.getText())
            else:
                value /= int(child.getText())
    return value'''

class Framework():
    def __init__(self):
        self.istream = InputStream("123456\n")
        self.lexer = langLexer(self.istream)
        self.tstream = CommonTokenStream(self.lexer)
        self.parser = langParser(self.tstream)
        self.parser.setTrace(True)
        self.vis = evalVisitor(self.parser)
        tree = self.parser.statement()
        self.vis.visitStatement(tree)

    def interpret(self, inputString):
        self.istream.strdata = inputString
        self.istream._loadString()
        print("Input:")
        print(self.istream)
        self.lexer.tokens = []
        self.lexer.indents = []
        self.lexer.opened = 0
        self.lexer.lastToken = None
        self.lexer.reset()

        for t in self.lexer.getAllTokens():
            print(t)

        self.tstream.reset()
        self.parser.reset()
        self.parser._input = self.tstream

        tree = self.parser.statement()
        print("Tree Print:")
        print(vars(tree))
        print(tree.toStringTree())
        return self.vis.visitStatement(tree)

def main(argv):
    '''if len(argv)>1:
        input = argv[1]
    else:
        input = sys.stdin.read() '''
    a = Framework()
    for line in sys.stdin:
        print(a.interpret(line))

if __name__ == '__main__':
    main(sys.argv)