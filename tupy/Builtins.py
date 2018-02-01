import tupy.Interpreter
import tupy.Argument
import tupy.Instance
import tupy.Variable
import inspect
import math
import random
import copy
import html
import builtins
from tupy.Type import Type

def initialize():
    function("asserção", Type.NULL, [Type.BOOL])
    function("assercao", Type.NULL, [Type.BOOL])
    function("escrever", Type.STRING, [Type.TUPLE])
    function("ler", Type.STRING, [Type.TUPLE], passByRef=[True])
    function("ler_linha", Type.STRING, [Type.STRING], passByRef=[True])
    function("copiar", Type.STRUCT, [Type.TUPLE])
    function("caracter", Type.CHAR, [Type.INT])
    function("caracter", Type.CHAR, [Type.STRING])
    function("real", Type.FLOAT, [Type.INT])
    function("real", Type.FLOAT, [Type.CHAR])
    function("real", Type.FLOAT, [Type.BOOL])
    function("real", Type.FLOAT, [Type.STRING])
    function("inteiro", Type.INT, [Type.FLOAT])
    function("inteiro", Type.INT, [Type.CHAR])
    function("inteiro", Type.INT, [Type.BOOL])
    function("inteiro", Type.INT, [Type.STRING, Type.INT],
             defaults=[None, tupy.Variable.Literal(tupy.Instance.Instance(Type.INT, 10))])
    function("cadeia", Type.STRING, [Type.TUPLE])
    # function("cadeia", Type.STRING, [Type.CHAR])
    # function("cadeia", Type.STRING, [Type.BOOL])
    # function("cadeia", Type.STRING, [Type.INT])
    # function("cadeia", Type.STRING, [Type.ARRAY])
    # function("cadeia", Type.STRING, [Type.NULL])
    function("binário", Type.STRING, [Type.INT])
    function("binario", Type.STRING, [Type.INT])
    function("octal", Type.STRING, [Type.INT])
    function("hexadecimal", Type.STRING, [Type.INT])
    function("logico", Type.BOOL, [Type.FLOAT])
    function("logico", Type.BOOL, [Type.CHAR])
    function("logico", Type.BOOL, [Type.INT])
    function("logico", Type.BOOL, [Type.STRING])
    function("lógico", Type.BOOL, [Type.FLOAT])
    function("lógico", Type.BOOL, [Type.CHAR])
    function("lógico", Type.BOOL, [Type.INT])
    function("lógico", Type.BOOL, [Type.STRING])
    function("log", Type.FLOAT, [Type.FLOAT, Type.FLOAT], 
             defaults=[None, tupy.Variable.Literal(tupy.Instance.Instance(Type.FLOAT, 10.0))])
    function("ln", Type.FLOAT, [Type.FLOAT])
    function("raiz", Type.FLOAT, [Type.FLOAT])
    function("raiz", Type.FLOAT, [Type.INT])
    function("exp", Type.FLOAT, [Type.FLOAT])
    function("exp", Type.FLOAT, [Type.INT])
    function("abs", Type.INT, [Type.INT])
    function("abs", Type.FLOAT, [Type.FLOAT])
    function("sinal", Type.INT, [Type.FLOAT])
    function("sinal", Type.INT, [Type.INT])
    function("piso", Type.FLOAT, [Type.FLOAT])
    function("teto", Type.FLOAT, [Type.FLOAT])
    function("arredondar", Type.FLOAT, [Type.FLOAT])
    function("graus", Type.FLOAT, [Type.FLOAT])
    function("graus", Type.FLOAT, [Type.INT])
    function("radianos", Type.FLOAT, [Type.FLOAT])
    function("radianos", Type.FLOAT, [Type.INT])
    function("sen", Type.FLOAT, [Type.FLOAT])
    function("cos", Type.FLOAT, [Type.FLOAT])
    function("tg", Type.FLOAT, [Type.FLOAT])
    function("arcsen", Type.FLOAT, [Type.FLOAT])
    function("arccos", Type.FLOAT, [Type.FLOAT])
    function("arctg", Type.FLOAT, [Type.FLOAT])
    function("arctg2", Type.FLOAT, [Type.FLOAT, Type.FLOAT])
    function("senh", Type.FLOAT, [Type.FLOAT])
    function("cosh", Type.FLOAT, [Type.FLOAT])
    function("tgh", Type.FLOAT, [Type.FLOAT])
    function("arsenh", Type.FLOAT, [Type.FLOAT])
    function("arcosh", Type.FLOAT, [Type.FLOAT])
    function("artgh", Type.FLOAT, [Type.FLOAT])
    function("aleatorio", Type.FLOAT, [])
    function("aleatorio", Type.FLOAT, [Type.FLOAT])
    function("aleatorio", Type.FLOAT, [Type.FLOAT, Type.FLOAT])
    function("aleatório", Type.FLOAT, [])
    function("aleatório", Type.FLOAT, [Type.FLOAT])
    function("aleatório", Type.FLOAT, [Type.FLOAT, Type.FLOAT])
    function("inteiro_aleatorio", Type.INT, [Type.INT])
    function("inteiro_aleatorio", Type.INT, [Type.INT, Type.INT])
    function("inteiro_aleatório", Type.INT, [Type.INT])
    function("inteiro_aleatório", Type.INT, [Type.INT, Type.INT])
    function("lista", Type.ARRAY, [Type.STRING, Type.STRING],
             defaults=[None, tupy.Variable.Literal(tupy.Instance.Instance(Type.STRING, ' '))])
    function("juntar", Type.STRING, [Type.TUPLE])
    function("embaralhar", Type.ARRAY, [Type.TUPLE])
    function("inserir", Type.ARRAY, [Type.TUPLE])
    function("remover", Type.ARRAY, [Type.TUPLE])
    for t in [Type.INT, Type.FLOAT, Type.CHAR, Type.STRING]:
        function("min", t, [t, t])
        function("mín", t, [t, t])
        function("max", t, [t, t])
        function("máx", t, [t, t])
    function("grafo_MA", Type.STRING, [Type.INT, Type.INT, Type.INT, Type.STRING], arrayDimensions=[2,1,2,0],
             defaults=[None, tupy.Variable.Literal(tupy.Instance.Instance(Type.ARRAY, [])),
                       tupy.Variable.Literal(tupy.Instance.Instance(Type.ARRAY, [], array_dimensions=2)),
                       tupy.Variable.Literal(tupy.Instance.Instance(Type.STRING, ""))])
    function("grafo_valorado_MA", Type.STRING, [Type.INT, Type.INT, Type.INT, Type.STRING], arrayDimensions=[2,1,2,0],
             defaults=[None, tupy.Variable.Literal(tupy.Instance.Instance(Type.ARRAY, [])),
                       tupy.Variable.Literal(tupy.Instance.Instance(Type.ARRAY, [], array_dimensions=2)),
                       tupy.Variable.Literal(tupy.Instance.Instance(Type.STRING, ""))])
    function("digrafo_MA", Type.STRING, [Type.INT, Type.INT, Type.INT, Type.STRING], arrayDimensions=[2,1,2,0],
             defaults=[None, tupy.Variable.Literal(tupy.Instance.Instance(Type.ARRAY, [])),
                       tupy.Variable.Literal(tupy.Instance.Instance(Type.ARRAY, [], array_dimensions=2)),
                       tupy.Variable.Literal(tupy.Instance.Instance(Type.STRING, ""))])
    function("digrafo_valorado_MA", Type.STRING, [Type.INT, Type.INT, Type.INT, Type.STRING], arrayDimensions=[2,1,2,0],
             defaults=[None, tupy.Variable.Literal(tupy.Instance.Instance(Type.ARRAY, [])),
                       tupy.Variable.Literal(tupy.Instance.Instance(Type.ARRAY, [], array_dimensions=2)),
                       tupy.Variable.Literal(tupy.Instance.Instance(Type.STRING, ""))])
    function("grafo_LA", Type.STRING, [Type.INT, Type.INT, Type.INT, Type.STRING], arrayDimensions=[2,1,2,0],
             defaults=[None, tupy.Variable.Literal(tupy.Instance.Instance(Type.ARRAY, [])),
                       tupy.Variable.Literal(tupy.Instance.Instance(Type.ARRAY, [], array_dimensions=2)),
                       tupy.Variable.Literal(tupy.Instance.Instance(Type.STRING, ""))])
    function("grafo_valorado_LA", Type.STRING, [Type.INT, Type.INT, Type.INT, Type.STRING], arrayDimensions=[3,1,2,0],
             defaults=[None, tupy.Variable.Literal(tupy.Instance.Instance(Type.ARRAY, [])),
                       tupy.Variable.Literal(tupy.Instance.Instance(Type.ARRAY, [], array_dimensions=2)),
                       tupy.Variable.Literal(tupy.Instance.Instance(Type.STRING, ""))])
    function("digrafo_LA", Type.STRING, [Type.INT, Type.INT, Type.INT, Type.STRING], arrayDimensions=[2,1,2,0],
             defaults=[None, tupy.Variable.Literal(tupy.Instance.Instance(Type.ARRAY, [])),
                       tupy.Variable.Literal(tupy.Instance.Instance(Type.ARRAY, [], array_dimensions=2)),
                       tupy.Variable.Literal(tupy.Instance.Instance(Type.STRING, ""))])
    function("digrafo_valorado_LA", Type.STRING, [Type.INT, Type.INT, Type.INT, Type.STRING], arrayDimensions=[3,1,2,0],
             defaults=[None, tupy.Variable.Literal(tupy.Instance.Instance(Type.ARRAY, [])),
                       tupy.Variable.Literal(tupy.Instance.Instance(Type.ARRAY, [], array_dimensions=2)),
                       tupy.Variable.Literal(tupy.Instance.Instance(Type.STRING, ""))])
    function("árvore", Type.STRING, [Type.TUPLE])
    function("arvore", Type.STRING, [Type.TUPLE])
    for t in [Type.INT, Type.FLOAT, Type.CHAR, Type.STRING, Type.BOOL]:
        function("matriz", Type.STRING, [t, Type.INT, Type.STRING], arrayDimensions=[2,2,0],
                defaults=[None, tupy.Variable.Literal(tupy.Instance.Instance(Type.ARRAY, [], array_dimensions=2)),
                        tupy.Variable.Literal(tupy.Instance.Instance(Type.STRING, ""))])
        function("vetor", Type.STRING, [t, Type.INT, Type.STRING], arrayDimensions=[1,1,0],
                defaults=[None, tupy.Variable.Literal(tupy.Instance.Instance(Type.ARRAY, [], array_dimensions=1)),
                        tupy.Variable.Literal(tupy.Instance.Instance(Type.STRING, ""))])
        function("pilha", Type.STRING, [t, Type.INT, Type.STRING], arrayDimensions=[1,1,0],
                defaults=[None, tupy.Variable.Literal(tupy.Instance.Instance(Type.ARRAY, [], array_dimensions=1)),
                        tupy.Variable.Literal(tupy.Instance.Instance(Type.STRING, ""))])
        function("fila", Type.STRING, [t, Type.INT, Type.STRING], arrayDimensions=[1,1,0],
                defaults=[None, tupy.Variable.Literal(tupy.Instance.Instance(Type.ARRAY, [], array_dimensions=1)),
                        tupy.Variable.Literal(tupy.Instance.Instance(Type.STRING, ""))])

