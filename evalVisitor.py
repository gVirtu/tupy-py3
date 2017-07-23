# Generated from lang.g4 by ANTLR 4.7
from Instance import Instance, Type

from antlr4 import *
if __name__ is not None and "." in __name__:
    from .langParser import langParser
else:
    from langParser import langParser

from errorHelper import error

# This class defines a complete generic visitor for a parse tree produced by langParser.

symbolTable = {}
callStack = []


class evalVisitor(ParseTreeVisitor):

    def __init__(self, parser):
        self.parser = parser

    # Visit a parse tree produced by langParser#r.
    def visitR(self, ctx:langParser.RContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:langParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#parameters.
    def visitParameters(self, ctx:langParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#typedArgsList.
    def visitTypedArgsList(self, ctx:langParser.TypedArgsListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#typedFunctionParam.
    def visitTypedFunctionParam(self, ctx:langParser.TypedFunctionParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#paramPassage.
    def visitParamPassage(self, ctx:langParser.ParamPassageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#importStatement.
    def visitImportStatement(self, ctx:langParser.ImportStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#statement.
    def visitStatement(self, ctx:langParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#simpleStatement.
    def visitSimpleStatement(self, ctx:langParser.SimpleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#smallStatement.
    def visitSmallStatement(self, ctx:langParser.SmallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#declarationStatement.
    def visitDeclarationStatement(self, ctx:langParser.DeclarationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#dataType.
    def visitDataType(self, ctx:langParser.DataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#testOrExpressionStatement.
    def visitTestOrExpressionStatement(self, ctx:langParser.TestOrExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#expressionList.
    def visitExpressionList(self, ctx:langParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#testOrExpression.
    def visitTestOrExpression(self, ctx:langParser.TestOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#enumSpecifier.
    def visitEnumSpecifier(self, ctx:langParser.EnumSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#enumeratorList.
    def visitEnumeratorList(self, ctx:langParser.EnumeratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#enumerator.
    def visitEnumerator(self, ctx:langParser.EnumeratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#flowStatement.
    def visitFlowStatement(self, ctx:langParser.FlowStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#breakStatement.
    def visitBreakStatement(self, ctx:langParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#continueStatement.
    def visitContinueStatement(self, ctx:langParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#returnStatement.
    def visitReturnStatement(self, ctx:langParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#nameList.
    def visitNameList(self, ctx:langParser.NameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#compoundStatement.
    def visitCompoundStatement(self, ctx:langParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#ifStatement.
    def visitIfStatement(self, ctx:langParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#whileStatement.
    def visitWhileStatement(self, ctx:langParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#forStatement.
    def visitForStatement(self, ctx:langParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#block.
    def visitBlock(self, ctx:langParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#test.
    def visitTest(self, ctx:langParser.TestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#orTest.
    def visitOrTest(self, ctx:langParser.OrTestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#andTest.
    def visitAndTest(self, ctx:langParser.AndTestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#notTest.
    def visitNotTest(self, ctx:langParser.NotTestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#comparison.
    def visitComparison(self, ctx:langParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#comparisonOperator.
    def visitComparisonOperator(self, ctx:langParser.ComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#loopRange.
    def visitLoopRange(self, ctx:langParser.LoopRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#rangeDelimiter.
    def visitRangeDelimiter(self, ctx:langParser.RangeDelimiterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#rangeList.
    def visitRangeList(self, ctx:langParser.RangeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#expression.
    def visitExpression(self, ctx:langParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#xorExpression.
    def visitXorExpression(self, ctx:langParser.XorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#andExpression.
    def visitAndExpression(self, ctx:langParser.AndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#shiftExpression.
    def visitShiftExpression(self, ctx:langParser.ShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#arithmeticExpression.
    def visitArithmeticExpression(self, ctx:langParser.ArithmeticExpressionContext):
        res = self.visitTerm(ctx.term(0))
        typ = res.type
        op = 0
        i_children = iter(ctx.getChildren())
        next(i_children) # all except first factor
        for c in i_children:
            if isinstance(c, TerminalNode): 
                op = c.getSymbol().type
            else:
                rhs = self.visitTerm(c)
                typ = self.resultType(c, typ, rhs.type)
                if op == self.parser.ADD:
                    if typ == Type.STRING:
                        res.value = self.stringConcat(res, rhs)
                    else:
                        res.value = res.value + rhs.value
                elif op == self.parser.MINUS:
                    res.value = res.value - rhs.value
        return Instance(typ, res.value)


    # Visit a parse tree produced by langParser#term.
    def visitTerm(self, ctx:langParser.TermContext):
        res = self.visitFactor(ctx.factor(0))
        typ = res.type
        op = 0
        i_children = iter(ctx.getChildren())
        next(i_children) # all except first factor
        for c in i_children:
            if isinstance(c, TerminalNode): 
                op = c.getSymbol().type
            else:
                rhs = self.visitFactor(c)
                typ = self.resultType(c, typ, rhs.type)
                if op == self.parser.STAR:
                    res.value = res.value * rhs.value
                elif op == self.parser.DIV:
                    res.value = res.value / rhs.value
                elif op == self.parser.MOD:
                    res.value = res.value % rhs.value
                elif op == self.parser.IDIV:
                    res.value = res.value // rhs.value
        return Instance(typ, res.value)


    # Visit a parse tree produced by langParser#factor.
    def visitFactor(self, ctx:langParser.FactorContext):
        if ctx.ADD() is not None:
            f = self.visitFactor(ctx.factor())
            return Instance(f.type, +f.value)
        elif ctx.MINUS() is not None:
            f = self.visitFactor(ctx.factor())
            return Instance(f.type, -f.value)
        elif ctx.NOT_OP() is not None:
            f = self.visitFactor(ctx.factor())
            if (f is not None and f.type != Type.INT): 
                error(TypeError, "Invalid type!", ctx.factor())
                # raise TypeError("Invalid type! Line: {0}".format(ctx.factor().start.line))
            return Instance(Type.INT, ~f.value)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#power.
    def visitPower(self, ctx:langParser.PowerContext):
        if ctx.POWER() is not None:
            at = self.visitAtom(ctx.atom())
            rhs = self.visitFactor(ctx.factor())
            typ = self.resultType(ctx.factor(), at.type, rhs.type)
            return Instance(typ, at.value ** rhs.value)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#atom.
    def visitAtom(self, ctx:langParser.AtomContext):
        if ctx.TRUE() is not None:
            return Instance(Type.BOOL, True);
        elif ctx.FALSE() is not None:
            return Instance(Type.BOOL, False);
        elif ctx.NULL() is not None:
            return Instance(Type.NULL, 0);
        else:
            return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#trailerArgs.
    def visitTrailerArgs(self, ctx:langParser.TrailerArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#trailerSubs.
    def visitTrailerSubs(self, ctx:langParser.TrailerSubsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#trailerDot.
    def visitTrailerDot(self, ctx:langParser.TrailerDotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#subscriptList.
    def visitSubscriptList(self, ctx:langParser.SubscriptListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#subscript.
    def visitSubscript(self, ctx:langParser.SubscriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#testOrExpressionList.
    def visitTestOrExpressionList(self, ctx:langParser.TestOrExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#classDefinition.
    def visitClassDefinition(self, ctx:langParser.ClassDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#argList.
    def visitArgList(self, ctx:langParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#argument.
    def visitArgument(self, ctx:langParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#string.
    def visitString(self, ctx:langParser.StringContext):
        return Instance(Type.STRING, str(self.visitChildren(ctx)))


    # Visit a parse tree produced by langParser#character.
    def visitCharacter(self, ctx:langParser.StringContext):
        return Instance(Type.CHAR, ord(self.visitChildren(ctx)))


    # Visit a parse tree produced by langParser#number.
    def visitNumber(self, ctx:langParser.NumberContext):
        if ctx.integer() is None:
            return Instance(Type.FLOAT, float(self.visitChildren(ctx)))
        else:
            return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#integer.
    def visitInteger(self, ctx:langParser.IntegerContext):
        return Instance(Type.INT, int(self.visitChildren(ctx)))


    def visitTerminal(self, node):
        # print("Got to terminal "+str(node))
        return str(node)


    def aggregateResult(self, aggregate, nextResult):
        #print("Aggregating "+str(aggregate)+" and "+str(nextResult))
        if aggregate is not None:
            res = aggregate + nextResult
        else:
            res = nextResult
        #print("Gives us "+str(res))
        return nextResult

    def resultType(self, ctx, a, b):
        if (a == Type.REFERENCE or b == Type.REFERENCE):
            error(TypeError, "Cannot operate on object of type REFERENCE!", ctx)
        elif (a == Type.NULL or b == Type.NULL):
            error(TypeError, "Cannot operate on object of type NULL!", ctx)
        else:
            if (a == Type.STRING or b == Type.STRING):
                return Type.STRING
            elif (a == Type.FLOAT or b == Type.FLOAT):
                return Type.FLOAT
            elif (a == Type.INT or b == Type.INT):
                return Type.INT
            elif (a == Type.CHAR or b == Type.CHAR):
                return Type.CHAR
            elif (a == Type.BOOL or b == Type.BOOL):
                return Type.BOOL

    def stringConcat(self, lhs, rhs):
        if (lhs.type == Type.CHAR): a = chr(lhs.value)
        else: a = str(lhs.value)

        if (rhs.type == Type.CHAR): b = chr(rhs.value)
        else: b = str(rhs.value)

        return a + b

del langParser