// Generated from langJAVA.g4 by ANTLR 4.7
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link langJAVAParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface langJAVAVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#r}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitR(langJAVAParser.RContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#functionDefinition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunctionDefinition(langJAVAParser.FunctionDefinitionContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#parameters}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParameters(langJAVAParser.ParametersContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#typedArgsList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTypedArgsList(langJAVAParser.TypedArgsListContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#typedFunctionParam}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTypedFunctionParam(langJAVAParser.TypedFunctionParamContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#paramPassage}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParamPassage(langJAVAParser.ParamPassageContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#importStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitImportStatement(langJAVAParser.ImportStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatement(langJAVAParser.StatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#simpleStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSimpleStatement(langJAVAParser.SimpleStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#smallStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSmallStatement(langJAVAParser.SmallStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#declarationStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeclarationStatement(langJAVAParser.DeclarationStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#dataType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDataType(langJAVAParser.DataTypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#testOrExpressionStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTestOrExpressionStatement(langJAVAParser.TestOrExpressionStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#expressionList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpressionList(langJAVAParser.ExpressionListContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#testOrExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTestOrExpression(langJAVAParser.TestOrExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#enumSpecifier}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEnumSpecifier(langJAVAParser.EnumSpecifierContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#enumeratorList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEnumeratorList(langJAVAParser.EnumeratorListContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#enumerator}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEnumerator(langJAVAParser.EnumeratorContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#flowStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFlowStatement(langJAVAParser.FlowStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#breakStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBreakStatement(langJAVAParser.BreakStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#continueStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitContinueStatement(langJAVAParser.ContinueStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#returnStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReturnStatement(langJAVAParser.ReturnStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#nameList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNameList(langJAVAParser.NameListContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#compoundStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCompoundStatement(langJAVAParser.CompoundStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#ifStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIfStatement(langJAVAParser.IfStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#whileStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWhileStatement(langJAVAParser.WhileStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#forStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitForStatement(langJAVAParser.ForStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#block}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBlock(langJAVAParser.BlockContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#test}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTest(langJAVAParser.TestContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#orTest}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOrTest(langJAVAParser.OrTestContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#andTest}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAndTest(langJAVAParser.AndTestContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#notTest}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNotTest(langJAVAParser.NotTestContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#comparison}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitComparison(langJAVAParser.ComparisonContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#comparisonOperator}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitComparisonOperator(langJAVAParser.ComparisonOperatorContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#loopRange}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLoopRange(langJAVAParser.LoopRangeContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#rangeDelimiter}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRangeDelimiter(langJAVAParser.RangeDelimiterContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#rangeList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRangeList(langJAVAParser.RangeListContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression(langJAVAParser.ExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#xorExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitXorExpression(langJAVAParser.XorExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#andExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAndExpression(langJAVAParser.AndExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#shiftExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShiftExpression(langJAVAParser.ShiftExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#arithmeticExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArithmeticExpression(langJAVAParser.ArithmeticExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#term}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTerm(langJAVAParser.TermContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#factor}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFactor(langJAVAParser.FactorContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#power}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPower(langJAVAParser.PowerContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAtom(langJAVAParser.AtomContext ctx);
	/**
	 * Visit a parse tree produced by the {@code trailerArgs}
	 * labeled alternative in {@link langJAVAParser#trailer}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTrailerArgs(langJAVAParser.TrailerArgsContext ctx);
	/**
	 * Visit a parse tree produced by the {@code trailerSubs}
	 * labeled alternative in {@link langJAVAParser#trailer}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTrailerSubs(langJAVAParser.TrailerSubsContext ctx);
	/**
	 * Visit a parse tree produced by the {@code trailerDot}
	 * labeled alternative in {@link langJAVAParser#trailer}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTrailerDot(langJAVAParser.TrailerDotContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#subscriptList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSubscriptList(langJAVAParser.SubscriptListContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#subscript}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSubscript(langJAVAParser.SubscriptContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#testOrExpressionList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTestOrExpressionList(langJAVAParser.TestOrExpressionListContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#classDefinition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitClassDefinition(langJAVAParser.ClassDefinitionContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#argList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArgList(langJAVAParser.ArgListContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#argument}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArgument(langJAVAParser.ArgumentContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#string}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitString(langJAVAParser.StringContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#character}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCharacter(langJAVAParser.CharacterContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#number}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNumber(langJAVAParser.NumberContext ctx);
	/**
	 * Visit a parse tree produced by {@link langJAVAParser#integer}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInteger(langJAVAParser.IntegerContext ctx);
}