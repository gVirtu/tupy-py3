import antlr4

class TupyError(Exception):
    pass

class TupyNameError(TupyError):
    pass

class TupyValueError(TupyError):
    pass

class TupyTypeError(TupyError):
    pass

class TupySyntaxError(TupyError):
    pass

class TupyRuntimeError(TupyError):
    pass

def nameError(message, ctx:antlr4.ParserRuleContext):
    raise TupyNameError("ERRO: {0}".format(message), ctx.start.line)

def valueError(message, ctx:antlr4.ParserRuleContext):
    raise TupyValueError("ERRO: {0}".format(message), ctx.start.line)

def typeError(message, ctx:antlr4.ParserRuleContext):
    raise TupyTypeError("ERRO: {0}".format(message), ctx.start.line)

def syntaxError(message, ctx:antlr4.ParserRuleContext):
    raise TupySyntaxError("ERRO: {0}".format(message), ctx.start.line)

def runtimeError(message, ctx:antlr4.ParserRuleContext):
    raise TupyRuntimeError("ERRO: {0}".format(message), ctx.start.line)
