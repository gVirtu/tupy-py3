import tupy.Interpreter
import tupy.Argument
import tupy.Instance
import tupy.Variable
import inspect
import math
import random
import copy
import builtins
from tupy.Type import Type

def initialize():
    function("escrever", Type.STRING, [Type.TUPLE])
    function("caracter", Type.CHAR, [Type.INT])
    function("real", Type.FLOAT, [Type.INT])
    function("real", Type.FLOAT, [Type.CHAR])
    function("real", Type.FLOAT, [Type.BOOL])
    function("real", Type.FLOAT, [Type.STRING])
    function("inteiro", Type.INT, [Type.FLOAT])
    function("inteiro", Type.INT, [Type.CHAR])
    function("inteiro", Type.INT, [Type.BOOL])
    function("inteiro", Type.INT, [Type.STRING, Type.INT],
             defaults=[None, tupy.Variable.Literal(tupy.Instance.Instance(Type.INT, 10))])
    function("cadeia", Type.STRING, [Type.FLOAT])
    function("cadeia", Type.STRING, [Type.CHAR])
    function("cadeia", Type.STRING, [Type.BOOL])
    function("cadeia", Type.STRING, [Type.INT])
    function("cadeia", Type.STRING, [Type.ARRAY])
    function("cadeia", Type.STRING, [Type.NULL])
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
             defaults=[None, tupy.Variable.Literal(tupy.Instance.Instance(Type.FLOAT, math.e))])
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
    function("embaralhar", Type.ARRAY, [Type.TUPLE])
    function("inserir", Type.ARRAY, [Type.TUPLE])
    function("remover", Type.ARRAY, [Type.TUPLE])
    function("min", Type.INT, [Type.INT, Type.INT])
    function("mín", Type.INT, [Type.INT, Type.INT])
    function("min", Type.FLOAT, [Type.FLOAT, Type.FLOAT])
    function("mín", Type.FLOAT, [Type.FLOAT, Type.FLOAT])
    function("min", Type.CHAR, [Type.CHAR, Type.CHAR])
    function("mín", Type.CHAR, [Type.CHAR, Type.CHAR])
    function("min", Type.STRING, [Type.STRING, Type.STRING])
    function("mín", Type.STRING, [Type.STRING, Type.STRING])
    function("máx", Type.INT, [Type.INT, Type.INT])
    function("max", Type.INT, [Type.INT, Type.INT])
    function("máx", Type.FLOAT, [Type.FLOAT, Type.FLOAT])
    function("max", Type.FLOAT, [Type.FLOAT, Type.FLOAT])
    function("máx", Type.CHAR, [Type.CHAR, Type.CHAR])
    function("max", Type.CHAR, [Type.CHAR, Type.CHAR])
    function("máx", Type.STRING, [Type.STRING, Type.STRING])
    function("max", Type.STRING, [Type.STRING, Type.STRING])
    function("grafo_MA", Type.STRING, [Type.INT, Type.INT], arrayDimensions=[2,1],
             defaults=[None, tupy.Variable.Literal(tupy.Instance.Instance(Type.ARRAY, []))])
    function("digrafo_MA", Type.STRING, [Type.INT, Type.INT], arrayDimensions=[2,1],
             defaults=[None, tupy.Variable.Literal(tupy.Instance.Instance(Type.ARRAY, []))])
    function("grafo_LA", Type.STRING, [Type.INT, Type.INT], arrayDimensions=[2,1],
             defaults=[None, tupy.Variable.Literal(tupy.Instance.Instance(Type.ARRAY, []))])
    function("digrafo_LA", Type.STRING, [Type.INT, Type.INT], arrayDimensions=[2,1],
             defaults=[None, tupy.Variable.Literal(tupy.Instance.Instance(Type.ARRAY, []))])

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

# HELPERS

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

def make_graph_LA_edge(i, j, edges:set):
    edges.add( (i, j) ); edges.add( (j, i) )
    return "{0} -- {1}; ".format(i, j)

def digraph_adj_in_bounds(node, node_count):
    if (node < node_count): return True
    else: raise IndexError()

# BUILT-IN FUNCTIONS

def escrever(argsTuple):
    out = ' '.join([stringProcess(printInstance(tupy.Interpreter.memRead(arg))) for arg in argsTuple.get().value])
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

def inteiro(literal, base=None):
    if (base):
        try:
            return tupy.Instance.Instance(Type.INT, int(literal.get().value, base.get().value))
        except ValueError:
            raise ValueError("Erro na conversão para INTEIRO!")
    else:
        return tupy.Instance.Instance(Type.INT, int(literal.get().value))

def cadeia(literal):
    return tupy.Instance.Instance(Type.STRING, stringProcess(printInstance(literal.get())))

def binário(literal):
    return tupy.Instance.Instance(Type.STRING, bin(literal.get().value)[2:])

def binario(literal):
    return binário(literal)

def octal(literal):
    return tupy.Instance.Instance(Type.STRING, oct(literal.get().value)[2:])

