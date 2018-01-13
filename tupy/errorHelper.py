import antlr4
import re

class TupyError(Exception):
    pass

class TupyIndexError(TupyError):
    pass

class TupyNameError(TupyError):
    pass

class TupyParseError(TupyError):
    pass

class TupyValueError(TupyError):
    pass

class TupyTypeError(TupyError):
    pass

class TupySyntaxError(TupyError):
    pass

class TupyRuntimeError(TupyError):
    pass

def indexError(message, ctx:antlr4.ParserRuleContext):
    raise TupyIndexError("ERRO: {0}".format(translate(message)), ctx.start.line)

def nameError(message, ctx:antlr4.ParserRuleContext):
    raise TupyNameError("ERRO: {0}".format(translate(message)), ctx.start.line)

def valueError(message, ctx:antlr4.ParserRuleContext):
    raise TupyValueError("ERRO: {0}".format(translate(message)), ctx.start.line)

def typeError(message, ctx:antlr4.ParserRuleContext):
    raise TupyTypeError("ERRO: {0}".format(translate(message)), ctx.start.line)

def parseError(message, line):
    raise TupyParseError("ERRO: {0}".format(translate(message)), line)

def syntaxError(message, ctx:antlr4.ParserRuleContext):
    raise TupySyntaxError("ERRO: {0}".format(translate(message)), ctx.start.line)

def runtimeError(message, ctx:antlr4.ParserRuleContext):
    raise TupyRuntimeError("ERRO: {0}".format(translate(message)), ctx.start.line)

def translate(msg):
    msg = str(msg)
    dicionario = {"mismatched input": "entrada incompatível", 
                    "expecting": "era esperado",
                    "no viable alternative at input": "não foi possível interpretar as instruções",
                    "unknown recognition error type": "erro desconhecido de reconhecimento",
                    "EOF": "FIM DE ARQUIVO",
                    "<unknown input>": "<entrada desconhecida>",
                    " rule": " regra",
                    "extraneous input": "entrada inválida",
                    "missing": "faltando",
                    " at ": " em ",
                    "list index out of range": "Acesso fora dos limites da lista!",
                    "Type.INT": "INTEIRO",
                    "Type.CHAR": "CARACTER",
                    "Type.FLOAT": "REAL",
                    "Type.STRING": "CADEIA",
                    "Type.BOOL": "LÓGICO",
                    "Type.STRUCT": "ESTRUTURA"
                    } 

    rep = dict((re.escape(k), v) for k, v in dicionario.items())
    pattern = re.compile("|".join(rep.keys()))
    msg = pattern.sub(lambda m: rep[re.escape(m.group(0))], msg)
    return msg
