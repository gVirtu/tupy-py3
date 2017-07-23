// Generated from langJAVA.g4 by ANTLR 4.7
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link langJAVAParser}.
 */
public interface langJAVAListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#r}.
	 * @param ctx the parse tree
	 */
	void enterR(langJAVAParser.RContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#r}.
	 * @param ctx the parse tree
	 */
	void exitR(langJAVAParser.RContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#functionDefinition}.
	 * @param ctx the parse tree
	 */
	void enterFunctionDefinition(langJAVAParser.FunctionDefinitionContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#functionDefinition}.
	 * @param ctx the parse tree
	 */
	void exitFunctionDefinition(langJAVAParser.FunctionDefinitionContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#parameters}.
	 * @param ctx the parse tree
	 */
	void enterParameters(langJAVAParser.ParametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#parameters}.
	 * @param ctx the parse tree
	 */
	void exitParameters(langJAVAParser.ParametersContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#typedArgsList}.
	 * @param ctx the parse tree
	 */
	void enterTypedArgsList(langJAVAParser.TypedArgsListContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#typedArgsList}.
	 * @param ctx the parse tree
	 */
	void exitTypedArgsList(langJAVAParser.TypedArgsListContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#typedFunctionParam}.
	 * @param ctx the parse tree
	 */
	void enterTypedFunctionParam(langJAVAParser.TypedFunctionParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#typedFunctionParam}.
	 * @param ctx the parse tree
	 */
	void exitTypedFunctionParam(langJAVAParser.TypedFunctionParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#paramPassage}.
	 * @param ctx the parse tree
	 */
	void enterParamPassage(langJAVAParser.ParamPassageContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#paramPassage}.
	 * @param ctx the parse tree
	 */
	void exitParamPassage(langJAVAParser.ParamPassageContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#importStatement}.
	 * @param ctx the parse tree
	 */
	void enterImportStatement(langJAVAParser.ImportStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#importStatement}.
	 * @param ctx the parse tree
	 */
	void exitImportStatement(langJAVAParser.ImportStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(langJAVAParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(langJAVAParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#simpleStatement}.
	 * @param ctx the parse tree
	 */
	void enterSimpleStatement(langJAVAParser.SimpleStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#simpleStatement}.
	 * @param ctx the parse tree
	 */
	void exitSimpleStatement(langJAVAParser.SimpleStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#smallStatement}.
	 * @param ctx the parse tree
	 */
	void enterSmallStatement(langJAVAParser.SmallStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#smallStatement}.
	 * @param ctx the parse tree
	 */
	void exitSmallStatement(langJAVAParser.SmallStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#declarationStatement}.
	 * @param ctx the parse tree
	 */
	void enterDeclarationStatement(langJAVAParser.DeclarationStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#declarationStatement}.
	 * @param ctx the parse tree
	 */
	void exitDeclarationStatement(langJAVAParser.DeclarationStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#dataType}.
	 * @param ctx the parse tree
	 */
	void enterDataType(langJAVAParser.DataTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#dataType}.
	 * @param ctx the parse tree
	 */
	void exitDataType(langJAVAParser.DataTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#testOrExpressionStatement}.
	 * @param ctx the parse tree
	 */
	void enterTestOrExpressionStatement(langJAVAParser.TestOrExpressionStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#testOrExpressionStatement}.
	 * @param ctx the parse tree
	 */
	void exitTestOrExpressionStatement(langJAVAParser.TestOrExpressionStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#expressionList}.
	 * @param ctx the parse tree
	 */
	void enterExpressionList(langJAVAParser.ExpressionListContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#expressionList}.
	 * @param ctx the parse tree
	 */
	void exitExpressionList(langJAVAParser.ExpressionListContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#testOrExpression}.
	 * @param ctx the parse tree
	 */
	void enterTestOrExpression(langJAVAParser.TestOrExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#testOrExpression}.
	 * @param ctx the parse tree
	 */
	void exitTestOrExpression(langJAVAParser.TestOrExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#enumSpecifier}.
	 * @param ctx the parse tree
	 */
	void enterEnumSpecifier(langJAVAParser.EnumSpecifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#enumSpecifier}.
	 * @param ctx the parse tree
	 */
	void exitEnumSpecifier(langJAVAParser.EnumSpecifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#enumeratorList}.
	 * @param ctx the parse tree
	 */
	void enterEnumeratorList(langJAVAParser.EnumeratorListContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#enumeratorList}.
	 * @param ctx the parse tree
	 */
	void exitEnumeratorList(langJAVAParser.EnumeratorListContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#enumerator}.
	 * @param ctx the parse tree
	 */
	void enterEnumerator(langJAVAParser.EnumeratorContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#enumerator}.
	 * @param ctx the parse tree
	 */
	void exitEnumerator(langJAVAParser.EnumeratorContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#flowStatement}.
	 * @param ctx the parse tree
	 */
	void enterFlowStatement(langJAVAParser.FlowStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#flowStatement}.
	 * @param ctx the parse tree
	 */
	void exitFlowStatement(langJAVAParser.FlowStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#breakStatement}.
	 * @param ctx the parse tree
	 */
	void enterBreakStatement(langJAVAParser.BreakStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#breakStatement}.
	 * @param ctx the parse tree
	 */
	void exitBreakStatement(langJAVAParser.BreakStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#continueStatement}.
	 * @param ctx the parse tree
	 */
	void enterContinueStatement(langJAVAParser.ContinueStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#continueStatement}.
	 * @param ctx the parse tree
	 */
	void exitContinueStatement(langJAVAParser.ContinueStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void enterReturnStatement(langJAVAParser.ReturnStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void exitReturnStatement(langJAVAParser.ReturnStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#nameList}.
	 * @param ctx the parse tree
	 */
	void enterNameList(langJAVAParser.NameListContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#nameList}.
	 * @param ctx the parse tree
	 */
	void exitNameList(langJAVAParser.NameListContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#compoundStatement}.
	 * @param ctx the parse tree
	 */
	void enterCompoundStatement(langJAVAParser.CompoundStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#compoundStatement}.
	 * @param ctx the parse tree
	 */
	void exitCompoundStatement(langJAVAParser.CompoundStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(langJAVAParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(langJAVAParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void enterWhileStatement(langJAVAParser.WhileStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void exitWhileStatement(langJAVAParser.WhileStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#forStatement}.
	 * @param ctx the parse tree
	 */
	void enterForStatement(langJAVAParser.ForStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#forStatement}.
	 * @param ctx the parse tree
	 */
	void exitForStatement(langJAVAParser.ForStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(langJAVAParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(langJAVAParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#test}.
	 * @param ctx the parse tree
	 */
	void enterTest(langJAVAParser.TestContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#test}.
	 * @param ctx the parse tree
	 */
	void exitTest(langJAVAParser.TestContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#orTest}.
	 * @param ctx the parse tree
	 */
	void enterOrTest(langJAVAParser.OrTestContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#orTest}.
	 * @param ctx the parse tree
	 */
	void exitOrTest(langJAVAParser.OrTestContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#andTest}.
	 * @param ctx the parse tree
	 */
	void enterAndTest(langJAVAParser.AndTestContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#andTest}.
	 * @param ctx the parse tree
	 */
	void exitAndTest(langJAVAParser.AndTestContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#notTest}.
	 * @param ctx the parse tree
	 */
	void enterNotTest(langJAVAParser.NotTestContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#notTest}.
	 * @param ctx the parse tree
	 */
	void exitNotTest(langJAVAParser.NotTestContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#comparison}.
	 * @param ctx the parse tree
	 */
	void enterComparison(langJAVAParser.ComparisonContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#comparison}.
	 * @param ctx the parse tree
	 */
	void exitComparison(langJAVAParser.ComparisonContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#comparisonOperator}.
	 * @param ctx the parse tree
	 */
	void enterComparisonOperator(langJAVAParser.ComparisonOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#comparisonOperator}.
	 * @param ctx the parse tree
	 */
	void exitComparisonOperator(langJAVAParser.ComparisonOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#loopRange}.
	 * @param ctx the parse tree
	 */
	void enterLoopRange(langJAVAParser.LoopRangeContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#loopRange}.
	 * @param ctx the parse tree
	 */
	void exitLoopRange(langJAVAParser.LoopRangeContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#rangeDelimiter}.
	 * @param ctx the parse tree
	 */
	void enterRangeDelimiter(langJAVAParser.RangeDelimiterContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#rangeDelimiter}.
	 * @param ctx the parse tree
	 */
	void exitRangeDelimiter(langJAVAParser.RangeDelimiterContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#rangeList}.
	 * @param ctx the parse tree
	 */
	void enterRangeList(langJAVAParser.RangeListContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#rangeList}.
	 * @param ctx the parse tree
	 */
	void exitRangeList(langJAVAParser.RangeListContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(langJAVAParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(langJAVAParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#xorExpression}.
	 * @param ctx the parse tree
	 */
	void enterXorExpression(langJAVAParser.XorExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#xorExpression}.
	 * @param ctx the parse tree
	 */
	void exitXorExpression(langJAVAParser.XorExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#andExpression}.
	 * @param ctx the parse tree
	 */
	void enterAndExpression(langJAVAParser.AndExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#andExpression}.
	 * @param ctx the parse tree
	 */
	void exitAndExpression(langJAVAParser.AndExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#shiftExpression}.
	 * @param ctx the parse tree
	 */
	void enterShiftExpression(langJAVAParser.ShiftExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#shiftExpression}.
	 * @param ctx the parse tree
	 */
	void exitShiftExpression(langJAVAParser.ShiftExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#arithmeticExpression}.
	 * @param ctx the parse tree
	 */
	void enterArithmeticExpression(langJAVAParser.ArithmeticExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#arithmeticExpression}.
	 * @param ctx the parse tree
	 */
	void exitArithmeticExpression(langJAVAParser.ArithmeticExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(langJAVAParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(langJAVAParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(langJAVAParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(langJAVAParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#power}.
	 * @param ctx the parse tree
	 */
	void enterPower(langJAVAParser.PowerContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#power}.
	 * @param ctx the parse tree
	 */
	void exitPower(langJAVAParser.PowerContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterAtom(langJAVAParser.AtomContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitAtom(langJAVAParser.AtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code trailerArgs}
	 * labeled alternative in {@link langJAVAParser#trailer}.
	 * @param ctx the parse tree
	 */
	void enterTrailerArgs(langJAVAParser.TrailerArgsContext ctx);
	/**
	 * Exit a parse tree produced by the {@code trailerArgs}
	 * labeled alternative in {@link langJAVAParser#trailer}.
	 * @param ctx the parse tree
	 */
	void exitTrailerArgs(langJAVAParser.TrailerArgsContext ctx);
	/**
	 * Enter a parse tree produced by the {@code trailerSubs}
	 * labeled alternative in {@link langJAVAParser#trailer}.
	 * @param ctx the parse tree
	 */
	void enterTrailerSubs(langJAVAParser.TrailerSubsContext ctx);
	/**
	 * Exit a parse tree produced by the {@code trailerSubs}
	 * labeled alternative in {@link langJAVAParser#trailer}.
	 * @param ctx the parse tree
	 */
	void exitTrailerSubs(langJAVAParser.TrailerSubsContext ctx);
	/**
	 * Enter a parse tree produced by the {@code trailerDot}
	 * labeled alternative in {@link langJAVAParser#trailer}.
	 * @param ctx the parse tree
	 */
	void enterTrailerDot(langJAVAParser.TrailerDotContext ctx);
	/**
	 * Exit a parse tree produced by the {@code trailerDot}
	 * labeled alternative in {@link langJAVAParser#trailer}.
	 * @param ctx the parse tree
	 */
	void exitTrailerDot(langJAVAParser.TrailerDotContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#subscriptList}.
	 * @param ctx the parse tree
	 */
	void enterSubscriptList(langJAVAParser.SubscriptListContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#subscriptList}.
	 * @param ctx the parse tree
	 */
	void exitSubscriptList(langJAVAParser.SubscriptListContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#subscript}.
	 * @param ctx the parse tree
	 */
	void enterSubscript(langJAVAParser.SubscriptContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#subscript}.
	 * @param ctx the parse tree
	 */
	void exitSubscript(langJAVAParser.SubscriptContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#testOrExpressionList}.
	 * @param ctx the parse tree
	 */
	void enterTestOrExpressionList(langJAVAParser.TestOrExpressionListContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#testOrExpressionList}.
	 * @param ctx the parse tree
	 */
	void exitTestOrExpressionList(langJAVAParser.TestOrExpressionListContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#classDefinition}.
	 * @param ctx the parse tree
	 */
	void enterClassDefinition(langJAVAParser.ClassDefinitionContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#classDefinition}.
	 * @param ctx the parse tree
	 */
	void exitClassDefinition(langJAVAParser.ClassDefinitionContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#argList}.
	 * @param ctx the parse tree
	 */
	void enterArgList(langJAVAParser.ArgListContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#argList}.
	 * @param ctx the parse tree
	 */
	void exitArgList(langJAVAParser.ArgListContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#argument}.
	 * @param ctx the parse tree
	 */
	void enterArgument(langJAVAParser.ArgumentContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#argument}.
	 * @param ctx the parse tree
	 */
	void exitArgument(langJAVAParser.ArgumentContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#string}.
	 * @param ctx the parse tree
	 */
	void enterString(langJAVAParser.StringContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#string}.
	 * @param ctx the parse tree
	 */
	void exitString(langJAVAParser.StringContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#character}.
	 * @param ctx the parse tree
	 */
	void enterCharacter(langJAVAParser.CharacterContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#character}.
	 * @param ctx the parse tree
	 */
	void exitCharacter(langJAVAParser.CharacterContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#number}.
	 * @param ctx the parse tree
	 */
	void enterNumber(langJAVAParser.NumberContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#number}.
	 * @param ctx the parse tree
	 */
	void exitNumber(langJAVAParser.NumberContext ctx);
	/**
	 * Enter a parse tree produced by {@link langJAVAParser#integer}.
	 * @param ctx the parse tree
	 */
	void enterInteger(langJAVAParser.IntegerContext ctx);
	/**
	 * Exit a parse tree produced by {@link langJAVAParser#integer}.
	 * @param ctx the parse tree
	 */
	void exitInteger(langJAVAParser.IntegerContext ctx);
}