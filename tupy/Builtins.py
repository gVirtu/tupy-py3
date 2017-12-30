import tupy.Interpreter
import tupy.Argument
import tupy.Instance
import tupy.Variable
import inspect
import math
import copy
from tupy.Type import Type

def initialize():
    function("escrever", Type.STRING, [Type.TUPLE])
    function("caracter", Type.CHAR, [Type.INT])
    function("caracter", Type.CHAR, [Type.FLOAT])
    function("real", Type.FLOAT, [Type.INT])
    function("real", Type.FLOAT, [Type.CHAR])
    function("real", Type.FLOAT, [Type.BOOL])
    function("real", Type.FLOAT, [Type.STRING])
    function("inteiro", Type.INT, [Type.FLOAT])
    function("inteiro", Type.INT, [Type.CHAR])
    function("inteiro", Type.INT, [Type.BOOL])
    function("inteiro", Type.INT, [Type.STRING])
    function("cadeia", Type.STRING, [Type.FLOAT])
    function("cadeia", Type.STRING, [Type.CHAR])
    function("cadeia", Type.STRING, [Type.BOOL])
    function("cadeia", Type.STRING, [Type.INT])
    function("cadeia", Type.STRING, [Type.ARRAY])
    function("cadeia", Type.STRING, [Type.NULL])
    function("logico", Type.BOOL, [Type.FLOAT])
    function("logico", Type.BOOL, [Type.CHAR])
    function("logico", Type.BOOL, [Type.INT])
    function("logico", Type.BOOL, [Type.STRING])
    function("lógico", Type.BOOL, [Type.FLOAT])
    function("lógico", Type.BOOL, [Type.CHAR])
    function("lógico", Type.BOOL, [Type.INT])
    function("lógico", Type.BOOL, [Type.STRING])
    function("log", Type.FLOAT, [Type.FLOAT, Type.FLOAT], 
             defaults=[None, tupy.Variable.Literal(tupy.Instance.Instance(Type.FLOAT, math.e))])

def function(name, ret, argTypes, arrayDimensions=None, passByRef=None, defaults=None):
    argSpecs = inspect.getargspec(globals()[name])
    argNames = copy.copy(argSpecs.args)

    if arrayDimensions is None:
        arrayDimensions = [0] * len(argNames)

    if passByRef is None:
        passByRef = [False] * len(argNames)

    if defaults is None:
        defaults = [None] * len(argNames)

    argParamList = list(zip(argNames, argTypes, arrayDimensions, passByRef, defaults))
    args = [tupy.Argument.Argument(*params) for params in argParamList]
    tupy.Interpreter.Interpreter.callStack.top().locals.defineFunction(name, ret, args, name, True)

# BUILT-IN FUNCTIONS

def escrever(argsTuple):
    out = ' '.join([stringProcess(printInstance(tupy.Interpreter.memRead(arg))) for arg in argsTuple.get().value])
    tupy.Interpreter.Interpreter.output(out)
    return tupy.Instance.Instance(Type.STRING, out)

def printInstance(arg):
    inst = arg
    typ = inst.type
    if typ == Type.ARRAY: 
        out = str([printInstance(tupy.Interpreter.memRead(child)) for child in inst.value])
    elif typ == Type.TUPLE: 
        out = str(tuple([printInstance(tupy.Interpreter.memRead(child)) for child in inst.value]))
    elif typ == Type.CHAR:
        out = chr(inst.value)
    elif typ == Type.BOOL:
        out = str(bool(inst.value))
    else:
        out = inst.value #str(inst.value)
    return out

def stringProcess(string):
    return str(string).replace("\\n", "\n")

def caracter(literal):
    return tupy.Instance.Instance(Type.CHAR, int(literal.get().value))

def real(literal):
    try:
        return tupy.Instance.Instance(Type.FLOAT, float(literal.get().value))
    except ValueError:
        raise ValueError("Erro na conversão para REAL!")

def inteiro(literal):
    try:
        return tupy.Instance.Instance(Type.INT, int(literal.get().value))
    except ValueError:
        raise ValueError("Erro na conversão para INTEIRO!")

def cadeia(literal):
    return tupy.Instance.Instance(Type.STRING, printInstance(literal.get()))

def lógico(literal):
    return tupy.Instance.Instance(Type.BOOL, bool(literal.get().value))

def logico(literal):
    return lógico(literal)

def log(n, b):
    return tupy.Instance.Instance(Type.FLOAT, math.log(n.get().value, b.get().value))