def function(name, ret, argTypes, arrayDimensions=None, passByRef=None, defaults=None, classNames=None):
    argSpecs = inspect.getargspec(globals()[name])
    argNames = copy.copy(argSpecs.args)

    if arrayDimensions is None:
        arrayDimensions = [0] * len(argNames)

    if passByRef is None:
        passByRef = [False] * len(argNames)

    if defaults is None:
        defaults = [None] * len(argNames)

    if classNames is None:
        classNames = [None] * len(argNames)

    invisible = [None] * len(argNames)

    argParamList = list(zip(argNames, argTypes, arrayDimensions, passByRef, classNames, invisible, defaults))
    args = [tupy.Argument.Argument(*params) for params in argParamList]
    tupy.Interpreter.Interpreter.callStack.top().locals.defineFunction(name, ret, args, name, True)

# HELPERS
def cast(instance, target_type):
    if target_type == Type.INT:
        string = instance.value.upper()
        base = 10
        if string.startswith("0X"):
            base = 16
        elif string.startswith("0O"):
            base = 8
        elif string.startswith("0B"):
            base = 2
        return inteiro(instance, tupy.Instance.Instance(Type.INT, base))
    elif target_type == Type.FLOAT:
        return real(instance)
    elif target_type == Type.CHAR:
        return caracter(instance)
    elif target_type == Type.STRING:
        return tupy.Instance.Instance(Type.STRING, stringProcess(printInstance(instance)))
    elif target_type == Type.BOOL:
        return lógico(instance)
    else:
        raise ValueError("Conversão de tipo não suportada!")

