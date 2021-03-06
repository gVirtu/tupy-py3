# Generated from lang.g4 by ANTLR 4.7

from tupy.Type import TrailerType, Type

from antlr4 import *
from tupy.langParser import langParser

import tupy.errorHelper

import tupy.Interpreter
import tupy.Argument
import tupy.evalVisitor

# This class defines a complete generic visitor for a parse tree produced by langParser.

class functionVisitor(ParseTreeVisitor):

    def __init__(self, parser, functionContext, className="", constructorContext=None):
        self.parser = parser
        self.functionContext = functionContext
        self.className = className
        self.evalV = tupy.Interpreter.Interpreter.visitor
        self.rootLevel = True
        if (constructorContext is not None):
            self.constructorContext = constructorContext
        else:
            self.constructorContext = functionContext

    # Visit a parse tree produced by langParser#r.
    def visitR(self, ctx:langParser.RContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:langParser.FunctionDefinitionContext):
        if not self.rootLevel:
            return
        try:
            function_name = str(ctx.NAME().getText())
            codeTree = ctx.block()
            return_type = Type.NULL
            try:
                return_type = self.mapLexType(ctx.dataType().getChild(0).getSymbol().type)
            except Exception:
                # Is a function with no return
                pass

            if return_type == Type.NULL:
                array_dimensions = 0
            else:
                array_dimensions = self.getArrayLength(ctx.OPEN_BRACK())
            argumentList = self.visitParameters(ctx.parameters())
            isConstructor = ("Definição da classe {0}".format(function_name) == self.className)

            self.functionContext.locals.defineFunction(function_name, (return_type, array_dimensions), argumentList, codeTree, isConstructor=isConstructor)
            if (isConstructor):
                self.constructorContext.locals.defineFunction(function_name, (return_type, array_dimensions), argumentList, codeTree, isConstructor=isConstructor)
            return self.visitBlock(ctx.block())
        except NameError as e:
            tupy.errorHelper.nameError(e.args[0], ctx)
        # except TypeError as e:
        #     tupy.errorHelper.typeError(e.args[0], ctx)
        # except SyntaxError as e:
        #     tupy.errorHelper.syntaxError(e.args[0], ctx)
        # except RuntimeError as e:
        #     tupy.errorHelper.runtimeError(e.args[0], ctx)
        # except ValueError as e:
        #     tupy.errorHelper.valueError(e.args[0], ctx)

    # Visit a parse tree produced by langParser#parameters.
    def visitParameters(self, ctx:langParser.ParametersContext):
        ret = [] if ctx.typedArgsList() is None \
                 else self.visitTypedArgsList(ctx.typedArgsList())
        return ret


    # Visit a parse tree produced by langParser#typedArgsList.
    def visitTypedArgsList(self, ctx:langParser.TypedArgsListContext):
        ret = []
        op = self.parser.COMMA
        variadic_param_passage = False
        for c in iter(ctx.getChildren()):
            if isinstance(c, TerminalNode):
                op = c.getSymbol().type
                # Variadic param
                if op == self.parser.NAME:
                    param_name = str(c.getText())
                    ret.append(tupy.Argument.Argument(param_name, Type.TUPLE, passByRef=variadic_param_passage))
            elif isinstance(c, langParser.ParamPassageContext):
                variadic_param_passage = self.visitParamPassage(c)
            else:
                if op == self.parser.COMMA:
                    element = self.visitTypedFunctionParam(c)
                    ret.append(element)
                elif op == self.parser.ASSIGN:
                    ret[-1].defaultValue = self.evalV.visitExpression(c)
        return ret


    # Visit a parse tree produced by langParser#typedFunctionParam.
    def visitTypedFunctionParam(self, ctx:langParser.TypedFunctionParamContext):
        param_name = str(ctx.NAME().getText())
        datatype = self.mapLexType(ctx.dataType().getChild(0).getSymbol().type)
        className = ctx.dataType().getChild(0).getText() if datatype == Type.STRUCT else None
        invisible = ctx.INVISIBLE() is not None
        array_dimensions = self.getArrayLength(ctx.OPEN_BRACK())
        if ctx.paramPassage() is not None:
            passByRef = self.visitParamPassage(ctx.paramPassage())
        else:
            passByRef = False
        return tupy.Argument.Argument(param_name, datatype, array_dimensions, passByRef, className, invisible)


    # Visit a parse tree produced by langParser#paramPassage.
    def visitParamPassage(self, ctx:langParser.ParamPassageContext):
        return True if ctx.REF() is not None else False


    # NOT IMPLEMENTED
    #====================================================================
    # # Visit a parse tree produced by langParser#importStatement.
    # def visitImportStatement(self, ctx:langParser.ImportStatementContext):
    #     return self.visitChildren(ctx)
    #====================================================================


    # Visit a parse tree produced by langParser#statement.
    def visitStatement(self, ctx:langParser.StatementContext):
        if ctx.simpleStatement():
            return #nada
        elif ctx.compoundStatement():
            return self.visitCompoundStatement(ctx.compoundStatement())

    # Visit a parse tree produced by langParser#simpleStatement.
    def visitSimpleStatement(self, ctx:langParser.SimpleStatementContext):
        return #self.visitChildren(ctx)
    # leave block parsing to the EvalVisitor

    # UNUSED (handled by evalVisitor)
    #====================================================================
    # # Visit a parse tree produced by langParser#smallStatement.
    # def visitSmallStatement(self, ctx:langParser.SmallStatementContext):
    #     return self.visitChildren(ctx)
    #
    # # Visit a parse tree produced by langParser#declarationStatement.
    # def visitDeclarationStatement(self, ctx:langParser.DeclarationStatementContext):
    #     return self.visitChildren(ctx)
    #====================================================================

    # Visit a parse tree produced by langParser#dataType.
    def visitDataType(self, ctx:langParser.DataTypeContext):
        return self.visitChildren(ctx)


    # UNUSED (handled by evalVisitor)
    #====================================================================
    # # Visit a parse tree produced by langParser#testOrExpressionStatement.
    # def visitTestOrExpressionStatement(self, ctx:langParser.TestOrExpressionStatementContext):
    #     return self.visitChildren(ctx)
    #====================================================================

    # Visit a parse tree produced by langParser#expressionList.
    def visitExpressionList(self, ctx:langParser.ExpressionListContext):
        return #self.visitChildren(ctx)
    # leave block parsing to the EvalVisitor


    # Visit a parse tree produced by langParser#testOrExpression.
    def visitTestOrExpression(self, ctx:langParser.TestOrExpressionContext):
        return #self.visitChildren(ctx)
    # leave block parsing to the EvalVisitor


    # NOT IMPLEMENTED
    #====================================================================
    # # Visit a parse tree produced by langParser#enumSpecifier.
    # def visitEnumSpecifier(self, ctx:langParser.EnumSpecifierContext):
    #     return self.visitChildren(ctx)
    #
    #
    # # Visit a parse tree produced by langParser#enumeratorList.
    # def visitEnumeratorList(self, ctx:langParser.EnumeratorListContext):
    #     return self.visitChildren(ctx)
    #
    #
    # # Visit a parse tree produced by langParser#enumerator.
    # def visitEnumerator(self, ctx:langParser.EnumeratorContext):
    #     return self.visitChildren(ctx)
    #====================================================================


    # UNUSED (handled by evalVisitor)
    #====================================================================
    # # Visit a parse tree produced by langParser#flowStatement.
    # def visitFlowStatement(self, ctx:langParser.FlowStatementContext):
    #     return self.visitChildren(ctx)
    #
    #
    # # Visit a parse tree produced by langParser#breakStatement.
    # def visitBreakStatement(self, ctx:langParser.BreakStatementContext):
    #     return self.visitChildren(ctx)
    #
    #
    # # Visit a parse tree produced by langParser#continueStatement.
    # def visitContinueStatement(self, ctx:langParser.ContinueStatementContext):
    #     return self.visitChildren(ctx)
    #
    #
    # # Visit a parse tree produced by langParser#returnStatement.
    # def visitReturnStatement(self, ctx:langParser.ReturnStatementContext):
    #     return self.visitChildren(ctx)
    #====================================================================

    # Visit a parse tree produced by langParser#nameList.
    def visitNameList(self, ctx:langParser.NameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#compoundStatement.
    def visitCompoundStatement(self, ctx:langParser.CompoundStatementContext):
        if ctx.functionDefinition():
            return self.visitFunctionDefinition(ctx.functionDefinition())


    # Visit a parse tree produced by langParser#ifStatement.
    def visitIfStatement(self, ctx:langParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#elseIf.
    def visitElseIf(self, ctx:langParser.ElseIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#whileStatement.
    def visitWhileStatement(self, ctx:langParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#forStatement.
    def visitForStatement(self, ctx:langParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#block.
    def visitBlock(self, ctx:langParser.BlockContext):
        return #self.visitChildren(ctx)
    # leave block parsing to the EvalVisitor


    # Visit a parse tree produced by langParser#test.
    def visitTest(self, ctx:langParser.TestContext):
        return #self.visitChildren(ctx)
    # leave block parsing to the EvalVisitor


    # UNUSED (handled by evalVisitor)
    #====================================================================
    # # Visit a parse tree produced by langParser#orTest.
    # def visitOrTest(self, ctx:langParser.OrTestContext):
    #     return self.visitChildren(ctx)
    #
    #
    # # Visit a parse tree produced by langParser#andTest.
    # def visitAndTest(self, ctx:langParser.AndTestContext):
    #     return self.visitChildren(ctx)
    #
    #
    # # Visit a parse tree produced by langParser#notTest.
    # def visitNotTest(self, ctx:langParser.NotTestContext):
    #     return self.visitChildren(ctx)
    #
    #
    # # Visit a parse tree produced by langParser#comparison.
    # def visitComparison(self, ctx:langParser.ComparisonContext):
    #     return self.visitChildren(ctx)
    #
    #
    # # Visit a parse tree produced by langParser#comparisonOperator.
    # def visitComparisonOperator(self, ctx:langParser.ComparisonOperatorContext):
    #     return self.visitChildren(ctx)
    #====================================================================

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

    """
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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#term.
    def visitTerm(self, ctx:langParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#factor.
    def visitFactor(self, ctx:langParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#power.
    def visitPower(self, ctx:langParser.PowerContext):
        return self.visitChildren(ctx)
    """

    # Visit a parse tree produced by langParser#atom.
    def visitAtom(self, ctx:langParser.AtomContext):
        return self.visitChildren(ctx)


    # UNUSED (handled by evalVisitor)
    #====================================================================
    # # Visit a parse tree produced by langParser#trailer.
    # def visitTrailer(self, ctx:langParser.TrailerContext):
    #     return self.visitChildren(ctx)
    #
    #
    # # Visit a parse tree produced by langParser#subscriptList.
    # def visitSubscriptList(self, ctx:langParser.SubscriptListContext):
    #     return self.visitChildren(ctx)
    #
    #
    # # Visit a parse tree produced by langParser#subscript.
    # def visitSubscript(self, ctx:langParser.SubscriptContext):
    #     return self.visitChildren(ctx)
    #
    #
    # # Visit a parse tree produced by langParser#testOrExpressionList.
    # def visitTestOrExpressionList(self, ctx:langParser.TestOrExpressionListContext):
    #     return self.visitChildren(ctx)
    #====================================================================

    # Visit a parse tree produced by langParser#classDefinition.
    def visitClassDefinition(self, ctx:langParser.ClassDefinitionContext):
        return self.visitChildren(ctx)


    # UNUSED (handled by evalVisitor)
    #====================================================================
    # # Visit a parse tree produced by langParser#argList.
    # def visitArgList(self, ctx:langParser.ArgListContext):
    #     return self.visitChildren(ctx)
    #
    #
    # # Visit a parse tree produced by langParser#string.
    # def visitString(self, ctx:langParser.StringContext):
    #     return self.visitChildren(ctx)
    #
    #
    # # Visit a parse tree produced by langParser#character.
    # def visitCharacter(self, ctx:langParser.CharacterContext):
    #     return self.visitChildren(ctx)
    #====================================================================

    # Visit a parse tree produced by langParser#number.
    def visitNumber(self, ctx:langParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#integer.
    def visitInteger(self, ctx:langParser.IntegerContext):
        return self.visitChildren(ctx)

    def mapLexType(self, lextype):
        return {
            self.parser.INTEGER: Type.INT,
            self.parser.REAL: Type.FLOAT,
            self.parser.CHAR: Type.CHAR,
            self.parser.STRING: Type.STRING,
            self.parser.BOOLEAN: Type.BOOL,
            self.parser.NAME: Type.STRUCT
        }.get(lextype, Type.NULL)

    def getArrayLength(self, bracketList):
        return 0 if bracketList is None \
                 else len(bracketList)
