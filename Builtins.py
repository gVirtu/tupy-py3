import Interpreter as ii
import Argument
import Instance
import Variable as v
import inspect
import math
import copy
from Type import Type

def initialize():
    function("escrever", Type.STRING, [Type.TUPLE])
    function("caracter", Type.CHAR, [Type.INT])
    function("real", Type.FLOAT, [Type.INT])
    function("log", Type.FLOAT, [Type.FLOAT, Type.FLOAT], 
             defaults=[None, v.Literal(Instance.Instance(Type.FLOAT, math.e))])

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
    args = [Argument.Argument(*params) for params in argParamList]
    ii.Interpreter.callStack.top().locals.defineFunction(name, ret, args, name, True)

# BUILT-IN FUNCTIONS

def escrever(argsTuple):
    out = ' '.join([stringProcess(printInstance(ii.memRead(arg))) for arg in argsTuple.get().value])
    ii.Interpreter.output(out)
    return out

def printInstance(arg):
    inst = arg
    typ = inst.type
    if typ == Type.ARRAY: 
        out = str([printInstance(ii.memRead(child)) for child in inst.value])
    elif typ == Type.TUPLE: 
        out = str(tuple([printInstance(ii.memRead(child)) for child in inst.value]))
    elif typ == Type.CHAR:
        out = chr(inst.value)
    else:
        out = inst.value #str(inst.value)
    return out

def stringProcess(string):
    return str(string).replace("\\n", "\n")

def caracter(inteiro):
    return Instance.Instance(Type.CHAR, inteiro.get().value)

def real(inteiro):
    return Instance.Instance(Type.FLOAT, inteiro.get().value)

def log(n, b):
    return Instance.Instance(Type.FLOAT, math.log(n.get().value, b.get().value))