def matrix_access(matrixVal, i, j):
    return cell_value(tupy.Interpreter.memRead(matrixVal[i]).value[j])

def cell_value(memoryCell):
    return tupy.Interpreter.memRead(memoryCell).value

def graph_nodes_and_highlights(node_count, highlights):
    # List nodes
    node_list = ["{0}; ".format(i) for i in range(node_count)]

    # Parse highlights
    parsed_highlights = ["{0} {1}".format(cell_value(elem), 
                                            _graph_highlight) for elem in highlights]

    return "".join(node_list + parsed_highlights)

def make_graph_edge_params(u, v, edge_highlights:set, weight, isWeighted):
    params = [" ["]
    if (u, v) in edge_highlights:
        params.append("color=\"red\"; ")
    if isWeighted:
        params.append("label=\"{0}\"; ".format(weight))
    params.append("]")
    return "".join(params)

def make_graph_LA_edge(i, j, edges:set, edge_highlights:set, weight=None):
    edges.add( (i, j) ); edges.add( (j, i) )
    params = [" ["]
    if (i, j) in edge_highlights:
        params.append("color=\"red\"; ")
    if (weight is not None):
        params.append("label=\"{0}\"; ".format(weight))
    params.append("]")
    return "{0} -- {1}{2}; ".format(i, j, "".join(params))

def digraph_adj_in_bounds(node, node_count):
    if (node < node_count): return True
    else: raise IndexError()

def dot_table_font_size(text):
    return {1: 27, 2: 23, 3: 20, 4: 15, 5: 12, 6: 10, 7: 9, 
            8: 8, 9: 7, 10: 6, 11: 6, 12: 5, 13: 5}.get(len(str(text)), 4)

# BUILT-IN FUNCTIONS

def asserção(cond):
    if not cond.value:
        raise AssertionError("Asserção violada!")
    return tupy.Instance.Instance(Type.NULL, 0)

def assercao(cond):
    return asserção(cond)

def escrever(argsTuple):
    out = ' '.join([stringProcess(printInstance(tupy.Interpreter.memRead(arg))) for arg in argsTuple.value])
    tupy.Interpreter.Interpreter.output(out)
    return tupy.Instance.Instance(Type.STRING, out)

def printInstance(arg):
    inst = arg
    typ = inst.type
    if typ == Type.ARRAY: 
        out = [printInstance(tupy.Interpreter.memRead(child)) for child in inst.value]
    elif typ == Type.TUPLE: 
        out = tuple([printInstance(tupy.Interpreter.memRead(child)) for child in inst.value])
    elif typ == Type.CHAR:
        out = chr(inst.value)
    elif typ == Type.BOOL:
        out = "verdadeiro" if (bool(inst.value)) else "falso"
    elif typ == Type.NULL:
        out = "nulo"
    elif typ == Type.STRUCT:
        out = inst.class_name
    elif typ == Type.FUNCTION:
        out = "função"
    elif typ == Type.REFERENCE:
        out = "referência a '{0}'".format(inst.value.name)
    else:
        out = inst.value #str(inst.value)
    return out

def stringProcess(string):
    return str(string).replace("\\n", "\n")

def ler(argsTuple):
    symbols = [cell_value(arg) for arg in argsTuple.value]

    # This is already checked by passByRef
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    # if not all([isinstance(symbol, tupy.Variable.Symbol) for symbol in symbols]):
    #     raise SyntaxError("A função ler não pode receber literais!")

    successCount = 0
    try:
        for symbol in symbols:
            content = tupy.Interpreter.Interpreter.inputSingle()
            inst = symbol.get()
            targetType = inst.type
            literal = tupy.Instance.Instance(Type.STRING, content)
            new_inst = cast(literal, targetType)
            tupy.Interpreter.Interpreter.storeSymbol(symbol.name, new_inst, symbol.trailers)
            successCount = successCount + 1
    except IndexError:
        pass    
    return tupy.Instance.Instance(Type.INT, successCount)

def ler_linha(instSimbolo):
    # if not isinstance(simbolo, tupy.Variable.Symbol):
    #     raise SyntaxError("A função ler_linha não pode receber um literal!")
    content = tupy.Interpreter.Interpreter.inputLine()
    result = False
    simbolo = instSimbolo.value
    if len(content) > 0:
        result = True
        new_inst = tupy.Instance.Instance(Type.STRING, content)
        tupy.Interpreter.Interpreter.storeSymbol(simbolo.name, new_inst, simbolo.trailers)
    return tupy.Instance.Instance(Type.BOOL, result)

def copiar(argsTuple):
    if len(argsTuple.value) != 1:
        raise ValueError("A função copiar espera exatamente um argumento!")
    instance = tupy.Interpreter.memRead(argsTuple.value[0])
    if instance.type != Type.STRUCT:
        raise TypeError("A função copiar não deve receber um tipo primitivo!")
    
    memo = {"structCopy": True}
    new_instance = copy.deepcopy(instance, memo)
    return new_instance

def caracter(literal):
    if literal.type == Type.INT:
        try:
            value = ord(chr(int(literal.value))) # Raises ValueErrors on negative
            return tupy.Instance.Instance(Type.CHAR, value)
        except ValueError:
            raise ValueError("Erro na conversão para CARACTER!")
    elif literal.type == Type.STRING:
        try:
            value = ord(literal.value) # Raises TypeErrors on strings of len != 1
            return tupy.Instance.Instance(Type.CHAR, value)
        except TypeError:
            try: # Maybe it's a string with a character code
                value = ord(chr(int(literal.value))) # Raises ValueErrors on negative
                return tupy.Instance.Instance(Type.CHAR, value)
            except ValueError:
                raise ValueError("Erro na conversão para CARACTER!")

