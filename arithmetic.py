import sys
from antlr4 import *
from langLexer import langLexer
from langParser import langParser
from evalVisitor import evalVisitor

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

def interpret(input):
    lexer = langLexer(InputStream(input))
    stream = CommonTokenStream(lexer)
    parser = langParser(stream)
    tree = parser.r()
    vis = evalVisitor(parser)
    print(tree.toStringTree())
    return vis.visitR(tree)

def main(argv):
    if len(argv)>1:
        input = argv[1]
    else:
        input = sys.stdin.read()
    return interpret(input)

if __name__ == '__main__':
    main(sys.argv)