def hexadecimal(literal):
    return tupy.Instance.Instance(Type.STRING, hex(literal.get().value)[2:].upper())

def lógico(literal):
    return tupy.Instance.Instance(Type.BOOL, bool(literal.get().value))

def logico(literal):
    return lógico(literal)

def log(n, b):
    return tupy.Instance.Instance(Type.FLOAT, math.log(n.get().value, b.get().value))

def ln(n):
    return tupy.Instance.Instance(Type.FLOAT, math.log(n.get().value))

def raiz(n):
    return tupy.Instance.Instance(Type.FLOAT, math.sqrt(n.get().value))

def exp(n):
    return tupy.Instance.Instance(Type.FLOAT, math.exp(n.get().value))

def abs(n):
    return tupy.Instance.Instance(n.get().type, builtins.abs(n.get().value))

def sinal(n):
    return tupy.Instance.Instance(Type.INT, math.copysign(1, n.get().value))

def piso(n):
    return tupy.Instance.Instance(Type.FLOAT, math.floor(n.get().value))

def teto(n):
    return tupy.Instance.Instance(Type.FLOAT, math.ceil(n.get().value))

def arredondar(n):
    return tupy.Instance.Instance(Type.FLOAT, builtins.round(n.get().value))

def graus(n):
    return tupy.Instance.Instance(Type.FLOAT, math.degrees(n.get().value))

def radianos(n):
    return tupy.Instance.Instance(Type.FLOAT, math.radians(n.get().value))

def sen(n):
    return tupy.Instance.Instance(Type.FLOAT, math.sin(n.get().value))

def arcsen(n):
    return tupy.Instance.Instance(Type.FLOAT, math.asin(n.get().value))

def arsenh(n):
    return tupy.Instance.Instance(Type.FLOAT, math.asinh(n.get().value))

def senh(n):
    return tupy.Instance.Instance(Type.FLOAT, math.sinh(n.get().value))

def cos(n):
    return tupy.Instance.Instance(Type.FLOAT, math.cos(n.get().value))

def arccos(n):
    return tupy.Instance.Instance(Type.FLOAT, math.acos(n.get().value))

def arcosh(n):
    return tupy.Instance.Instance(Type.FLOAT, math.acosh(n.get().value))

def cosh(n):
    return tupy.Instance.Instance(Type.FLOAT, math.cosh(n.get().value))

def tg(n):
    return tupy.Instance.Instance(Type.FLOAT, math.tan(n.get().value))

def arctg(n):
    return tupy.Instance.Instance(Type.FLOAT, math.atan(n.get().value))

def arctg2(y, x):
    return tupy.Instance.Instance(Type.FLOAT, math.atan2(y.get().value, x.get().value))

def artgh(n):
    return tupy.Instance.Instance(Type.FLOAT, math.atanh(n.get().value))

def tgh(n):
    return tupy.Instance.Instance(Type.FLOAT, math.tanh(n.get().value))

def lista(string, sep):
    string_raw = string.get().value
    splitted = string_raw.split(sep.get().value)
    array = [tupy.Interpreter.memAlloc(tupy.Instance.Instance(Type.STRING, s)) for s in splitted]
    return tupy.Instance.Instance(Type.ARRAY, array)

def aleatorio(x=None, y=None):
    return aleatório(x,y)

def aleatório(x=None, y=None):
    if (x is None):
        return tupy.Instance.Instance(Type.FLOAT, random.random())
    elif (y is None):
        return tupy.Instance.Instance(Type.FLOAT, random.uniform(0, x.get().value))
    else:
        return tupy.Instance.Instance(Type.FLOAT, random.uniform(x.get().value, y.get().value))

def inteiro_aleatorio(x, y=None):
    return inteiro_aleatório(x,y)

def inteiro_aleatório(x, y=None):
    if (y is None):
        a = 0; b = x.get().value
    else:
        a = y.get().value; b = x.get().value

    return tupy.Instance.Instance(Type.INT, random.randint(builtins.min(a,b), builtins.max(a,b)))

def embaralhar(argsTuple):
    argsTuple = argsTuple.get().value
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
    argsTuple = argsTuple.get().value
    if (len(argsTuple) < 2):
        raise TypeError("Faltam argumentos para a função inserir(lista, elemento, [pos])!")
    elif (len(argsTuple) > 3):
        raise TypeError("A função inserir(lista, elemento, [pos]) recebeu argumentos demais!")
    else:
        inst = tupy.Interpreter.memRead(argsTuple[0])
        if (inst.is_pure_array()):
            val = inst.value
            elem_inst = tupy.Interpreter.memRead(argsTuple[1])

            if (elem_inst.type != inst.roottype and inst.roottype != Type.ARRAY): # Root type == Array when is empty
                raise TypeError("A função inserir espera receber como segundo argumento um elemento de mesmo tipo que os contidos na lista!")

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

            return new_inst
        else:
            raise TypeError("A função inserir espera receber uma lista como primeiro argumento!")