def real(literal):
    try:
        return tupy.Instance.Instance(Type.FLOAT, float(literal.value))
    except ValueError:
        raise ValueError("Erro na conversão para REAL!")

def inteiro(literal, base=None):
    if (base):
        try:
            return tupy.Instance.Instance(Type.INT, int(literal.value, base.value))
        except ValueError:
            raise ValueError("Erro na conversão para INTEIRO (base {0})!".format(base))
    else:
        # No try/except needed because base will only be None when calling
        # inteiro with a FLOAT, BOOL or CHAR literal.
        return tupy.Instance.Instance(Type.INT, int(literal.value))

def cadeia(argsTuple):
    if len(argsTuple.value) != 1:
        raise ValueError("A função cadeia espera exatamente um argumento!")
    instance = tupy.Interpreter.memRead(argsTuple.value[0])
    return tupy.Instance.Instance(Type.STRING, stringProcess(printInstance(instance)))

def binário(literal):
    return tupy.Instance.Instance(Type.STRING, bin(literal.value)[2:])

def binario(literal):
    return binário(literal)

def octal(literal):
    return tupy.Instance.Instance(Type.STRING, oct(literal.value)[2:])

def hexadecimal(literal):
    return tupy.Instance.Instance(Type.STRING, hex(literal.value)[2:].upper())

def lógico(literal):
    return tupy.Instance.Instance(Type.BOOL, bool(literal.value))

def logico(literal):
    return lógico(literal)

def log(n, b):
    return tupy.Instance.Instance(Type.FLOAT, math.log(n.value, b.value))

def ln(n):
    return tupy.Instance.Instance(Type.FLOAT, math.log(n.value))

def raiz(n):
    return tupy.Instance.Instance(Type.FLOAT, math.sqrt(n.value))

def exp(n):
    return tupy.Instance.Instance(Type.FLOAT, math.exp(n.value))

def abs(n):
    return tupy.Instance.Instance(n.type, builtins.abs(n.value))

def sinal(n):
    return tupy.Instance.Instance(Type.INT, math.copysign(1, n.value))

def piso(n):
    return tupy.Instance.Instance(Type.FLOAT, math.floor(n.value))

def teto(n):
    return tupy.Instance.Instance(Type.FLOAT, math.ceil(n.value))

def arredondar(n):
    return tupy.Instance.Instance(Type.FLOAT, builtins.round(n.value))

def graus(n):
    return tupy.Instance.Instance(Type.FLOAT, math.degrees(n.value))

def radianos(n):
    return tupy.Instance.Instance(Type.FLOAT, math.radians(n.value))

def sen(n):
    return tupy.Instance.Instance(Type.FLOAT, math.sin(n.value))

def arcsen(n):
    return tupy.Instance.Instance(Type.FLOAT, math.asin(n.value))

def arsenh(n):
    return tupy.Instance.Instance(Type.FLOAT, math.asinh(n.value))

def senh(n):
    return tupy.Instance.Instance(Type.FLOAT, math.sinh(n.value))

def cos(n):
    return tupy.Instance.Instance(Type.FLOAT, math.cos(n.value))

def arccos(n):
    return tupy.Instance.Instance(Type.FLOAT, math.acos(n.value))

def arcosh(n):
    return tupy.Instance.Instance(Type.FLOAT, math.acosh(n.value))

def cosh(n):
    return tupy.Instance.Instance(Type.FLOAT, math.cosh(n.value))

def tg(n):
    return tupy.Instance.Instance(Type.FLOAT, math.tan(n.value))

def arctg(n):
    return tupy.Instance.Instance(Type.FLOAT, math.atan(n.value))

def arctg2(y, x):
    return tupy.Instance.Instance(Type.FLOAT, math.atan2(y.value, x.value))

def artgh(n):
    return tupy.Instance.Instance(Type.FLOAT, math.atanh(n.value))

def tgh(n):
    return tupy.Instance.Instance(Type.FLOAT, math.tanh(n.value))

def lista(string, sep):
    string_raw = string.value
    splitted = string_raw.split(sep.value)
    array = [tupy.Interpreter.memAlloc(tupy.Instance.Instance(Type.STRING, s)) for s in splitted]
    return tupy.Instance.Instance(Type.ARRAY, array)

def juntar(args):
    args = args.value
    list_inst = tupy.Interpreter.memRead(args[0])
    if (list_inst.type != Type.ARRAY and list_inst.type != Type.TUPLE):
        raise TypeError("O primeiro parâmetro da função juntar deve ser uma lista ou tupla!")

    if (len(args) < 2):
        sep = ""
    else:
        sep_inst = tupy.Interpreter.memRead(args[1])
        if (sep_inst.type != Type.STRING):
            raise TypeError("O segundo parâmetro da função juntar deve ser uma cadeia!")
        sep = str(sep_inst.value)

    ret = sep.join([stringProcess(printInstance(tupy.Interpreter.memRead(elem))) for elem in list_inst.value])
    return tupy.Instance.Instance(Type.STRING, ret)

def aleatorio(x=None, y=None):
    return aleatório(x,y)

def aleatório(x=None, y=None):
    if (x is None):
        return tupy.Instance.Instance(Type.FLOAT, random.random())
    elif (y is None):
        return tupy.Instance.Instance(Type.FLOAT, random.uniform(0, x.value))
    else:
        return tupy.Instance.Instance(Type.FLOAT, random.uniform(x.value, y.value))

def inteiro_aleatorio(x, y=None):
    return inteiro_aleatório(x,y)

def inteiro_aleatório(x, y=None):
    if (y is None):
        a = 0; b = x.value
    else:
        a = y.value; b = x.value

    return tupy.Instance.Instance(Type.INT, random.randint(builtins.min(a,b), builtins.max(a,b)))

def embaralhar(argsTuple):
    argsTuple = argsTuple.value
    if (len(argsTuple) == 1):
        inst = tupy.Interpreter.memRead(argsTuple[0])
        if (inst.is_pure_array()):
            val = inst.value
            return tupy.Instance.Instance(Type.ARRAY, random.sample(val, len(val)))
        else:
            raise TypeError("A função embaralhar não pode receber tipos que não sejam listas!")
    else:
        raise TypeError("A função embaralhar deve receber apenas uma lista!")

