// Generated from /home/gian/uerjInterpreter/lang.g4 by ANTLR 4.7

import re

import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class langParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		RETURN=1, IMPORT=2, IF=3, ELSE=4, WHILE=5, FOR=6, OR=7, AND=8, NOT=9, 
		NULL=10, TRUE=11, FALSE=12, CLASS=13, CONTINUE=14, BREAK=15, ENUM=16, 
		STEP=17, UNTIL=18, DOT=19, CARDINALITY_OP=20, OPEN_PAREN=21, CLOSE_PAREN=22, 
		COMMA=23, COLON=24, SEMI_COLON=25, POWER=26, ASSIGN=27, OPEN_BRACK=28, 
		CLOSE_BRACK=29, OR_OP=30, XOR=31, AND_OP=32, LEFT_SHIFT=33, RIGHT_SHIFT=34, 
		ADD=35, MINUS=36, STAR=37, DIV=38, MOD=39, IDIV=40, NOT_OP=41, OPEN_BRACE=42, 
		CLOSE_BRACE=43, LESS_THAN=44, GREATER_THAN=45, EQUALS=46, GT_EQ=47, LT_EQ=48, 
		NOT_EQ=49, AT=50, ARROW=51, VAL=52, REF=53, INTEGER=54, REAL=55, CHAR=56, 
		STRING=57, BOOLEAN=58, CONSTANT=59, NEWLINE=60, NAME=61, STRING_LITERAL=62, 
		CHAR_LITERAL=63, BYTES_LITERAL=64, DECIMAL_INTEGER=65, OCT_INTEGER=66, 
		HEX_INTEGER=67, BIN_INTEGER=68, FLOAT_NUMBER=69, IMAG_NUMBER=70, SKIP_=71, 
		UNKNOWN_CHAR=72, INDENT=73, DEDENT=74;
	public static final int
		RULE_r = 0, RULE_functionDefinition = 1, RULE_parameters = 2, RULE_typedArgsList = 3, 
		RULE_typedFunctionParam = 4, RULE_paramPassage = 5, RULE_importStatement = 6, 
		RULE_statement = 7, RULE_simpleStatement = 8, RULE_smallStatement = 9, 
		RULE_declarationStatement = 10, RULE_dataType = 11, RULE_testOrExpressionStatement = 12, 
		RULE_expressionList = 13, RULE_testOrExpression = 14, RULE_enumSpecifier = 15, 
		RULE_enumeratorList = 16, RULE_enumerator = 17, RULE_flowStatement = 18, 
		RULE_breakStatement = 19, RULE_continueStatement = 20, RULE_returnStatement = 21, 
		RULE_nameList = 22, RULE_compoundStatement = 23, RULE_ifStatement = 24, 
		RULE_whileStatement = 25, RULE_forStatement = 26, RULE_block = 27, RULE_test = 28, 
		RULE_orTest = 29, RULE_andTest = 30, RULE_notTest = 31, RULE_comparison = 32, 
		RULE_comparisonOperator = 33, RULE_loopRange = 34, RULE_rangeDelimiter = 35, 
		RULE_rangeList = 36, RULE_expression = 37, RULE_xorExpression = 38, RULE_andExpression = 39, 
		RULE_shiftExpression = 40, RULE_arithmeticExpression = 41, RULE_term = 42, 
		RULE_factor = 43, RULE_power = 44, RULE_atom = 45, RULE_trailer = 46, 
		RULE_subscriptList = 47, RULE_subscript = 48, RULE_testOrExpressionList = 49, 
		RULE_classDefinition = 50, RULE_argList = 51, RULE_argument = 52, RULE_string = 53, 
		RULE_character = 54, RULE_number = 55, RULE_integer = 56;
	public static final String[] ruleNames = {
		"r", "functionDefinition", "parameters", "typedArgsList", "typedFunctionParam", 
		"paramPassage", "importStatement", "statement", "simpleStatement", "smallStatement", 
		"declarationStatement", "dataType", "testOrExpressionStatement", "expressionList", 
		"testOrExpression", "enumSpecifier", "enumeratorList", "enumerator", "flowStatement", 
		"breakStatement", "continueStatement", "returnStatement", "nameList", 
		"compoundStatement", "ifStatement", "whileStatement", "forStatement", 
		"block", "test", "orTest", "andTest", "notTest", "comparison", "comparisonOperator", 
		"loopRange", "rangeDelimiter", "rangeList", "expression", "xorExpression", 
		"andExpression", "shiftExpression", "arithmeticExpression", "term", "factor", 
		"power", "atom", "trailer", "subscriptList", "subscript", "testOrExpressionList", 
		"classDefinition", "argList", "argument", "string", "character", "number", 
		"integer"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'retornar'", "'usando'", "'se'", null, "'enquanto'", "'para'", 
		"'ou'", "'e'", null, "'nulo'", "'verdadeiro'", "'falso'", "'tipo'", "'continuar'", 
		"'parar'", null, "'passo'", null, "'.'", "'|'", "'('", "')'", "','", "':'", 
		"';'", "'^'", "'<-'", "'['", "']'", "'||'", "'xor'", "'&&'", "'<<'", "'>>'", 
		"'+'", "'-'", "'*'", "'/'", "'mod'", "'div'", "'~'", "'{'", "'}'", "'<'", 
		"'>'", "'='", "'>='", "'<='", "'~='", "'@'", "'->'", "'val'", "'ref'", 
		"'inteiro'", "'real'", "'caracter'", "'cadeia'", null, "'constante'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "RETURN", "IMPORT", "IF", "ELSE", "WHILE", "FOR", "OR", "AND", "NOT", 
		"NULL", "TRUE", "FALSE", "CLASS", "CONTINUE", "BREAK", "ENUM", "STEP", 
		"UNTIL", "DOT", "CARDINALITY_OP", "OPEN_PAREN", "CLOSE_PAREN", "COMMA", 
		"COLON", "SEMI_COLON", "POWER", "ASSIGN", "OPEN_BRACK", "CLOSE_BRACK", 
		"OR_OP", "XOR", "AND_OP", "LEFT_SHIFT", "RIGHT_SHIFT", "ADD", "MINUS", 
		"STAR", "DIV", "MOD", "IDIV", "NOT_OP", "OPEN_BRACE", "CLOSE_BRACE", "LESS_THAN", 
		"GREATER_THAN", "EQUALS", "GT_EQ", "LT_EQ", "NOT_EQ", "AT", "ARROW", "VAL", 
		"REF", "INTEGER", "REAL", "CHAR", "STRING", "BOOLEAN", "CONSTANT", "NEWLINE", 
		"NAME", "STRING_LITERAL", "CHAR_LITERAL", "BYTES_LITERAL", "DECIMAL_INTEGER", 
		"OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER", "FLOAT_NUMBER", "IMAG_NUMBER", 
		"SKIP_", "UNKNOWN_CHAR", "INDENT", "DEDENT"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "lang.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public langParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class RContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(langParser.EOF, 0); }
		public List<TerminalNode> NEWLINE() { return getTokens(langParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(langParser.NEWLINE, i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public List<ImportStatementContext> importStatement() {
			return getRuleContexts(ImportStatementContext.class);
		}
		public ImportStatementContext importStatement(int i) {
			return getRuleContext(ImportStatementContext.class,i);
		}
		public RContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_r; }
	}

	public final RContext r() throws RecognitionException {
		RContext _localctx = new RContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_r);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(121);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << RETURN) | (1L << IMPORT) | (1L << IF) | (1L << WHILE) | (1L << FOR) | (1L << NOT) | (1L << NULL) | (1L << TRUE) | (1L << FALSE) | (1L << CLASS) | (1L << CONTINUE) | (1L << BREAK) | (1L << ENUM) | (1L << CARDINALITY_OP) | (1L << OPEN_PAREN) | (1L << ADD) | (1L << MINUS) | (1L << NOT_OP) | (1L << INTEGER) | (1L << REAL) | (1L << CHAR) | (1L << STRING) | (1L << BOOLEAN) | (1L << NEWLINE) | (1L << NAME) | (1L << STRING_LITERAL) | (1L << CHAR_LITERAL))) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & ((1L << (BYTES_LITERAL - 64)) | (1L << (DECIMAL_INTEGER - 64)) | (1L << (OCT_INTEGER - 64)) | (1L << (HEX_INTEGER - 64)) | (1L << (BIN_INTEGER - 64)) | (1L << (FLOAT_NUMBER - 64)) | (1L << (IMAG_NUMBER - 64)))) != 0)) {
				{
				setState(119);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case NEWLINE:
					{
					setState(114);
					match(NEWLINE);
					}
					break;
				case RETURN:
				case IMPORT:
				case IF:
				case WHILE:
				case FOR:
				case NOT:
				case NULL:
				case TRUE:
				case FALSE:
				case CLASS:
				case CONTINUE:
				case BREAK:
				case ENUM:
				case CARDINALITY_OP:
				case OPEN_PAREN:
				case ADD:
				case MINUS:
				case NOT_OP:
				case INTEGER:
				case REAL:
				case CHAR:
				case STRING:
				case BOOLEAN:
				case NAME:
				case STRING_LITERAL:
				case CHAR_LITERAL:
				case BYTES_LITERAL:
				case DECIMAL_INTEGER:
				case OCT_INTEGER:
				case HEX_INTEGER:
				case BIN_INTEGER:
				case FLOAT_NUMBER:
				case IMAG_NUMBER:
					{
					setState(116);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==IMPORT) {
						{
						setState(115);
						importStatement();
						}
					}

					setState(118);
					statement();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(123);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(124);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionDefinitionContext extends ParserRuleContext {
		public TerminalNode NAME() { return getToken(langParser.NAME, 0); }
		public ParametersContext parameters() {
			return getRuleContext(ParametersContext.class,0);
		}
		public TerminalNode COLON() { return getToken(langParser.COLON, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public DataTypeContext dataType() {
			return getRuleContext(DataTypeContext.class,0);
		}
		public FunctionDefinitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionDefinition; }
	}

	public final FunctionDefinitionContext functionDefinition() throws RecognitionException {
		FunctionDefinitionContext _localctx = new FunctionDefinitionContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_functionDefinition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(127);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				setState(126);
				dataType();
				}
				break;
			}
			setState(129);
			match(NAME);
			setState(130);
			parameters();
			setState(131);
			match(COLON);
			setState(132);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParametersContext extends ParserRuleContext {
		public TerminalNode OPEN_PAREN() { return getToken(langParser.OPEN_PAREN, 0); }
		public TerminalNode CLOSE_PAREN() { return getToken(langParser.CLOSE_PAREN, 0); }
		public TypedArgsListContext typedArgsList() {
			return getRuleContext(TypedArgsListContext.class,0);
		}
		public ParametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameters; }
	}

	public final ParametersContext parameters() throws RecognitionException {
		ParametersContext _localctx = new ParametersContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_parameters);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(134);
			match(OPEN_PAREN);
			setState(136);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << VAL) | (1L << REF) | (1L << INTEGER) | (1L << REAL) | (1L << CHAR) | (1L << STRING) | (1L << BOOLEAN) | (1L << NAME))) != 0)) {
				{
				setState(135);
				typedArgsList();
				}
			}

			setState(138);
			match(CLOSE_PAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypedArgsListContext extends ParserRuleContext {
		public List<TypedFunctionParamContext> typedFunctionParam() {
			return getRuleContexts(TypedFunctionParamContext.class);
		}
		public TypedFunctionParamContext typedFunctionParam(int i) {
			return getRuleContext(TypedFunctionParamContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(langParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(langParser.COMMA, i);
		}
		public List<TerminalNode> ASSIGN() { return getTokens(langParser.ASSIGN); }
		public TerminalNode ASSIGN(int i) {
			return getToken(langParser.ASSIGN, i);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TypedArgsListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typedArgsList; }
	}

	public final TypedArgsListContext typedArgsList() throws RecognitionException {
		TypedArgsListContext _localctx = new TypedArgsListContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_typedArgsList);
		int _la;
		try {
			int _alt;
			setState(171);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(140);
				typedFunctionParam();
				setState(145);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(141);
						match(COMMA);
						setState(142);
						typedFunctionParam();
						}
						} 
					}
					setState(147);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
				}
				setState(155);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(148);
					match(COMMA);
					setState(149);
					typedFunctionParam();
					setState(150);
					match(ASSIGN);
					setState(151);
					expression();
					}
					}
					setState(157);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(158);
				typedFunctionParam();
				setState(159);
				match(ASSIGN);
				setState(160);
				expression();
				setState(168);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(161);
					match(COMMA);
					setState(162);
					typedFunctionParam();
					setState(163);
					match(ASSIGN);
					setState(164);
					expression();
					}
					}
					setState(170);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypedFunctionParamContext extends ParserRuleContext {
		public DataTypeContext dataType() {
			return getRuleContext(DataTypeContext.class,0);
		}
		public TerminalNode NAME() { return getToken(langParser.NAME, 0); }
		public ParamPassageContext paramPassage() {
			return getRuleContext(ParamPassageContext.class,0);
		}
		public TypedFunctionParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typedFunctionParam; }
	}

	public final TypedFunctionParamContext typedFunctionParam() throws RecognitionException {
		TypedFunctionParamContext _localctx = new TypedFunctionParamContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_typedFunctionParam);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(174);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VAL || _la==REF) {
				{
				setState(173);
				paramPassage();
				}
			}

			setState(176);
			dataType();
			setState(177);
			match(NAME);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParamPassageContext extends ParserRuleContext {
		public TerminalNode VAL() { return getToken(langParser.VAL, 0); }
		public TerminalNode REF() { return getToken(langParser.REF, 0); }
		public ParamPassageContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paramPassage; }
	}

	public final ParamPassageContext paramPassage() throws RecognitionException {
		ParamPassageContext _localctx = new ParamPassageContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_paramPassage);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(179);
			_la = _input.LA(1);
			if ( !(_la==VAL || _la==REF) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ImportStatementContext extends ParserRuleContext {
		public TerminalNode IMPORT() { return getToken(langParser.IMPORT, 0); }
		public NameListContext nameList() {
			return getRuleContext(NameListContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(langParser.NEWLINE, 0); }
		public TerminalNode SEMI_COLON() { return getToken(langParser.SEMI_COLON, 0); }
		public ImportStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_importStatement; }
	}

	public final ImportStatementContext importStatement() throws RecognitionException {
		ImportStatementContext _localctx = new ImportStatementContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_importStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(181);
			match(IMPORT);
			setState(182);
			nameList();
			setState(184);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMI_COLON) {
				{
				setState(183);
				match(SEMI_COLON);
				}
			}

			setState(186);
			match(NEWLINE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public SimpleStatementContext simpleStatement() {
			return getRuleContext(SimpleStatementContext.class,0);
		}
		public CompoundStatementContext compoundStatement() {
			return getRuleContext(CompoundStatementContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_statement);
		try {
			setState(190);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(188);
				simpleStatement();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(189);
				compoundStatement();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SimpleStatementContext extends ParserRuleContext {
		public List<SmallStatementContext> smallStatement() {
			return getRuleContexts(SmallStatementContext.class);
		}
		public SmallStatementContext smallStatement(int i) {
			return getRuleContext(SmallStatementContext.class,i);
		}
		public TerminalNode NEWLINE() { return getToken(langParser.NEWLINE, 0); }
		public List<TerminalNode> SEMI_COLON() { return getTokens(langParser.SEMI_COLON); }
		public TerminalNode SEMI_COLON(int i) {
			return getToken(langParser.SEMI_COLON, i);
		}
		public SimpleStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_simpleStatement; }
	}

	public final SimpleStatementContext simpleStatement() throws RecognitionException {
		SimpleStatementContext _localctx = new SimpleStatementContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_simpleStatement);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(192);
			smallStatement();
			setState(197);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(193);
					match(SEMI_COLON);
					setState(194);
					smallStatement();
					}
					} 
				}
				setState(199);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			}
			setState(201);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMI_COLON) {
				{
				setState(200);
				match(SEMI_COLON);
				}
			}

			setState(203);
			match(NEWLINE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SmallStatementContext extends ParserRuleContext {
		public TestOrExpressionStatementContext testOrExpressionStatement() {
			return getRuleContext(TestOrExpressionStatementContext.class,0);
		}
		public DeclarationStatementContext declarationStatement() {
			return getRuleContext(DeclarationStatementContext.class,0);
		}
		public FlowStatementContext flowStatement() {
			return getRuleContext(FlowStatementContext.class,0);
		}
		public EnumSpecifierContext enumSpecifier() {
			return getRuleContext(EnumSpecifierContext.class,0);
		}
		public SmallStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_smallStatement; }
	}

	public final SmallStatementContext smallStatement() throws RecognitionException {
		SmallStatementContext _localctx = new SmallStatementContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_smallStatement);
		try {
			setState(209);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(205);
				testOrExpressionStatement();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(206);
				declarationStatement();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(207);
				flowStatement();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(208);
				enumSpecifier();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclarationStatementContext extends ParserRuleContext {
		public DataTypeContext dataType() {
			return getRuleContext(DataTypeContext.class,0);
		}
		public TestOrExpressionStatementContext testOrExpressionStatement() {
			return getRuleContext(TestOrExpressionStatementContext.class,0);
		}
		public TerminalNode CONSTANT() { return getToken(langParser.CONSTANT, 0); }
		public DeclarationStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declarationStatement; }
	}

	public final DeclarationStatementContext declarationStatement() throws RecognitionException {
		DeclarationStatementContext _localctx = new DeclarationStatementContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_declarationStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(211);
			dataType();
			setState(213);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==CONSTANT) {
				{
				setState(212);
				match(CONSTANT);
				}
			}

			setState(215);
			testOrExpressionStatement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DataTypeContext extends ParserRuleContext {
		public TerminalNode INTEGER() { return getToken(langParser.INTEGER, 0); }
		public TerminalNode REAL() { return getToken(langParser.REAL, 0); }
		public TerminalNode CHAR() { return getToken(langParser.CHAR, 0); }
		public TerminalNode STRING() { return getToken(langParser.STRING, 0); }
		public TerminalNode BOOLEAN() { return getToken(langParser.BOOLEAN, 0); }
		public TerminalNode NAME() { return getToken(langParser.NAME, 0); }
		public DataTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dataType; }
	}

	public final DataTypeContext dataType() throws RecognitionException {
		DataTypeContext _localctx = new DataTypeContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_dataType);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(217);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INTEGER) | (1L << REAL) | (1L << CHAR) | (1L << STRING) | (1L << BOOLEAN) | (1L << NAME))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TestOrExpressionStatementContext extends ParserRuleContext {
		public List<TestOrExpressionListContext> testOrExpressionList() {
			return getRuleContexts(TestOrExpressionListContext.class);
		}
		public TestOrExpressionListContext testOrExpressionList(int i) {
			return getRuleContext(TestOrExpressionListContext.class,i);
		}
		public List<TerminalNode> ASSIGN() { return getTokens(langParser.ASSIGN); }
		public TerminalNode ASSIGN(int i) {
			return getToken(langParser.ASSIGN, i);
		}
		public TestOrExpressionStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_testOrExpressionStatement; }
	}

	public final TestOrExpressionStatementContext testOrExpressionStatement() throws RecognitionException {
		TestOrExpressionStatementContext _localctx = new TestOrExpressionStatementContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_testOrExpressionStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(219);
			testOrExpressionList();
			setState(224);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ASSIGN) {
				{
				{
				setState(220);
				match(ASSIGN);
				setState(221);
				testOrExpressionList();
				}
				}
				setState(226);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionListContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(langParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(langParser.COMMA, i);
		}
		public ExpressionListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressionList; }
	}

	public final ExpressionListContext expressionList() throws RecognitionException {
		ExpressionListContext _localctx = new ExpressionListContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_expressionList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(227);
			expression();
			setState(232);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(228);
				match(COMMA);
				setState(229);
				expression();
				}
				}
				setState(234);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TestOrExpressionContext extends ParserRuleContext {
		public TestContext test() {
			return getRuleContext(TestContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TestOrExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_testOrExpression; }
	}

	public final TestOrExpressionContext testOrExpression() throws RecognitionException {
		TestOrExpressionContext _localctx = new TestOrExpressionContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_testOrExpression);
		try {
			setState(237);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(235);
				test();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(236);
				expression();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EnumSpecifierContext extends ParserRuleContext {
		public TerminalNode ENUM() { return getToken(langParser.ENUM, 0); }
		public TerminalNode OPEN_BRACE() { return getToken(langParser.OPEN_BRACE, 0); }
		public EnumeratorListContext enumeratorList() {
			return getRuleContext(EnumeratorListContext.class,0);
		}
		public TerminalNode CLOSE_BRACE() { return getToken(langParser.CLOSE_BRACE, 0); }
		public TerminalNode NAME() { return getToken(langParser.NAME, 0); }
		public EnumSpecifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_enumSpecifier; }
	}

	public final EnumSpecifierContext enumSpecifier() throws RecognitionException {
		EnumSpecifierContext _localctx = new EnumSpecifierContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_enumSpecifier);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(239);
			match(ENUM);
			setState(241);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NAME) {
				{
				setState(240);
				match(NAME);
				}
			}

			setState(243);
			match(OPEN_BRACE);
			setState(244);
			enumeratorList(0);
			setState(245);
			match(CLOSE_BRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EnumeratorListContext extends ParserRuleContext {
		public EnumeratorContext enumerator() {
			return getRuleContext(EnumeratorContext.class,0);
		}
		public EnumeratorListContext enumeratorList() {
			return getRuleContext(EnumeratorListContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(langParser.COMMA, 0); }
		public EnumeratorListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_enumeratorList; }
	}

	public final EnumeratorListContext enumeratorList() throws RecognitionException {
		return enumeratorList(0);
	}

	private EnumeratorListContext enumeratorList(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		EnumeratorListContext _localctx = new EnumeratorListContext(_ctx, _parentState);
		EnumeratorListContext _prevctx = _localctx;
		int _startState = 32;
		enterRecursionRule(_localctx, 32, RULE_enumeratorList, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(248);
			enumerator();
			}
			_ctx.stop = _input.LT(-1);
			setState(255);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new EnumeratorListContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_enumeratorList);
					setState(250);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(251);
					match(COMMA);
					setState(252);
					enumerator();
					}
					} 
				}
				setState(257);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class EnumeratorContext extends ParserRuleContext {
		public TerminalNode NAME() { return getToken(langParser.NAME, 0); }
		public TerminalNode EQUALS() { return getToken(langParser.EQUALS, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public EnumeratorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_enumerator; }
	}

	public final EnumeratorContext enumerator() throws RecognitionException {
		EnumeratorContext _localctx = new EnumeratorContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_enumerator);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(258);
			match(NAME);
			setState(261);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				{
				setState(259);
				match(EQUALS);
				setState(260);
				expression();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FlowStatementContext extends ParserRuleContext {
		public BreakStatementContext breakStatement() {
			return getRuleContext(BreakStatementContext.class,0);
		}
		public ContinueStatementContext continueStatement() {
			return getRuleContext(ContinueStatementContext.class,0);
		}
		public ReturnStatementContext returnStatement() {
			return getRuleContext(ReturnStatementContext.class,0);
		}
		public FlowStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_flowStatement; }
	}

	public final FlowStatementContext flowStatement() throws RecognitionException {
		FlowStatementContext _localctx = new FlowStatementContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_flowStatement);
		try {
			setState(266);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BREAK:
				enterOuterAlt(_localctx, 1);
				{
				setState(263);
				breakStatement();
				}
				break;
			case CONTINUE:
				enterOuterAlt(_localctx, 2);
				{
				setState(264);
				continueStatement();
				}
				break;
			case RETURN:
				enterOuterAlt(_localctx, 3);
				{
				setState(265);
				returnStatement();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BreakStatementContext extends ParserRuleContext {
		public TerminalNode BREAK() { return getToken(langParser.BREAK, 0); }
		public BreakStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_breakStatement; }
	}

	public final BreakStatementContext breakStatement() throws RecognitionException {
		BreakStatementContext _localctx = new BreakStatementContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_breakStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(268);
			match(BREAK);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ContinueStatementContext extends ParserRuleContext {
		public TerminalNode CONTINUE() { return getToken(langParser.CONTINUE, 0); }
		public ContinueStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_continueStatement; }
	}

	public final ContinueStatementContext continueStatement() throws RecognitionException {
		ContinueStatementContext _localctx = new ContinueStatementContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_continueStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(270);
			match(CONTINUE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ReturnStatementContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(langParser.RETURN, 0); }
		public TestOrExpressionListContext testOrExpressionList() {
			return getRuleContext(TestOrExpressionListContext.class,0);
		}
		public ReturnStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnStatement; }
	}

	public final ReturnStatementContext returnStatement() throws RecognitionException {
		ReturnStatementContext _localctx = new ReturnStatementContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_returnStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(272);
			match(RETURN);
			setState(274);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 9)) & ~0x3f) == 0 && ((1L << (_la - 9)) & ((1L << (NOT - 9)) | (1L << (NULL - 9)) | (1L << (TRUE - 9)) | (1L << (FALSE - 9)) | (1L << (CARDINALITY_OP - 9)) | (1L << (OPEN_PAREN - 9)) | (1L << (ADD - 9)) | (1L << (MINUS - 9)) | (1L << (NOT_OP - 9)) | (1L << (NAME - 9)) | (1L << (STRING_LITERAL - 9)) | (1L << (CHAR_LITERAL - 9)) | (1L << (BYTES_LITERAL - 9)) | (1L << (DECIMAL_INTEGER - 9)) | (1L << (OCT_INTEGER - 9)) | (1L << (HEX_INTEGER - 9)) | (1L << (BIN_INTEGER - 9)) | (1L << (FLOAT_NUMBER - 9)) | (1L << (IMAG_NUMBER - 9)))) != 0)) {
				{
				setState(273);
				testOrExpressionList();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NameListContext extends ParserRuleContext {
		public List<TerminalNode> NAME() { return getTokens(langParser.NAME); }
		public TerminalNode NAME(int i) {
			return getToken(langParser.NAME, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(langParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(langParser.COMMA, i);
		}
		public NameListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_nameList; }
	}

	public final NameListContext nameList() throws RecognitionException {
		NameListContext _localctx = new NameListContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_nameList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(276);
			match(NAME);
			setState(281);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(277);
				match(COMMA);
				setState(278);
				match(NAME);
				}
				}
				setState(283);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CompoundStatementContext extends ParserRuleContext {
		public IfStatementContext ifStatement() {
			return getRuleContext(IfStatementContext.class,0);
		}
		public WhileStatementContext whileStatement() {
			return getRuleContext(WhileStatementContext.class,0);
		}
		public ForStatementContext forStatement() {
			return getRuleContext(ForStatementContext.class,0);
		}
		public FunctionDefinitionContext functionDefinition() {
			return getRuleContext(FunctionDefinitionContext.class,0);
		}
		public ClassDefinitionContext classDefinition() {
			return getRuleContext(ClassDefinitionContext.class,0);
		}
		public CompoundStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_compoundStatement; }
	}

	public final CompoundStatementContext compoundStatement() throws RecognitionException {
		CompoundStatementContext _localctx = new CompoundStatementContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_compoundStatement);
		try {
			setState(289);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IF:
				enterOuterAlt(_localctx, 1);
				{
				setState(284);
				ifStatement();
				}
				break;
			case WHILE:
				enterOuterAlt(_localctx, 2);
				{
				setState(285);
				whileStatement();
				}
				break;
			case FOR:
				enterOuterAlt(_localctx, 3);
				{
				setState(286);
				forStatement();
				}
				break;
			case INTEGER:
			case REAL:
			case CHAR:
			case STRING:
			case BOOLEAN:
			case NAME:
				enterOuterAlt(_localctx, 4);
				{
				setState(287);
				functionDefinition();
				}
				break;
			case CLASS:
				enterOuterAlt(_localctx, 5);
				{
				setState(288);
				classDefinition();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IfStatementContext extends ParserRuleContext {
		public List<TerminalNode> IF() { return getTokens(langParser.IF); }
		public TerminalNode IF(int i) {
			return getToken(langParser.IF, i);
		}
		public List<TestContext> test() {
			return getRuleContexts(TestContext.class);
		}
		public TestContext test(int i) {
			return getRuleContext(TestContext.class,i);
		}
		public List<TerminalNode> COLON() { return getTokens(langParser.COLON); }
		public TerminalNode COLON(int i) {
			return getToken(langParser.COLON, i);
		}
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public List<TerminalNode> ELSE() { return getTokens(langParser.ELSE); }
		public TerminalNode ELSE(int i) {
			return getToken(langParser.ELSE, i);
		}
		public IfStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStatement; }
	}

	public final IfStatementContext ifStatement() throws RecognitionException {
		IfStatementContext _localctx = new IfStatementContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_ifStatement);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(291);
			match(IF);
			setState(292);
			test();
			setState(293);
			match(COLON);
			setState(294);
			block();
			setState(303);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,26,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(295);
					match(ELSE);
					setState(296);
					match(IF);
					setState(297);
					test();
					setState(298);
					match(COLON);
					setState(299);
					block();
					}
					} 
				}
				setState(305);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,26,_ctx);
			}
			setState(309);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(306);
				match(ELSE);
				setState(307);
				match(COLON);
				setState(308);
				block();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class WhileStatementContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(langParser.WHILE, 0); }
		public TestContext test() {
			return getRuleContext(TestContext.class,0);
		}
		public TerminalNode COLON() { return getToken(langParser.COLON, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public WhileStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileStatement; }
	}

	public final WhileStatementContext whileStatement() throws RecognitionException {
		WhileStatementContext _localctx = new WhileStatementContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_whileStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(311);
			match(WHILE);
			setState(312);
			test();
			setState(313);
			match(COLON);
			setState(314);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ForStatementContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(langParser.FOR, 0); }
		public NameListContext nameList() {
			return getRuleContext(NameListContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(langParser.ASSIGN, 0); }
		public RangeListContext rangeList() {
			return getRuleContext(RangeListContext.class,0);
		}
		public TerminalNode COLON() { return getToken(langParser.COLON, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode STEP() { return getToken(langParser.STEP, 0); }
		public ExpressionListContext expressionList() {
			return getRuleContext(ExpressionListContext.class,0);
		}
		public ForStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forStatement; }
	}

	public final ForStatementContext forStatement() throws RecognitionException {
		ForStatementContext _localctx = new ForStatementContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_forStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(316);
			match(FOR);
			setState(317);
			nameList();
			setState(318);
			match(ASSIGN);
			setState(319);
			rangeList();
			setState(322);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==STEP) {
				{
				setState(320);
				match(STEP);
				setState(321);
				expressionList();
				}
			}

			setState(324);
			match(COLON);
			setState(325);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlockContext extends ParserRuleContext {
		public SimpleStatementContext simpleStatement() {
			return getRuleContext(SimpleStatementContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(langParser.NEWLINE, 0); }
		public TerminalNode INDENT() { return getToken(langParser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(langParser.DEDENT, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_block);
		int _la;
		try {
			setState(337);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case RETURN:
			case NOT:
			case NULL:
			case TRUE:
			case FALSE:
			case CONTINUE:
			case BREAK:
			case ENUM:
			case CARDINALITY_OP:
			case OPEN_PAREN:
			case ADD:
			case MINUS:
			case NOT_OP:
			case INTEGER:
			case REAL:
			case CHAR:
			case STRING:
			case BOOLEAN:
			case NAME:
			case STRING_LITERAL:
			case CHAR_LITERAL:
			case BYTES_LITERAL:
			case DECIMAL_INTEGER:
			case OCT_INTEGER:
			case HEX_INTEGER:
			case BIN_INTEGER:
			case FLOAT_NUMBER:
			case IMAG_NUMBER:
				enterOuterAlt(_localctx, 1);
				{
				setState(327);
				simpleStatement();
				}
				break;
			case NEWLINE:
				enterOuterAlt(_localctx, 2);
				{
				setState(328);
				match(NEWLINE);
				setState(329);
				match(INDENT);
				setState(331); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(330);
					statement();
					}
					}
					setState(333); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << RETURN) | (1L << IF) | (1L << WHILE) | (1L << FOR) | (1L << NOT) | (1L << NULL) | (1L << TRUE) | (1L << FALSE) | (1L << CLASS) | (1L << CONTINUE) | (1L << BREAK) | (1L << ENUM) | (1L << CARDINALITY_OP) | (1L << OPEN_PAREN) | (1L << ADD) | (1L << MINUS) | (1L << NOT_OP) | (1L << INTEGER) | (1L << REAL) | (1L << CHAR) | (1L << STRING) | (1L << BOOLEAN) | (1L << NAME) | (1L << STRING_LITERAL) | (1L << CHAR_LITERAL))) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & ((1L << (BYTES_LITERAL - 64)) | (1L << (DECIMAL_INTEGER - 64)) | (1L << (OCT_INTEGER - 64)) | (1L << (HEX_INTEGER - 64)) | (1L << (BIN_INTEGER - 64)) | (1L << (FLOAT_NUMBER - 64)) | (1L << (IMAG_NUMBER - 64)))) != 0) );
				setState(335);
				match(DEDENT);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TestContext extends ParserRuleContext {
		public List<TerminalNode> CARDINALITY_OP() { return getTokens(langParser.CARDINALITY_OP); }
		public TerminalNode CARDINALITY_OP(int i) {
			return getToken(langParser.CARDINALITY_OP, i);
		}
		public OrTestContext orTest() {
			return getRuleContext(OrTestContext.class,0);
		}
		public TestContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_test; }
	}

	public final TestContext test() throws RecognitionException {
		TestContext _localctx = new TestContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_test);
		try {
			setState(344);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CARDINALITY_OP:
				enterOuterAlt(_localctx, 1);
				{
				setState(339);
				match(CARDINALITY_OP);
				setState(340);
				orTest();
				setState(341);
				match(CARDINALITY_OP);
				}
				break;
			case NOT:
			case NULL:
			case TRUE:
			case FALSE:
			case OPEN_PAREN:
			case ADD:
			case MINUS:
			case NOT_OP:
			case NAME:
			case STRING_LITERAL:
			case CHAR_LITERAL:
			case BYTES_LITERAL:
			case DECIMAL_INTEGER:
			case OCT_INTEGER:
			case HEX_INTEGER:
			case BIN_INTEGER:
			case FLOAT_NUMBER:
			case IMAG_NUMBER:
				enterOuterAlt(_localctx, 2);
				{
				setState(343);
				orTest();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class OrTestContext extends ParserRuleContext {
		public List<AndTestContext> andTest() {
			return getRuleContexts(AndTestContext.class);
		}
		public AndTestContext andTest(int i) {
			return getRuleContext(AndTestContext.class,i);
		}
		public List<TerminalNode> OR() { return getTokens(langParser.OR); }
		public TerminalNode OR(int i) {
			return getToken(langParser.OR, i);
		}
		public OrTestContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_orTest; }
	}

	public final OrTestContext orTest() throws RecognitionException {
		OrTestContext _localctx = new OrTestContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_orTest);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(346);
			andTest();
			setState(351);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OR) {
				{
				{
				setState(347);
				match(OR);
				setState(348);
				andTest();
				}
				}
				setState(353);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AndTestContext extends ParserRuleContext {
		public List<NotTestContext> notTest() {
			return getRuleContexts(NotTestContext.class);
		}
		public NotTestContext notTest(int i) {
			return getRuleContext(NotTestContext.class,i);
		}
		public List<TerminalNode> AND() { return getTokens(langParser.AND); }
		public TerminalNode AND(int i) {
			return getToken(langParser.AND, i);
		}
		public AndTestContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_andTest; }
	}

	public final AndTestContext andTest() throws RecognitionException {
		AndTestContext _localctx = new AndTestContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_andTest);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(354);
			notTest();
			setState(359);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND) {
				{
				{
				setState(355);
				match(AND);
				setState(356);
				notTest();
				}
				}
				setState(361);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NotTestContext extends ParserRuleContext {
		public TerminalNode NOT() { return getToken(langParser.NOT, 0); }
		public NotTestContext notTest() {
			return getRuleContext(NotTestContext.class,0);
		}
		public ComparisonContext comparison() {
			return getRuleContext(ComparisonContext.class,0);
		}
		public NotTestContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_notTest; }
	}

	public final NotTestContext notTest() throws RecognitionException {
		NotTestContext _localctx = new NotTestContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_notTest);
		try {
			setState(365);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(362);
				match(NOT);
				setState(363);
				notTest();
				}
				break;
			case NULL:
			case TRUE:
			case FALSE:
			case OPEN_PAREN:
			case ADD:
			case MINUS:
			case NOT_OP:
			case NAME:
			case STRING_LITERAL:
			case CHAR_LITERAL:
			case BYTES_LITERAL:
			case DECIMAL_INTEGER:
			case OCT_INTEGER:
			case HEX_INTEGER:
			case BIN_INTEGER:
			case FLOAT_NUMBER:
			case IMAG_NUMBER:
				enterOuterAlt(_localctx, 2);
				{
				setState(364);
				comparison();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ComparisonContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<ComparisonOperatorContext> comparisonOperator() {
			return getRuleContexts(ComparisonOperatorContext.class);
		}
		public ComparisonOperatorContext comparisonOperator(int i) {
			return getRuleContext(ComparisonOperatorContext.class,i);
		}
		public ComparisonContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparison; }
	}

	public final ComparisonContext comparison() throws RecognitionException {
		ComparisonContext _localctx = new ComparisonContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_comparison);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(367);
			expression();
			setState(373);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LESS_THAN) | (1L << GREATER_THAN) | (1L << EQUALS) | (1L << GT_EQ) | (1L << LT_EQ) | (1L << NOT_EQ))) != 0)) {
				{
				{
				setState(368);
				comparisonOperator();
				setState(369);
				expression();
				}
				}
				setState(375);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ComparisonOperatorContext extends ParserRuleContext {
		public TerminalNode GREATER_THAN() { return getToken(langParser.GREATER_THAN, 0); }
		public TerminalNode LESS_THAN() { return getToken(langParser.LESS_THAN, 0); }
		public TerminalNode EQUALS() { return getToken(langParser.EQUALS, 0); }
		public TerminalNode GT_EQ() { return getToken(langParser.GT_EQ, 0); }
		public TerminalNode LT_EQ() { return getToken(langParser.LT_EQ, 0); }
		public TerminalNode NOT_EQ() { return getToken(langParser.NOT_EQ, 0); }
		public ComparisonOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparisonOperator; }
	}

	public final ComparisonOperatorContext comparisonOperator() throws RecognitionException {
		ComparisonOperatorContext _localctx = new ComparisonOperatorContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_comparisonOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(376);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LESS_THAN) | (1L << GREATER_THAN) | (1L << EQUALS) | (1L << GT_EQ) | (1L << LT_EQ) | (1L << NOT_EQ))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LoopRangeContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public RangeDelimiterContext rangeDelimiter() {
			return getRuleContext(RangeDelimiterContext.class,0);
		}
		public LoopRangeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_loopRange; }
	}

	public final LoopRangeContext loopRange() throws RecognitionException {
		LoopRangeContext _localctx = new LoopRangeContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_loopRange);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(378);
			expression();
			setState(382);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,36,_ctx) ) {
			case 1:
				{
				setState(379);
				rangeDelimiter();
				setState(380);
				expression();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class RangeDelimiterContext extends ParserRuleContext {
		public TerminalNode UNTIL() { return getToken(langParser.UNTIL, 0); }
		public TerminalNode COLON() { return getToken(langParser.COLON, 0); }
		public RangeDelimiterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rangeDelimiter; }
	}

	public final RangeDelimiterContext rangeDelimiter() throws RecognitionException {
		RangeDelimiterContext _localctx = new RangeDelimiterContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_rangeDelimiter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(384);
			_la = _input.LA(1);
			if ( !(_la==UNTIL || _la==COLON) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class RangeListContext extends ParserRuleContext {
		public List<LoopRangeContext> loopRange() {
			return getRuleContexts(LoopRangeContext.class);
		}
		public LoopRangeContext loopRange(int i) {
			return getRuleContext(LoopRangeContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(langParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(langParser.COMMA, i);
		}
		public RangeListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rangeList; }
	}

	public final RangeListContext rangeList() throws RecognitionException {
		RangeListContext _localctx = new RangeListContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_rangeList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(386);
			loopRange();
			setState(391);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(387);
				match(COMMA);
				setState(388);
				loopRange();
				}
				}
				setState(393);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public List<XorExpressionContext> xorExpression() {
			return getRuleContexts(XorExpressionContext.class);
		}
		public XorExpressionContext xorExpression(int i) {
			return getRuleContext(XorExpressionContext.class,i);
		}
		public List<TerminalNode> OR_OP() { return getTokens(langParser.OR_OP); }
		public TerminalNode OR_OP(int i) {
			return getToken(langParser.OR_OP, i);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_expression);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(394);
			xorExpression();
			setState(399);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,38,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(395);
					match(OR_OP);
					setState(396);
					xorExpression();
					}
					} 
				}
				setState(401);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,38,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class XorExpressionContext extends ParserRuleContext {
		public List<AndExpressionContext> andExpression() {
			return getRuleContexts(AndExpressionContext.class);
		}
		public AndExpressionContext andExpression(int i) {
			return getRuleContext(AndExpressionContext.class,i);
		}
		public List<TerminalNode> XOR() { return getTokens(langParser.XOR); }
		public TerminalNode XOR(int i) {
			return getToken(langParser.XOR, i);
		}
		public XorExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_xorExpression; }
	}

	public final XorExpressionContext xorExpression() throws RecognitionException {
		XorExpressionContext _localctx = new XorExpressionContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_xorExpression);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(402);
			andExpression();
			setState(407);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,39,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(403);
					match(XOR);
					setState(404);
					andExpression();
					}
					} 
				}
				setState(409);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,39,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AndExpressionContext extends ParserRuleContext {
		public List<ShiftExpressionContext> shiftExpression() {
			return getRuleContexts(ShiftExpressionContext.class);
		}
		public ShiftExpressionContext shiftExpression(int i) {
			return getRuleContext(ShiftExpressionContext.class,i);
		}
		public List<TerminalNode> AND_OP() { return getTokens(langParser.AND_OP); }
		public TerminalNode AND_OP(int i) {
			return getToken(langParser.AND_OP, i);
		}
		public AndExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_andExpression; }
	}

	public final AndExpressionContext andExpression() throws RecognitionException {
		AndExpressionContext _localctx = new AndExpressionContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_andExpression);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(410);
			shiftExpression();
			setState(415);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,40,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(411);
					match(AND_OP);
					setState(412);
					shiftExpression();
					}
					} 
				}
				setState(417);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,40,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ShiftExpressionContext extends ParserRuleContext {
		public List<ArithmeticExpressionContext> arithmeticExpression() {
			return getRuleContexts(ArithmeticExpressionContext.class);
		}
		public ArithmeticExpressionContext arithmeticExpression(int i) {
			return getRuleContext(ArithmeticExpressionContext.class,i);
		}
		public List<TerminalNode> LEFT_SHIFT() { return getTokens(langParser.LEFT_SHIFT); }
		public TerminalNode LEFT_SHIFT(int i) {
			return getToken(langParser.LEFT_SHIFT, i);
		}
		public List<TerminalNode> RIGHT_SHIFT() { return getTokens(langParser.RIGHT_SHIFT); }
		public TerminalNode RIGHT_SHIFT(int i) {
			return getToken(langParser.RIGHT_SHIFT, i);
		}
		public ShiftExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_shiftExpression; }
	}

	public final ShiftExpressionContext shiftExpression() throws RecognitionException {
		ShiftExpressionContext _localctx = new ShiftExpressionContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_shiftExpression);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(418);
			arithmeticExpression();
			setState(425);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,42,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					setState(423);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case LEFT_SHIFT:
						{
						setState(419);
						match(LEFT_SHIFT);
						setState(420);
						arithmeticExpression();
						}
						break;
					case RIGHT_SHIFT:
						{
						setState(421);
						match(RIGHT_SHIFT);
						setState(422);
						arithmeticExpression();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					} 
				}
				setState(427);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,42,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArithmeticExpressionContext extends ParserRuleContext {
		public List<TermContext> term() {
			return getRuleContexts(TermContext.class);
		}
		public TermContext term(int i) {
			return getRuleContext(TermContext.class,i);
		}
		public List<TerminalNode> ADD() { return getTokens(langParser.ADD); }
		public TerminalNode ADD(int i) {
			return getToken(langParser.ADD, i);
		}
		public List<TerminalNode> MINUS() { return getTokens(langParser.MINUS); }
		public TerminalNode MINUS(int i) {
			return getToken(langParser.MINUS, i);
		}
		public ArithmeticExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arithmeticExpression; }
	}

	public final ArithmeticExpressionContext arithmeticExpression() throws RecognitionException {
		ArithmeticExpressionContext _localctx = new ArithmeticExpressionContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_arithmeticExpression);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(428);
			term();
			setState(435);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,44,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					setState(433);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case ADD:
						{
						setState(429);
						match(ADD);
						setState(430);
						term();
						}
						break;
					case MINUS:
						{
						setState(431);
						match(MINUS);
						setState(432);
						term();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					} 
				}
				setState(437);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,44,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TermContext extends ParserRuleContext {
		public List<FactorContext> factor() {
			return getRuleContexts(FactorContext.class);
		}
		public FactorContext factor(int i) {
			return getRuleContext(FactorContext.class,i);
		}
		public List<TerminalNode> STAR() { return getTokens(langParser.STAR); }
		public TerminalNode STAR(int i) {
			return getToken(langParser.STAR, i);
		}
		public List<TerminalNode> DIV() { return getTokens(langParser.DIV); }
		public TerminalNode DIV(int i) {
			return getToken(langParser.DIV, i);
		}
		public List<TerminalNode> MOD() { return getTokens(langParser.MOD); }
		public TerminalNode MOD(int i) {
			return getToken(langParser.MOD, i);
		}
		public List<TerminalNode> IDIV() { return getTokens(langParser.IDIV); }
		public TerminalNode IDIV(int i) {
			return getToken(langParser.IDIV, i);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_term);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(438);
			factor();
			setState(449);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,46,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					setState(447);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case STAR:
						{
						setState(439);
						match(STAR);
						setState(440);
						factor();
						}
						break;
					case DIV:
						{
						setState(441);
						match(DIV);
						setState(442);
						factor();
						}
						break;
					case MOD:
						{
						setState(443);
						match(MOD);
						setState(444);
						factor();
						}
						break;
					case IDIV:
						{
						setState(445);
						match(IDIV);
						setState(446);
						factor();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					} 
				}
				setState(451);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,46,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FactorContext extends ParserRuleContext {
		public TerminalNode ADD() { return getToken(langParser.ADD, 0); }
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public TerminalNode MINUS() { return getToken(langParser.MINUS, 0); }
		public TerminalNode NOT_OP() { return getToken(langParser.NOT_OP, 0); }
		public PowerContext power() {
			return getRuleContext(PowerContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_factor);
		try {
			setState(459);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ADD:
				enterOuterAlt(_localctx, 1);
				{
				setState(452);
				match(ADD);
				setState(453);
				factor();
				}
				break;
			case MINUS:
				enterOuterAlt(_localctx, 2);
				{
				setState(454);
				match(MINUS);
				setState(455);
				factor();
				}
				break;
			case NOT_OP:
				enterOuterAlt(_localctx, 3);
				{
				setState(456);
				match(NOT_OP);
				setState(457);
				factor();
				}
				break;
			case NULL:
			case TRUE:
			case FALSE:
			case OPEN_PAREN:
			case NAME:
			case STRING_LITERAL:
			case CHAR_LITERAL:
			case BYTES_LITERAL:
			case DECIMAL_INTEGER:
			case OCT_INTEGER:
			case HEX_INTEGER:
			case BIN_INTEGER:
			case FLOAT_NUMBER:
			case IMAG_NUMBER:
				enterOuterAlt(_localctx, 4);
				{
				setState(458);
				power();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PowerContext extends ParserRuleContext {
		public AtomContext atom() {
			return getRuleContext(AtomContext.class,0);
		}
		public List<TrailerContext> trailer() {
			return getRuleContexts(TrailerContext.class);
		}
		public TrailerContext trailer(int i) {
			return getRuleContext(TrailerContext.class,i);
		}
		public TerminalNode POWER() { return getToken(langParser.POWER, 0); }
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public PowerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_power; }
	}

	public final PowerContext power() throws RecognitionException {
		PowerContext _localctx = new PowerContext(_ctx, getState());
		enterRule(_localctx, 88, RULE_power);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(461);
			atom();
			setState(465);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,48,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(462);
					trailer();
					}
					} 
				}
				setState(467);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,48,_ctx);
			}
			setState(470);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,49,_ctx) ) {
			case 1:
				{
				setState(468);
				match(POWER);
				setState(469);
				factor();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AtomContext extends ParserRuleContext {
		public TerminalNode OPEN_PAREN() { return getToken(langParser.OPEN_PAREN, 0); }
		public TestOrExpressionListContext testOrExpressionList() {
			return getRuleContext(TestOrExpressionListContext.class,0);
		}
		public TerminalNode CLOSE_PAREN() { return getToken(langParser.CLOSE_PAREN, 0); }
		public TerminalNode NAME() { return getToken(langParser.NAME, 0); }
		public NumberContext number() {
			return getRuleContext(NumberContext.class,0);
		}
		public List<StringContext> string() {
			return getRuleContexts(StringContext.class);
		}
		public StringContext string(int i) {
			return getRuleContext(StringContext.class,i);
		}
		public CharacterContext character() {
			return getRuleContext(CharacterContext.class,0);
		}
		public TerminalNode NULL() { return getToken(langParser.NULL, 0); }
		public TerminalNode TRUE() { return getToken(langParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(langParser.FALSE, 0); }
		public AtomContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atom; }
	}

	public final AtomContext atom() throws RecognitionException {
		AtomContext _localctx = new AtomContext(_ctx, getState());
		enterRule(_localctx, 90, RULE_atom);
		try {
			int _alt;
			setState(487);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPEN_PAREN:
				enterOuterAlt(_localctx, 1);
				{
				setState(472);
				match(OPEN_PAREN);
				setState(473);
				testOrExpressionList();
				setState(474);
				match(CLOSE_PAREN);
				}
				break;
			case NAME:
				enterOuterAlt(_localctx, 2);
				{
				setState(476);
				match(NAME);
				}
				break;
			case DECIMAL_INTEGER:
			case OCT_INTEGER:
			case HEX_INTEGER:
			case BIN_INTEGER:
			case FLOAT_NUMBER:
			case IMAG_NUMBER:
				enterOuterAlt(_localctx, 3);
				{
				setState(477);
				number();
				}
				break;
			case STRING_LITERAL:
			case BYTES_LITERAL:
				enterOuterAlt(_localctx, 4);
				{
				setState(479); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(478);
						string();
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(481); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,50,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				}
				break;
			case CHAR_LITERAL:
				enterOuterAlt(_localctx, 5);
				{
				setState(483);
				character();
				}
				break;
			case NULL:
				enterOuterAlt(_localctx, 6);
				{
				setState(484);
				match(NULL);
				}
				break;
			case TRUE:
				enterOuterAlt(_localctx, 7);
				{
				setState(485);
				match(TRUE);
				}
				break;
			case FALSE:
				enterOuterAlt(_localctx, 8);
				{
				setState(486);
				match(FALSE);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TrailerContext extends ParserRuleContext {
		public TrailerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_trailer; }
	 
		public TrailerContext() { }
		public void copyFrom(TrailerContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class TrailerSubsContext extends TrailerContext {
		public TerminalNode OPEN_BRACK() { return getToken(langParser.OPEN_BRACK, 0); }
		public SubscriptListContext subscriptList() {
			return getRuleContext(SubscriptListContext.class,0);
		}
		public TerminalNode CLOSE_BRACK() { return getToken(langParser.CLOSE_BRACK, 0); }
		public TrailerSubsContext(TrailerContext ctx) { copyFrom(ctx); }
	}
	public static class TrailerDotContext extends TrailerContext {
		public TerminalNode DOT() { return getToken(langParser.DOT, 0); }
		public TerminalNode NAME() { return getToken(langParser.NAME, 0); }
		public TrailerDotContext(TrailerContext ctx) { copyFrom(ctx); }
	}
	public static class TrailerArgsContext extends TrailerContext {
		public TerminalNode OPEN_PAREN() { return getToken(langParser.OPEN_PAREN, 0); }
		public TerminalNode CLOSE_PAREN() { return getToken(langParser.CLOSE_PAREN, 0); }
		public ArgListContext argList() {
			return getRuleContext(ArgListContext.class,0);
		}
		public TrailerArgsContext(TrailerContext ctx) { copyFrom(ctx); }
	}

	public final TrailerContext trailer() throws RecognitionException {
		TrailerContext _localctx = new TrailerContext(_ctx, getState());
		enterRule(_localctx, 92, RULE_trailer);
		int _la;
		try {
			setState(500);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPEN_PAREN:
				_localctx = new TrailerArgsContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(489);
				match(OPEN_PAREN);
				setState(491);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (((((_la - 9)) & ~0x3f) == 0 && ((1L << (_la - 9)) & ((1L << (NOT - 9)) | (1L << (NULL - 9)) | (1L << (TRUE - 9)) | (1L << (FALSE - 9)) | (1L << (CARDINALITY_OP - 9)) | (1L << (OPEN_PAREN - 9)) | (1L << (ADD - 9)) | (1L << (MINUS - 9)) | (1L << (NOT_OP - 9)) | (1L << (NAME - 9)) | (1L << (STRING_LITERAL - 9)) | (1L << (CHAR_LITERAL - 9)) | (1L << (BYTES_LITERAL - 9)) | (1L << (DECIMAL_INTEGER - 9)) | (1L << (OCT_INTEGER - 9)) | (1L << (HEX_INTEGER - 9)) | (1L << (BIN_INTEGER - 9)) | (1L << (FLOAT_NUMBER - 9)) | (1L << (IMAG_NUMBER - 9)))) != 0)) {
					{
					setState(490);
					argList();
					}
				}

				setState(493);
				match(CLOSE_PAREN);
				}
				break;
			case OPEN_BRACK:
				_localctx = new TrailerSubsContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(494);
				match(OPEN_BRACK);
				setState(495);
				subscriptList();
				setState(496);
				match(CLOSE_BRACK);
				}
				break;
			case DOT:
				_localctx = new TrailerDotContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(498);
				match(DOT);
				setState(499);
				match(NAME);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SubscriptListContext extends ParserRuleContext {
		public List<SubscriptContext> subscript() {
			return getRuleContexts(SubscriptContext.class);
		}
		public SubscriptContext subscript(int i) {
			return getRuleContext(SubscriptContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(langParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(langParser.COMMA, i);
		}
		public SubscriptListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subscriptList; }
	}

	public final SubscriptListContext subscriptList() throws RecognitionException {
		SubscriptListContext _localctx = new SubscriptListContext(_ctx, getState());
		enterRule(_localctx, 94, RULE_subscriptList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(502);
			subscript();
			setState(507);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(503);
				match(COMMA);
				setState(504);
				subscript();
				}
				}
				setState(509);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SubscriptContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public RangeDelimiterContext rangeDelimiter() {
			return getRuleContext(RangeDelimiterContext.class,0);
		}
		public TerminalNode STAR() { return getToken(langParser.STAR, 0); }
		public SubscriptContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subscript; }
	}

	public final SubscriptContext subscript() throws RecognitionException {
		SubscriptContext _localctx = new SubscriptContext(_ctx, getState());
		enterRule(_localctx, 96, RULE_subscript);
		try {
			setState(516);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,55,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(510);
				expression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(511);
				expression();
				setState(512);
				rangeDelimiter();
				setState(513);
				expression();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(515);
				match(STAR);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TestOrExpressionListContext extends ParserRuleContext {
		public List<TestOrExpressionContext> testOrExpression() {
			return getRuleContexts(TestOrExpressionContext.class);
		}
		public TestOrExpressionContext testOrExpression(int i) {
			return getRuleContext(TestOrExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(langParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(langParser.COMMA, i);
		}
		public TestOrExpressionListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_testOrExpressionList; }
	}

	public final TestOrExpressionListContext testOrExpressionList() throws RecognitionException {
		TestOrExpressionListContext _localctx = new TestOrExpressionListContext(_ctx, getState());
		enterRule(_localctx, 98, RULE_testOrExpressionList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(518);
			testOrExpression();
			setState(523);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(519);
				match(COMMA);
				setState(520);
				testOrExpression();
				}
				}
				setState(525);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ClassDefinitionContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(langParser.CLASS, 0); }
		public List<TerminalNode> NAME() { return getTokens(langParser.NAME); }
		public TerminalNode NAME(int i) {
			return getToken(langParser.NAME, i);
		}
		public TerminalNode COLON() { return getToken(langParser.COLON, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode OPEN_PAREN() { return getToken(langParser.OPEN_PAREN, 0); }
		public TerminalNode CLOSE_PAREN() { return getToken(langParser.CLOSE_PAREN, 0); }
		public ClassDefinitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classDefinition; }
	}

	public final ClassDefinitionContext classDefinition() throws RecognitionException {
		ClassDefinitionContext _localctx = new ClassDefinitionContext(_ctx, getState());
		enterRule(_localctx, 100, RULE_classDefinition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(526);
			match(CLASS);
			setState(527);
			match(NAME);
			setState(533);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==OPEN_PAREN) {
				{
				setState(528);
				match(OPEN_PAREN);
				setState(530);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==NAME) {
					{
					setState(529);
					match(NAME);
					}
				}

				setState(532);
				match(CLOSE_PAREN);
				}
			}

			setState(535);
			match(COLON);
			setState(536);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArgListContext extends ParserRuleContext {
		public List<ArgumentContext> argument() {
			return getRuleContexts(ArgumentContext.class);
		}
		public ArgumentContext argument(int i) {
			return getRuleContext(ArgumentContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(langParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(langParser.COMMA, i);
		}
		public ArgListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argList; }
	}

	public final ArgListContext argList() throws RecognitionException {
		ArgListContext _localctx = new ArgListContext(_ctx, getState());
		enterRule(_localctx, 102, RULE_argList);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(543);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,59,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(538);
					argument();
					setState(539);
					match(COMMA);
					}
					} 
				}
				setState(545);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,59,_ctx);
			}
			setState(546);
			argument();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArgumentContext extends ParserRuleContext {
		public List<TestContext> test() {
			return getRuleContexts(TestContext.class);
		}
		public TestContext test(int i) {
			return getRuleContext(TestContext.class,i);
		}
		public TerminalNode ASSIGN() { return getToken(langParser.ASSIGN, 0); }
		public ArgumentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argument; }
	}

	public final ArgumentContext argument() throws RecognitionException {
		ArgumentContext _localctx = new ArgumentContext(_ctx, getState());
		enterRule(_localctx, 104, RULE_argument);
		try {
			setState(553);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,60,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(548);
				test();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(549);
				test();
				setState(550);
				match(ASSIGN);
				setState(551);
				test();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StringContext extends ParserRuleContext {
		public TerminalNode STRING_LITERAL() { return getToken(langParser.STRING_LITERAL, 0); }
		public TerminalNode BYTES_LITERAL() { return getToken(langParser.BYTES_LITERAL, 0); }
		public StringContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_string; }
	}

	public final StringContext string() throws RecognitionException {
		StringContext _localctx = new StringContext(_ctx, getState());
		enterRule(_localctx, 106, RULE_string);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(555);
			_la = _input.LA(1);
			if ( !(_la==STRING_LITERAL || _la==BYTES_LITERAL) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CharacterContext extends ParserRuleContext {
		public TerminalNode CHAR_LITERAL() { return getToken(langParser.CHAR_LITERAL, 0); }
		public CharacterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_character; }
	}

	public final CharacterContext character() throws RecognitionException {
		CharacterContext _localctx = new CharacterContext(_ctx, getState());
		enterRule(_localctx, 108, RULE_character);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(557);
			match(CHAR_LITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NumberContext extends ParserRuleContext {
		public IntegerContext integer() {
			return getRuleContext(IntegerContext.class,0);
		}
		public TerminalNode FLOAT_NUMBER() { return getToken(langParser.FLOAT_NUMBER, 0); }
		public TerminalNode IMAG_NUMBER() { return getToken(langParser.IMAG_NUMBER, 0); }
		public NumberContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_number; }
	}

	public final NumberContext number() throws RecognitionException {
		NumberContext _localctx = new NumberContext(_ctx, getState());
		enterRule(_localctx, 110, RULE_number);
		try {
			setState(562);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case DECIMAL_INTEGER:
			case OCT_INTEGER:
			case HEX_INTEGER:
			case BIN_INTEGER:
				enterOuterAlt(_localctx, 1);
				{
				setState(559);
				integer();
				}
				break;
			case FLOAT_NUMBER:
				enterOuterAlt(_localctx, 2);
				{
				setState(560);
				match(FLOAT_NUMBER);
				}
				break;
			case IMAG_NUMBER:
				enterOuterAlt(_localctx, 3);
				{
				setState(561);
				match(IMAG_NUMBER);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IntegerContext extends ParserRuleContext {
		public TerminalNode DECIMAL_INTEGER() { return getToken(langParser.DECIMAL_INTEGER, 0); }
		public TerminalNode OCT_INTEGER() { return getToken(langParser.OCT_INTEGER, 0); }
		public TerminalNode HEX_INTEGER() { return getToken(langParser.HEX_INTEGER, 0); }
		public TerminalNode BIN_INTEGER() { return getToken(langParser.BIN_INTEGER, 0); }
		public IntegerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_integer; }
	}

	public final IntegerContext integer() throws RecognitionException {
		IntegerContext _localctx = new IntegerContext(_ctx, getState());
		enterRule(_localctx, 112, RULE_integer);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(564);
			_la = _input.LA(1);
			if ( !(((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & ((1L << (DECIMAL_INTEGER - 65)) | (1L << (OCT_INTEGER - 65)) | (1L << (HEX_INTEGER - 65)) | (1L << (BIN_INTEGER - 65)))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 16:
			return enumeratorList_sempred((EnumeratorListContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean enumeratorList_sempred(EnumeratorListContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3L\u0239\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\3\2\3\2\5\2w\n\2\3"+
		"\2\7\2z\n\2\f\2\16\2}\13\2\3\2\3\2\3\3\5\3\u0082\n\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\4\3\4\5\4\u008b\n\4\3\4\3\4\3\5\3\5\3\5\7\5\u0092\n\5\f\5\16\5\u0095"+
		"\13\5\3\5\3\5\3\5\3\5\3\5\7\5\u009c\n\5\f\5\16\5\u009f\13\5\3\5\3\5\3"+
		"\5\3\5\3\5\3\5\3\5\3\5\7\5\u00a9\n\5\f\5\16\5\u00ac\13\5\5\5\u00ae\n\5"+
		"\3\6\5\6\u00b1\n\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\b\5\b\u00bb\n\b\3\b\3"+
		"\b\3\t\3\t\5\t\u00c1\n\t\3\n\3\n\3\n\7\n\u00c6\n\n\f\n\16\n\u00c9\13\n"+
		"\3\n\5\n\u00cc\n\n\3\n\3\n\3\13\3\13\3\13\3\13\5\13\u00d4\n\13\3\f\3\f"+
		"\5\f\u00d8\n\f\3\f\3\f\3\r\3\r\3\16\3\16\3\16\7\16\u00e1\n\16\f\16\16"+
		"\16\u00e4\13\16\3\17\3\17\3\17\7\17\u00e9\n\17\f\17\16\17\u00ec\13\17"+
		"\3\20\3\20\5\20\u00f0\n\20\3\21\3\21\5\21\u00f4\n\21\3\21\3\21\3\21\3"+
		"\21\3\22\3\22\3\22\3\22\3\22\3\22\7\22\u0100\n\22\f\22\16\22\u0103\13"+
		"\22\3\23\3\23\3\23\5\23\u0108\n\23\3\24\3\24\3\24\5\24\u010d\n\24\3\25"+
		"\3\25\3\26\3\26\3\27\3\27\5\27\u0115\n\27\3\30\3\30\3\30\7\30\u011a\n"+
		"\30\f\30\16\30\u011d\13\30\3\31\3\31\3\31\3\31\3\31\5\31\u0124\n\31\3"+
		"\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\7\32\u0130\n\32\f\32"+
		"\16\32\u0133\13\32\3\32\3\32\3\32\5\32\u0138\n\32\3\33\3\33\3\33\3\33"+
		"\3\33\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0145\n\34\3\34\3\34\3\34\3\35"+
		"\3\35\3\35\3\35\6\35\u014e\n\35\r\35\16\35\u014f\3\35\3\35\5\35\u0154"+
		"\n\35\3\36\3\36\3\36\3\36\3\36\5\36\u015b\n\36\3\37\3\37\3\37\7\37\u0160"+
		"\n\37\f\37\16\37\u0163\13\37\3 \3 \3 \7 \u0168\n \f \16 \u016b\13 \3!"+
		"\3!\3!\5!\u0170\n!\3\"\3\"\3\"\3\"\7\"\u0176\n\"\f\"\16\"\u0179\13\"\3"+
		"#\3#\3$\3$\3$\3$\5$\u0181\n$\3%\3%\3&\3&\3&\7&\u0188\n&\f&\16&\u018b\13"+
		"&\3\'\3\'\3\'\7\'\u0190\n\'\f\'\16\'\u0193\13\'\3(\3(\3(\7(\u0198\n(\f"+
		"(\16(\u019b\13(\3)\3)\3)\7)\u01a0\n)\f)\16)\u01a3\13)\3*\3*\3*\3*\3*\7"+
		"*\u01aa\n*\f*\16*\u01ad\13*\3+\3+\3+\3+\3+\7+\u01b4\n+\f+\16+\u01b7\13"+
		"+\3,\3,\3,\3,\3,\3,\3,\3,\3,\7,\u01c2\n,\f,\16,\u01c5\13,\3-\3-\3-\3-"+
		"\3-\3-\3-\5-\u01ce\n-\3.\3.\7.\u01d2\n.\f.\16.\u01d5\13.\3.\3.\5.\u01d9"+
		"\n.\3/\3/\3/\3/\3/\3/\3/\6/\u01e2\n/\r/\16/\u01e3\3/\3/\3/\3/\5/\u01ea"+
		"\n/\3\60\3\60\5\60\u01ee\n\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\5\60"+
		"\u01f7\n\60\3\61\3\61\3\61\7\61\u01fc\n\61\f\61\16\61\u01ff\13\61\3\62"+
		"\3\62\3\62\3\62\3\62\3\62\5\62\u0207\n\62\3\63\3\63\3\63\7\63\u020c\n"+
		"\63\f\63\16\63\u020f\13\63\3\64\3\64\3\64\3\64\5\64\u0215\n\64\3\64\5"+
		"\64\u0218\n\64\3\64\3\64\3\64\3\65\3\65\3\65\7\65\u0220\n\65\f\65\16\65"+
		"\u0223\13\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\5\66\u022c\n\66\3\67\3"+
		"\67\38\38\39\39\39\59\u0235\n9\3:\3:\3:\2\3\";\2\4\6\b\n\f\16\20\22\24"+
		"\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnpr\2"+
		"\b\3\2\66\67\4\28<??\3\2.\63\4\2\24\24\32\32\4\2@@BB\3\2CF\2\u0250\2{"+
		"\3\2\2\2\4\u0081\3\2\2\2\6\u0088\3\2\2\2\b\u00ad\3\2\2\2\n\u00b0\3\2\2"+
		"\2\f\u00b5\3\2\2\2\16\u00b7\3\2\2\2\20\u00c0\3\2\2\2\22\u00c2\3\2\2\2"+
		"\24\u00d3\3\2\2\2\26\u00d5\3\2\2\2\30\u00db\3\2\2\2\32\u00dd\3\2\2\2\34"+
		"\u00e5\3\2\2\2\36\u00ef\3\2\2\2 \u00f1\3\2\2\2\"\u00f9\3\2\2\2$\u0104"+
		"\3\2\2\2&\u010c\3\2\2\2(\u010e\3\2\2\2*\u0110\3\2\2\2,\u0112\3\2\2\2."+
		"\u0116\3\2\2\2\60\u0123\3\2\2\2\62\u0125\3\2\2\2\64\u0139\3\2\2\2\66\u013e"+
		"\3\2\2\28\u0153\3\2\2\2:\u015a\3\2\2\2<\u015c\3\2\2\2>\u0164\3\2\2\2@"+
		"\u016f\3\2\2\2B\u0171\3\2\2\2D\u017a\3\2\2\2F\u017c\3\2\2\2H\u0182\3\2"+
		"\2\2J\u0184\3\2\2\2L\u018c\3\2\2\2N\u0194\3\2\2\2P\u019c\3\2\2\2R\u01a4"+
		"\3\2\2\2T\u01ae\3\2\2\2V\u01b8\3\2\2\2X\u01cd\3\2\2\2Z\u01cf\3\2\2\2\\"+
		"\u01e9\3\2\2\2^\u01f6\3\2\2\2`\u01f8\3\2\2\2b\u0206\3\2\2\2d\u0208\3\2"+
		"\2\2f\u0210\3\2\2\2h\u0221\3\2\2\2j\u022b\3\2\2\2l\u022d\3\2\2\2n\u022f"+
		"\3\2\2\2p\u0234\3\2\2\2r\u0236\3\2\2\2tz\7>\2\2uw\5\16\b\2vu\3\2\2\2v"+
		"w\3\2\2\2wx\3\2\2\2xz\5\20\t\2yt\3\2\2\2yv\3\2\2\2z}\3\2\2\2{y\3\2\2\2"+
		"{|\3\2\2\2|~\3\2\2\2}{\3\2\2\2~\177\7\2\2\3\177\3\3\2\2\2\u0080\u0082"+
		"\5\30\r\2\u0081\u0080\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0083\3\2\2\2"+
		"\u0083\u0084\7?\2\2\u0084\u0085\5\6\4\2\u0085\u0086\7\32\2\2\u0086\u0087"+
		"\58\35\2\u0087\5\3\2\2\2\u0088\u008a\7\27\2\2\u0089\u008b\5\b\5\2\u008a"+
		"\u0089\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008d\7\30"+
		"\2\2\u008d\7\3\2\2\2\u008e\u0093\5\n\6\2\u008f\u0090\7\31\2\2\u0090\u0092"+
		"\5\n\6\2\u0091\u008f\3\2\2\2\u0092\u0095\3\2\2\2\u0093\u0091\3\2\2\2\u0093"+
		"\u0094\3\2\2\2\u0094\u009d\3\2\2\2\u0095\u0093\3\2\2\2\u0096\u0097\7\31"+
		"\2\2\u0097\u0098\5\n\6\2\u0098\u0099\7\35\2\2\u0099\u009a\5L\'\2\u009a"+
		"\u009c\3\2\2\2\u009b\u0096\3\2\2\2\u009c\u009f\3\2\2\2\u009d\u009b\3\2"+
		"\2\2\u009d\u009e\3\2\2\2\u009e\u00ae\3\2\2\2\u009f\u009d\3\2\2\2\u00a0"+
		"\u00a1\5\n\6\2\u00a1\u00a2\7\35\2\2\u00a2\u00aa\5L\'\2\u00a3\u00a4\7\31"+
		"\2\2\u00a4\u00a5\5\n\6\2\u00a5\u00a6\7\35\2\2\u00a6\u00a7\5L\'\2\u00a7"+
		"\u00a9\3\2\2\2\u00a8\u00a3\3\2\2\2\u00a9\u00ac\3\2\2\2\u00aa\u00a8\3\2"+
		"\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ae\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ad"+
		"\u008e\3\2\2\2\u00ad\u00a0\3\2\2\2\u00ae\t\3\2\2\2\u00af\u00b1\5\f\7\2"+
		"\u00b0\u00af\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3"+
		"\5\30\r\2\u00b3\u00b4\7?\2\2\u00b4\13\3\2\2\2\u00b5\u00b6\t\2\2\2\u00b6"+
		"\r\3\2\2\2\u00b7\u00b8\7\4\2\2\u00b8\u00ba\5.\30\2\u00b9\u00bb\7\33\2"+
		"\2\u00ba\u00b9\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00bd"+
		"\7>\2\2\u00bd\17\3\2\2\2\u00be\u00c1\5\22\n\2\u00bf\u00c1\5\60\31\2\u00c0"+
		"\u00be\3\2\2\2\u00c0\u00bf\3\2\2\2\u00c1\21\3\2\2\2\u00c2\u00c7\5\24\13"+
		"\2\u00c3\u00c4\7\33\2\2\u00c4\u00c6\5\24\13\2\u00c5\u00c3\3\2\2\2\u00c6"+
		"\u00c9\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00cb\3\2"+
		"\2\2\u00c9\u00c7\3\2\2\2\u00ca\u00cc\7\33\2\2\u00cb\u00ca\3\2\2\2\u00cb"+
		"\u00cc\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00ce\7>\2\2\u00ce\23\3\2\2\2"+
		"\u00cf\u00d4\5\32\16\2\u00d0\u00d4\5\26\f\2\u00d1\u00d4\5&\24\2\u00d2"+
		"\u00d4\5 \21\2\u00d3\u00cf\3\2\2\2\u00d3\u00d0\3\2\2\2\u00d3\u00d1\3\2"+
		"\2\2\u00d3\u00d2\3\2\2\2\u00d4\25\3\2\2\2\u00d5\u00d7\5\30\r\2\u00d6\u00d8"+
		"\7=\2\2\u00d7\u00d6\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9"+
		"\u00da\5\32\16\2\u00da\27\3\2\2\2\u00db\u00dc\t\3\2\2\u00dc\31\3\2\2\2"+
		"\u00dd\u00e2\5d\63\2\u00de\u00df\7\35\2\2\u00df\u00e1\5d\63\2\u00e0\u00de"+
		"\3\2\2\2\u00e1\u00e4\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3"+
		"\33\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e5\u00ea\5L\'\2\u00e6\u00e7\7\31\2"+
		"\2\u00e7\u00e9\5L\'\2\u00e8\u00e6\3\2\2\2\u00e9\u00ec\3\2\2\2\u00ea\u00e8"+
		"\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\35\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ed"+
		"\u00f0\5:\36\2\u00ee\u00f0\5L\'\2\u00ef\u00ed\3\2\2\2\u00ef\u00ee\3\2"+
		"\2\2\u00f0\37\3\2\2\2\u00f1\u00f3\7\22\2\2\u00f2\u00f4\7?\2\2\u00f3\u00f2"+
		"\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f6\7,\2\2\u00f6"+
		"\u00f7\5\"\22\2\u00f7\u00f8\7-\2\2\u00f8!\3\2\2\2\u00f9\u00fa\b\22\1\2"+
		"\u00fa\u00fb\5$\23\2\u00fb\u0101\3\2\2\2\u00fc\u00fd\f\3\2\2\u00fd\u00fe"+
		"\7\31\2\2\u00fe\u0100\5$\23\2\u00ff\u00fc\3\2\2\2\u0100\u0103\3\2\2\2"+
		"\u0101\u00ff\3\2\2\2\u0101\u0102\3\2\2\2\u0102#\3\2\2\2\u0103\u0101\3"+
		"\2\2\2\u0104\u0107\7?\2\2\u0105\u0106\7\60\2\2\u0106\u0108\5L\'\2\u0107"+
		"\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108%\3\2\2\2\u0109\u010d\5(\25\2"+
		"\u010a\u010d\5*\26\2\u010b\u010d\5,\27\2\u010c\u0109\3\2\2\2\u010c\u010a"+
		"\3\2\2\2\u010c\u010b\3\2\2\2\u010d\'\3\2\2\2\u010e\u010f\7\21\2\2\u010f"+
		")\3\2\2\2\u0110\u0111\7\20\2\2\u0111+\3\2\2\2\u0112\u0114\7\3\2\2\u0113"+
		"\u0115\5d\63\2\u0114\u0113\3\2\2\2\u0114\u0115\3\2\2\2\u0115-\3\2\2\2"+
		"\u0116\u011b\7?\2\2\u0117\u0118\7\31\2\2\u0118\u011a\7?\2\2\u0119\u0117"+
		"\3\2\2\2\u011a\u011d\3\2\2\2\u011b\u0119\3\2\2\2\u011b\u011c\3\2\2\2\u011c"+
		"/\3\2\2\2\u011d\u011b\3\2\2\2\u011e\u0124\5\62\32\2\u011f\u0124\5\64\33"+
		"\2\u0120\u0124\5\66\34\2\u0121\u0124\5\4\3\2\u0122\u0124\5f\64\2\u0123"+
		"\u011e\3\2\2\2\u0123\u011f\3\2\2\2\u0123\u0120\3\2\2\2\u0123\u0121\3\2"+
		"\2\2\u0123\u0122\3\2\2\2\u0124\61\3\2\2\2\u0125\u0126\7\5\2\2\u0126\u0127"+
		"\5:\36\2\u0127\u0128\7\32\2\2\u0128\u0131\58\35\2\u0129\u012a\7\6\2\2"+
		"\u012a\u012b\7\5\2\2\u012b\u012c\5:\36\2\u012c\u012d\7\32\2\2\u012d\u012e"+
		"\58\35\2\u012e\u0130\3\2\2\2\u012f\u0129\3\2\2\2\u0130\u0133\3\2\2\2\u0131"+
		"\u012f\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0137\3\2\2\2\u0133\u0131\3\2"+
		"\2\2\u0134\u0135\7\6\2\2\u0135\u0136\7\32\2\2\u0136\u0138\58\35\2\u0137"+
		"\u0134\3\2\2\2\u0137\u0138\3\2\2\2\u0138\63\3\2\2\2\u0139\u013a\7\7\2"+
		"\2\u013a\u013b\5:\36\2\u013b\u013c\7\32\2\2\u013c\u013d\58\35\2\u013d"+
		"\65\3\2\2\2\u013e\u013f\7\b\2\2\u013f\u0140\5.\30\2\u0140\u0141\7\35\2"+
		"\2\u0141\u0144\5J&\2\u0142\u0143\7\23\2\2\u0143\u0145\5\34\17\2\u0144"+
		"\u0142\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0147\7\32"+
		"\2\2\u0147\u0148\58\35\2\u0148\67\3\2\2\2\u0149\u0154\5\22\n\2\u014a\u014b"+
		"\7>\2\2\u014b\u014d\7K\2\2\u014c\u014e\5\20\t\2\u014d\u014c\3\2\2\2\u014e"+
		"\u014f\3\2\2\2\u014f\u014d\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u0151\3\2"+
		"\2\2\u0151\u0152\7L\2\2\u0152\u0154\3\2\2\2\u0153\u0149\3\2\2\2\u0153"+
		"\u014a\3\2\2\2\u01549\3\2\2\2\u0155\u0156\7\26\2\2\u0156\u0157\5<\37\2"+
		"\u0157\u0158\7\26\2\2\u0158\u015b\3\2\2\2\u0159\u015b\5<\37\2\u015a\u0155"+
		"\3\2\2\2\u015a\u0159\3\2\2\2\u015b;\3\2\2\2\u015c\u0161\5> \2\u015d\u015e"+
		"\7\t\2\2\u015e\u0160\5> \2\u015f\u015d\3\2\2\2\u0160\u0163\3\2\2\2\u0161"+
		"\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162=\3\2\2\2\u0163\u0161\3\2\2\2"+
		"\u0164\u0169\5@!\2\u0165\u0166\7\n\2\2\u0166\u0168\5@!\2\u0167\u0165\3"+
		"\2\2\2\u0168\u016b\3\2\2\2\u0169\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016a"+
		"?\3\2\2\2\u016b\u0169\3\2\2\2\u016c\u016d\7\13\2\2\u016d\u0170\5@!\2\u016e"+
		"\u0170\5B\"\2\u016f\u016c\3\2\2\2\u016f\u016e\3\2\2\2\u0170A\3\2\2\2\u0171"+
		"\u0177\5L\'\2\u0172\u0173\5D#\2\u0173\u0174\5L\'\2\u0174\u0176\3\2\2\2"+
		"\u0175\u0172\3\2\2\2\u0176\u0179\3\2\2\2\u0177\u0175\3\2\2\2\u0177\u0178"+
		"\3\2\2\2\u0178C\3\2\2\2\u0179\u0177\3\2\2\2\u017a\u017b\t\4\2\2\u017b"+
		"E\3\2\2\2\u017c\u0180\5L\'\2\u017d\u017e\5H%\2\u017e\u017f\5L\'\2\u017f"+
		"\u0181\3\2\2\2\u0180\u017d\3\2\2\2\u0180\u0181\3\2\2\2\u0181G\3\2\2\2"+
		"\u0182\u0183\t\5\2\2\u0183I\3\2\2\2\u0184\u0189\5F$\2\u0185\u0186\7\31"+
		"\2\2\u0186\u0188\5F$\2\u0187\u0185\3\2\2\2\u0188\u018b\3\2\2\2\u0189\u0187"+
		"\3\2\2\2\u0189\u018a\3\2\2\2\u018aK\3\2\2\2\u018b\u0189\3\2\2\2\u018c"+
		"\u0191\5N(\2\u018d\u018e\7 \2\2\u018e\u0190\5N(\2\u018f\u018d\3\2\2\2"+
		"\u0190\u0193\3\2\2\2\u0191\u018f\3\2\2\2\u0191\u0192\3\2\2\2\u0192M\3"+
		"\2\2\2\u0193\u0191\3\2\2\2\u0194\u0199\5P)\2\u0195\u0196\7!\2\2\u0196"+
		"\u0198\5P)\2\u0197\u0195\3\2\2\2\u0198\u019b\3\2\2\2\u0199\u0197\3\2\2"+
		"\2\u0199\u019a\3\2\2\2\u019aO\3\2\2\2\u019b\u0199\3\2\2\2\u019c\u01a1"+
		"\5R*\2\u019d\u019e\7\"\2\2\u019e\u01a0\5R*\2\u019f\u019d\3\2\2\2\u01a0"+
		"\u01a3\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2Q\3\2\2\2"+
		"\u01a3\u01a1\3\2\2\2\u01a4\u01ab\5T+\2\u01a5\u01a6\7#\2\2\u01a6\u01aa"+
		"\5T+\2\u01a7\u01a8\7$\2\2\u01a8\u01aa\5T+\2\u01a9\u01a5\3\2\2\2\u01a9"+
		"\u01a7\3\2\2\2\u01aa\u01ad\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ab\u01ac\3\2"+
		"\2\2\u01acS\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ae\u01b5\5V,\2\u01af\u01b0"+
		"\7%\2\2\u01b0\u01b4\5V,\2\u01b1\u01b2\7&\2\2\u01b2\u01b4\5V,\2\u01b3\u01af"+
		"\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b4\u01b7\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b5"+
		"\u01b6\3\2\2\2\u01b6U\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b8\u01c3\5X-\2\u01b9"+
		"\u01ba\7\'\2\2\u01ba\u01c2\5X-\2\u01bb\u01bc\7(\2\2\u01bc\u01c2\5X-\2"+
		"\u01bd\u01be\7)\2\2\u01be\u01c2\5X-\2\u01bf\u01c0\7*\2\2\u01c0\u01c2\5"+
		"X-\2\u01c1\u01b9\3\2\2\2\u01c1\u01bb\3\2\2\2\u01c1\u01bd\3\2\2\2\u01c1"+
		"\u01bf\3\2\2\2\u01c2\u01c5\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c3\u01c4\3\2"+
		"\2\2\u01c4W\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c6\u01c7\7%\2\2\u01c7\u01ce"+
		"\5X-\2\u01c8\u01c9\7&\2\2\u01c9\u01ce\5X-\2\u01ca\u01cb\7+\2\2\u01cb\u01ce"+
		"\5X-\2\u01cc\u01ce\5Z.\2\u01cd\u01c6\3\2\2\2\u01cd\u01c8\3\2\2\2\u01cd"+
		"\u01ca\3\2\2\2\u01cd\u01cc\3\2\2\2\u01ceY\3\2\2\2\u01cf\u01d3\5\\/\2\u01d0"+
		"\u01d2\5^\60\2\u01d1\u01d0\3\2\2\2\u01d2\u01d5\3\2\2\2\u01d3\u01d1\3\2"+
		"\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d8\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d6"+
		"\u01d7\7\34\2\2\u01d7\u01d9\5X-\2\u01d8\u01d6\3\2\2\2\u01d8\u01d9\3\2"+
		"\2\2\u01d9[\3\2\2\2\u01da\u01db\7\27\2\2\u01db\u01dc\5d\63\2\u01dc\u01dd"+
		"\7\30\2\2\u01dd\u01ea\3\2\2\2\u01de\u01ea\7?\2\2\u01df\u01ea\5p9\2\u01e0"+
		"\u01e2\5l\67\2\u01e1\u01e0\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3\u01e1\3\2"+
		"\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01ea\3\2\2\2\u01e5\u01ea\5n8\2\u01e6\u01ea"+
		"\7\f\2\2\u01e7\u01ea\7\r\2\2\u01e8\u01ea\7\16\2\2\u01e9\u01da\3\2\2\2"+
		"\u01e9\u01de\3\2\2\2\u01e9\u01df\3\2\2\2\u01e9\u01e1\3\2\2\2\u01e9\u01e5"+
		"\3\2\2\2\u01e9\u01e6\3\2\2\2\u01e9\u01e7\3\2\2\2\u01e9\u01e8\3\2\2\2\u01ea"+
		"]\3\2\2\2\u01eb\u01ed\7\27\2\2\u01ec\u01ee\5h\65\2\u01ed\u01ec\3\2\2\2"+
		"\u01ed\u01ee\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef\u01f7\7\30\2\2\u01f0\u01f1"+
		"\7\36\2\2\u01f1\u01f2\5`\61\2\u01f2\u01f3\7\37\2\2\u01f3\u01f7\3\2\2\2"+
		"\u01f4\u01f5\7\25\2\2\u01f5\u01f7\7?\2\2\u01f6\u01eb\3\2\2\2\u01f6\u01f0"+
		"\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f7_\3\2\2\2\u01f8\u01fd\5b\62\2\u01f9"+
		"\u01fa\7\31\2\2\u01fa\u01fc\5b\62\2\u01fb\u01f9\3\2\2\2\u01fc\u01ff\3"+
		"\2\2\2\u01fd\u01fb\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fea\3\2\2\2\u01ff\u01fd"+
		"\3\2\2\2\u0200\u0207\5L\'\2\u0201\u0202\5L\'\2\u0202\u0203\5H%\2\u0203"+
		"\u0204\5L\'\2\u0204\u0207\3\2\2\2\u0205\u0207\7\'\2\2\u0206\u0200\3\2"+
		"\2\2\u0206\u0201\3\2\2\2\u0206\u0205\3\2\2\2\u0207c\3\2\2\2\u0208\u020d"+
		"\5\36\20\2\u0209\u020a\7\31\2\2\u020a\u020c\5\36\20\2\u020b\u0209\3\2"+
		"\2\2\u020c\u020f\3\2\2\2\u020d\u020b\3\2\2\2\u020d\u020e\3\2\2\2\u020e"+
		"e\3\2\2\2\u020f\u020d\3\2\2\2\u0210\u0211\7\17\2\2\u0211\u0217\7?\2\2"+
		"\u0212\u0214\7\27\2\2\u0213\u0215\7?\2\2\u0214\u0213\3\2\2\2\u0214\u0215"+
		"\3\2\2\2\u0215\u0216\3\2\2\2\u0216\u0218\7\30\2\2\u0217\u0212\3\2\2\2"+
		"\u0217\u0218\3\2\2\2\u0218\u0219\3\2\2\2\u0219\u021a\7\32\2\2\u021a\u021b"+
		"\58\35\2\u021bg\3\2\2\2\u021c\u021d\5j\66\2\u021d\u021e\7\31\2\2\u021e"+
		"\u0220\3\2\2\2\u021f\u021c\3\2\2\2\u0220\u0223\3\2\2\2\u0221\u021f\3\2"+
		"\2\2\u0221\u0222\3\2\2\2\u0222\u0224\3\2\2\2\u0223\u0221\3\2\2\2\u0224"+
		"\u0225\5j\66\2\u0225i\3\2\2\2\u0226\u022c\5:\36\2\u0227\u0228\5:\36\2"+
		"\u0228\u0229\7\35\2\2\u0229\u022a\5:\36\2\u022a\u022c\3\2\2\2\u022b\u0226"+
		"\3\2\2\2\u022b\u0227\3\2\2\2\u022ck\3\2\2\2\u022d\u022e\t\6\2\2\u022e"+
		"m\3\2\2\2\u022f\u0230\7A\2\2\u0230o\3\2\2\2\u0231\u0235\5r:\2\u0232\u0235"+
		"\7G\2\2\u0233\u0235\7H\2\2\u0234\u0231\3\2\2\2\u0234\u0232\3\2\2\2\u0234"+
		"\u0233\3\2\2\2\u0235q\3\2\2\2\u0236\u0237\t\7\2\2\u0237s\3\2\2\2@vy{\u0081"+
		"\u008a\u0093\u009d\u00aa\u00ad\u00b0\u00ba\u00c0\u00c7\u00cb\u00d3\u00d7"+
		"\u00e2\u00ea\u00ef\u00f3\u0101\u0107\u010c\u0114\u011b\u0123\u0131\u0137"+
		"\u0144\u014f\u0153\u015a\u0161\u0169\u016f\u0177\u0180\u0189\u0191\u0199"+
		"\u01a1\u01a9\u01ab\u01b3\u01b5\u01c1\u01c3\u01cd\u01d3\u01d8\u01e3\u01e9"+
		"\u01ed\u01f6\u01fd\u0206\u020d\u0214\u0217\u0221\u022b\u0234";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}