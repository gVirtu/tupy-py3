# Generated from arithmetic.g4 by ANTLR 4.7
from antlr4 import *
from arithmeticVisitor import arithmeticVisitor
if __name__ is not None and "." in __name__:
    from .arithmeticParser import arithmeticParser
else:
    from arithmeticParser import arithmeticParser

# This class defines a complete generic visitor for a parse tree produced by arithmeticParser.

class evalVisitor(arithmeticVisitor):

    # Visit a parse tree produced by arithmeticParser#equation.
    def visitEquation(self, ctx:arithmeticParser.EquationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by arithmeticParser#expression.
    def visitExpression(self, ctx:arithmeticParser.ExpressionContext):
        ret = self.visitChildren(ctx)
        return ret


    # Visit a parse tree produced by arithmeticParser#term.
    def visitTerm(self, ctx:arithmeticParser.TermContext):
        #if ctx.TIMES is not None:
        #    return 
        return {'ret': 3, 'retType': 'INTEGER'} #self.visitChildren(ctx)


    # Visit a parse tree produced by arithmeticParser#factor.
    def visitFactor(self, ctx:arithmeticParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by arithmeticParser#atom.
    def visitAtom(self, ctx:arithmeticParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by arithmeticParser#scientific.
    def visitScientific(self, ctx:arithmeticParser.ScientificContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by arithmeticParser#relop.
    def visitRelop(self, ctx:arithmeticParser.RelopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by arithmeticParser#number.
    def visitNumber(self, ctx:arithmeticParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by arithmeticParser#variable.
    def visitVariable(self, ctx:arithmeticParser.VariableContext):
        return self.visitChildren(ctx)



del arithmeticParser