def inserir(argsTuple):
    argsTuple = argsTuple.value
    if (len(argsTuple) < 2):
        raise TypeError("Faltam argumentos para a função inserir(lista, elemento, [pos])!")
    elif (len(argsTuple) > 3):
        raise TypeError("A função inserir(lista, elemento, [pos]) recebeu argumentos demais!")
    else:
        inst = tupy.Interpreter.memRead(argsTuple[0])
        if (inst.is_pure_array()):
            val = inst.value
            elem_inst = tupy.Interpreter.memRead(argsTuple[1])

            # Root type == Literal Array when is empty, so most things are okay
            if (elem_inst.array_dimensions != inst.array_dimensions - 1 and inst.roottype != Type.ARRAY):
                dimensions = inst.array_dimensions - 1
                if dimensions == 0:
                    raise TypeError("A função inserir espera receber um segundo argumento primitivo!")
                else:
                    raise TypeError("A função inserir espera receber como segundo argumento um elemento de {0} dimens{1}!"
                                  .format(dimensions, "ão" if dimensions == 1 else "ões"))

            if (elem_inst.roottype != inst.roottype and inst.roottype != Type.ARRAY): 
                raise TypeError("A função inserir espera receber como segundo argumento um elemento de mesmo tipo que os contidos na lista!")

            if (elem_inst.type == Type.STRUCT and 
                not tupy.Interpreter.Interpreter.areClassNamesCompatible(inst.class_name, elem_inst.class_name)):
                raise TypeError("A classe {1} não pode ser inserida em uma lista de {0}!".format(inst.class_name, elem_inst.class_name))

            if len(argsTuple)>2:
                pos_inst = tupy.Interpreter.memRead(argsTuple[2])
                if (pos_inst.type == Type.INT):
                    pos = pos_inst.value
                else:
                    raise TypeError("A função inserir espera receber um inteiro como terceiro argumento!")
            else:
                pos = len(val)

            new_inst = copy.deepcopy(inst)
            new_inst.value.insert(pos, tupy.Interpreter.memAlloc(elem_inst))
            new_inst.update_size()

            return new_inst
        else:
            raise TypeError("A função inserir espera receber uma lista como primeiro argumento!")

def remover(argsTuple):
    argsTuple = argsTuple.value
    if (len(argsTuple) != 2):
        raise TypeError("A função remover(lista, pos) espera receber dois argumentos!")
    else:
        inst = tupy.Interpreter.memRead(argsTuple[0])
        if (inst.is_pure_array()):
            val = inst.value

            pos_inst = tupy.Interpreter.memRead(argsTuple[1])
            if (pos_inst.type == Type.INT):
                pos = pos_inst.value
            else:
                raise TypeError("A função remover espera receber um inteiro como segundo argumento!")

            new_inst = copy.deepcopy(inst)
            new_inst.value.pop(pos)
            new_inst.update_size()

            return new_inst
        else:
            raise TypeError("A função remover espera receber uma lista como primeiro argumento!")

def min(x, y):
    return tupy.Instance.Instance(x.type, builtins.min(x.value, y.value))

def max(x, y):
    return tupy.Instance.Instance(x.type, builtins.max(x.value, y.value))

def mín(x, y):
    return min(x, y)

def máx(x, y):
    return max(x, y)

_graph_opts = "overlap=false; node [fontsize=16 width=0.2 margin=0.05 shape=circle]; edge [arrowsize=0.8]; "
_graph_highlight = "[style = filled fillcolor = yellow]; "
_empty_graphviz_return = "[[DOT digraph G {{ 1 [label = \"{0} vazio!\" fontsize=\"25\" shape = \"plaintext\"] }}]]".format(chr(0x1F4E5))

def grafo_MA(matrix, highlights, edgeHighlights, extra, weighted=False):
    header = "[[DOT strict graph {"
    trailer = "}]]"
    matrix = matrix.value
    highlights = highlights.value
    edgeHighlights = edgeHighlights.value

    edgeHighlightSet = set()
    # Parse edge highlights into a set
    for highlight in edgeHighlights:
        highlight = cell_value(highlight)
        if len(highlight) != 2:
            raise ValueError("A lista de arestas destacadas deve conter listas de exatamente dois elementos!")
        pair = tuple(sorted([cell_value(coord) for coord in highlight]))
        edgeHighlightSet.add(pair)

    extra = extra.value

    n_lines = len(matrix)
    if all(len(cell_value(line)) == n_lines for line in matrix):
        if all(cell_value(elem) < n_lines for elem in highlights):
            # Parse connections
            parsed_connections = ["{0} -- {1}{2}; ".format(i, j, make_graph_edge_params(i, j, edgeHighlightSet, val, weighted))
                                                             for i in range(n_lines) \
                                                             for j in range(i, n_lines) \
                                                             for val in [matrix_access(matrix, i, j)] \
                                                             if val and matrix_access(matrix, j, i)]
            parsed_connections = "".join(parsed_connections)

            ret = "".join([header, _graph_opts, extra, graph_nodes_and_highlights(n_lines, highlights), 
                            parsed_connections, extra, trailer])
            return tupy.Instance.Instance(Type.STRING, ret)
        else:
            raise ValueError("A lista de nós destacados contém nós que não existem!")
    else:
        raise ValueError("A matriz de adjacências deve ser quadrada!")

def grafo_valorado_MA(matrix, highlights, edgeHighlights, extra):
    return grafo_MA(matrix, highlights, edgeHighlights, extra, True)

