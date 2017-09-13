import Interpreter as ii
import Argument
import inspect
import copy
from Type import Type

def initialize():
    function("escrever", Type.STRING, [Type.TUPLE])

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
    ii.Interpreter.defineFunction(name, ret, args, name, True)

# BUILT-IN FUNCTIONS

def escrever(argsTuple):
    out = ' '.join([printLiteral(arg) for arg in argsTuple.get().value])
    ii.Interpreter.output(out)
    return out

def printLiteral(arg):
    inst = arg.get()
    typ = inst.type
    if typ == Type.ARRAY: 
        out = str([printLiteral(child) for child in inst.value])
    elif typ == Type.TUPLE: 
        out = str(tuple([printLiteral(child) for child in inst.value]))
    elif typ == Type.CHAR:
        out = chr(inst.value)
    else:
        out = str(inst.value)
    return out