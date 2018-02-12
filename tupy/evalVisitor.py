# Generated from lang.g4 by ANTLR 4.7
from tupy.Subscript import Subscript
from tupy.Type import TrailerType, Type

from antlr4 import *
from tupy.langParser import langParser

import tupy.errorHelper

import math
import copy
import tupy.Instance
import tupy.Interpreter
import traceback
import tupy.Context
import tupy.Stack
import tupy.Builtins
import tupy.Variable
import tupy.functionVisitor as fv

# This class defines a complete generic visitor for a parse tree produced by langParser.

class evalVisitor(ParseTreeVisitor):

    def __init__(self):
        self.parser = None

    CONST_ATOM_OPERAND = 0
    CONST_EXPR_OPERAND = 1
    CONST_LITERAL_OPERAND = 2
    CONST_OPERATOR = 3
    CONST_DUMMY = 99999999999

    def setParser(self, parser):
        self.parser = parser
        self.opMap = {
            (self.parser.ADD, 1): "positive",
            (self.parser.MINUS, 1): "negative",
            (self.parser.NOT_OP, 1): "bitwise_flip",
            (self.parser.OR_OP, 2): "bitwise_or",
            (self.parser.XOR, 2): "bitwise_xor",
            (self.parser.AND_OP, 2): "bitwise_and",
            (self.parser.LEFT_SHIFT, 2): "left_shift",
            (self.parser.RIGHT_SHIFT, 2): "right_shift",
            (self.parser.ADD, 2): "add",
            (self.parser.MINUS, 2): "subtract",
            (self.parser.STAR, 2): "multiply",
            (self.parser.DIV, 2): "divide",
            (self.parser.MOD, 2): "modulo",
            (self.parser.IDIV, 2): "integer_divide",
            (self.parser.POWER, 2): "power",
            (self.parser.GREATER_THAN, 2): "gt",
            (self.parser.LESS_THAN, 2): "lt",
            (self.parser.EQUALS, 2): "eq",
            (self.parser.GT_EQ, 2): "gt_eq",
            (self.parser.LT_EQ, 2): "lt_eq",
            (self.parser.NOT_EQ, 2): "neq",
            (self.parser.NOT, 1): "logic_not",
            (self.parser.AND, 2): "logic_and",
            (self.parser.OR, 2): "logic_or"
        }

    def parsePN(self, evalList):
        # Parse a prefix notation expression iteratively to maximize user's max recursion depth
        evalStack = []
        operatorIndices = []
        shortCircuitType = None
        shortCircuitIndex = -1
        i = 0

        while i < len(evalList) or len(operatorIndices) > 0:
            tupy.Interpreter.logger.debug("[PARSEPN] EVALSTACK = {0}".format(evalStack))
            tupy.Interpreter.logger.debug("[PARSEPN] OPERATOR INDICES = {0}".format(operatorIndices))

            if (i < len(evalList)):
                (kind, elem) = evalList[i]
                if kind == self.CONST_OPERATOR:
                    operatorIndices.append(len(evalStack))
                    tupy.Interpreter.logger.debug("[PARSEPN] Pushing operator {0}".format(elem))
                    evalStack.append(elem)
                elif shortCircuitType is None:
                    if kind == self.CONST_LITERAL_OPERAND:
                        evalStack.append(elem)
                    elif kind == self.CONST_EXPR_OPERAND:
                        evalStack.append(self.visitExpression(elem))
                    elif kind == self.CONST_ATOM_OPERAND:
                        (atom, trailers) = elem
                        myvar = self.visitAtom(atom)
                        for t in trailers:
                            myvar.trailers.append(self.visitTrailer(t))
                        evalStack.append(myvar)
                else:
                    evalStack.append(self.CONST_DUMMY)

                i = i + 1

                if not len(operatorIndices): break

            topOperatorIndex = operatorIndices[-1]
            opElem = (opType, arity) = evalStack[topOperatorIndex]

            if len(evalStack)-(topOperatorIndex)-1 >= arity:
                op = self.opMap.get(opElem)
                if arity == 1:
                    singleVar = evalStack.pop()
                    evalStack.pop() #operator
                    tupy.Interpreter.logger.debug("[PARSEPN] Doing operation {0} {1}".format(op, singleVar))
                    if shortCircuitType is None:
                        evalStack.append( getattr(singleVar, op)() )
                    else:
                        evalStack.append( tupy.Variable.Literal(tupy.Instance.Instance(Type.BOOL, shortCircuitType)) )
                else:
                    rhsVar = evalStack.pop()
                    lhsVar = evalStack.pop()
                    evalStack.pop() #operator
                    tupy.Interpreter.logger.debug("[PARSEPN] Doing operation {0} {1} {2}".format(lhsVar, op, rhsVar))
                    if shortCircuitType is None:
                        evalStack.append( getattr(lhsVar, op)(rhsVar) )
                    else:
                        evalStack.append( tupy.Variable.Literal(tupy.Instance.Instance(Type.BOOL, shortCircuitType)) )

                if topOperatorIndex == shortCircuitIndex:
                    shortCircuitType = None
                    shortCircuitIndex = -1

                operatorIndices.pop()

            if len(operatorIndices) and shortCircuitType is None:
                topOperatorIndex = operatorIndices[-1]
                (opType, arity) = evalStack[topOperatorIndex]

                if opType == self.parser.AND and len(evalStack)-(topOperatorIndex)-1 >= 1:
                    if not evalStack[-1].get().value:
                        shortCircuitType = False
                        shortCircuitIndex = topOperatorIndex
                elif opType == self.parser.OR and len(evalStack)-(topOperatorIndex)-1 >= 1:
                    if evalStack[-1].get().value:
                        shortCircuitType = True
                        shortCircuitIndex = topOperatorIndex
        return evalStack[-1]

    # Visit a parse tree produced by langParser#r.
    def visitR(self, ctx:langParser.RContext):
        res = self.executeStatements(ctx.statement())
        tupy.Interpreter.logger.debug("ALL DONE!")
        tupy.Interpreter.logger.debug("CallStack top is {0}".format(str(tupy.Interpreter.Interpreter.callStack.top())))
        tupy.Interpreter.logger.debug("Returnin {0}".format(res))
        tupy.Interpreter.Interpreter.trace(ctx.stop.line, res)
        return res

    # Visit a parse tree produced by langParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:langParser.FunctionDefinitionContext):
        return None


    # HANDLED BY FUNCTION VISITOR
    #====================================================================
    # Visit a parse tree produced by langParser#parameters.
    # def visitParameters(self, ctx:langParser.ParametersContext):
    #     return self.visitChildren(ctx)


    # # Visit a parse tree produced by langParser#typedArgsList.
    # def visitTypedArgsList(self, ctx:langParser.TypedArgsListContext):
    #     return self.visitChildren(ctx)


    # # Visit a parse tree produced by langParser#typedFunctionParam.
    # def visitTypedFunctionParam(self, ctx:langParser.TypedFunctionParamContext):
    #     return self.visitChildren(ctx)


    # # Visit a parse tree produced by langParser#paramPassage.
    # def visitParamPassage(self, ctx:langParser.ParamPassageContext):
    #     return self.visitChildren(ctx)
    #====================================================================


    # NOT IMPLEMENTED
    #====================================================================
    # # Visit a parse tree produced by langParser#importStatement.
    # def visitImportStatement(self, ctx:langParser.ImportStatementContext):
    #     return self.visitChildren(ctx)
    #====================================================================

    # Visit a parse tree produced by langParser#statement.
    def visitStatement(self, ctx:langParser.StatementContext):
        if ctx.simpleStatement():
            return self.visitSimpleStatement(ctx.simpleStatement())
        elif ctx.compoundStatement():
            return self.visitCompoundStatement(ctx.compoundStatement())

    # Visit a parse tree produced by langParser#simpleStatement.
    def visitSimpleStatement(self, ctx:langParser.SimpleStatementContext):
        for statement in ctx.smallStatement():
            if ctx.SEMI_COLON():
                tupy.Interpreter.Interpreter.traceSmallStatement = True
            res = self.visitSmallStatement(statement)
        tupy.Interpreter.Interpreter.traceSmallStatement = False
        return res


    # Visit a parse tree produced by langParser#smallStatement.
    def visitSmallStatement(self, ctx:langParser.SmallStatementContext):
        if ctx.testOrExpressionStatement():
            return self.visitTestOrExpressionStatement(ctx.testOrExpressionStatement())
        elif ctx.declarationStatement():
            return self.visitDeclarationStatement(ctx.declarationStatement())
        elif ctx.breakStatement():
            return self.visitBreakStatement(ctx.breakStatement())
        elif ctx.continueStatement():
            return self.visitContinueStatement(ctx.continueStatement())
        else:
            return self.visitReturnStatement(ctx.returnStatement())


    # Visit a parse tree produced by langParser#declarationStatement.
    def visitDeclarationStatement(self, ctx:langParser.DeclarationStatementContext):
        return self.visitTestOrExpressionStatement(ctx.testOrExpressionStatement())


    # UNUSED - TOKEN ACCESSED DIRECTLY
    #====================================================================
    # Visit a parse tree produced by langParser#dataType.
    # def visitDataType(self, ctx:langParser.DataTypeContext):
    #     return self.visitChildren(ctx)
    #====================================================================


    # Visit a parse tree produced by langParser#testOrExpressionStatement.
    def visitTestOrExpressionStatement(self, ctx:langParser.TestOrExpressionStatementContext):
        # Trace - Test/Expression Statement
        tupy.Interpreter.Interpreter.trace(ctx.start.line)

        childcount = len(ctx.testOrExpressionList())
        isDeclaration = isinstance(ctx.parentCtx, langParser.DeclarationStatementContext)
        decltype = Type.NULL
        declaredClass = None
        isInvisible = False

        if (isDeclaration):
            declaredDataType = ctx.parentCtx.dataType().getChild(0)
            if (ctx.parentCtx.dataType().NAME()):
                declaredClass = declaredDataType.getText()
            decltype = self.mapLexType(declaredDataType.getSymbol().type)
            isInvisible = (ctx.parentCtx.INVISIBLE() is not None)

        rhs = self.visitTestOrExpressionList(ctx.testOrExpressionList(childcount-1))
        # Only for return purposes when no assignment is done
        lhs = rhs
        current_child = 1
        is_reference_assign = False
        if (isDeclaration and childcount == current_child):
            self.doDeclare(lhs, decltype, ctx.testOrExpressionList(childcount-1), declaredClass, isInvisible)

        i_children = iter(reversed(list(ctx.getChildren())))
        next(i_children) # all except last

        for c in i_children:
            if isinstance(c, TerminalNode) and c.getSymbol().type == self.parser.REF:
                is_reference_assign = True
            elif isinstance(c, langParser.TestOrExpressionListContext):
                # Visit expression lists pairwise from right to left
                lhs = self.visitTestOrExpressionList(c)
                current_child += 1
                if (isDeclaration and childcount == current_child):
                    self.doDeclare(lhs, decltype, c, declaredClass, isInvisible)

                tupy.Interpreter.logger.debug("VISITTESTOREXPRESSIONSTATEMENT")
                # tupy.Interpreter.logger.debug("LHS = "+str(lhs))
                # tupy.Interpreter.logger.debug("RHS = "+str(rhs))
                if (len(lhs) == len(rhs)):
                    # Cache r-value evaluation so stuff like a, b, c <- b, c, a works
                    if not all(isinstance(lval, tupy.Variable.Symbol) for lval in lhs):
                        tupy.errorHelper.syntaxError("Não é possível atribuir a um literal!", c)
                    rvalCache = [literal.get() for literal in rhs]
                    rvalCache = [tupy.Instance.Instance(elem.type, elem.value, className=elem.class_name)
                                 for elem in rvalCache]
                    for ind in range(0, len(lhs)):
                        # tupy.Interpreter.logger.debug("ind="+str(ind))
                        lval = lhs[ind]
                        rval = rhs[ind]

                        effectiveTrailers = [] if isDeclaration else lval.trailers

                        if (is_reference_assign):
                            if isinstance(rval, tupy.Variable.Symbol):
                                cell = tupy.Interpreter.Interpreter.getMemoryCell(rval.name)
                                if (rval.trailers):
                                    try:
                                        cell = tupy.Interpreter.Interpreter.getDeepMemoryCell(tupy.Interpreter.memRead(cell), rval.trailers)
                                    except tupy.Interpreter.InvalidMemoryAccessException as e:
                                        tupy.errorHelper.syntaxError("Não é possível referenciar {0}!".format(e.args[0]), c)
                                tupy.Interpreter.Interpreter.referenceSymbol(lval.name, cell, trailerList=effectiveTrailers)
                            else:
                                tupy.errorHelper.syntaxError("Não é possível referenciar um literal!", c)
                        else:
                            tupy.Interpreter.Interpreter.storeSymbol(lval.name, rvalCache[ind], effectiveTrailers)
                else:
                    tupy.errorHelper.valueError("Não é possível fazer uma atribuição com duas listas de expressões de tamanhos diferentes!", ctx)
                rhs = lhs
                is_reference_assign = False

        if isDeclaration:
            # Bypass trailers during tupy.Instance.Instance retrieval. e.g.:
            # inteiro A[2] <- [10, 20]
            # Would return A instead of A[2] (which is invalid)
            return tuple(tupy.Interpreter.Interpreter.loadSymbol(literal.name) for literal in lhs)
        else:
            return tuple(literal.get() for literal in lhs)


    # Visit a parse tree produced by langParser#expressionList.
    def visitExpressionList(self, ctx:langParser.ExpressionListContext):
        return tuple(self.visitExpression(expr) for expr in ctx.expression())


    # Visit a parse tree produced by langParser#testOrExpression.
    def visitTestOrExpression(self, ctx:langParser.TestOrExpressionContext):
        try:
            if ctx.test():
                return self.visitTest(ctx.test())
            else:
                return self.visitExpression(ctx.expression())
        # except NameError as e:
        #     tupy.errorHelper.nameError(e.args[0], ctx)
        except TypeError as e:
            tupy.errorHelper.typeError(e.args[0], ctx)
        # except SyntaxError as e:
        #     tupy.errorHelper.syntaxError(e.args[0], ctx)
        # except RuntimeError as e:
        #     tupy.errorHelper.runtimeError(e.args[0], ctx)
        # except ValueError as e:
        #     tupy.errorHelper.valueError(e.args[0], ctx)


    # NOT IMPLEMENTED
    #====================================================================
    # Visit a parse tree produced by langParser#enumSpecifier.
    # def visitEnumSpecifier(self, ctx:langParser.EnumSpecifierContext):
    #     return self.visitChildren(ctx)


    # # Visit a parse tree produced by langParser#enumeratorList.
    # def visitEnumeratorList(self, ctx:langParser.EnumeratorListContext):
    #     return self.visitChildren(ctx)


    # # Visit a parse tree produced by langParser#enumerator.
    # def visitEnumerator(self, ctx:langParser.EnumeratorContext):
    #     return self.visitChildren(ctx)
    #====================================================================


    # Visit a parse tree produced by langParser#breakStatement.
    def visitBreakStatement(self, ctx:langParser.BreakStatementContext):
        # Trace - Flow Statement 1
        tupy.Interpreter.Interpreter.trace(ctx.start.line)

        tupy.Interpreter.Interpreter.doBreak()
        return None


    # Visit a parse tree produced by langParser#continueStatement.
    def visitContinueStatement(self, ctx:langParser.ContinueStatementContext):
        # Trace - Flow Statement 2
        tupy.Interpreter.Interpreter.trace(ctx.start.line)

        tupy.Interpreter.Interpreter.doContinue()
        return None


    # Visit a parse tree produced by langParser#returnStatement.
    def visitReturnStatement(self, ctx:langParser.ReturnStatementContext):
        expr = None

        # Trace - Flow Statement 3
        tupy.Interpreter.Interpreter.trace(ctx.start.line)

        if ctx.testOrExpressionList():
            try:
                expr = []
                for literal in self.visitTestOrExpressionList(ctx.testOrExpressionList()):
                    expr.append(literal.get())
            except RecursionError as e:
                tupy.errorHelper.runtimeError("Limite de recursão alcançado!", ctx)
            except Exception as e:
                raise e

        tupy.Interpreter.Interpreter.doReturn(expr)
        return None


    # Visit a parse tree produced by langParser#nameList.
    def visitNameList(self, ctx:langParser.NameListContext):
        return tuple(name.getText() for name in ctx.NAME())


    # Visit a parse tree produced by langParser#compoundStatement.
    def visitCompoundStatement(self, ctx:langParser.CompoundStatementContext):
        if ctx.ifStatement():
            return self.visitIfStatement(ctx.ifStatement())
        elif ctx.whileStatement():
            return self.visitWhileStatement(ctx.whileStatement())
        elif ctx.forStatement():
            return self.visitForStatement(ctx.forStatement())
        elif ctx.functionDefinition():
            return self.visitFunctionDefinition(ctx.functionDefinition())
        else:
            return self.visitClassDefinition(ctx.classDefinition())


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
                # Trace - If/Else Statement
                tupy.Interpreter.Interpreter.trace(c.start.line)
                test = bool(self.visitTest(c).get().value)
            elif isinstance(c, langParser.BlockContext) and ((test is True) or (lastOne)):
                ret = self.visitBlock(c, funcName="Desvio Condicional")
                break
        return ret


    # Visit a parse tree produced by langParser#whileStatement.
    def visitWhileStatement(self, ctx:langParser.WhileStatementContext):
        ret = None
        testTree = ctx.test()
        iterations = 0
        # Trace - While Statement
        # tupy.Interpreter.Interpreter.trace(ctx.start.line)
        while( bool(self.visitTest(testTree).get().value) ):
            ret = self.visitBlock(ctx.block(), funcName="Laço (enquanto)")
            if (tupy.Interpreter.Interpreter.lastEvent == tupy.Interpreter.FlowEvent.BREAK or
                tupy.Interpreter.Interpreter.flow == tupy.Interpreter.FlowEvent.RETURN):
                    break
            iterations += 1
            if iterations > tupy.Interpreter.Interpreter.iterationLimit:
                tupy.errorHelper.runtimeError("Limite de iterações alcançado!", ctx.block())
        return ret


    # Visit a parse tree produced by langParser#forStatement.
    def visitForStatement(self, ctx:langParser.ForStatementContext):
        names = self.visitNameList(ctx.nameList())
        ranges = self.visitRangeList(ctx.rangeList())
        fillSteps = False
        if (ctx.expressionList() is None):
            steps = []
            fillSteps = True
        else:
            steps = self.visitExpressionList(ctx.expressionList())
        stopFuncs = []
        stopFuncGT = lambda iterator, limit : (iterator > limit)
        stopFuncLT = lambda iterator, limit : (iterator < limit)
        stopFuncGTEQ = lambda iterator, limit : (iterator >= limit)
        stopFuncLTEQ = lambda iterator, limit : (iterator <= limit)

        if (len(names) == len(ranges) and (len(ranges) == len(steps) or fillSteps)):
            for r in ranges:
                if (r[1].value >= r[0].value):
                    if (r[2]): # Inclusive?
                        stopFuncs.append(stopFuncGT)
                    else:
                        stopFuncs.append(stopFuncGTEQ)
                    if fillSteps:
                        steps.append(tupy.Variable.Literal(tupy.Instance.Instance(Type.INT, 1)))
                else:
                    if (r[2]): # Inclusive?
                        stopFuncs.append(stopFuncLT)
                    else:
                        stopFuncs.append(stopFuncLTEQ)
                    if fillSteps:
                        steps.append(tupy.Variable.Literal(tupy.Instance.Instance(Type.INT, -1)))

            # Trace - For Statement
            # tupy.Interpreter.Interpreter.trace(ctx.start.line)

            ret = self.handleInnerFor(None, names, ranges, steps, stopFuncs, ctx.block())

            return ret
        else:
            tupy.errorHelper.syntaxError("Laço 'para' precisa ter o mesmo número de iteradores e intervalos!", ctx.nameList())

    def handleInnerFor(self, ret, names, ranges, steps, stopFuncs, block):
        remaining = len(names)
        tupy.Interpreter.Interpreter.storeSymbol(names[0], ranges[0][0], [])
        currentInstance = ranges[0][0]
        iterations = 0
        while (not stopFuncs[0](currentInstance.value, ranges[0][1].value)):
            tupy.Interpreter.logger.debug("-------------------FOR LOOP: {0} = {1} (limit is {2})".format(names[0], currentInstance.value, ranges[0][1].value))
            if (remaining > 1):
                self.handleInnerFor(ret, names[1:], ranges[1:], steps[1:], stopFuncs[1:], block)
            else:
                ret = self.visitBlock(block, funcName="Laço (para)")

            if (tupy.Interpreter.Interpreter.lastEvent == tupy.Interpreter.FlowEvent.BREAK or
                tupy.Interpreter.Interpreter.flow == tupy.Interpreter.FlowEvent.RETURN):
                break

            currentInstance = tupy.Interpreter.Interpreter.loadSymbol(names[0])
            iteratorType = currentInstance.type

            currentLiteral = tupy.Variable.Literal(currentInstance)
            currentInstance = (currentLiteral.add(steps[0])).get()
            currentInstance = tupy.Builtins.cast(currentInstance, iteratorType)

            tupy.Interpreter.Interpreter.storeSymbol(names[0], currentInstance, [])

            iterations += 1
            if iterations > tupy.Interpreter.Interpreter.iterationLimit:
                tupy.errorHelper.runtimeError("Limite de iterações alcançado!", block)
        return ret

    # Visit a parse tree produced by langParser#block.
    def visitBlock(self, ctx:langParser.BlockContext, injectList=None, returnType=None, funcName=None, originalContext=None):
        if (injectList is None): injectList = []

        returnable = isinstance(ctx.parentCtx, langParser.FunctionDefinitionContext)
        breakable  = returnable \
                  or isinstance(ctx.parentCtx, langParser.ForStatementContext) \
                  or isinstance(ctx.parentCtx, langParser.WhileStatementContext)
        isClassDef = isinstance(ctx.parentCtx, langParser.ClassDefinitionContext)

        if not isClassDef:
            tupy.Interpreter.Interpreter.pushFrame(returnable=returnable, breakable=breakable,
                                     returnType=returnType, funcName=funcName)
        tupy.Interpreter.logger.debug("INJECT LIST IS: {0}".format(injectList))

        for (name, datatype, arrayDimensions, referenceData, invisible, className, inst) in injectList:
            subscriptList = [Subscript(isWildcard=True)] * arrayDimensions
            tupy.Interpreter.Interpreter.declareSymbol(name, datatype, subscriptList, className, invisible)
            tupy.Interpreter.Interpreter.storeSymbol(name, inst, [])

            (referenceDepth, referenceCell, referenceTrailers) = referenceData

            if (inst.type != Type.TUPLE and referenceDepth > -1): #Pass-by-reference only (except variadic)
                # Grabbing the correct memory cell is trickier if there are trailers
                # We are mostly concerned with where the result of retrieveWithTrailers
                # is contained (i.e. the parent_triple). The negative depths are a tiny hack
                # so that we can easily tell whether the referenced entity is the result of
                # a SUBSCRIPT (depth >= 0), CALL (depth = -1) or MEMBER (depth = -2)
                if (referenceTrailers):
                    try:
                        refInst = tupy.Interpreter.memRead(referenceCell)
                        referenceCell = tupy.Interpreter.Interpreter.getDeepMemoryCell(refInst, referenceTrailers)
                    except tupy.Interpreter.InvalidMemoryAccessException as e:
                        tupy.errorHelper.syntaxError("Não é possível referenciar {0}!".format(e.args[0]), ctx.parentCtx)

                tupy.Interpreter.Interpreter.referenceSymbol(name, referenceCell)

        if isClassDef:
            if funcName.startswith("Definição da classe "):
                className = funcName
                classContext = tupy.Interpreter.Interpreter.callStack.top()
                funcvisitor = fv.functionVisitor(self.parser, classContext, className, originalContext)
                funcvisitor.visitChildren(ctx)
        else:
            funcvisitor = fv.functionVisitor(self.parser, tupy.Interpreter.Interpreter.callStack.top())
            funcvisitor.visitChildren(ctx)

        if ctx.simpleStatement() is not None:
            ret = self.visitSimpleStatement(ctx.simpleStatement())
        else:
            ret = self.executeStatements(ctx.statement())
        #ret = self.visitChildren(ctx)

        returned_explicitly = tupy.Interpreter.Interpreter.flow == tupy.Interpreter.FlowEvent.RETURN

        # Check if return is valid
        if tupy.Interpreter.Interpreter.canReturn():
            retType = Type.NULL
            retDimensions = 0

            if (ret is not None):
                if (returned_explicitly):
                    if (isinstance(ret, list)):
                        ret_res = [tupy.Interpreter.memAlloc(element) for element in ret]
                        ret = tupy.Instance.Instance(Type.TUPLE, tuple(ret_res))

                    retType = ret.roottype
                    retDimensions = ret.array_dimensions

                    # Trace return (end block)
                    if (breakable and not returnable): # loops shouldn't trace returns per iteration
                        pass
                    else:
                        tupy.Interpreter.Interpreter.trace(ctx.stop.line, ret)
                else:
                    # Cannot return from a function without "retornar"
                    tupy.Interpreter.logger.debug("YOU SHOULD NOT BE RETURNING {0}".format(ret))
                    ret = tupy.Instance.Instance(Type.NULL, 0)
            else:
                # Retorna nulo
                tupy.Interpreter.logger.debug("NULL RET")
                ret = tupy.Instance.Instance(retType, retDimensions)

            (desiredType, arrayDimensions) = tupy.Interpreter.Interpreter.getReturnType()
            #desiredType = None -> Don't care
            if desiredType is None or \
            (desiredType == retType and arrayDimensions == retDimensions):
                tupy.Interpreter.Interpreter.doStep()
            else:
                tupy.Interpreter.logger.debug("Returned {0}".format(retType))
                tupy.errorHelper.typeError("A função deveria retornar {0}!".format(tupy.Interpreter.Interpreter.getReturnType()[0]), ctx)

        if not isClassDef:
            tupy.Interpreter.Interpreter.popFrame()

        return ret


    # Visit a parse tree produced by langParser#test.
    def visitTest(self, ctx:langParser.TestContext, evalList = None):
        if evalList is None:
            evalList = []
            isRoot = True
        else:
            isRoot = False

        if (ctx.expression()):
            evalList.append( (self.CONST_EXPR_OPERAND, ctx.expression()) )
        else:
            # Unary/Binary operators
            evalList.append( (self.CONST_OPERATOR, (ctx.op.type, len(ctx.test()))) )
            for expr in ctx.test():
                self.visitTest(expr, evalList)

        if isRoot:
            return self.parsePN(evalList)
        else:
            return evalList

    # UNUSED - TOKEN ACCESSED DIRECTLY
    #====================================================================
    # Visit a parse tree produced by langParser#comparisonOperator.
    # def visitComparisonOperator(self, ctx:langParser.ComparisonOperatorContext):
    #     return self.visitChildren(ctx)
    #====================================================================

    # Visit a parse tree produced by langParser#loopRange.
    def visitLoopRange(self, ctx:langParser.LoopRangeContext):
        begin_inst = self.visitExpression(ctx.expression(0)).get()
        end_inst = self.visitExpression(ctx.expression(1)).get()
        return (begin_inst, end_inst, ctx.INCLUSIVE() is not None)


    # UNUSED - TOKEN ACCESSED DIRECTLY
    #====================================================================
    # Visit a parse tree produced by langParser#rangeDelimiter.
    # def visitRangeDelimiter(self, ctx:langParser.RangeDelimiterContext):
    #     return self.visitChildren(ctx)
    #====================================================================


    # Visit a parse tree produced by langParser#rangeList.
    def visitRangeList(self, ctx:langParser.RangeListContext):
        return tuple(self.visitLoopRange(rng) for rng in ctx.loopRange())


    # Visit a parse tree produced by langParser#expression.
    def visitExpression(self, ctx:langParser.ExpressionContext, evalList = None):
        if evalList is None:
            evalList = []
            isRoot = True
        else:
            isRoot = False

        if (ctx.atom()):
            # Atomic expressions
            evalList.append( (self.CONST_ATOM_OPERAND, (ctx.atom(), ctx.trailer())) )
        else:
            # Unary/Binary operators
            evalList.append( (self.CONST_OPERATOR, (ctx.op.type, len(ctx.expression()))) )
            for expr in ctx.expression():
                self.visitExpression(expr, evalList)

        if isRoot:
            return self.parsePN(evalList)
        else:
            return evalList

    # Visit a parse tree produced by langParser#atom.
    def visitAtom(self, ctx:langParser.AtomContext):
        if ctx.dataType() is not None: #Any NAME
            return tupy.Variable.Symbol(str(ctx.dataType().getChild(0).getText()))
        elif ctx.TRUE() is not None:
            return tupy.Variable.Literal(tupy.Instance.Instance(Type.BOOL, True));
        elif ctx.FALSE() is not None:
            return tupy.Variable.Literal(tupy.Instance.Instance(Type.BOOL, False));
        elif ctx.NULL() is not None:
            return tupy.Variable.Literal(tupy.Instance.Instance(Type.NULL, 0));
        elif ctx.PI() is not None:
            return tupy.Variable.Literal(tupy.Instance.Instance(Type.FLOAT, math.pi));
        elif ctx.THIS() is not None:
            return tupy.Variable.Literal(tupy.Interpreter.Interpreter.getContextInst());
        elif len(ctx.CARDINALITY_OP()) == 2:
            res = self.visitTestOrExpression(ctx.testOrExpression())
            return res.cardinality()
        elif ctx.OPEN_PAREN() is not None:
            res = ()
            if ctx.testOrExpressionList() is not None:
                res = self.visitTestOrExpressionList(ctx.testOrExpressionList())
            if len(res)==1:
                return res[0]
            else:
                ret_res = [tupy.Interpreter.memAlloc(element.get()) for element in res]
                return tupy.Variable.Literal(tupy.Instance.Instance(Type.TUPLE, tuple(ret_res)));
        elif ctx.OPEN_BRACK() is not None:
            res = []
            if ctx.testOrExpressionList() is not None:
                lit_res = self.visitTestOrExpressionList(ctx.testOrExpressionList())
                res = [tupy.Interpreter.memAlloc(element.get()) for element in lit_res]
            try:
                return tupy.Variable.Literal(tupy.Instance.Instance(Type.ARRAY, list(res)));
            except TypeError:
                tupy.errorHelper.typeError("Os tipos dos elementos de uma lista devem ser consistentes!", ctx)
        else:
            return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#trailerArgs.
    def visitTrailer(self, ctx:langParser.TrailerContext):
        if ctx.OPEN_PAREN() is not None:
            trailerType = TrailerType.CALL
            trailerId = []
            if ctx.argList() is not None:
                trailerId = self.visitArgList(ctx.argList())
        elif ctx.OPEN_BRACK() is not None:
            trailerType = TrailerType.SUBSCRIPT
            trailerId = self.visitSubscriptList(ctx.subscriptList())
        else:
            trailerType = TrailerType.MEMBER
            trailerId = ctx.NAME().getText()
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
                tupy.errorHelper.syntaxError("Intervalo inválido!", ctx)
        else:
            return Subscript(begin=int(self.visitExpression(ctx.expression(0)).get().value),
                             end=int(self.visitExpression(ctx.expression(0)).get().value),
                             isSingle=True)

    # Visit a parse tree produced by langParser#testOrExpressionList.
    def visitTestOrExpressionList(self, ctx:langParser.TestOrExpressionListContext):
        return tuple(self.visitTestOrExpression(expr) for expr in ctx.testOrExpression())


    # Visit a parse tree produced by langParser#classDefinition.
    def visitClassDefinition(self, ctx:langParser.ClassDefinitionContext):
        names = ctx.NAME()
        className = names[0].getText()
        tupy.Interpreter.logger.debug("Visiting a class named {0}".format(className))
        classContext = tupy.Context.Context(tupy.Interpreter.Interpreter.classContextDepth,
                                True, struct=className, funcName="Classe {0}".format(className))

        lineage = [className]

        callStackTop = tupy.Interpreter.Interpreter.callStack.top()

        if (len(names) > 1):
            try:
                inherited = tupy.Interpreter.Interpreter.getClassContext(names[1].getText())
            except KeyError:
                tupy.errorHelper.typeError("A classe herdada {0} não foi encontrada!".format(names[1].getText()), ctx)

            # Because classes are parsed during eval (unlike functions),
            # there cannot be cycles in lineage
            # e.g.: A has child B which has child C which has child A

            inheritLineage = tupy.Interpreter.Interpreter.getClassLineage(names[1].getText())
            lineage.extend(inheritLineage)
            tupy.Interpreter.logger.debug("Inheriting from {0}".format(names[1].getText()))
            classContext.inheritSymbolTable(inherited)
            classContext.depth = inherited.depth + 1

        tupy.Interpreter.Interpreter.putClassContext(className, classContext, lineage)
        callStackTop.locals.defineFunction(className, (Type.NULL, 0), [], ctx.block(), isConstructor=True, overrideable=True)
        tupy.Interpreter.Interpreter.pushContext(classContext)
        tupy.Interpreter.Interpreter.putClassContext(className, classContext, lineage) # Make autoreferences possible

        ret = self.visitBlock(ctx.block(), funcName="Definição da classe {0}".format(className), originalContext=callStackTop)
        tupy.Interpreter.Interpreter.callStack.pop()
        return ret


    # Visit a parse tree produced by langParser#argList.
    def visitArgList(self, ctx:langParser.ArgListContext):
        return [self.visitTest(tt) for tt in ctx.test()]


    # Visit a parse tree produced by langParser#string.
    def visitString(self, ctx:langParser.StringContext):
        string = "".join([str(token.getText()) for token in ctx.STRING_LITERAL()]).replace("\\\"", "\"")
        return tupy.Variable.Literal(tupy.Instance.Instance(Type.STRING, string))


    # Visit a parse tree produced by langParser#character.
    def visitCharacter(self, ctx:langParser.StringContext):
        return tupy.Variable.Literal(tupy.Instance.Instance(Type.CHAR, ord(self.visitChildren(ctx).replace('\\\'', '\''))))


    # Visit a parse tree produced by langParser#number.
    def visitNumber(self, ctx:langParser.NumberContext):
        if ctx.integer() is None:
            return tupy.Variable.Literal(tupy.Instance.Instance(Type.FLOAT, float(self.visitChildren(ctx))))
        else:
            return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#integer.
    def visitInteger(self, ctx:langParser.IntegerContext):
        if ctx.DECIMAL_INTEGER() is not None:
            return tupy.Variable.Literal(tupy.Instance.Instance(Type.INT, int(self.visitChildren(ctx))))
        elif ctx.BIN_INTEGER() is not None:
            return tupy.Variable.Literal(tupy.Instance.Instance(Type.INT, int(self.visitChildren(ctx), 2)))
        elif ctx.HEX_INTEGER() is not None:
            return tupy.Variable.Literal(tupy.Instance.Instance(Type.INT, int(self.visitChildren(ctx), 16)))
        else: #ctx.OCT_INTEGER() is not None
            return tupy.Variable.Literal(tupy.Instance.Instance(Type.INT, int(self.visitChildren(ctx), 8)))

    def visitTerminal(self, node):
        # tupy.Interpreter.logger.debug("Got to terminal "+str(node))
        return str(node)


    def aggregateResult(self, aggregate, nextResult):
        # tupy.Interpreter.logger.debug("Aggregating "+str(aggregate)+" and "+str(nextResult))
        # if aggregate is not None:
        #     res = aggregate
        # else:
        res = nextResult
        # tupy.Interpreter.logger.debug("Gives us "+str(res))
        return res

    def mapLexType(self, lextype):
        return {
            self.parser.INTEGER: Type.INT,
            self.parser.REAL: Type.FLOAT,
            self.parser.CHAR: Type.CHAR,
            self.parser.STRING: Type.STRING,
            self.parser.BOOLEAN: Type.BOOL,
            self.parser.NAME: Type.STRUCT
        }.get(lextype, Type.NULL)

    def doDeclare(self, lhs, decltype, ctx, className, isInvisible):
        for lval in lhs:
            trailerCount = len(lval.trailers)
            if trailerCount == 1:
                if lval.trailers[0][0] == TrailerType.SUBSCRIPT:
                    subscriptList = lval.trailers[0][1]
                else:
                    tupy.errorHelper.syntaxError("Declaração inválida!", ctx)
            elif trailerCount == 0:
                subscriptList = []
            else:
                tupy.errorHelper.syntaxError("Declaração inválida!\n(Para declaração de matrizes, use M[x,y] ao invés de M[x][y])", ctx)

            if any((not x.isSingle and not x.isWildcard) for x in subscriptList):
                tupy.errorHelper.syntaxError("As dimensões de uma declaração não devem conter intervalos!", ctx)

            if any((x.begin < 1 and not x.isWildcard) for x in subscriptList):
                tupy.errorHelper.syntaxError("As dimensões de uma declaração devem ser maiores que zero!", ctx)

            if decltype==Type.STRUCT and not tupy.Interpreter.Interpreter.isValidClass(className):
                tupy.errorHelper.typeError("A classe {0} não foi declarada!".format(className), ctx)

            tupy.Interpreter.Interpreter.declareSymbol(lval.name, decltype, subscriptList, className, isInvisible)

    def executeStatements(self, statementList):
        s = statementList[0]
        try:
            ret = None
            for s in statementList:
                # tupy.Interpreter.logger.debug("visiting {0}".format(s))
                tupy.Interpreter.logger.debug("Executing statement ({1}) at line {0}...".format(s.start.line, type(s)))

                ret = self.visitStatement(s)

                # tupy.Interpreter.logger.debug("after visit I got {0}".format(ret))
                flow = tupy.Interpreter.Interpreter.flow
                if flow == tupy.Interpreter.FlowEvent.BREAK or flow == tupy.Interpreter.FlowEvent.CONTINUE:
                    tupy.Interpreter.logger.debug("BREAKING OR CONTINUING")
                    if tupy.Interpreter.Interpreter.canBreak():
                        tupy.Interpreter.Interpreter.doStep()
                    break
                elif flow == tupy.Interpreter.FlowEvent.RETURN:
                    ret = tupy.Interpreter.Interpreter.returnData
                    tupy.Interpreter.logger.debug("RETURNING {0}".format(ret))
                    break

            #TODO: Double check whether this is intended
            # try:
            try:
                if (len(ret)<=1):
                    return ret[0]
                else:
                    return ret
            except TypeError:
                return ret
        except AssertionError as e:
            tupy.errorHelper.assertionError(e.args[0], s)
        except NameError as e:
            tupy.errorHelper.nameError(e.args[0], s)
        except TypeError as e:
            tupy.errorHelper.typeError(e.args[0], s)
        except SyntaxError as e:
            tupy.errorHelper.syntaxError(e.args[0], s)
        except RuntimeError as e:
            tupy.errorHelper.runtimeError(e.args[0], s)
        except ValueError as e:
            tupy.errorHelper.valueError(e.args[0], s)
        except IndexError as e:
            tupy.errorHelper.indexError(e.args[0], s)

        # except Exception as e:
            # tupy.Interpreter.logger.debug("Poop, returning {0}. Got {1}".format(ret,e))
            # return ret