def digrafo_MA(matrix, highlights, edgeHighlights, extra, weighted=False):
    header = "[[DOT digraph {"
    trailer = "}]]"
    matrix = matrix.value
    highlights = highlights.value
    edgeHighlights = edgeHighlights.value
    extra = extra.value

    edgeHighlightSet = set()
    # Parse edge highlights into a set
    for highlight in edgeHighlights:
        highlight = cell_value(highlight)
        if len(highlight) != 2:
            raise ValueError("A lista de arestas destacadas deve conter listas de exatamente dois elementos!")
        pair = tuple([cell_value(coord) for coord in highlight])
        edgeHighlightSet.add(pair)

    n_lines = len(matrix)
    if all(len(cell_value(line)) == n_lines for line in matrix):
        if all(cell_value(elem) < n_lines for elem in highlights):            
            # Parse connections
            parsed_connections = ["{0} -> {1}{2}; ".format(i, j, make_graph_edge_params(i, j, edgeHighlightSet, val, weighted)) 
                                                             for i in range(n_lines) \
                                                             for j in range(n_lines) \
                                                             for val in [matrix_access(matrix, i, j)] \
                                                             if val]
            parsed_connections = "".join(parsed_connections)

            ret = "".join([header, _graph_opts, extra, graph_nodes_and_highlights(n_lines, highlights), 
                            parsed_connections, extra, trailer])
            return tupy.Instance.Instance(Type.STRING, ret)
        else:
            raise ValueError("A lista de nós destacados contém nós que não existem!")
    else:
        raise ValueError("A matriz de adjacências deve ser quadrada!")

def digrafo_valorado_MA(matrix, highlights, edgeHighlights, extra):
    return digrafo_MA(matrix, highlights, edgeHighlights, extra, True)

def grafo_LA(adjList, highlights, edgeHighlights, extra, weighted=False):
    header = "[[DOT strict graph {"
    trailer = "}]]"
    adjList = adjList.value
    highlights = highlights.value
    edgeHighlights = edgeHighlights.value

    edgeHighlightSet = set()
    # Parse edge highlights into a set
    for highlight in edgeHighlights:
        highlight = cell_value(highlight)
        if len(highlight) != 2:
            raise ValueError("A lista de arestas destacadas deve conter listas de exatamente dois elementos!")
        pair = tuple(sorted([cell_value(coord) for coord in highlight]))
        edgeHighlightSet.add(pair)

    extra = extra.value

    n_nodes = len(adjList)
    if all(cell_value(elem) < n_nodes for elem in highlights):
            try:           
                existing_connections = set()    
                # Parse connections
                if weighted:
                    parsed_connections = [ make_graph_LA_edge(i, valJ, existing_connections, edgeHighlightSet, weight) \
                                                                for i, elem in enumerate(adjList) \
                                                                for elemJ   in cell_value(elem) \
                                                                for pairJ   in [cell_value(elemJ)] \
                                                                for valJ    in [cell_value(pairJ[0])] \
                                                                for weight  in [cell_value(pairJ[1])] \
                                                                if (i, valJ) not in existing_connections \
                                                                and i in [cell_value(cell_value(cell)[0]) \
                                                                        for cell in cell_value(adjList[valJ])] 
                                                                ]
                else:
                    parsed_connections = [ make_graph_LA_edge(i, valJ, existing_connections, edgeHighlightSet) \
                                                                for i, elem in enumerate(adjList) \
                                                                for elemJ in cell_value(elem) \
                                                                for valJ in [cell_value(elemJ)] \
                                                                if (i, valJ) not in existing_connections \
                                                                and i in [cell_value(cell) \
                                                                        for cell in cell_value(adjList[valJ])] 
                                                                ]
                parsed_connections = "".join(parsed_connections)

                ret = "".join([header, _graph_opts, extra, graph_nodes_and_highlights(n_nodes, highlights), 
                                parsed_connections, extra, trailer])
                return tupy.Instance.Instance(Type.STRING, ret)
            except IndexError as ex:
                raise IndexError("A lista contém uma ou mais adjacências com nós que não existem!")
    else:
        raise ValueError("A lista de nós destacados contém nós que não existem!")

def grafo_valorado_LA(adjList, highlights, edgeHighlights, extra):
    return grafo_LA(adjList, highlights, edgeHighlights, extra, True)

def digrafo_LA(adjList, highlights, edgeHighlights, extra, weighted=False):
    header = "[[DOT digraph {"
    trailer = "}]]"
    adjList = adjList.value
    highlights = highlights.value
    edgeHighlights = edgeHighlights.value
    extra = extra.value

    edgeHighlightSet = set()
    # Parse edge highlights into a set
    for highlight in edgeHighlights:
        highlight = cell_value(highlight)
        if len(highlight) != 2:
            raise ValueError("A lista de arestas destacadas deve conter listas de exatamente dois elementos!")
        pair = tuple([cell_value(coord) for coord in highlight])
        edgeHighlightSet.add(pair)

    n_nodes = len(adjList)
    if all(cell_value(elem) < n_nodes for elem in highlights):
            try:               
                # Parse connections
                if weighted:
                    parsed_connections = ["{0} -> {1}{2}; ".format(i, valJ, make_graph_edge_params(i, valJ, edgeHighlightSet, weight, True)) \
                                                                for i, elem in enumerate(adjList) \
                                                                for elemJ in cell_value(elem) \
                                                                for pairJ   in [cell_value(elemJ)] \
                                                                for valJ    in [cell_value(pairJ[0])] \
                                                                for weight  in [cell_value(pairJ[1])] \
                                                                if digraph_adj_in_bounds(valJ, n_nodes)
                                                                ]
                else:
                    parsed_connections = ["{0} -> {1}{2}; ".format(i, valJ, make_graph_edge_params(i, valJ, edgeHighlightSet, 0, False)) \
                                                                for i, elem in enumerate(adjList) \
                                                                for elemJ in cell_value(elem) \
                                                                for valJ in [cell_value(elemJ)] \
                                                                if digraph_adj_in_bounds(valJ, n_nodes)
                                                                ]
                parsed_connections = "".join(parsed_connections)

                ret = "".join([header, _graph_opts, extra, graph_nodes_and_highlights(n_nodes, highlights), 
                                parsed_connections, extra, trailer])
                return tupy.Instance.Instance(Type.STRING, ret)
            except IndexError as ex:
                raise IndexError("A lista contém uma ou mais adjacências com nós que não existem!")
    else:
        raise ValueError("A lista de nós destacados contém nós que não existem!")

def digrafo_valorado_LA(adjList, highlights, edgeHighlights, extra):
    return digrafo_LA(adjList, highlights, edgeHighlights, extra, True)

