// Generated from /home/gian/uerjInterpreter/Lang.g4 by ANTLR 4.7
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class LangParser extends Parser {
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
		BYTES_LITERAL=63, DECIMAL_INTEGER=64, OCT_INTEGER=65, HEX_INTEGER=66, 
		BIN_INTEGER=67, FLOAT_NUMBER=68, IMAG_NUMBER=69, SKIP_=70, UNKNOWN_CHAR=71, 
		INDENT=72, DEDENT=73;
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
		RULE_number = 54, RULE_integer = 55;
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
		"classDefinition", "argList", "argument", "string", "number", "integer"
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
		"NAME", "STRING_LITERAL", "BYTES_LITERAL", "DECIMAL_INTEGER", "OCT_INTEGER", 
		"HEX_INTEGER", "BIN_INTEGER", "FLOAT_NUMBER", "IMAG_NUMBER", "SKIP_", 
		"UNKNOWN_CHAR", "INDENT", "DEDENT"
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
	public String getGrammarFileName() { return "Lang.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public LangParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class RContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(LangParser.EOF, 0); }
		public List<TerminalNode> NEWLINE() { return getTokens(LangParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(LangParser.NEWLINE, i);
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
			setState(119);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << RETURN) | (1L << IMPORT) | (1L << IF) | (1L << WHILE) | (1L << FOR) | (1L << NOT) | (1L << NULL) | (1L << TRUE) | (1L << FALSE) | (1L << CLASS) | (1L << CONTINUE) | (1L << BREAK) | (1L << ENUM) | (1L << CARDINALITY_OP) | (1L << OPEN_PAREN) | (1L << ADD) | (1L << MINUS) | (1L << NOT_OP) | (1L << INTEGER) | (1L << REAL) | (1L << CHAR) | (1L << STRING) | (1L << BOOLEAN) | (1L << NEWLINE) | (1L << NAME) | (1L << STRING_LITERAL) | (1L << BYTES_LITERAL))) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & ((1L << (DECIMAL_INTEGER - 64)) | (1L << (OCT_INTEGER - 64)) | (1L << (HEX_INTEGER - 64)) | (1L << (BIN_INTEGER - 64)) | (1L << (FLOAT_NUMBER - 64)) | (1L << (IMAG_NUMBER - 64)))) != 0)) {
				{
				setState(117);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case NEWLINE:
					{
					setState(112);
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
				case BYTES_LITERAL:
				case DECIMAL_INTEGER:
				case OCT_INTEGER:
				case HEX_INTEGER:
				case BIN_INTEGER:
				case FLOAT_NUMBER:
				case IMAG_NUMBER:
					{
					setState(114);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==IMPORT) {
						{
						setState(113);
						importStatement();
						}
					}

					setState(116);
					statement();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(121);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(122);
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
		public TerminalNode NAME() { return getToken(LangParser.NAME, 0); }
		public ParametersContext parameters() {
			return getRuleContext(ParametersContext.class,0);
		}
		public TerminalNode COLON() { return getToken(LangParser.COLON, 0); }
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
			setState(125);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				setState(124);
				dataType();
				}
				break;
			}
			setState(127);
			match(NAME);
			setState(128);
			parameters();
			setState(129);
			match(COLON);
			setState(130);
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
		public TerminalNode OPEN_PAREN() { return getToken(LangParser.OPEN_PAREN, 0); }
		public TerminalNode CLOSE_PAREN() { return getToken(LangParser.CLOSE_PAREN, 0); }
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
			setState(132);
			match(OPEN_PAREN);
			setState(134);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << VAL) | (1L << REF) | (1L << INTEGER) | (1L << REAL) | (1L << CHAR) | (1L << STRING) | (1L << BOOLEAN) | (1L << NAME))) != 0)) {
				{
				setState(133);
				typedArgsList();
				}
			}

			setState(136);
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
		public List<TerminalNode> COMMA() { return getTokens(LangParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(LangParser.COMMA, i);
		}
		public List<TerminalNode> ASSIGN() { return getTokens(LangParser.ASSIGN); }
		public TerminalNode ASSIGN(int i) {
			return getToken(LangParser.ASSIGN, i);
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
			setState(169);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(138);
				typedFunctionParam();
				setState(143);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(139);
						match(COMMA);
						setState(140);
						typedFunctionParam();
						}
						} 
					}
					setState(145);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
				}
				setState(153);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(146);
					match(COMMA);
					setState(147);
					typedFunctionParam();
					setState(148);
					match(ASSIGN);
					setState(149);
					expression();
					}
					}
					setState(155);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(156);
				typedFunctionParam();
				setState(157);
				match(ASSIGN);
				setState(158);
				expression();
				setState(166);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(159);
					match(COMMA);
					setState(160);
					typedFunctionParam();
					setState(161);
					match(ASSIGN);
					setState(162);
					expression();
					}
					}
					setState(168);
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
		public TerminalNode NAME() { return getToken(LangParser.NAME, 0); }
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
			setState(172);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VAL || _la==REF) {
				{
				setState(171);
				paramPassage();
				}
			}

			setState(174);
			dataType();
			setState(175);
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
		public TerminalNode VAL() { return getToken(LangParser.VAL, 0); }
		public TerminalNode REF() { return getToken(LangParser.REF, 0); }
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
			setState(177);
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
		public TerminalNode IMPORT() { return getToken(LangParser.IMPORT, 0); }
		public NameListContext nameList() {
			return getRuleContext(NameListContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(LangParser.NEWLINE, 0); }
		public TerminalNode SEMI_COLON() { return getToken(LangParser.SEMI_COLON, 0); }
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
			setState(179);
			match(IMPORT);
			setState(180);
			nameList();
			setState(182);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMI_COLON) {
				{
				setState(181);
				match(SEMI_COLON);
				}
			}

			setState(184);
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
			setState(188);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(186);
				simpleStatement();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(187);
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
		public TerminalNode NEWLINE() { return getToken(LangParser.NEWLINE, 0); }
		public List<TerminalNode> SEMI_COLON() { return getTokens(LangParser.SEMI_COLON); }
		public TerminalNode SEMI_COLON(int i) {
			return getToken(LangParser.SEMI_COLON, i);
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
			setState(190);
			smallStatement();
			setState(195);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(191);
					match(SEMI_COLON);
					setState(192);
					smallStatement();
					}
					} 
				}
				setState(197);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			}
			setState(199);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMI_COLON) {
				{
				setState(198);
				match(SEMI_COLON);
				}
			}

			setState(201);
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
			setState(207);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(203);
				testOrExpressionStatement();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(204);
				declarationStatement();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(205);
				flowStatement();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(206);
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
		public TerminalNode CONSTANT() { return getToken(LangParser.CONSTANT, 0); }
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
			setState(209);
			dataType();
			setState(211);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==CONSTANT) {
				{
				setState(210);
				match(CONSTANT);
				}
			}

			setState(213);
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
		public TerminalNode INTEGER() { return getToken(LangParser.INTEGER, 0); }
		public TerminalNode REAL() { return getToken(LangParser.REAL, 0); }
		public TerminalNode CHAR() { return getToken(LangParser.CHAR, 0); }
		public TerminalNode STRING() { return getToken(LangParser.STRING, 0); }
		public TerminalNode BOOLEAN() { return getToken(LangParser.BOOLEAN, 0); }
		public TerminalNode NAME() { return getToken(LangParser.NAME, 0); }
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
			setState(215);
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
		public List<TerminalNode> ASSIGN() { return getTokens(LangParser.ASSIGN); }
		public TerminalNode ASSIGN(int i) {
			return getToken(LangParser.ASSIGN, i);
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
			setState(217);
			testOrExpressionList();
			setState(222);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ASSIGN) {
				{
				{
				setState(218);
				match(ASSIGN);
				setState(219);
				testOrExpressionList();
				}
				}
				setState(224);
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
		public List<TerminalNode> COMMA() { return getTokens(LangParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(LangParser.COMMA, i);
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
			setState(225);
			expression();
			setState(230);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(226);
				match(COMMA);
				setState(227);
				expression();
				}
				}
				setState(232);
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
			setState(235);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(233);
				test();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(234);
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
		public TerminalNode ENUM() { return getToken(LangParser.ENUM, 0); }
		public TerminalNode OPEN_BRACE() { return getToken(LangParser.OPEN_BRACE, 0); }
		public EnumeratorListContext enumeratorList() {
			return getRuleContext(EnumeratorListContext.class,0);
		}
		public TerminalNode CLOSE_BRACE() { return getToken(LangParser.CLOSE_BRACE, 0); }
		public TerminalNode NAME() { return getToken(LangParser.NAME, 0); }
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
			setState(237);
			match(ENUM);
			setState(239);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NAME) {
				{
				setState(238);
				match(NAME);
				}
			}

			setState(241);
			match(OPEN_BRACE);
			setState(242);
			enumeratorList(0);
			setState(243);
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
		public TerminalNode COMMA() { return getToken(LangParser.COMMA, 0); }
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
			setState(246);
			enumerator();
			}
			_ctx.stop = _input.LT(-1);
			setState(253);
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
					setState(248);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(249);
					match(COMMA);
					setState(250);
					enumerator();
					}
					} 
				}
				setState(255);
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
		public TerminalNode NAME() { return getToken(LangParser.NAME, 0); }
		public TerminalNode EQUALS() { return getToken(LangParser.EQUALS, 0); }
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
			setState(256);
			match(NAME);
			setState(259);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				{
				setState(257);
				match(EQUALS);
				setState(258);
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
			setState(264);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BREAK:
				enterOuterAlt(_localctx, 1);
				{
				setState(261);
				breakStatement();
				}
				break;
			case CONTINUE:
				enterOuterAlt(_localctx, 2);
				{
				setState(262);
				continueStatement();
				}
				break;
			case RETURN:
				enterOuterAlt(_localctx, 3);
				{
				setState(263);
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
		public TerminalNode BREAK() { return getToken(LangParser.BREAK, 0); }
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
			setState(266);
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
		public TerminalNode CONTINUE() { return getToken(LangParser.CONTINUE, 0); }
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
			setState(268);
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
		public TerminalNode RETURN() { return getToken(LangParser.RETURN, 0); }
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
			setState(270);
			match(RETURN);
			setState(272);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 9)) & ~0x3f) == 0 && ((1L << (_la - 9)) & ((1L << (NOT - 9)) | (1L << (NULL - 9)) | (1L << (TRUE - 9)) | (1L << (FALSE - 9)) | (1L << (CARDINALITY_OP - 9)) | (1L << (OPEN_PAREN - 9)) | (1L << (ADD - 9)) | (1L << (MINUS - 9)) | (1L << (NOT_OP - 9)) | (1L << (NAME - 9)) | (1L << (STRING_LITERAL - 9)) | (1L << (BYTES_LITERAL - 9)) | (1L << (DECIMAL_INTEGER - 9)) | (1L << (OCT_INTEGER - 9)) | (1L << (HEX_INTEGER - 9)) | (1L << (BIN_INTEGER - 9)) | (1L << (FLOAT_NUMBER - 9)) | (1L << (IMAG_NUMBER - 9)))) != 0)) {
				{
				setState(271);
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
		public List<TerminalNode> NAME() { return getTokens(LangParser.NAME); }
		public TerminalNode NAME(int i) {
			return getToken(LangParser.NAME, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(LangParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(LangParser.COMMA, i);
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
			setState(274);
			match(NAME);
			setState(279);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(275);
				match(COMMA);
				setState(276);
				match(NAME);
				}
				}
				setState(281);
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
			setState(287);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IF:
				enterOuterAlt(_localctx, 1);
				{
				setState(282);
				ifStatement();
				}
				break;
			case WHILE:
				enterOuterAlt(_localctx, 2);
				{
				setState(283);
				whileStatement();
				}
				break;
			case FOR:
				enterOuterAlt(_localctx, 3);
				{
				setState(284);
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
				setState(285);
				functionDefinition();
				}
				break;
			case CLASS:
				enterOuterAlt(_localctx, 5);
				{
				setState(286);
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
		public List<TerminalNode> IF() { return getTokens(LangParser.IF); }
		public TerminalNode IF(int i) {
			return getToken(LangParser.IF, i);
		}
		public List<TestContext> test() {
			return getRuleContexts(TestContext.class);
		}
		public TestContext test(int i) {
			return getRuleContext(TestContext.class,i);
		}
		public List<TerminalNode> COLON() { return getTokens(LangParser.COLON); }
		public TerminalNode COLON(int i) {
			return getToken(LangParser.COLON, i);
		}
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public List<TerminalNode> ELSE() { return getTokens(LangParser.ELSE); }
		public TerminalNode ELSE(int i) {
			return getToken(LangParser.ELSE, i);
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
			setState(289);
			match(IF);
			setState(290);
			test();
			setState(291);
			match(COLON);
			setState(292);
			block();
			setState(301);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,26,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(293);
					match(ELSE);
					setState(294);
					match(IF);
					setState(295);
					test();
					setState(296);
					match(COLON);
					setState(297);
					block();
					}
					} 
				}
				setState(303);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,26,_ctx);
			}
			setState(307);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(304);
				match(ELSE);
				setState(305);
				match(COLON);
				setState(306);
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
		public TerminalNode WHILE() { return getToken(LangParser.WHILE, 0); }
		public TestContext test() {
			return getRuleContext(TestContext.class,0);
		}
		public TerminalNode COLON() { return getToken(LangParser.COLON, 0); }
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
			setState(309);
			match(WHILE);
			setState(310);
			test();
			setState(311);
			match(COLON);
			setState(312);
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
		public TerminalNode FOR() { return getToken(LangParser.FOR, 0); }
		public NameListContext nameList() {
			return getRuleContext(NameListContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(LangParser.ASSIGN, 0); }
		public RangeListContext rangeList() {
			return getRuleContext(RangeListContext.class,0);
		}
		public TerminalNode COLON() { return getToken(LangParser.COLON, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode STEP() { return getToken(LangParser.STEP, 0); }
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
			setState(314);
			match(FOR);
			setState(315);
			nameList();
			setState(316);
			match(ASSIGN);
			setState(317);
			rangeList();
			setState(320);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==STEP) {
				{
				setState(318);
				match(STEP);
				setState(319);
				expressionList();
				}
			}

			setState(322);
			match(COLON);
			setState(323);
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
		public TerminalNode NEWLINE() { return getToken(LangParser.NEWLINE, 0); }
		public TerminalNode INDENT() { return getToken(LangParser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(LangParser.DEDENT, 0); }
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
			setState(335);
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
			case BYTES_LITERAL:
			case DECIMAL_INTEGER:
			case OCT_INTEGER:
			case HEX_INTEGER:
			case BIN_INTEGER:
			case FLOAT_NUMBER:
			case IMAG_NUMBER:
				enterOuterAlt(_localctx, 1);
				{
				setState(325);
				simpleStatement();
				}
				break;
			case NEWLINE:
				enterOuterAlt(_localctx, 2);
				{
				setState(326);
				match(NEWLINE);
				setState(327);
				match(INDENT);
				setState(329); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(328);
					statement();
					}
					}
					setState(331); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << RETURN) | (1L << IF) | (1L << WHILE) | (1L << FOR) | (1L << NOT) | (1L << NULL) | (1L << TRUE) | (1L << FALSE) | (1L << CLASS) | (1L << CONTINUE) | (1L << BREAK) | (1L << ENUM) | (1L << CARDINALITY_OP) | (1L << OPEN_PAREN) | (1L << ADD) | (1L << MINUS) | (1L << NOT_OP) | (1L << INTEGER) | (1L << REAL) | (1L << CHAR) | (1L << STRING) | (1L << BOOLEAN) | (1L << NAME) | (1L << STRING_LITERAL) | (1L << BYTES_LITERAL))) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & ((1L << (DECIMAL_INTEGER - 64)) | (1L << (OCT_INTEGER - 64)) | (1L << (HEX_INTEGER - 64)) | (1L << (BIN_INTEGER - 64)) | (1L << (FLOAT_NUMBER - 64)) | (1L << (IMAG_NUMBER - 64)))) != 0) );
				setState(333);
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
		public List<TerminalNode> CARDINALITY_OP() { return getTokens(LangParser.CARDINALITY_OP); }
		public TerminalNode CARDINALITY_OP(int i) {
			return getToken(LangParser.CARDINALITY_OP, i);
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
			setState(342);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CARDINALITY_OP:
				enterOuterAlt(_localctx, 1);
				{
				setState(337);
				match(CARDINALITY_OP);
				setState(338);
				orTest();
				setState(339);
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
			case BYTES_LITERAL:
			case DECIMAL_INTEGER:
			case OCT_INTEGER:
			case HEX_INTEGER:
			case BIN_INTEGER:
			case FLOAT_NUMBER:
			case IMAG_NUMBER:
				enterOuterAlt(_localctx, 2);
				{
				setState(341);
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
		public List<TerminalNode> OR() { return getTokens(LangParser.OR); }
		public TerminalNode OR(int i) {
			return getToken(LangParser.OR, i);
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
			setState(344);
			andTest();
			setState(349);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OR) {
				{
				{
				setState(345);
				match(OR);
				setState(346);
				andTest();
				}
				}
				setState(351);
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
		public List<TerminalNode> AND() { return getTokens(LangParser.AND); }
		public TerminalNode AND(int i) {
			return getToken(LangParser.AND, i);
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
			setState(352);
			notTest();
			setState(357);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND) {
				{
				{
				setState(353);
				match(AND);
				setState(354);
				notTest();
				}
				}
				setState(359);
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
		public TerminalNode NOT() { return getToken(LangParser.NOT, 0); }
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
			setState(363);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(360);
				match(NOT);
				setState(361);
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
			case BYTES_LITERAL:
			case DECIMAL_INTEGER:
			case OCT_INTEGER:
			case HEX_INTEGER:
			case BIN_INTEGER:
			case FLOAT_NUMBER:
			case IMAG_NUMBER:
				enterOuterAlt(_localctx, 2);
				{
				setState(362);
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
			setState(365);
			expression();
			setState(371);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LESS_THAN) | (1L << GREATER_THAN) | (1L << EQUALS) | (1L << GT_EQ) | (1L << LT_EQ) | (1L << NOT_EQ))) != 0)) {
				{
				{
				setState(366);
				comparisonOperator();
				setState(367);
				expression();
				}
				}
				setState(373);
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
		public TerminalNode GREATER_THAN() { return getToken(LangParser.GREATER_THAN, 0); }
		public TerminalNode LESS_THAN() { return getToken(LangParser.LESS_THAN, 0); }
		public TerminalNode EQUALS() { return getToken(LangParser.EQUALS, 0); }
		public TerminalNode GT_EQ() { return getToken(LangParser.GT_EQ, 0); }
		public TerminalNode LT_EQ() { return getToken(LangParser.LT_EQ, 0); }
		public TerminalNode NOT_EQ() { return getToken(LangParser.NOT_EQ, 0); }
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
			setState(374);
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
			setState(376);
			expression();
			setState(380);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,36,_ctx) ) {
			case 1:
				{
				setState(377);
				rangeDelimiter();
				setState(378);
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
		public TerminalNode UNTIL() { return getToken(LangParser.UNTIL, 0); }
		public TerminalNode COLON() { return getToken(LangParser.COLON, 0); }
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
			setState(382);
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
		public List<TerminalNode> COMMA() { return getTokens(LangParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(LangParser.COMMA, i);
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
			setState(384);
			loopRange();
			setState(389);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(385);
				match(COMMA);
				setState(386);
				loopRange();
				}
				}
				setState(391);
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
		public List<TerminalNode> OR_OP() { return getTokens(LangParser.OR_OP); }
		public TerminalNode OR_OP(int i) {
			return getToken(LangParser.OR_OP, i);
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
			setState(392);
			xorExpression();
			setState(397);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,38,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(393);
					match(OR_OP);
					setState(394);
					xorExpression();
					}
					} 
				}
				setState(399);
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
		public List<TerminalNode> XOR() { return getTokens(LangParser.XOR); }
		public TerminalNode XOR(int i) {
			return getToken(LangParser.XOR, i);
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
			setState(400);
			andExpression();
			setState(405);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,39,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(401);
					match(XOR);
					setState(402);
					andExpression();
					}
					} 
				}
				setState(407);
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
		public List<TerminalNode> AND_OP() { return getTokens(LangParser.AND_OP); }
		public TerminalNode AND_OP(int i) {
			return getToken(LangParser.AND_OP, i);
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
			setState(408);
			shiftExpression();
			setState(413);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,40,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(409);
					match(AND_OP);
					setState(410);
					shiftExpression();
					}
					} 
				}
				setState(415);
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
		public List<TerminalNode> LEFT_SHIFT() { return getTokens(LangParser.LEFT_SHIFT); }
		public TerminalNode LEFT_SHIFT(int i) {
			return getToken(LangParser.LEFT_SHIFT, i);
		}
		public List<TerminalNode> RIGHT_SHIFT() { return getTokens(LangParser.RIGHT_SHIFT); }
		public TerminalNode RIGHT_SHIFT(int i) {
			return getToken(LangParser.RIGHT_SHIFT, i);
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
			setState(416);
			arithmeticExpression();
			setState(423);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,42,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					setState(421);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case LEFT_SHIFT:
						{
						setState(417);
						match(LEFT_SHIFT);
						setState(418);
						arithmeticExpression();
						}
						break;
					case RIGHT_SHIFT:
						{
						setState(419);
						match(RIGHT_SHIFT);
						setState(420);
						arithmeticExpression();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					} 
				}
				setState(425);
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
		public List<TerminalNode> ADD() { return getTokens(LangParser.ADD); }
		public TerminalNode ADD(int i) {
			return getToken(LangParser.ADD, i);
		}
		public List<TerminalNode> MINUS() { return getTokens(LangParser.MINUS); }
		public TerminalNode MINUS(int i) {
			return getToken(LangParser.MINUS, i);
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
			setState(426);
			term();
			setState(433);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,44,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					setState(431);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case ADD:
						{
						setState(427);
						match(ADD);
						setState(428);
						term();
						}
						break;
					case MINUS:
						{
						setState(429);
						match(MINUS);
						setState(430);
						term();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					} 
				}
				setState(435);
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
		public List<TerminalNode> STAR() { return getTokens(LangParser.STAR); }
		public TerminalNode STAR(int i) {
			return getToken(LangParser.STAR, i);
		}
		public List<TerminalNode> DIV() { return getTokens(LangParser.DIV); }
		public TerminalNode DIV(int i) {
			return getToken(LangParser.DIV, i);
		}
		public List<TerminalNode> MOD() { return getTokens(LangParser.MOD); }
		public TerminalNode MOD(int i) {
			return getToken(LangParser.MOD, i);
		}
		public List<TerminalNode> IDIV() { return getTokens(LangParser.IDIV); }
		public TerminalNode IDIV(int i) {
			return getToken(LangParser.IDIV, i);
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
			setState(436);
			factor();
			setState(447);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,46,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					setState(445);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case STAR:
						{
						setState(437);
						match(STAR);
						setState(438);
						factor();
						}
						break;
					case DIV:
						{
						setState(439);
						match(DIV);
						setState(440);
						factor();
						}
						break;
					case MOD:
						{
						setState(441);
						match(MOD);
						setState(442);
						factor();
						}
						break;
					case IDIV:
						{
						setState(443);
						match(IDIV);
						setState(444);
						factor();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					} 
				}
				setState(449);
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
		public TerminalNode ADD() { return getToken(LangParser.ADD, 0); }
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public TerminalNode MINUS() { return getToken(LangParser.MINUS, 0); }
		public TerminalNode NOT_OP() { return getToken(LangParser.NOT_OP, 0); }
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
			setState(457);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ADD:
				enterOuterAlt(_localctx, 1);
				{
				setState(450);
				match(ADD);
				setState(451);
				factor();
				}
				break;
			case MINUS:
				enterOuterAlt(_localctx, 2);
				{
				setState(452);
				match(MINUS);
				setState(453);
				factor();
				}
				break;
			case NOT_OP:
				enterOuterAlt(_localctx, 3);
				{
				setState(454);
				match(NOT_OP);
				setState(455);
				factor();
				}
				break;
			case NULL:
			case TRUE:
			case FALSE:
			case OPEN_PAREN:
			case NAME:
			case STRING_LITERAL:
			case BYTES_LITERAL:
			case DECIMAL_INTEGER:
			case OCT_INTEGER:
			case HEX_INTEGER:
			case BIN_INTEGER:
			case FLOAT_NUMBER:
			case IMAG_NUMBER:
				enterOuterAlt(_localctx, 4);
				{
				setState(456);
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
		public TerminalNode POWER() { return getToken(LangParser.POWER, 0); }
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
			setState(459);
			atom();
			setState(463);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,48,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(460);
					trailer();
					}
					} 
				}
				setState(465);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,48,_ctx);
			}
			setState(468);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,49,_ctx) ) {
			case 1:
				{
				setState(466);
				match(POWER);
				setState(467);
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
		public TerminalNode OPEN_PAREN() { return getToken(LangParser.OPEN_PAREN, 0); }
		public TestOrExpressionListContext testOrExpressionList() {
			return getRuleContext(TestOrExpressionListContext.class,0);
		}
		public TerminalNode CLOSE_PAREN() { return getToken(LangParser.CLOSE_PAREN, 0); }
		public TerminalNode NAME() { return getToken(LangParser.NAME, 0); }
		public NumberContext number() {
			return getRuleContext(NumberContext.class,0);
		}
		public List<StringContext> string() {
			return getRuleContexts(StringContext.class);
		}
		public StringContext string(int i) {
			return getRuleContext(StringContext.class,i);
		}
		public TerminalNode NULL() { return getToken(LangParser.NULL, 0); }
		public TerminalNode TRUE() { return getToken(LangParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(LangParser.FALSE, 0); }
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
			setState(484);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPEN_PAREN:
				enterOuterAlt(_localctx, 1);
				{
				setState(470);
				match(OPEN_PAREN);
				setState(471);
				testOrExpressionList();
				setState(472);
				match(CLOSE_PAREN);
				}
				break;
			case NAME:
				enterOuterAlt(_localctx, 2);
				{
				setState(474);
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
				setState(475);
				number();
				}
				break;
			case STRING_LITERAL:
			case BYTES_LITERAL:
				enterOuterAlt(_localctx, 4);
				{
				setState(477); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(476);
						string();
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(479); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,50,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				}
				break;
			case NULL:
				enterOuterAlt(_localctx, 5);
				{
				setState(481);
				match(NULL);
				}
				break;
			case TRUE:
				enterOuterAlt(_localctx, 6);
				{
				setState(482);
				match(TRUE);
				}
				break;
			case FALSE:
				enterOuterAlt(_localctx, 7);
				{
				setState(483);
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
		public TerminalNode OPEN_BRACK() { return getToken(LangParser.OPEN_BRACK, 0); }
		public SubscriptListContext subscriptList() {
			return getRuleContext(SubscriptListContext.class,0);
		}
		public TerminalNode CLOSE_BRACK() { return getToken(LangParser.CLOSE_BRACK, 0); }
		public TrailerSubsContext(TrailerContext ctx) { copyFrom(ctx); }
	}
	public static class TrailerDotContext extends TrailerContext {
		public TerminalNode DOT() { return getToken(LangParser.DOT, 0); }
		public TerminalNode NAME() { return getToken(LangParser.NAME, 0); }
		public TrailerDotContext(TrailerContext ctx) { copyFrom(ctx); }
	}
	public static class TrailerArgsContext extends TrailerContext {
		public TerminalNode OPEN_PAREN() { return getToken(LangParser.OPEN_PAREN, 0); }
		public TerminalNode CLOSE_PAREN() { return getToken(LangParser.CLOSE_PAREN, 0); }
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
			setState(497);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPEN_PAREN:
				_localctx = new TrailerArgsContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(486);
				match(OPEN_PAREN);
				setState(488);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (((((_la - 9)) & ~0x3f) == 0 && ((1L << (_la - 9)) & ((1L << (NOT - 9)) | (1L << (NULL - 9)) | (1L << (TRUE - 9)) | (1L << (FALSE - 9)) | (1L << (CARDINALITY_OP - 9)) | (1L << (OPEN_PAREN - 9)) | (1L << (ADD - 9)) | (1L << (MINUS - 9)) | (1L << (NOT_OP - 9)) | (1L << (NAME - 9)) | (1L << (STRING_LITERAL - 9)) | (1L << (BYTES_LITERAL - 9)) | (1L << (DECIMAL_INTEGER - 9)) | (1L << (OCT_INTEGER - 9)) | (1L << (HEX_INTEGER - 9)) | (1L << (BIN_INTEGER - 9)) | (1L << (FLOAT_NUMBER - 9)) | (1L << (IMAG_NUMBER - 9)))) != 0)) {
					{
					setState(487);
					argList();
					}
				}

				setState(490);
				match(CLOSE_PAREN);
				}
				break;
			case OPEN_BRACK:
				_localctx = new TrailerSubsContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(491);
				match(OPEN_BRACK);
				setState(492);
				subscriptList();
				setState(493);
				match(CLOSE_BRACK);
				}
				break;
			case DOT:
				_localctx = new TrailerDotContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(495);
				match(DOT);
				setState(496);
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
		public List<TerminalNode> COMMA() { return getTokens(LangParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(LangParser.COMMA, i);
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
			setState(499);
			subscript();
			setState(504);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(500);
				match(COMMA);
				setState(501);
				subscript();
				}
				}
				setState(506);
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
		public TerminalNode STAR() { return getToken(LangParser.STAR, 0); }
		public SubscriptContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subscript; }
	}

	public final SubscriptContext subscript() throws RecognitionException {
		SubscriptContext _localctx = new SubscriptContext(_ctx, getState());
		enterRule(_localctx, 96, RULE_subscript);
		try {
			setState(513);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,55,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(507);
				expression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(508);
				expression();
				setState(509);
				rangeDelimiter();
				setState(510);
				expression();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(512);
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
		public List<TerminalNode> COMMA() { return getTokens(LangParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(LangParser.COMMA, i);
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
			setState(515);
			testOrExpression();
			setState(520);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(516);
				match(COMMA);
				setState(517);
				testOrExpression();
				}
				}
				setState(522);
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
		public TerminalNode CLASS() { return getToken(LangParser.CLASS, 0); }
		public List<TerminalNode> NAME() { return getTokens(LangParser.NAME); }
		public TerminalNode NAME(int i) {
			return getToken(LangParser.NAME, i);
		}
		public TerminalNode COLON() { return getToken(LangParser.COLON, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode OPEN_PAREN() { return getToken(LangParser.OPEN_PAREN, 0); }
		public TerminalNode CLOSE_PAREN() { return getToken(LangParser.CLOSE_PAREN, 0); }
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
			setState(523);
			match(CLASS);
			setState(524);
			match(NAME);
			setState(530);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==OPEN_PAREN) {
				{
				setState(525);
				match(OPEN_PAREN);
				setState(527);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==NAME) {
					{
					setState(526);
					match(NAME);
					}
				}

				setState(529);
				match(CLOSE_PAREN);
				}
			}

			setState(532);
			match(COLON);
			setState(533);
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
		public List<TerminalNode> COMMA() { return getTokens(LangParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(LangParser.COMMA, i);
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
			setState(540);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,59,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(535);
					argument();
					setState(536);
					match(COMMA);
					}
					} 
				}
				setState(542);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,59,_ctx);
			}
			setState(543);
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
		public TerminalNode ASSIGN() { return getToken(LangParser.ASSIGN, 0); }
		public ArgumentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argument; }
	}

	public final ArgumentContext argument() throws RecognitionException {
		ArgumentContext _localctx = new ArgumentContext(_ctx, getState());
		enterRule(_localctx, 104, RULE_argument);
		try {
			setState(550);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,60,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(545);
				test();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(546);
				test();
				setState(547);
				match(ASSIGN);
				setState(548);
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
		public TerminalNode STRING_LITERAL() { return getToken(LangParser.STRING_LITERAL, 0); }
		public TerminalNode BYTES_LITERAL() { return getToken(LangParser.BYTES_LITERAL, 0); }
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
			setState(552);
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

	public static class NumberContext extends ParserRuleContext {
		public IntegerContext integer() {
			return getRuleContext(IntegerContext.class,0);
		}
		public TerminalNode FLOAT_NUMBER() { return getToken(LangParser.FLOAT_NUMBER, 0); }
		public TerminalNode IMAG_NUMBER() { return getToken(LangParser.IMAG_NUMBER, 0); }
		public NumberContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_number; }
	}

	public final NumberContext number() throws RecognitionException {
		NumberContext _localctx = new NumberContext(_ctx, getState());
		enterRule(_localctx, 108, RULE_number);
		try {
			setState(557);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case DECIMAL_INTEGER:
			case OCT_INTEGER:
			case HEX_INTEGER:
			case BIN_INTEGER:
				enterOuterAlt(_localctx, 1);
				{
				setState(554);
				integer();
				}
				break;
			case FLOAT_NUMBER:
				enterOuterAlt(_localctx, 2);
				{
				setState(555);
				match(FLOAT_NUMBER);
				}
				break;
			case IMAG_NUMBER:
				enterOuterAlt(_localctx, 3);
				{
				setState(556);
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
		public TerminalNode DECIMAL_INTEGER() { return getToken(LangParser.DECIMAL_INTEGER, 0); }
		public TerminalNode OCT_INTEGER() { return getToken(LangParser.OCT_INTEGER, 0); }
		public TerminalNode HEX_INTEGER() { return getToken(LangParser.HEX_INTEGER, 0); }
		public TerminalNode BIN_INTEGER() { return getToken(LangParser.BIN_INTEGER, 0); }
		public IntegerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_integer; }
	}

	public final IntegerContext integer() throws RecognitionException {
		IntegerContext _localctx = new IntegerContext(_ctx, getState());
		enterRule(_localctx, 110, RULE_integer);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(559);
			_la = _input.LA(1);
			if ( !(((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & ((1L << (DECIMAL_INTEGER - 64)) | (1L << (OCT_INTEGER - 64)) | (1L << (HEX_INTEGER - 64)) | (1L << (BIN_INTEGER - 64)))) != 0)) ) {
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3K\u0234\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\3\2\5\2u\n\2\3\2\7\2"+
		"x\n\2\f\2\16\2{\13\2\3\2\3\2\3\3\5\3\u0080\n\3\3\3\3\3\3\3\3\3\3\3\3\4"+
		"\3\4\5\4\u0089\n\4\3\4\3\4\3\5\3\5\3\5\7\5\u0090\n\5\f\5\16\5\u0093\13"+
		"\5\3\5\3\5\3\5\3\5\3\5\7\5\u009a\n\5\f\5\16\5\u009d\13\5\3\5\3\5\3\5\3"+
		"\5\3\5\3\5\3\5\3\5\7\5\u00a7\n\5\f\5\16\5\u00aa\13\5\5\5\u00ac\n\5\3\6"+
		"\5\6\u00af\n\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\b\5\b\u00b9\n\b\3\b\3\b\3"+
		"\t\3\t\5\t\u00bf\n\t\3\n\3\n\3\n\7\n\u00c4\n\n\f\n\16\n\u00c7\13\n\3\n"+
		"\5\n\u00ca\n\n\3\n\3\n\3\13\3\13\3\13\3\13\5\13\u00d2\n\13\3\f\3\f\5\f"+
		"\u00d6\n\f\3\f\3\f\3\r\3\r\3\16\3\16\3\16\7\16\u00df\n\16\f\16\16\16\u00e2"+
		"\13\16\3\17\3\17\3\17\7\17\u00e7\n\17\f\17\16\17\u00ea\13\17\3\20\3\20"+
		"\5\20\u00ee\n\20\3\21\3\21\5\21\u00f2\n\21\3\21\3\21\3\21\3\21\3\22\3"+
		"\22\3\22\3\22\3\22\3\22\7\22\u00fe\n\22\f\22\16\22\u0101\13\22\3\23\3"+
		"\23\3\23\5\23\u0106\n\23\3\24\3\24\3\24\5\24\u010b\n\24\3\25\3\25\3\26"+
		"\3\26\3\27\3\27\5\27\u0113\n\27\3\30\3\30\3\30\7\30\u0118\n\30\f\30\16"+
		"\30\u011b\13\30\3\31\3\31\3\31\3\31\3\31\5\31\u0122\n\31\3\32\3\32\3\32"+
		"\3\32\3\32\3\32\3\32\3\32\3\32\3\32\7\32\u012e\n\32\f\32\16\32\u0131\13"+
		"\32\3\32\3\32\3\32\5\32\u0136\n\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34"+
		"\3\34\3\34\3\34\3\34\5\34\u0143\n\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35"+
		"\6\35\u014c\n\35\r\35\16\35\u014d\3\35\3\35\5\35\u0152\n\35\3\36\3\36"+
		"\3\36\3\36\3\36\5\36\u0159\n\36\3\37\3\37\3\37\7\37\u015e\n\37\f\37\16"+
		"\37\u0161\13\37\3 \3 \3 \7 \u0166\n \f \16 \u0169\13 \3!\3!\3!\5!\u016e"+
		"\n!\3\"\3\"\3\"\3\"\7\"\u0174\n\"\f\"\16\"\u0177\13\"\3#\3#\3$\3$\3$\3"+
		"$\5$\u017f\n$\3%\3%\3&\3&\3&\7&\u0186\n&\f&\16&\u0189\13&\3\'\3\'\3\'"+
		"\7\'\u018e\n\'\f\'\16\'\u0191\13\'\3(\3(\3(\7(\u0196\n(\f(\16(\u0199\13"+
		"(\3)\3)\3)\7)\u019e\n)\f)\16)\u01a1\13)\3*\3*\3*\3*\3*\7*\u01a8\n*\f*"+
		"\16*\u01ab\13*\3+\3+\3+\3+\3+\7+\u01b2\n+\f+\16+\u01b5\13+\3,\3,\3,\3"+
		",\3,\3,\3,\3,\3,\7,\u01c0\n,\f,\16,\u01c3\13,\3-\3-\3-\3-\3-\3-\3-\5-"+
		"\u01cc\n-\3.\3.\7.\u01d0\n.\f.\16.\u01d3\13.\3.\3.\5.\u01d7\n.\3/\3/\3"+
		"/\3/\3/\3/\3/\6/\u01e0\n/\r/\16/\u01e1\3/\3/\3/\5/\u01e7\n/\3\60\3\60"+
		"\5\60\u01eb\n\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\5\60\u01f4\n\60\3"+
		"\61\3\61\3\61\7\61\u01f9\n\61\f\61\16\61\u01fc\13\61\3\62\3\62\3\62\3"+
		"\62\3\62\3\62\5\62\u0204\n\62\3\63\3\63\3\63\7\63\u0209\n\63\f\63\16\63"+
		"\u020c\13\63\3\64\3\64\3\64\3\64\5\64\u0212\n\64\3\64\5\64\u0215\n\64"+
		"\3\64\3\64\3\64\3\65\3\65\3\65\7\65\u021d\n\65\f\65\16\65\u0220\13\65"+
		"\3\65\3\65\3\66\3\66\3\66\3\66\3\66\5\66\u0229\n\66\3\67\3\67\38\38\3"+
		"8\58\u0230\n8\39\39\39\2\3\":\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 "+
		"\"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnp\2\b\3\2\66\67\4\28"+
		"<??\3\2.\63\4\2\24\24\32\32\3\2@A\3\2BE\2\u024b\2y\3\2\2\2\4\177\3\2\2"+
		"\2\6\u0086\3\2\2\2\b\u00ab\3\2\2\2\n\u00ae\3\2\2\2\f\u00b3\3\2\2\2\16"+
		"\u00b5\3\2\2\2\20\u00be\3\2\2\2\22\u00c0\3\2\2\2\24\u00d1\3\2\2\2\26\u00d3"+
		"\3\2\2\2\30\u00d9\3\2\2\2\32\u00db\3\2\2\2\34\u00e3\3\2\2\2\36\u00ed\3"+
		"\2\2\2 \u00ef\3\2\2\2\"\u00f7\3\2\2\2$\u0102\3\2\2\2&\u010a\3\2\2\2(\u010c"+
		"\3\2\2\2*\u010e\3\2\2\2,\u0110\3\2\2\2.\u0114\3\2\2\2\60\u0121\3\2\2\2"+
		"\62\u0123\3\2\2\2\64\u0137\3\2\2\2\66\u013c\3\2\2\28\u0151\3\2\2\2:\u0158"+
		"\3\2\2\2<\u015a\3\2\2\2>\u0162\3\2\2\2@\u016d\3\2\2\2B\u016f\3\2\2\2D"+
		"\u0178\3\2\2\2F\u017a\3\2\2\2H\u0180\3\2\2\2J\u0182\3\2\2\2L\u018a\3\2"+
		"\2\2N\u0192\3\2\2\2P\u019a\3\2\2\2R\u01a2\3\2\2\2T\u01ac\3\2\2\2V\u01b6"+
		"\3\2\2\2X\u01cb\3\2\2\2Z\u01cd\3\2\2\2\\\u01e6\3\2\2\2^\u01f3\3\2\2\2"+
		"`\u01f5\3\2\2\2b\u0203\3\2\2\2d\u0205\3\2\2\2f\u020d\3\2\2\2h\u021e\3"+
		"\2\2\2j\u0228\3\2\2\2l\u022a\3\2\2\2n\u022f\3\2\2\2p\u0231\3\2\2\2rx\7"+
		">\2\2su\5\16\b\2ts\3\2\2\2tu\3\2\2\2uv\3\2\2\2vx\5\20\t\2wr\3\2\2\2wt"+
		"\3\2\2\2x{\3\2\2\2yw\3\2\2\2yz\3\2\2\2z|\3\2\2\2{y\3\2\2\2|}\7\2\2\3}"+
		"\3\3\2\2\2~\u0080\5\30\r\2\177~\3\2\2\2\177\u0080\3\2\2\2\u0080\u0081"+
		"\3\2\2\2\u0081\u0082\7?\2\2\u0082\u0083\5\6\4\2\u0083\u0084\7\32\2\2\u0084"+
		"\u0085\58\35\2\u0085\5\3\2\2\2\u0086\u0088\7\27\2\2\u0087\u0089\5\b\5"+
		"\2\u0088\u0087\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u008b"+
		"\7\30\2\2\u008b\7\3\2\2\2\u008c\u0091\5\n\6\2\u008d\u008e\7\31\2\2\u008e"+
		"\u0090\5\n\6\2\u008f\u008d\3\2\2\2\u0090\u0093\3\2\2\2\u0091\u008f\3\2"+
		"\2\2\u0091\u0092\3\2\2\2\u0092\u009b\3\2\2\2\u0093\u0091\3\2\2\2\u0094"+
		"\u0095\7\31\2\2\u0095\u0096\5\n\6\2\u0096\u0097\7\35\2\2\u0097\u0098\5"+
		"L\'\2\u0098\u009a\3\2\2\2\u0099\u0094\3\2\2\2\u009a\u009d\3\2\2\2\u009b"+
		"\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u00ac\3\2\2\2\u009d\u009b\3\2"+
		"\2\2\u009e\u009f\5\n\6\2\u009f\u00a0\7\35\2\2\u00a0\u00a8\5L\'\2\u00a1"+
		"\u00a2\7\31\2\2\u00a2\u00a3\5\n\6\2\u00a3\u00a4\7\35\2\2\u00a4\u00a5\5"+
		"L\'\2\u00a5\u00a7\3\2\2\2\u00a6\u00a1\3\2\2\2\u00a7\u00aa\3\2\2\2\u00a8"+
		"\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00ac\3\2\2\2\u00aa\u00a8\3\2"+
		"\2\2\u00ab\u008c\3\2\2\2\u00ab\u009e\3\2\2\2\u00ac\t\3\2\2\2\u00ad\u00af"+
		"\5\f\7\2\u00ae\u00ad\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0"+
		"\u00b1\5\30\r\2\u00b1\u00b2\7?\2\2\u00b2\13\3\2\2\2\u00b3\u00b4\t\2\2"+
		"\2\u00b4\r\3\2\2\2\u00b5\u00b6\7\4\2\2\u00b6\u00b8\5.\30\2\u00b7\u00b9"+
		"\7\33\2\2\u00b8\u00b7\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba\3\2\2\2"+
		"\u00ba\u00bb\7>\2\2\u00bb\17\3\2\2\2\u00bc\u00bf\5\22\n\2\u00bd\u00bf"+
		"\5\60\31\2\u00be\u00bc\3\2\2\2\u00be\u00bd\3\2\2\2\u00bf\21\3\2\2\2\u00c0"+
		"\u00c5\5\24\13\2\u00c1\u00c2\7\33\2\2\u00c2\u00c4\5\24\13\2\u00c3\u00c1"+
		"\3\2\2\2\u00c4\u00c7\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6"+
		"\u00c9\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c8\u00ca\7\33\2\2\u00c9\u00c8\3"+
		"\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cc\7>\2\2\u00cc"+
		"\23\3\2\2\2\u00cd\u00d2\5\32\16\2\u00ce\u00d2\5\26\f\2\u00cf\u00d2\5&"+
		"\24\2\u00d0\u00d2\5 \21\2\u00d1\u00cd\3\2\2\2\u00d1\u00ce\3\2\2\2\u00d1"+
		"\u00cf\3\2\2\2\u00d1\u00d0\3\2\2\2\u00d2\25\3\2\2\2\u00d3\u00d5\5\30\r"+
		"\2\u00d4\u00d6\7=\2\2\u00d5\u00d4\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d7"+
		"\3\2\2\2\u00d7\u00d8\5\32\16\2\u00d8\27\3\2\2\2\u00d9\u00da\t\3\2\2\u00da"+
		"\31\3\2\2\2\u00db\u00e0\5d\63\2\u00dc\u00dd\7\35\2\2\u00dd\u00df\5d\63"+
		"\2\u00de\u00dc\3\2\2\2\u00df\u00e2\3\2\2\2\u00e0\u00de\3\2\2\2\u00e0\u00e1"+
		"\3\2\2\2\u00e1\33\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e3\u00e8\5L\'\2\u00e4"+
		"\u00e5\7\31\2\2\u00e5\u00e7\5L\'\2\u00e6\u00e4\3\2\2\2\u00e7\u00ea\3\2"+
		"\2\2\u00e8\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\35\3\2\2\2\u00ea\u00e8"+
		"\3\2\2\2\u00eb\u00ee\5:\36\2\u00ec\u00ee\5L\'\2\u00ed\u00eb\3\2\2\2\u00ed"+
		"\u00ec\3\2\2\2\u00ee\37\3\2\2\2\u00ef\u00f1\7\22\2\2\u00f0\u00f2\7?\2"+
		"\2\u00f1\u00f0\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f4"+
		"\7,\2\2\u00f4\u00f5\5\"\22\2\u00f5\u00f6\7-\2\2\u00f6!\3\2\2\2\u00f7\u00f8"+
		"\b\22\1\2\u00f8\u00f9\5$\23\2\u00f9\u00ff\3\2\2\2\u00fa\u00fb\f\3\2\2"+
		"\u00fb\u00fc\7\31\2\2\u00fc\u00fe\5$\23\2\u00fd\u00fa\3\2\2\2\u00fe\u0101"+
		"\3\2\2\2\u00ff\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2\u0100#\3\2\2\2\u0101"+
		"\u00ff\3\2\2\2\u0102\u0105\7?\2\2\u0103\u0104\7\60\2\2\u0104\u0106\5L"+
		"\'\2\u0105\u0103\3\2\2\2\u0105\u0106\3\2\2\2\u0106%\3\2\2\2\u0107\u010b"+
		"\5(\25\2\u0108\u010b\5*\26\2\u0109\u010b\5,\27\2\u010a\u0107\3\2\2\2\u010a"+
		"\u0108\3\2\2\2\u010a\u0109\3\2\2\2\u010b\'\3\2\2\2\u010c\u010d\7\21\2"+
		"\2\u010d)\3\2\2\2\u010e\u010f\7\20\2\2\u010f+\3\2\2\2\u0110\u0112\7\3"+
		"\2\2\u0111\u0113\5d\63\2\u0112\u0111\3\2\2\2\u0112\u0113\3\2\2\2\u0113"+
		"-\3\2\2\2\u0114\u0119\7?\2\2\u0115\u0116\7\31\2\2\u0116\u0118\7?\2\2\u0117"+
		"\u0115\3\2\2\2\u0118\u011b\3\2\2\2\u0119\u0117\3\2\2\2\u0119\u011a\3\2"+
		"\2\2\u011a/\3\2\2\2\u011b\u0119\3\2\2\2\u011c\u0122\5\62\32\2\u011d\u0122"+
		"\5\64\33\2\u011e\u0122\5\66\34\2\u011f\u0122\5\4\3\2\u0120\u0122\5f\64"+
		"\2\u0121\u011c\3\2\2\2\u0121\u011d\3\2\2\2\u0121\u011e\3\2\2\2\u0121\u011f"+
		"\3\2\2\2\u0121\u0120\3\2\2\2\u0122\61\3\2\2\2\u0123\u0124\7\5\2\2\u0124"+
		"\u0125\5:\36\2\u0125\u0126\7\32\2\2\u0126\u012f\58\35\2\u0127\u0128\7"+
		"\6\2\2\u0128\u0129\7\5\2\2\u0129\u012a\5:\36\2\u012a\u012b\7\32\2\2\u012b"+
		"\u012c\58\35\2\u012c\u012e\3\2\2\2\u012d\u0127\3\2\2\2\u012e\u0131\3\2"+
		"\2\2\u012f\u012d\3\2\2\2\u012f\u0130\3\2\2\2\u0130\u0135\3\2\2\2\u0131"+
		"\u012f\3\2\2\2\u0132\u0133\7\6\2\2\u0133\u0134\7\32\2\2\u0134\u0136\5"+
		"8\35\2\u0135\u0132\3\2\2\2\u0135\u0136\3\2\2\2\u0136\63\3\2\2\2\u0137"+
		"\u0138\7\7\2\2\u0138\u0139\5:\36\2\u0139\u013a\7\32\2\2\u013a\u013b\5"+
		"8\35\2\u013b\65\3\2\2\2\u013c\u013d\7\b\2\2\u013d\u013e\5.\30\2\u013e"+
		"\u013f\7\35\2\2\u013f\u0142\5J&\2\u0140\u0141\7\23\2\2\u0141\u0143\5\34"+
		"\17\2\u0142\u0140\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0144\3\2\2\2\u0144"+
		"\u0145\7\32\2\2\u0145\u0146\58\35\2\u0146\67\3\2\2\2\u0147\u0152\5\22"+
		"\n\2\u0148\u0149\7>\2\2\u0149\u014b\7J\2\2\u014a\u014c\5\20\t\2\u014b"+
		"\u014a\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014e\3\2"+
		"\2\2\u014e\u014f\3\2\2\2\u014f\u0150\7K\2\2\u0150\u0152\3\2\2\2\u0151"+
		"\u0147\3\2\2\2\u0151\u0148\3\2\2\2\u01529\3\2\2\2\u0153\u0154\7\26\2\2"+
		"\u0154\u0155\5<\37\2\u0155\u0156\7\26\2\2\u0156\u0159\3\2\2\2\u0157\u0159"+
		"\5<\37\2\u0158\u0153\3\2\2\2\u0158\u0157\3\2\2\2\u0159;\3\2\2\2\u015a"+
		"\u015f\5> \2\u015b\u015c\7\t\2\2\u015c\u015e\5> \2\u015d\u015b\3\2\2\2"+
		"\u015e\u0161\3\2\2\2\u015f\u015d\3\2\2\2\u015f\u0160\3\2\2\2\u0160=\3"+
		"\2\2\2\u0161\u015f\3\2\2\2\u0162\u0167\5@!\2\u0163\u0164\7\n\2\2\u0164"+
		"\u0166\5@!\2\u0165\u0163\3\2\2\2\u0166\u0169\3\2\2\2\u0167\u0165\3\2\2"+
		"\2\u0167\u0168\3\2\2\2\u0168?\3\2\2\2\u0169\u0167\3\2\2\2\u016a\u016b"+
		"\7\13\2\2\u016b\u016e\5@!\2\u016c\u016e\5B\"\2\u016d\u016a\3\2\2\2\u016d"+
		"\u016c\3\2\2\2\u016eA\3\2\2\2\u016f\u0175\5L\'\2\u0170\u0171\5D#\2\u0171"+
		"\u0172\5L\'\2\u0172\u0174\3\2\2\2\u0173\u0170\3\2\2\2\u0174\u0177\3\2"+
		"\2\2\u0175\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176C\3\2\2\2\u0177\u0175"+
		"\3\2\2\2\u0178\u0179\t\4\2\2\u0179E\3\2\2\2\u017a\u017e\5L\'\2\u017b\u017c"+
		"\5H%\2\u017c\u017d\5L\'\2\u017d\u017f\3\2\2\2\u017e\u017b\3\2\2\2\u017e"+
		"\u017f\3\2\2\2\u017fG\3\2\2\2\u0180\u0181\t\5\2\2\u0181I\3\2\2\2\u0182"+
		"\u0187\5F$\2\u0183\u0184\7\31\2\2\u0184\u0186\5F$\2\u0185\u0183\3\2\2"+
		"\2\u0186\u0189\3\2\2\2\u0187\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188K"+
		"\3\2\2\2\u0189\u0187\3\2\2\2\u018a\u018f\5N(\2\u018b\u018c\7 \2\2\u018c"+
		"\u018e\5N(\2\u018d\u018b\3\2\2\2\u018e\u0191\3\2\2\2\u018f\u018d\3\2\2"+
		"\2\u018f\u0190\3\2\2\2\u0190M\3\2\2\2\u0191\u018f\3\2\2\2\u0192\u0197"+
		"\5P)\2\u0193\u0194\7!\2\2\u0194\u0196\5P)\2\u0195\u0193\3\2\2\2\u0196"+
		"\u0199\3\2\2\2\u0197\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198O\3\2\2\2"+
		"\u0199\u0197\3\2\2\2\u019a\u019f\5R*\2\u019b\u019c\7\"\2\2\u019c\u019e"+
		"\5R*\2\u019d\u019b\3\2\2\2\u019e\u01a1\3\2\2\2\u019f\u019d\3\2\2\2\u019f"+
		"\u01a0\3\2\2\2\u01a0Q\3\2\2\2\u01a1\u019f\3\2\2\2\u01a2\u01a9\5T+\2\u01a3"+
		"\u01a4\7#\2\2\u01a4\u01a8\5T+\2\u01a5\u01a6\7$\2\2\u01a6\u01a8\5T+\2\u01a7"+
		"\u01a3\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a8\u01ab\3\2\2\2\u01a9\u01a7\3\2"+
		"\2\2\u01a9\u01aa\3\2\2\2\u01aaS\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ac\u01b3"+
		"\5V,\2\u01ad\u01ae\7%\2\2\u01ae\u01b2\5V,\2\u01af\u01b0\7&\2\2\u01b0\u01b2"+
		"\5V,\2\u01b1\u01ad\3\2\2\2\u01b1\u01af\3\2\2\2\u01b2\u01b5\3\2\2\2\u01b3"+
		"\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4U\3\2\2\2\u01b5\u01b3\3\2\2\2"+
		"\u01b6\u01c1\5X-\2\u01b7\u01b8\7\'\2\2\u01b8\u01c0\5X-\2\u01b9\u01ba\7"+
		"(\2\2\u01ba\u01c0\5X-\2\u01bb\u01bc\7)\2\2\u01bc\u01c0\5X-\2\u01bd\u01be"+
		"\7*\2\2\u01be\u01c0\5X-\2\u01bf\u01b7\3\2\2\2\u01bf\u01b9\3\2\2\2\u01bf"+
		"\u01bb\3\2\2\2\u01bf\u01bd\3\2\2\2\u01c0\u01c3\3\2\2\2\u01c1\u01bf\3\2"+
		"\2\2\u01c1\u01c2\3\2\2\2\u01c2W\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c4\u01c5"+
		"\7%\2\2\u01c5\u01cc\5X-\2\u01c6\u01c7\7&\2\2\u01c7\u01cc\5X-\2\u01c8\u01c9"+
		"\7+\2\2\u01c9\u01cc\5X-\2\u01ca\u01cc\5Z.\2\u01cb\u01c4\3\2\2\2\u01cb"+
		"\u01c6\3\2\2\2\u01cb\u01c8\3\2\2\2\u01cb\u01ca\3\2\2\2\u01ccY\3\2\2\2"+
		"\u01cd\u01d1\5\\/\2\u01ce\u01d0\5^\60\2\u01cf\u01ce\3\2\2\2\u01d0\u01d3"+
		"\3\2\2\2\u01d1\u01cf\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d6\3\2\2\2\u01d3"+
		"\u01d1\3\2\2\2\u01d4\u01d5\7\34\2\2\u01d5\u01d7\5X-\2\u01d6\u01d4\3\2"+
		"\2\2\u01d6\u01d7\3\2\2\2\u01d7[\3\2\2\2\u01d8\u01d9\7\27\2\2\u01d9\u01da"+
		"\5d\63\2\u01da\u01db\7\30\2\2\u01db\u01e7\3\2\2\2\u01dc\u01e7\7?\2\2\u01dd"+
		"\u01e7\5n8\2\u01de\u01e0\5l\67\2\u01df\u01de\3\2\2\2\u01e0\u01e1\3\2\2"+
		"\2\u01e1\u01df\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e7\3\2\2\2\u01e3\u01e7"+
		"\7\f\2\2\u01e4\u01e7\7\r\2\2\u01e5\u01e7\7\16\2\2\u01e6\u01d8\3\2\2\2"+
		"\u01e6\u01dc\3\2\2\2\u01e6\u01dd\3\2\2\2\u01e6\u01df\3\2\2\2\u01e6\u01e3"+
		"\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e6\u01e5\3\2\2\2\u01e7]\3\2\2\2\u01e8"+
		"\u01ea\7\27\2\2\u01e9\u01eb\5h\65\2\u01ea\u01e9\3\2\2\2\u01ea\u01eb\3"+
		"\2\2\2\u01eb\u01ec\3\2\2\2\u01ec\u01f4\7\30\2\2\u01ed\u01ee\7\36\2\2\u01ee"+
		"\u01ef\5`\61\2\u01ef\u01f0\7\37\2\2\u01f0\u01f4\3\2\2\2\u01f1\u01f2\7"+
		"\25\2\2\u01f2\u01f4\7?\2\2\u01f3\u01e8\3\2\2\2\u01f3\u01ed\3\2\2\2\u01f3"+
		"\u01f1\3\2\2\2\u01f4_\3\2\2\2\u01f5\u01fa\5b\62\2\u01f6\u01f7\7\31\2\2"+
		"\u01f7\u01f9\5b\62\2\u01f8\u01f6\3\2\2\2\u01f9\u01fc\3\2\2\2\u01fa\u01f8"+
		"\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fba\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fd"+
		"\u0204\5L\'\2\u01fe\u01ff\5L\'\2\u01ff\u0200\5H%\2\u0200\u0201\5L\'\2"+
		"\u0201\u0204\3\2\2\2\u0202\u0204\7\'\2\2\u0203\u01fd\3\2\2\2\u0203\u01fe"+
		"\3\2\2\2\u0203\u0202\3\2\2\2\u0204c\3\2\2\2\u0205\u020a\5\36\20\2\u0206"+
		"\u0207\7\31\2\2\u0207\u0209\5\36\20\2\u0208\u0206\3\2\2\2\u0209\u020c"+
		"\3\2\2\2\u020a\u0208\3\2\2\2\u020a\u020b\3\2\2\2\u020be\3\2\2\2\u020c"+
		"\u020a\3\2\2\2\u020d\u020e\7\17\2\2\u020e\u0214\7?\2\2\u020f\u0211\7\27"+
		"\2\2\u0210\u0212\7?\2\2\u0211\u0210\3\2\2\2\u0211\u0212\3\2\2\2\u0212"+
		"\u0213\3\2\2\2\u0213\u0215\7\30\2\2\u0214\u020f\3\2\2\2\u0214\u0215\3"+
		"\2\2\2\u0215\u0216\3\2\2\2\u0216\u0217\7\32\2\2\u0217\u0218\58\35\2\u0218"+
		"g\3\2\2\2\u0219\u021a\5j\66\2\u021a\u021b\7\31\2\2\u021b\u021d\3\2\2\2"+
		"\u021c\u0219\3\2\2\2\u021d\u0220\3\2\2\2\u021e\u021c\3\2\2\2\u021e\u021f"+
		"\3\2\2\2\u021f\u0221\3\2\2\2\u0220\u021e\3\2\2\2\u0221\u0222\5j\66\2\u0222"+
		"i\3\2\2\2\u0223\u0229\5:\36\2\u0224\u0225\5:\36\2\u0225\u0226\7\35\2\2"+
		"\u0226\u0227\5:\36\2\u0227\u0229\3\2\2\2\u0228\u0223\3\2\2\2\u0228\u0224"+
		"\3\2\2\2\u0229k\3\2\2\2\u022a\u022b\t\6\2\2\u022bm\3\2\2\2\u022c\u0230"+
		"\5p9\2\u022d\u0230\7F\2\2\u022e\u0230\7G\2\2\u022f\u022c\3\2\2\2\u022f"+
		"\u022d\3\2\2\2\u022f\u022e\3\2\2\2\u0230o\3\2\2\2\u0231\u0232\t\7\2\2"+
		"\u0232q\3\2\2\2@twy\177\u0088\u0091\u009b\u00a8\u00ab\u00ae\u00b8\u00be"+
		"\u00c5\u00c9\u00d1\u00d5\u00e0\u00e8\u00ed\u00f1\u00ff\u0105\u010a\u0112"+
		"\u0119\u0121\u012f\u0135\u0142\u014d\u0151\u0158\u015f\u0167\u016d\u0175"+
		"\u017e\u0187\u018f\u0197\u019f\u01a7\u01a9\u01b1\u01b3\u01bf\u01c1\u01cb"+
		"\u01d1\u01d6\u01e1\u01e6\u01ea\u01f3\u01fa\u0203\u020a\u0211\u0214\u021e"+
		"\u0228\u022f";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}