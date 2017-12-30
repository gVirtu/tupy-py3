import antlr4

class TupyNameError(Exception):
    pass

class TupyValueError(Exception):
    pass

class TupyTypeError(Exception):
    pass

class TupySyntaxError(Exception):
    pass

class TupyRuntimeError(Exception):
    pass

def nameError(message, ctx:antlr4.ParserRuleContext):
    raise TupyNameError("ERRO: {0} - Linha: {1}".format(message, ctx.start.line))

def valueError(message, ctx:antlr4.ParserRuleContext):
    raise TupyValueError("ERRO: {0} - Linha: {1}".format(message, ctx.start.line))

def typeError(message, ctx:antlr4.ParserRuleContext):
    raise TupyTypeError("ERRO: {0} - Linha: {1}".format(message, ctx.start.line))

def syntaxError(message, ctx:antlr4.ParserRuleContext):
    raise TupySyntaxError("ERRO: {0} - Linha: {1}".format(message, ctx.start.line))

def runtimeError(message, ctx:antlr4.ParserRuleContext):
    raise TupyRuntimeError("ERRO: {0} - Linha: {1}".format(message, ctx.start.line))