def árvore(argsTuple):
    argsTuple = argsTuple.value
    if (len(argsTuple) < 3):
        raise TypeError("Faltam argumentos para a função árvore(estrutura, nome_chave, nome_filhos, [destaques, opções])!")
    elif (len(argsTuple) > 5):
        raise TypeError("A função árvore(estrutura, nome_chave, nome_filhos, [destaques, opções]) recebeu argumentos demais!")
    else:
        header = "[[DOT digraph {"
        trailer = "}]]"

        # Gather and validate parameters

        treeInst = tupy.Interpreter.memRead(argsTuple[0])
        treeKeyNameInst = tupy.Interpreter.memRead(argsTuple[1])
        treeEdgesNameInst = tupy.Interpreter.memRead(argsTuple[2])
        highlightsInst = tupy.Interpreter.memRead(argsTuple[3]) if len(argsTuple) > 3 \
                                                        else tupy.Instance.Instance(Type.ARRAY, [])
        optsInst = tupy.Interpreter.memRead(argsTuple[4]) if len(argsTuple) > 4 \
                                                    else tupy.Instance.Instance(Type.STRING, "")

        if (treeInst.type != Type.STRUCT):
            raise TypeError("O primeiro parâmetro para a função árvore deve ser uma estrutura representando a raiz da árvore!")
        if (treeKeyNameInst.type != Type.STRING):
            raise TypeError("O segundo parâmetro para a função árvore deve ser uma cadeia com o nome do atributo que contém a chave do nó!")
        if (treeEdgesNameInst.type != Type.STRING):
            raise TypeError("O terceiro parâmetro para a função árvore deve ser uma cadeia com o nome do atributo que contém uma lista de filhos!")
        if (not highlightsInst.is_pure_array() or 
            (highlightsInst.array_length() > 0 and
             not tupy.Interpreter.Interpreter.areClassNamesCompatible(treeInst.class_name, highlightsInst.class_name))):
            raise TypeError("O quarto parâmetro para a função árvore (opcional) deve ser uma lista de referências para nós que serão destacados!")
        if (optsInst.type != Type.STRING):
            raise TypeError("O quinto parâmetro para a função árvore (opcional) deve ser uma cadeia com instruções DOT que serão acrescentadas à definição!")

        treeKeyName = treeKeyNameInst.value
        treeEdgesName = treeEdgesNameInst.value
        if (not treeInst.value.locals.hasKey(treeKeyName)):
            raise NameError("A árvore fornecida não possui o atributo '{0}' para a chave!".format(treeKeyName))
        if (not treeInst.value.locals.hasKey(treeEdgesName)):
            raise NameError("A árvore fornecida não possui o atributo '{0}' para a lista de filhos!".format(treeEdgesName))
        if (not tupy.Interpreter.Interpreter.areClassNamesCompatible(treeInst.class_name, treeInst.value.locals.classname[treeEdgesName])):
            raise TypeError("A lista de filhos da árvore deve possuir referências para estruturas compatíveis com o tipo da árvore!")
        
        levelMap = {}
        highlights = set( [id(cell_value(treeCell)) for treeCell in highlightsInst.value ] )
        treeDefinition = "".join(recurse_tree(treeInst, None, 0, treeKeyName, treeEdgesName, highlights, set(), levelMap))
        levelDefinitions = []
        for nodeLevel, nodeList in levelMap.items():
            level = "".join("{0}; ".format(node) for node in nodeList)  
            level = ["{rank = same; ", level, "}; "]
            level = "".join(level)
            levelDefinitions.append(level)
        levelDefinitions = "".join(levelDefinitions)

        extra = optsInst.value

        ret = "".join([header, _graph_opts, extra, treeDefinition, levelDefinitions, extra, trailer])
        return tupy.Instance.Instance(Type.STRING, ret)

def arvore(argsTuple):
    return árvore(argsTuple)

def recurse_tree(treeInst, parentIdentifier, level, keyName, edgesName, 
                    highlights:set, nameMapping:set, levelMap:dict):
    identifier = len(nameMapping)
    if (id(treeInst) in nameMapping):
        raise RuntimeError("A estrutura fornecida para a função árvore não pode conter ciclos!")

    nameMapping.add(id(treeInst))

    if (level not in levelMap):
        levelMap[level] = []
    levelMap[level].append(identifier)

    if (treeInst.type == Type.NULL):
        return "{0} -> {1} [style = invis]; {1} [style = invis]; ".format(parentIdentifier, identifier)
    else :
        neighbors = [tupy.Interpreter.memRead(neighbor) \
                        for neighbor in treeInst.value.locals.get(edgesName).value]

        if all(neighbor.type == Type.NULL for neighbor in neighbors):
            result = [] # avoid putting unnecessary stuff
        else:
            result = [recurse_tree(neighbor, identifier, level+1, keyName, edgesName, \
                                highlights, nameMapping, levelMap) \
                                for neighbor in neighbors]

        if (parentIdentifier is not None):
            result.append("{0} -> {1}; ".format(parentIdentifier, identifier))

        if (id(treeInst.value) in highlights):
            result.append("{0} {1}".format(identifier, _graph_highlight))
        
        keyInst = treeInst.value.locals.get(keyName)
        result.append("{0} [label = \"{1}\"]; ".format(identifier, stringProcess(printInstance(keyInst))))
        resultString = "".join(result)

        return resultString

