# Generated from lang.g4 by ANTLR 4.7
from Instance import Instance
from Variable import Variable, Literal, Symbol
from Subscript import Subscript
from Type import TrailerType, Type

from antlr4 import *
if __name__ is not None and "." in __name__:
    from .langParser import langParser
else:
    from langParser import langParser

from errorHelper import error

import Interpreter as ii
import traceback

# This class defines a complete generic visitor for a parse tree produced by langParser.

class evalVisitor(ParseTreeVisitor):

    def __init__(self):
        self.parser = None

    def setParser(self, parser):
        self.parser = parser

    # Visit a parse tree produced by langParser#r.
    def visitR(self, ctx:langParser.RContext):
        for s in ctx.statement():
            res = self.visitStatement(s)
        print("ALL DONE!")
        print("CallStack top is {0}".format(str(ii.Interpreter.callStack.top())))
        print("Returnin {0}".format(res[0]))
        if (len(res)>1):
            return tuple((c.get()) for c in res)
        else:
            return res[0].get()

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
        for statement in ctx.smallStatement():
            res = self.visitSmallStatement(statement)
        return res


    # Visit a parse tree produced by langParser#smallStatement.
    def visitSmallStatement(self, ctx:langParser.SmallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#declarationStatement.
    def visitDeclarationStatement(self, ctx:langParser.DeclarationStatementContext):
        return self.visitTestOrExpressionStatement(ctx.testOrExpressionStatement())


    # Visit a parse tree produced by langParser#dataType.
    def visitDataType(self, ctx:langParser.DataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#testOrExpressionStatement.
    def visitTestOrExpressionStatement(self, ctx:langParser.TestOrExpressionStatementContext):
        childcount = len(ctx.testOrExpressionList())
        isDeclaration = isinstance(ctx.parentCtx, langParser.DeclarationStatementContext)
        decltype = Type.NULL
        if (isDeclaration):
            decltype = self.mapLexType(ctx.parentCtx.dataType().getChild(0).getSymbol().type)

        rhs = self.visitTestOrExpressionList(ctx.testOrExpressionList(childcount-1))
        # Only for return purposes when no assignment is done
        lhs = rhs 
        current_child = 1
        if (isDeclaration and childcount == current_child):
            self.doDeclare(lhs, decltype)
        
        i_children = iter(reversed(list(ctx.testOrExpressionList())))
        next(i_children) # all except last
        
        for c in i_children:
            # Visit expression lists pairwise from right to left
            lhs = self.visitTestOrExpressionList(c)
            current_child += 1
            if (isDeclaration and childcount == current_child):
                self.doDeclare(lhs, decltype)

            print("VISITTESTOREXPRESSIONSTATEMENT")
            print("LHS = "+str(lhs))
            print("RHS = "+str(rhs))
            if (len(lhs) == len(rhs)):
                for ind in range(0, len(lhs)):
                    print("ind="+str(ind))
                    lval = lhs[ind]
                    rval = rhs[ind]
                    if isinstance(lval, Symbol):
                        if isDeclaration:
                            ii.Interpreter.storeSymbol(lval.name, rval.get(), [])
                        else:
                            ii.Interpreter.storeSymbol(lval.name, rval.get(), lval.trailers)
                    else:
                        error(SyntaxError, "Cannot assign to literal!", ctx)
            else:
                error(SyntaxError, "Cannot assign expression lists of different sizes!", ctx)
            rhs = lhs
            
        return lhs


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
        ret = None
        test = False
        lastOne = False
        for c in ctx.getChildren():
            if isinstance(c, TerminalNode) and c.getSymbol().type == self.parser.ELSE:
                lastOne = True
            elif isinstance(c, langParser.ElseIfContext):
                pass
            elif isinstance(c, langParser.TestContext):
                test = bool(self.visitTest(c).get().value)
            elif isinstance(c, langParser.BlockContext) and ((test is True) or (lastOne)):
                ret = self.visitBlock(c)
                break
        return ret


    # Visit a parse tree produced by langParser#whileStatement.
    def visitWhileStatement(self, ctx:langParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#forStatement.
    def visitForStatement(self, ctx:langParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#block.
    def visitBlock(self, ctx:langParser.BlockContext):
        ii.Interpreter.pushFrame()
        ret = self.visitChildren(ctx)
        ii.Interpreter.popFrame()
        return ret


    # Visit a parse tree produced by langParser#test.
    def visitTest(self, ctx:langParser.TestContext):
        res = self.visitOrTest(ctx.orTest())
        if ctx.CARDINALITY_OP(0) is not None:
            return res.cardinality()
        else:
            return res


    # Visit a parse tree produced by langParser#orTest.
    def visitOrTest(self, ctx:langParser.OrTestContext):
        res = self.visitAndTest(ctx.andTest(0))
        op = 0
        i_children = iter(ctx.getChildren())
        next(i_children) # all except first factor
        for c in i_children:
            if isinstance(c, TerminalNode): 
                op = c.getSymbol().type
            else:
                rhs = self.visitAndTest(c)
                res = res.logic_or(rhs)
        return res


    # Visit a parse tree produced by langParser#andTest.
    def visitAndTest(self, ctx:langParser.AndTestContext):
        res = self.visitNotTest(ctx.notTest(0))
        op = 0
        i_children = iter(ctx.getChildren())
        next(i_children) # all except first factor
        for c in i_children:
            if isinstance(c, TerminalNode): 
                op = c.getSymbol().type
            else:
                rhs = self.visitNotTest(c)
                res = res.logic_and(rhs)
        return res


    # Visit a parse tree produced by langParser#notTest.
    def visitNotTest(self, ctx:langParser.NotTestContext):
        if ctx.NOT() is not None:
            res = self.visitNotTest(ctx.notTest())
            return res.logic_not()
        else:
            return self.visitComparison(ctx.comparison())


    # Visit a parse tree produced by langParser#comparison.
    def visitComparison(self, ctx:langParser.ComparisonContext):
        res = self.visitExpression(ctx.expression(0))
        op = 0
        i_children = iter(ctx.getChildren())
        next(i_children) # all except first factor
        for c in i_children:
            if isinstance(c, self.parser.ComparisonOperatorContext): 
                op = c.getChild(0).getSymbol().type
            else:
                rhs = self.visitExpression(c)
                if op == self.parser.GREATER_THAN:
                    res = res.gt(rhs)
                elif op == self.parser.LESS_THAN:
                    res = res.lt(rhs)
                elif op == self.parser.EQUALS:
                    res = res.eq(rhs)
                elif op == self.parser.GT_EQ:
                    res = res.gt_eq(rhs)
                elif op == self.parser.LT_EQ:
                    res = res.lt_eq(rhs)
                elif op == self.parser.NOT_EQ:
                    res = res.neq(rhs)
        return res


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
        res = self.visitXorExpression(ctx.xorExpression(0))
        op = 0
        i_children = iter(ctx.getChildren())
        next(i_children) # all except first factor
        for c in i_children:
            if isinstance(c, TerminalNode): 
                op = c.getSymbol().type
            else:
                rhs = self.visitXorExpression(c)
                res = res.bitwise_or(rhs)
        return res


    # Visit a parse tree produced by langParser#xorExpression.
    def visitXorExpression(self, ctx:langParser.XorExpressionContext):
        res = self.visitAndExpression(ctx.andExpression(0))
        op = 0
        i_children = iter(ctx.getChildren())
        next(i_children) # all except first factor
        for c in i_children:
            if isinstance(c, TerminalNode): 
                op = c.getSymbol().type
            else:
                rhs = self.visitAndExpression(c)
                res = res.bitwise_xor(rhs)
        return res


    # Visit a parse tree produced by langParser#andExpression.
    def visitAndExpression(self, ctx:langParser.AndExpressionContext):
        res = self.visitShiftExpression(ctx.shiftExpression(0))
        op = 0
        i_children = iter(ctx.getChildren())
        next(i_children) # all except first factor
        for c in i_children:
            if isinstance(c, TerminalNode): 
                op = c.getSymbol().type
            else:
                rhs = self.visitShiftExpression(c)
                res = res.bitwise_and(rhs)
        return res


    # Visit a parse tree produced by langParser#shiftExpression.
    def visitShiftExpression(self, ctx:langParser.ShiftExpressionContext):
        res = self.visitArithmeticExpression(ctx.arithmeticExpression(0))
        op = 0
        i_children = iter(ctx.getChildren())
        next(i_children) # all except first factor
        for c in i_children:
            if isinstance(c, TerminalNode): 
                op = c.getSymbol().type
            else:
                rhs = self.visitArithmeticExpression(c)
                if op == self.parser.LEFT_SHIFT:
                    res = res.left_shift(rhs)
                elif op == self.parser.RIGHT_SHIFT:
                    res = res.right_shift(rhs)
        return res


    # Visit a parse tree produced by langParser#arithmeticExpression.
    def visitArithmeticExpression(self, ctx:langParser.ArithmeticExpressionContext):
        res = self.visitTerm(ctx.term(0))
        op = 0
        i_children = iter(ctx.getChildren())
        next(i_children) # all except first factor
        for c in i_children:
            if isinstance(c, TerminalNode): 
                op = c.getSymbol().type
            else:
                rhs = self.visitTerm(c)
                if op == self.parser.ADD:
                    res = res.add(rhs)
                elif op == self.parser.MINUS:
                    res = res.subtract(rhs)
        return res


    # Visit a parse tree produced by langParser#term.
    def visitTerm(self, ctx:langParser.TermContext):
        res = self.visitFactor(ctx.factor(0))
        op = 0
        i_children = iter(ctx.getChildren())
        next(i_children) # all except first factor
        for c in i_children:
            if isinstance(c, TerminalNode): 
                op = c.getSymbol().type
            else:
                rhs = self.visitFactor(c)
                if op == self.parser.STAR:
                    res = res.multiply(rhs)
                elif op == self.parser.DIV:
                    res = res.divide(rhs)
                elif op == self.parser.MOD:
                    res = res.modulo(rhs)
                elif op == self.parser.IDIV:
                    res = res.integer_divide(rhs)
        return res


    # Visit a parse tree produced by langParser#factor.
    def visitFactor(self, ctx:langParser.FactorContext):
        if ctx.ADD() is not None:
            f = self.visitFactor(ctx.factor())
            return f.positive()
        elif ctx.MINUS() is not None:
            f = self.visitFactor(ctx.factor())
            return f.negative()
        elif ctx.NOT_OP() is not None:
            f = self.visitFactor(ctx.factor())
            return f.bitwise_flip()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#power.
    def visitPower(self, ctx:langParser.PowerContext):
        at = self.visitAtom(ctx.atom())
        print(at)
        for t in ctx.trailer():
            at.trailers.append(self.visitTrailer(t))

        if ctx.POWER() is not None:
            rhs = self.visitFactor(ctx.factor())
            return at.power(rhs)
        return at


    # Visit a parse tree produced by langParser#atom.
    def visitAtom(self, ctx:langParser.AtomContext):
        if ctx.NAME() is not None:
            return Symbol(str(ctx.NAME().getText()))
        elif ctx.TRUE() is not None:
            return Literal(Instance(Type.BOOL, True));
        elif ctx.FALSE() is not None:
            return Literal(Instance(Type.BOOL, False));
        elif ctx.NULL() is not None:
            return Literal(Instance(Type.NULL, 0));
        elif ctx.OPEN_PAREN() is not None:
            res = ()
            if ctx.testOrExpressionList() is not None:
                res = self.visitTestOrExpressionList(ctx.testOrExpressionList())
            return Literal(Instance(Type.TUPLE, tuple(res)));
        elif ctx.OPEN_BRACK() is not None:
            res = []
            if ctx.testOrExpressionList() is not None:
                res = self.visitTestOrExpressionList(ctx.testOrExpressionList())
            try:
                return Literal(Instance(Type.ARRAY, list(res)));
            except TypeError:
                error(TypeError, "Types in array must be consistent!", ctx)
        else:
            return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#trailerArgs.
    def visitTrailer(self, ctx:langParser.TrailerContext):
        if ctx.OPEN_PAREN() is not None:
            trailerType = TrailerType.CALL
            trailerId = None #TODO
        elif ctx.OPEN_BRACK() is not None:
            trailerType = TrailerType.SUBSCRIPT
            trailerId = self.visitSubscriptList(ctx.subscriptList())
        else:
            trailerType = TrailerType.MEMBER
            trailerId = None #TODO
        return (trailerType, trailerId)


    # Visit a parse tree produced by langParser#subscriptList.
    def visitSubscriptList(self, ctx:langParser.SubscriptListContext):
        return [self.visitSubscript(ss) for ss in ctx.subscript()]


    # Visit a parse tree produced by langParser#subscript.
    def visitSubscript(self, ctx:langParser.SubscriptContext):
        if ctx.STAR() is not None:
            return Subscript(isWildcard=True)
        elif ctx.rangeDelimiter() is not None: #error check this
            begin_pos = int(self.visitExpression(ctx.expression(0)).get().value)
            end_pos = int(self.visitExpression(ctx.expression(1)).get().value)
            if begin_pos <= end_pos:
                return Subscript(begin=begin_pos, 
                                end=end_pos)
            else:
                raise SyntaxError("Invalid range!")
        else:
            return Subscript(begin=int(self.visitExpression(ctx.expression(0)).get().value), 
                             end=int(self.visitExpression(ctx.expression(0)).get().value),
                             isSingle=True)

    # Visit a parse tree produced by langParser#testOrExpressionList.
    def visitTestOrExpressionList(self, ctx:langParser.TestOrExpressionListContext):
        return tuple(self.visitTestOrExpression(expr) for expr in ctx.testOrExpression())


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
        return Literal(Instance(Type.STRING, str(self.visitChildren(ctx))))


    # Visit a parse tree produced by langParser#character.
    def visitCharacter(self, ctx:langParser.StringContext):
        return Literal(Instance(Type.CHAR, ord(self.visitChildren(ctx))))


    # Visit a parse tree produced by langParser#number.
    def visitNumber(self, ctx:langParser.NumberContext):
        if ctx.integer() is None:
            return Literal(Instance(Type.FLOAT, float(self.visitChildren(ctx))))
        else:
            return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#integer.
    def visitInteger(self, ctx:langParser.IntegerContext):
        return Literal(Instance(Type.INT, int(self.visitChildren(ctx))))


    def visitTerminal(self, node):
        # print("Got to terminal "+str(node))
        return str(node)


    def aggregateResult(self, aggregate, nextResult):
        # print("Aggregating "+str(aggregate)+" and "+str(nextResult))
        if aggregate is not None:
            res = aggregate
        else:
            res = nextResult
        # print("Gives us "+str(res))
        return res

    def mapLexType(self, lextype):
        return {
            self.parser.INTEGER: Type.INT,
            self.parser.REAL: Type.FLOAT,
            self.parser.CHAR: Type.CHAR,
            self.parser.STRING: Type.STRING,
            self.parser.BOOLEAN: Type.BOOL,
            self.parser.NAME: Type.REFERENCE
        }.get(lextype, Type.NULL)

    def doDeclare(self, lhs, decltype):
        for lval in lhs:
            if len(lval.trailers) > 0:
                if lval.trailers[0][0] == TrailerType.SUBSCRIPT:
                    subscriptList = lval.trailers[0][1]
                else:
                    raise SyntaxError("Invalid declaration!")
            else:
                subscriptList = []
            ii.Interpreter.declareSymbol(lval.name, decltype, subscriptList)