def remover(argsTuple):
    argsTuple = argsTuple.get().value
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

            return new_inst
        else:
            raise TypeError("A função remover espera receber uma lista como primeiro argumento!")

def min(x, y):
    return tupy.Instance.Instance(x.get().type, builtins.min(x.get().value, y.get().value))

def max(x, y):
    return tupy.Instance.Instance(x.get().type, builtins.max(x.get().value, y.get().value))

def mín(x, y):
    return min(x, y)

def máx(x, y):
    return max(x, y)

_graph_opts = "overlap=false; node [fontsize=16 width=0.2 margin=0.05 shape=circle]; edge [arrowsize=0.8]; "
_graph_highlight = "[style = filled fillcolor = yellow]; "

def grafo_MA(matrix, highlights):
    header = "[[DOT strict graph {"
    trailer = "}]]"
    matrix = matrix.get().value
    highlights = highlights.get().value

    n_lines = len(matrix)
    if all(len(cell_value(line)) == n_lines for line in matrix):
        if all(cell_value(elem) < n_lines for elem in highlights):
            # Parse connections
            parsed_connections = ["{0} -- {1}; ".format(i, j) for i in range(n_lines) \
                                                             for j in range(i, n_lines) \
                                                             if matrix_access(matrix, i, j) \
                                                             and matrix_access(matrix, j, i)]
            parsed_connections = "".join(parsed_connections)

            ret = "".join([header, _graph_opts, graph_nodes_and_highlights(n_lines, highlights), 
                            parsed_connections, trailer])
            return tupy.Instance.Instance(Type.STRING, ret)
        else:
            raise ValueError("A lista de nós destacados contém nós que não existem!")
    else:
        raise ValueError("A matriz de adjacências deve ser quadrada!")

def digrafo_MA(matrix, highlights):
    header = "[[DOT digraph {"
    trailer = "}]]"
    matrix = matrix.get().value
    highlights = highlights.get().value

    n_lines = len(matrix)
    if all(len(cell_value(line)) == n_lines for line in matrix):
        if all(cell_value(elem) < n_lines for elem in highlights):            
            # Parse connections
            parsed_connections = ["{0} -> {1}; ".format(i, j) for i in range(n_lines) \
                                                             for j in range(n_lines) \
                                                             if matrix_access(matrix, i, j)]
            parsed_connections = "".join(parsed_connections)

            ret = "".join([header, _graph_opts, graph_nodes_and_highlights(n_lines, highlights), 
                            parsed_connections, trailer])
            return tupy.Instance.Instance(Type.STRING, ret)
        else:
            raise ValueError("A lista de nós destacados contém nós que não existem!")
    else:
        raise ValueError("A matriz de adjacências deve ser quadrada!")

def grafo_LA(adjList, highlights):
    header = "[[DOT strict graph {"
    trailer = "}]]"
    adjList = adjList.get().value
    highlights = highlights.get().value

    n_nodes = len(adjList)
    if all(cell_value(elem) < n_nodes for elem in highlights):
            try:           
                existing_connections = set()    
                # Parse connections
                parsed_connections = [ make_graph_LA_edge(i, valJ, existing_connections) \
                                                            for i, elem in enumerate(adjList) \
                                                            for elemJ in cell_value(elem) \
                                                            for valJ in [cell_value(elemJ)] \
                                                            if (i, valJ) not in existing_connections \
                                                            and i in [cell_value(cell) \
                                                                      for cell in cell_value(adjList[valJ])] 
                                                            ]
                parsed_connections = "".join(parsed_connections)

                ret = "".join([header, _graph_opts, graph_nodes_and_highlights(n_nodes, highlights), 
                                parsed_connections, trailer])
                return tupy.Instance.Instance(Type.STRING, ret)
            except IndexError as ex:
                raise IndexError("A lista contém uma ou mais adjacências com nós que não existem!")
    else:
        raise ValueError("A lista de nós destacados contém nós que não existem!")

def digrafo_LA(adjList, highlights):
    header = "[[DOT digraph {"
    trailer = "}]]"
    adjList = adjList.get().value
    highlights = highlights.get().value

    n_nodes = len(adjList)
    if all(cell_value(elem) < n_nodes for elem in highlights):
            try:               
                # Parse connections
                parsed_connections = ["{0} -> {1}; ".format(i, valJ) \
                                                            for i, elem in enumerate(adjList) \
                                                            for elemJ in cell_value(elem) \
                                                            for valJ in [cell_value(elemJ)] \
                                                            if digraph_adj_in_bounds(valJ, n_nodes)
                                                            ]
                parsed_connections = "".join(parsed_connections)

                ret = "".join([header, _graph_opts, graph_nodes_and_highlights(n_nodes, highlights), 
                                parsed_connections, trailer])
                return tupy.Instance.Instance(Type.STRING, ret)
            except IndexError as ex:
                raise IndexError("A lista contém uma ou mais adjacências com nós que não existem!")
    else:
        raise ValueError("A lista de nós destacados contém nós que não existem!")