def matriz(matriz, highlights, extra):
    matriz = matriz.value
    if not len(matriz): return tupy.Instance.Instance(Type.STRING, _empty_graphviz_return)
    highlights = highlights.value
    highlightSet = set()
    # Parse highlights into a set
    for highlight in highlights:
        highlight = cell_value(highlight)
        if len(highlight) != 2:
            raise ValueError("A lista de destaques da função matriz deve conter listas de exatamente dois elementos cada!")
        pair = tuple([cell_value(coord) for coord in highlight])
        highlightSet.add(pair)
    extra = extra.value
    header = "[[DOT digraph G {node [shape=plaintext]; 1 [label = <<TABLE BORDER=\"0\" CELLPADDING=\"0\" CELLSPACING=\"0\">"
    trailer = "</TABLE>>]; {0}}}]]".format(extra)
    rowHeader = "<TR>"
    rowTrailer = "</TR>"
    element = "<TD PORT=\"{4}\" BGCOLOR=\"{3}\" BORDER=\"{2}\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\"><FONT FACE=\"COURIER\" POINT-SIZE=\"{1}\">{0}</FONT></TD>"
    getBgColor = lambda i,j : "YELLOW" if (i,j) in highlightSet else "WHITE"
    result = [header]
    rowResults = []
    columns = 0
    for i, row in enumerate(matriz):
        row = cell_value(row)
        columns = builtins.max(len(row), columns)
        rowResults.append(rowHeader)
        rowResults.append(element.format(i, dot_table_font_size(i), 0, "WHITE", "r{0}".format(i)))
        for j, column in enumerate(row):
            columnInst = tupy.Interpreter.memRead(column)
            columnText = html.escape(stringProcess(printInstance(columnInst)))
            rowResults.append(element.format(columnText, dot_table_font_size(columnText), 1, getBgColor(i,j), "v{0}_{1}".format(i, j)))
        rowResults.append(rowTrailer)

    result.append(rowHeader)
    result.append(element.format(" ", dot_table_font_size(" "), 0, "WHITE", "rc"))
    for i in range(columns):
        result.append(element.format(i, dot_table_font_size(i), 0, "WHITE", "c{0}".format(i)))
    result.append(rowTrailer)

    result.extend(rowResults)
    result.append(trailer)

    return tupy.Instance.Instance(Type.STRING, "".join(result))

def vetor(vetor, highlights, extra):
    vetor = vetor.value
    columns = len(vetor)
    if not columns: return tupy.Instance.Instance(Type.STRING, _empty_graphviz_return)
    highlights = [cell_value(cell) for cell in highlights.value]
    highlightSet = set(highlights)
    extra = extra.value
    header = "[[DOT digraph G {node [shape=plaintext]; 1 [label = <<TABLE BORDER=\"0\" CELLPADDING=\"0\" CELLSPACING=\"0\">"
    trailer = "</TABLE>>]; {0}}}]]".format(extra)
    rowHeader = "<TR>"; rowTrailer = "</TR>"
    element = "<TD PORT=\"{4}\" BGCOLOR=\"{3}\" BORDER=\"{2}\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\"><FONT FACE=\"COURIER\" POINT-SIZE=\"{1}\">{0}</FONT></TD>"
    getBgColor = lambda i : "YELLOW" if i in highlightSet else "WHITE"
    result = [header]
    result.append(rowHeader)
    for i in range(columns):
        result.append(element.format(i, dot_table_font_size(i), 0, "WHITE", "c{0}".format(i)))
    result.append(rowTrailer)
    result.append(rowHeader)
    for i, column in enumerate(vetor):
        columnInst = tupy.Interpreter.memRead(column)
        columnText = html.escape(stringProcess(printInstance(columnInst)))
        result.append(element.format(columnText, dot_table_font_size(columnText), 1, getBgColor(i), "v{0}".format(i)))
    result.append(rowTrailer)
    result.append(trailer)
    return tupy.Instance.Instance(Type.STRING, "".join(result))

def pilha(vetor, highlights, extra):
    vetor = vetor.value
    rows = len(vetor)
    if not rows: return tupy.Instance.Instance(Type.STRING, _empty_graphviz_return)
    highlights = [cell_value(cell) for cell in highlights.value]
    highlightSet = set(highlights)
    extra = extra.value
    header = ("[[DOT digraph G {node [shape=plaintext]; edge [arrowsize = 0.5]; "
              "0 [label = \" \"]; 0 -> 1; 1 -> 0; 1 [label = <<TABLE BORDER=\"0\" "
              "CELLPADDING=\"0\" CELLSPACING=\"0\">")
    trailer = "</TABLE>>]; {0}}}]]".format(extra)
    element = ("<TR><TD PORT=\"{5}\" SIDES=\"{4}\" BGCOLOR=\"{3}\" BORDER=\"{2}\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
               "<FONT FACE=\"COURIER\" POINT-SIZE=\"{1}\">{0}</FONT></TD></TR>")
    getBgColor = lambda i : "YELLOW" if i in highlightSet else "WHITE"
    getSides = lambda i: "LBR" if i == 0 else "LBRT"
    result = [header]
    for i, row in enumerate(reversed(vetor)):
        rowInst = tupy.Interpreter.memRead(row)
        rowText = html.escape(stringProcess(printInstance(rowInst)))
        result.append(element.format(rowText, dot_table_font_size(rowText), 1, getBgColor(i), getSides(i), "v{0}".format(len(vetor)-i-1)))
    result.append(trailer)
    return tupy.Instance.Instance(Type.STRING, "".join(result))

def fila(vetor, highlights, extra):
    vetor = vetor.value
    columns = len(vetor)
    if not columns: return tupy.Instance.Instance(Type.STRING, _empty_graphviz_return)
    highlights = [cell_value(cell) for cell in highlights.value]
    highlightSet = set(highlights)
    extra = extra.value
    header = ("[[DOT digraph G {node [shape=plaintext]; edge [arrowsize = 0.5]; "
              "C [label = \" \"]; F [label = \" \"]; F -> 1; 1 -> C; {rank = same; F; 1; C;} 1 [label = "
              "<<TABLE BORDER=\"0\" CELLPADDING=\"0\" CELLSPACING=\"0\">")
    trailer = "</TABLE>>]; {0}}}]]".format(extra)
    element = ("<TD PORT=\"{5}\" SIDES=\"{4}\" BGCOLOR=\"{3}\" BORDER=\"{2}\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
               "<FONT FACE=\"COURIER\" POINT-SIZE=\"{1}\">{0}</FONT></TD>")
    rowHeader = "<TR>"; rowTrailer = "</TR>"
    getBgColor = lambda i : "YELLOW" if i in highlightSet else "WHITE"
    getSides = lambda i: "BT" if columns == 1 else {0: "BRT", (columns-1): "LBT"}.get(i, "LBRT")
    result = [header]
    result.append(rowHeader)
    for i, column in enumerate(reversed(vetor)):
        columnInst = tupy.Interpreter.memRead(column)
        columnText = html.escape(stringProcess(printInstance(columnInst)))
        result.append(element.format(columnText, dot_table_font_size(columnText), 1, getBgColor(i), getSides(i), "v{0}".format(len(vetor)-i-1)))
    result.append(rowTrailer)
    result.append(trailer)
    return tupy.Instance.Instance(Type.STRING, "".join(result))
