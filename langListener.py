# Generated from lang.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .langParser import langParser
else:
    from langParser import langParser

import re


# This class defines a complete listener for a parse tree produced by langParser.
class langListener(ParseTreeListener):

    # Enter a parse tree produced by langParser#r.
    def enterR(self, ctx:langParser.RContext):
        pass

    # Exit a parse tree produced by langParser#r.
    def exitR(self, ctx:langParser.RContext):
        pass


    # Enter a parse tree produced by langParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:langParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by langParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:langParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by langParser#parameters.
    def enterParameters(self, ctx:langParser.ParametersContext):
        pass

    # Exit a parse tree produced by langParser#parameters.
    def exitParameters(self, ctx:langParser.ParametersContext):
        pass


    # Enter a parse tree produced by langParser#typedArgsList.
    def enterTypedArgsList(self, ctx:langParser.TypedArgsListContext):
        pass

    # Exit a parse tree produced by langParser#typedArgsList.
    def exitTypedArgsList(self, ctx:langParser.TypedArgsListContext):
        pass


    # Enter a parse tree produced by langParser#typedFunctionParam.
    def enterTypedFunctionParam(self, ctx:langParser.TypedFunctionParamContext):
        pass

    # Exit a parse tree produced by langParser#typedFunctionParam.
    def exitTypedFunctionParam(self, ctx:langParser.TypedFunctionParamContext):
        pass


    # Enter a parse tree produced by langParser#paramPassage.
    def enterParamPassage(self, ctx:langParser.ParamPassageContext):
        pass

    # Exit a parse tree produced by langParser#paramPassage.
    def exitParamPassage(self, ctx:langParser.ParamPassageContext):
        pass


    # Enter a parse tree produced by langParser#importStatement.
    def enterImportStatement(self, ctx:langParser.ImportStatementContext):
        pass

    # Exit a parse tree produced by langParser#importStatement.
    def exitImportStatement(self, ctx:langParser.ImportStatementContext):
        pass


    # Enter a parse tree produced by langParser#statement.
    def enterStatement(self, ctx:langParser.StatementContext):
        pass

    # Exit a parse tree produced by langParser#statement.
    def exitStatement(self, ctx:langParser.StatementContext):
        pass


    # Enter a parse tree produced by langParser#simpleStatement.
    def enterSimpleStatement(self, ctx:langParser.SimpleStatementContext):
        pass

    # Exit a parse tree produced by langParser#simpleStatement.
    def exitSimpleStatement(self, ctx:langParser.SimpleStatementContext):
        pass


    # Enter a parse tree produced by langParser#smallStatement.
    def enterSmallStatement(self, ctx:langParser.SmallStatementContext):
        pass

    # Exit a parse tree produced by langParser#smallStatement.
    def exitSmallStatement(self, ctx:langParser.SmallStatementContext):
        pass


    # Enter a parse tree produced by langParser#declarationStatement.
    def enterDeclarationStatement(self, ctx:langParser.DeclarationStatementContext):
        pass

    # Exit a parse tree produced by langParser#declarationStatement.
    def exitDeclarationStatement(self, ctx:langParser.DeclarationStatementContext):
        pass


    # Enter a parse tree produced by langParser#dataType.
    def enterDataType(self, ctx:langParser.DataTypeContext):
        pass

    # Exit a parse tree produced by langParser#dataType.
    def exitDataType(self, ctx:langParser.DataTypeContext):
        pass


    # Enter a parse tree produced by langParser#testOrExpressionStatement.
    def enterTestOrExpressionStatement(self, ctx:langParser.TestOrExpressionStatementContext):
        pass

    # Exit a parse tree produced by langParser#testOrExpressionStatement.
    def exitTestOrExpressionStatement(self, ctx:langParser.TestOrExpressionStatementContext):
        pass


    # Enter a parse tree produced by langParser#expressionList.
    def enterExpressionList(self, ctx:langParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by langParser#expressionList.
    def exitExpressionList(self, ctx:langParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by langParser#testOrExpression.
    def enterTestOrExpression(self, ctx:langParser.TestOrExpressionContext):
        pass

    # Exit a parse tree produced by langParser#testOrExpression.
    def exitTestOrExpression(self, ctx:langParser.TestOrExpressionContext):
        pass


    # Enter a parse tree produced by langParser#enumSpecifier.
    def enterEnumSpecifier(self, ctx:langParser.EnumSpecifierContext):
        pass

    # Exit a parse tree produced by langParser#enumSpecifier.
    def exitEnumSpecifier(self, ctx:langParser.EnumSpecifierContext):
        pass


    # Enter a parse tree produced by langParser#enumeratorList.
    def enterEnumeratorList(self, ctx:langParser.EnumeratorListContext):
        pass

    # Exit a parse tree produced by langParser#enumeratorList.
    def exitEnumeratorList(self, ctx:langParser.EnumeratorListContext):
        pass


    # Enter a parse tree produced by langParser#enumerator.
    def enterEnumerator(self, ctx:langParser.EnumeratorContext):
        pass

    # Exit a parse tree produced by langParser#enumerator.
    def exitEnumerator(self, ctx:langParser.EnumeratorContext):
        pass


    # Enter a parse tree produced by langParser#flowStatement.
    def enterFlowStatement(self, ctx:langParser.FlowStatementContext):
        pass

    # Exit a parse tree produced by langParser#flowStatement.
    def exitFlowStatement(self, ctx:langParser.FlowStatementContext):
        pass


    # Enter a parse tree produced by langParser#breakStatement.
    def enterBreakStatement(self, ctx:langParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by langParser#breakStatement.
    def exitBreakStatement(self, ctx:langParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by langParser#continueStatement.
    def enterContinueStatement(self, ctx:langParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by langParser#continueStatement.
    def exitContinueStatement(self, ctx:langParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by langParser#returnStatement.
    def enterReturnStatement(self, ctx:langParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by langParser#returnStatement.
    def exitReturnStatement(self, ctx:langParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by langParser#nameList.
    def enterNameList(self, ctx:langParser.NameListContext):
        pass

    # Exit a parse tree produced by langParser#nameList.
    def exitNameList(self, ctx:langParser.NameListContext):
        pass


    # Enter a parse tree produced by langParser#compoundStatement.
    def enterCompoundStatement(self, ctx:langParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by langParser#compoundStatement.
    def exitCompoundStatement(self, ctx:langParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by langParser#ifStatement.
    def enterIfStatement(self, ctx:langParser.IfStatementContext):
        pass

    # Exit a parse tree produced by langParser#ifStatement.
    def exitIfStatement(self, ctx:langParser.IfStatementContext):
        pass


    # Enter a parse tree produced by langParser#whileStatement.
    def enterWhileStatement(self, ctx:langParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by langParser#whileStatement.
    def exitWhileStatement(self, ctx:langParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by langParser#forStatement.
    def enterForStatement(self, ctx:langParser.ForStatementContext):
        pass

    # Exit a parse tree produced by langParser#forStatement.
    def exitForStatement(self, ctx:langParser.ForStatementContext):
        pass


    # Enter a parse tree produced by langParser#block.
    def enterBlock(self, ctx:langParser.BlockContext):
        pass

    # Exit a parse tree produced by langParser#block.
    def exitBlock(self, ctx:langParser.BlockContext):
        pass


    # Enter a parse tree produced by langParser#test.
    def enterTest(self, ctx:langParser.TestContext):
        pass

    # Exit a parse tree produced by langParser#test.
    def exitTest(self, ctx:langParser.TestContext):
        pass


    # Enter a parse tree produced by langParser#orTest.
    def enterOrTest(self, ctx:langParser.OrTestContext):
        pass

    # Exit a parse tree produced by langParser#orTest.
    def exitOrTest(self, ctx:langParser.OrTestContext):
        pass


    # Enter a parse tree produced by langParser#andTest.
    def enterAndTest(self, ctx:langParser.AndTestContext):
        pass

    # Exit a parse tree produced by langParser#andTest.
    def exitAndTest(self, ctx:langParser.AndTestContext):
        pass


    # Enter a parse tree produced by langParser#notTest.
    def enterNotTest(self, ctx:langParser.NotTestContext):
        pass

    # Exit a parse tree produced by langParser#notTest.
    def exitNotTest(self, ctx:langParser.NotTestContext):
        pass


    # Enter a parse tree produced by langParser#comparison.
    def enterComparison(self, ctx:langParser.ComparisonContext):
        pass

    # Exit a parse tree produced by langParser#comparison.
    def exitComparison(self, ctx:langParser.ComparisonContext):
        pass


    # Enter a parse tree produced by langParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:langParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by langParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:langParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by langParser#loopRange.
    def enterLoopRange(self, ctx:langParser.LoopRangeContext):
        pass

    # Exit a parse tree produced by langParser#loopRange.
    def exitLoopRange(self, ctx:langParser.LoopRangeContext):
        pass


    # Enter a parse tree produced by langParser#rangeDelimiter.
    def enterRangeDelimiter(self, ctx:langParser.RangeDelimiterContext):
        pass

    # Exit a parse tree produced by langParser#rangeDelimiter.
    def exitRangeDelimiter(self, ctx:langParser.RangeDelimiterContext):
        pass


    # Enter a parse tree produced by langParser#rangeList.
    def enterRangeList(self, ctx:langParser.RangeListContext):
        pass

    # Exit a parse tree produced by langParser#rangeList.
    def exitRangeList(self, ctx:langParser.RangeListContext):
        pass


    # Enter a parse tree produced by langParser#expression.
    def enterExpression(self, ctx:langParser.ExpressionContext):
        pass

    # Exit a parse tree produced by langParser#expression.
    def exitExpression(self, ctx:langParser.ExpressionContext):
        pass


    # Enter a parse tree produced by langParser#xorExpression.
    def enterXorExpression(self, ctx:langParser.XorExpressionContext):
        pass

    # Exit a parse tree produced by langParser#xorExpression.
    def exitXorExpression(self, ctx:langParser.XorExpressionContext):
        pass


    # Enter a parse tree produced by langParser#andExpression.
    def enterAndExpression(self, ctx:langParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by langParser#andExpression.
    def exitAndExpression(self, ctx:langParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by langParser#shiftExpression.
    def enterShiftExpression(self, ctx:langParser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by langParser#shiftExpression.
    def exitShiftExpression(self, ctx:langParser.ShiftExpressionContext):
        pass


    # Enter a parse tree produced by langParser#arithmeticExpression.
    def enterArithmeticExpression(self, ctx:langParser.ArithmeticExpressionContext):
        pass

    # Exit a parse tree produced by langParser#arithmeticExpression.
    def exitArithmeticExpression(self, ctx:langParser.ArithmeticExpressionContext):
        pass


    # Enter a parse tree produced by langParser#term.
    def enterTerm(self, ctx:langParser.TermContext):
        pass

    # Exit a parse tree produced by langParser#term.
    def exitTerm(self, ctx:langParser.TermContext):
        pass


    # Enter a parse tree produced by langParser#factor.
    def enterFactor(self, ctx:langParser.FactorContext):
        pass

    # Exit a parse tree produced by langParser#factor.
    def exitFactor(self, ctx:langParser.FactorContext):
        pass


    # Enter a parse tree produced by langParser#power.
    def enterPower(self, ctx:langParser.PowerContext):
        pass

    # Exit a parse tree produced by langParser#power.
    def exitPower(self, ctx:langParser.PowerContext):
        pass


    # Enter a parse tree produced by langParser#atom.
    def enterAtom(self, ctx:langParser.AtomContext):
        pass

    # Exit a parse tree produced by langParser#atom.
    def exitAtom(self, ctx:langParser.AtomContext):
        pass


    # Enter a parse tree produced by langParser#trailerArgs.
    def enterTrailerArgs(self, ctx:langParser.TrailerArgsContext):
        pass

    # Exit a parse tree produced by langParser#trailerArgs.
    def exitTrailerArgs(self, ctx:langParser.TrailerArgsContext):
        pass


    # Enter a parse tree produced by langParser#trailerSubs.
    def enterTrailerSubs(self, ctx:langParser.TrailerSubsContext):
        pass

    # Exit a parse tree produced by langParser#trailerSubs.
    def exitTrailerSubs(self, ctx:langParser.TrailerSubsContext):
        pass


    # Enter a parse tree produced by langParser#trailerDot.
    def enterTrailerDot(self, ctx:langParser.TrailerDotContext):
        pass

    # Exit a parse tree produced by langParser#trailerDot.
    def exitTrailerDot(self, ctx:langParser.TrailerDotContext):
        pass


    # Enter a parse tree produced by langParser#subscriptList.
    def enterSubscriptList(self, ctx:langParser.SubscriptListContext):
        pass

    # Exit a parse tree produced by langParser#subscriptList.
    def exitSubscriptList(self, ctx:langParser.SubscriptListContext):
        pass


    # Enter a parse tree produced by langParser#subscript.
    def enterSubscript(self, ctx:langParser.SubscriptContext):
        pass

    # Exit a parse tree produced by langParser#subscript.
    def exitSubscript(self, ctx:langParser.SubscriptContext):
        pass


    # Enter a parse tree produced by langParser#testOrExpressionList.
    def enterTestOrExpressionList(self, ctx:langParser.TestOrExpressionListContext):
        pass

    # Exit a parse tree produced by langParser#testOrExpressionList.
    def exitTestOrExpressionList(self, ctx:langParser.TestOrExpressionListContext):
        pass


    # Enter a parse tree produced by langParser#classDefinition.
    def enterClassDefinition(self, ctx:langParser.ClassDefinitionContext):
        pass

    # Exit a parse tree produced by langParser#classDefinition.
    def exitClassDefinition(self, ctx:langParser.ClassDefinitionContext):
        pass


    # Enter a parse tree produced by langParser#argList.
    def enterArgList(self, ctx:langParser.ArgListContext):
        pass

    # Exit a parse tree produced by langParser#argList.
    def exitArgList(self, ctx:langParser.ArgListContext):
        pass


    # Enter a parse tree produced by langParser#argument.
    def enterArgument(self, ctx:langParser.ArgumentContext):
        pass

    # Exit a parse tree produced by langParser#argument.
    def exitArgument(self, ctx:langParser.ArgumentContext):
        pass


    # Enter a parse tree produced by langParser#string.
    def enterString(self, ctx:langParser.StringContext):
        pass

    # Exit a parse tree produced by langParser#string.
    def exitString(self, ctx:langParser.StringContext):
        pass


    # Enter a parse tree produced by langParser#character.
    def enterCharacter(self, ctx:langParser.CharacterContext):
        pass

    # Exit a parse tree produced by langParser#character.
    def exitCharacter(self, ctx:langParser.CharacterContext):
        pass


    # Enter a parse tree produced by langParser#number.
    def enterNumber(self, ctx:langParser.NumberContext):
        pass

    # Exit a parse tree produced by langParser#number.
    def exitNumber(self, ctx:langParser.NumberContext):
        pass


    # Enter a parse tree produced by langParser#integer.
    def enterInteger(self, ctx:langParser.IntegerContext):
        pass

    # Exit a parse tree produced by langParser#integer.
    def exitInteger(self, ctx:langParser.IntegerContext):
        pass


