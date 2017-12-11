import Interpreter as ii
import Argument
import Instance
import inspect
import copy
from Type import Type

def initialize():
    function("escrever", Type.STRING, [Type.TUPLE])
    function("caracter", Type.CHAR, [Type.INT])

def function(name, ret, argTypes, arrayDimensions=None, passByRef=None, defaults=None):
    argSpecs = inspect.getargspec(globals()[name])
    argNames = copy.copy(argSpecs.args)
    if argSpecs.varargs is not None:
        argNames.append(argSpecs.varargs)

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
        out = str(inst.value)
    return out

def stringProcess(string):
    return string.replace("\\n", "\n")

def caracter(inteiro):
    return Instance.Instance(Type.CHAR, inteiro.get().value)
