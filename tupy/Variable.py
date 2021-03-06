from tupy.Type import TrailerType, Type
import tupy.Interpreter #as ii
import copy
import tupy.Instance
import tupy.Context
import tupy.Builtins

class Variable(object):
    @classmethod
    def retrieveWithTrailers(cls, inst, trailers):
        ret = inst
        classContextsPushed = 0
        # Parent is useful when we want to assign ranges
        # e.g.: A[5, 1..2] <- [10, 20]
        # We retrieveWithTrailers(A) but we want to change A[5] specifically
        # so we don't go down all the way to A[5, 1..2]
        parent = (inst, None, 0)
        for (ttype, tid) in trailers:
            if ttype == TrailerType.SUBSCRIPT:
                # Parse subscript list
                depth = 0
                for level in range(len(tid)):
                    ss = tid[level]
                    parent = (ret, ss, depth)
                    if ss.isWildcard:
                        depth += 1
                        pass
                    elif ss.isSingle:
                        (newvalue, newtype) = cls.get_array_range(ret, ss.begin, ss.begin, depth, True)
                        orig_root_type = ret.roottype
                        orig_class_name = ret.class_name
                        orig_array_dimensions = ret.array_dimensions
                        ret = tupy.Instance.Instance(newtype, newvalue)
                        if (orig_root_type != Type.STRING): #Let STRING become CHAR
                            ret.roottype = orig_root_type
                            ret.array_dimensions = orig_array_dimensions - 1
                        ret.class_name = orig_class_name
                    else:
                        (newvalue, newtype) = cls.get_array_range(ret, ss.begin, ss.end, depth)
                        orig_root_type = ret.roottype
                        orig_class_name = ret.class_name
                        orig_array_dimensions = ret.array_dimensions
                        ret = tupy.Instance.Instance(newtype, newvalue)
                        ret.roottype = orig_root_type
                        ret.array_dimensions = orig_array_dimensions
                        ret.class_name = orig_class_name
                        depth += 1
            elif ttype == TrailerType.CALL:
                # try:
                # tupy.Interpreter.logger.debug("tid {0}".format(tid))
                parent = (ret, None, -1)
                ret = tupy.Interpreter.Interpreter.executeBlock(ret.value, tid, classContextsPushed)
                # except Exception:
                    # raise TypeError("{0} is not callable!".format(ret.type))
            elif ttype == TrailerType.MEMBER:
                if ret.type == Type.NULL:
                    raise RuntimeError("Tentativa de acessar o campo {0} de instância não inicializada!".format(tid))
                tupy.Interpreter.Interpreter.pushContext(ret.value, ret)
                parent = (ret, tid, -2)
                if ret.value.locals.hasKey(tid):
                    ret = tupy.Interpreter.memRead(ret.value.locals.get(tid))
                else:
                    raise NameError("O tipo {0} não possui o atributo {1}!".format(ret.value.structName, tid))
                classContextsPushed = classContextsPushed+1

        for i in range(classContextsPushed):
            tupy.Interpreter.Interpreter.popFrame()

        return (ret, parent)

    @classmethod
    def get_array_range(cls, inst, begin, end, level, single=False):
        if __debug__:
            tupy.Interpreter.logger.debug("get_array_range({0}, {1}, {2}, {3})".format(inst, begin, end, level))
        if level == 0:
            if not inst.is_subscriptable_array():
                raise TypeError("{0} não contém elementos para acesso posicional!".format(inst.type))

            if (single):
                if inst.type == Type.STRING:
                    if __debug__:
                        tupy.Interpreter.logger.debug("...returned {0}".format(inst.value[begin]))
                    return (ord(inst.value[begin]), Type.CHAR)
                else:
                    if __debug__:
                        tupy.Interpreter.logger.debug("...returned {0}".format(tupy.Interpreter.memRead(inst.value[begin]).value))
                    return (tupy.Interpreter.memRead(inst.value[begin]).value, tupy.Interpreter.memRead(inst.value[begin]).type)
            else:
                if __debug__:
                    tupy.Interpreter.logger.debug("...returned {0}".format(inst.value[begin:end]))
                return (inst.value[begin:end], inst.type)
        else:
            ret = []
            if __debug__:
                tupy.Interpreter.logger.debug("Welp, first gotta check {0}".format(inst.value))
            for memoryCell in inst.value:
                lower_inst = tupy.Interpreter.memRead(memoryCell)
                lower_level = cls.get_array_range(lower_inst, begin, end, level-1, single)[0] #Not interested in type
                if (single and level==1):
                    new_inst = tupy.Instance.Instance(lower_inst.heldtype, lower_level)
                else:
                    new_inst = tupy.Instance.Instance(lower_inst.type, lower_level)
                ret.append(tupy.Interpreter.memAlloc(new_inst))

            if __debug__:
                tupy.Interpreter.logger.debug("...returned {0}".format(ret))
            return (ret, inst.heldtype)

    @classmethod
    def makeDefaultValue(cls, datatype, declSubscripts=None, heldType=None, className=None):
        if declSubscripts is None:
            declSubscripts = []
        if datatype == Type.ARRAY:
            return cls.array_init(declSubscripts, heldType, className)
        elif datatype == Type.STRING:
            return tupy.Instance.Instance(datatype, "")
        elif datatype == Type.TUPLE:
            return tupy.Instance.Instance(datatype, ())
        elif datatype == Type.STRUCT:
            return tupy.Instance.Instance(Type.NULL, 0, className=className)
        else:
            return tupy.Instance.Instance(datatype, 0)

    @classmethod
    def array_init(cls, declSubscripts, heldType, className=None):
        if len(declSubscripts)==0:
            # At lowest level, initialize an element
            ret = cls.makeDefaultValue(heldType, className=className)
            return ret
        else:
            subs = declSubscripts[0]
            sz = subs.begin
            content = [tupy.Interpreter.memAlloc(cls.array_init(declSubscripts[1:], heldType, className)) for _ in range(sz)]
            ret = tupy.Instance.Instance(Type.ARRAY, content, className=className)
            return ret

    def power(self, rhs:'Variable'):
        li, ri = self.get(), rhs.get()
        self.validateNumbers([li.type, ri.type])
        typ = self.resultType(li.type, ri.type)
        return Literal(tupy.Instance.Instance(typ, li.value ** ri.value))

    def positive(self):
        li = self.get()
        self.validateNumbers([li.type])
        return Literal(tupy.Instance.Instance(li.type, +li.value))

    def negative(self):
        li = self.get()
        self.validateNumbers([li.type])
        return Literal(tupy.Instance.Instance(li.type, -li.value))

    def bitwise_flip(self):
        li = self.get()
        if (li.type != Type.INT):
            raise TypeError("Não é possível fazer negação de bits com tipo não-inteiro!")
        return Literal(tupy.Instance.Instance(Type.INT, ~li.value))

    def multiply(self, rhs:'Variable'):
        li, ri = self.get(), rhs.get()
        typ = self.resultType(li.type, ri.type)
        if (li.type == ri.type and li.type in [Type.STRING, Type.ARRAY]):
            raise TypeError("Não é possível multiplicar duas variáveis do tipo {0}!".format(li.type))
        return Literal(tupy.Instance.Instance(typ, li.value * ri.value))

    def divide(self, rhs:'Variable'):
        li, ri = self.get(), rhs.get()
        self.validateNumbers([li.type, ri.type])
        typ = self.resultType(li.type, ri.type)
        return Literal(tupy.Instance.Instance(typ, li.value / ri.value))

    def modulo(self, rhs:'Variable'):
        li, ri = self.get(), rhs.get()
        typ = self.resultType(li.type, ri.type)
        if (li.type == ri.type and li.type in [Type.STRING, Type.ARRAY]):
            raise TypeError("Não é possível multiplicar duas variáveis do tipo {0}!".format(li.type))
        return Literal(tupy.Instance.Instance(typ, li.value % ri.value))

    def integer_divide(self, rhs:'Variable'):
        li, ri = self.get(), rhs.get()
        self.validateNumbers([li.type, ri.type])
        typ = self.resultType(li.type, ri.type)
        return Literal(tupy.Instance.Instance(typ, li.value // ri.value))

    def add(self, rhs:'Variable'):
        li, ri = self.get(), rhs.get()
        typ = self.resultType(li.type, ri.type)
        if typ == Type.STRING:
            return Literal(tupy.Instance.Instance(typ, self.stringConcat(li, ri)))
        else:
            return Literal(tupy.Instance.Instance(typ, li.value + ri.value))

    def subtract(self, rhs:'Variable'):
        li, ri = self.get(), rhs.get()
        self.validateNumbers([li.type, ri.type])
        typ = self.resultType(li.type, ri.type)
        return Literal(tupy.Instance.Instance(typ, li.value - ri.value))

    def left_shift(self, rhs:'Variable'):
        li, ri = self.get(), rhs.get()
        if (li.type != Type.INT or ri.type != Type.INT):
            raise TypeError("Não é possível fazer deslocamento de bits para a esquerda com tipo não-inteiro!")
        return Literal(tupy.Instance.Instance(Type.INT, li.value << ri.value))

    def right_shift(self, rhs:'Variable'):
        li, ri = self.get(), rhs.get()
        if (li.type != Type.INT or ri.type != Type.INT):
            raise TypeError("Não é possível fazer deslocamento de bits para a direita com tipo não-inteiro!")
        return Literal(tupy.Instance.Instance(Type.INT, li.value >> ri.value))

    def bitwise_and(self, rhs:'Variable'):
        li, ri = self.get(), rhs.get()
        if (li.type != Type.INT or ri.type != Type.INT):
            raise TypeError("Não é possível fazer E (AND) de bits com tipo não-inteiro!")
        return Literal(tupy.Instance.Instance(Type.INT, li.value & ri.value))

    def bitwise_or(self, rhs:'Variable'):
        li, ri = self.get(), rhs.get()
        if (li.type != Type.INT or ri.type != Type.INT):
            raise TypeError("Não é possível fazer OU (OR) de bits com tipo não-inteiro!")
        typ = Type.INT
        return Literal(tupy.Instance.Instance(Type.INT, li.value | ri.value))

    def bitwise_xor(self, rhs:'Variable'):
        li, ri = self.get(), rhs.get()
        if (li.type != Type.INT or ri.type != Type.INT):
            raise TypeError("Não é possível fazer OU EXCLUSIVO (XOR) de bits com tipo não-inteiro!")
        return Literal(tupy.Instance.Instance(Type.INT, li.value ^ ri.value))

    def gt(self, rhs:'Variable'):
        li, ri = self.get(), rhs.get()
        if (li == Type.STRUCT or ri == Type.STRUCT):
            raise TypeError("Comparação não permitida para tipos compostos!")
        return Literal(tupy.Instance.Instance(Type.BOOL,
                                              self.validateComparisonTypes(li.type,
                                                                           ri.type) and
                                              li.to_python_repr() > ri.to_python_repr()))

    def lt(self, rhs:'Variable'):
        li, ri = self.get(), rhs.get()
        if (li == Type.STRUCT or ri == Type.STRUCT):
            raise TypeError("Comparação não permitida para tipos compostos!")
        return Literal(tupy.Instance.Instance(Type.BOOL,
                                              self.validateComparisonTypes(li.type,
                                                                           ri.type) and
                                              li.to_python_repr() < ri.to_python_repr()))

    def gt_eq(self, rhs:'Variable'):
        li, ri = self.get(), rhs.get()
        if (li == Type.STRUCT or ri == Type.STRUCT):
            raise TypeError("Comparação não permitida para tipos compostos!")
        return Literal(tupy.Instance.Instance(Type.BOOL,
                                              self.validateComparisonTypes(li.type,
                                                                           ri.type) and
                                              li.to_python_repr() >= ri.to_python_repr()))

    def lt_eq(self, rhs:'Variable'):
        li, ri = self.get(), rhs.get()
        if (li == Type.STRUCT or ri == Type.STRUCT):
            raise TypeError("Comparação não permitida para tipos compostos!")
        return Literal(tupy.Instance.Instance(Type.BOOL,
                                              self.validateComparisonTypes(li.type,
                                                                           ri.type) and
                                              li.to_python_repr() <= ri.to_python_repr()))

    def eq(self, rhs:'Variable'):
        li, ri = self.get(), rhs.get()
        return Literal(tupy.Instance.Instance(Type.BOOL,
                                              self.validateComparisonTypes(li.type,
                                                                           ri.type) and
                                              li.to_python_repr() == ri.to_python_repr()))

    def neq(self, rhs:'Variable'):
        li, ri = self.get(), rhs.get()
        return Literal(tupy.Instance.Instance(Type.BOOL,
                                              not self.validateComparisonTypes(li.type,
                                                                           ri.type) or
                                              li.to_python_repr() != ri.to_python_repr()))

    def logic_not(self):
        li = self.get()
        return Literal(tupy.Instance.Instance(Type.BOOL, not li.value))

    def logic_and(self, rhs:'Variable'):
        ri = rhs.get()
        return Literal(tupy.Instance.Instance(Type.BOOL, ri.value))

    def logic_or(self, rhs:'Variable'):
        ri = rhs.get()
        return Literal(tupy.Instance.Instance(Type.BOOL, ri.value))

    def cardinality(self):
        li = self.get()
        return Literal(tupy.Instance.Instance(Type.INT, self.get().size))

    def validateNumbers(self, typelist):
        numbers = [Type.INT, Type.FLOAT, Type.CHAR]
        if not all(t in numbers for t in typelist):
            raise TypeError("Essa operação é restrita para números!")

    def validateComparisonTypes(self, a, b):
        if (a == Type.FUNCTION or b == Type.FUNCTION):
            raise TypeError("Comparação proibida para funções!")
        elif (a == Type.REFERENCE or b == Type.REFERENCE):
            raise TypeError("Comparação proibida para referências!")
        elif (a == b):
            # Comparison is always ok for the same type
            return True
        elif (a == Type.NULL or b == Type.NULL):
            return False
        elif (a == Type.ARRAY or b == Type.ARRAY):
            raise TypeError("Uma lista somente pode ser comparada com outras listas!")
        elif (a == Type.TUPLE or b == Type.TUPLE):
            raise TypeError("Uma tupla somente pode ser comparada com outras tuplas!")
        elif (a == Type.FLOAT or b == Type.FLOAT):
            raise TypeError("Um número real somente pode ser comparado com outros números reais!")
        elif (a == Type.STRING or b == Type.STRING):
            raise TypeError("Uma cadeia somente pode ser comparada com outras cadeias!")

    def resultType(self, a, b):
        if (a == Type.REFERENCE or b == Type.REFERENCE):
            raise TypeError("Operação proibida para referências!")
        if (a == Type.STRUCT or b == Type.STRUCT):
            raise TypeError("Operação proibida para tipos compostos!")
        elif (a == Type.FUNCTION or b == Type.FUNCTION):
            raise TypeError("Operação proibida para funções!")
        elif (a == Type.NULL or b == Type.NULL):
            raise TypeError("Operação proibida para o tipo nulo!")
        elif (a == Type.NULL or b == Type.TUPLE):
            raise TypeError("Operação proibida para tuplas!")
        elif (a == Type.ARRAY or b == Type.ARRAY):
            if (a == Type.ARRAY and b == Type.ARRAY):
                return Type.ARRAY
            else:
                raise TypeError("Uma lista somente pode fazer operações com outras listas!")
        else:
            if (a == Type.STRING or b == Type.STRING):
                return Type.STRING
            elif (a == Type.FLOAT or b == Type.FLOAT):
                return Type.FLOAT
            elif (a == Type.INT or b == Type.INT):
                return Type.INT
            elif (a == Type.CHAR or b == Type.CHAR):
                return Type.INT
            elif (a == Type.BOOL or b == Type.BOOL):
                return Type.INT

    def stringConcat(self, lhs, rhs):
        return tupy.Builtins.cast(lhs, Type.STRING).value + tupy.Builtins.cast(rhs, Type.STRING).value


class Literal(Variable):
    __slots__ = [
        'inst', 'trailers'
    ]

    def __init__(self, instance):
        self.trailers = []
        self.inst = instance

    #def __str__(self):
    #    return "LITERAL<{0}>".format(str(self.inst))

    def __repr__(self):
        return "L{0}".format(str(self.inst))

    def get(self):
        # retrieveWithTrailers returns a tuple of (instance, parent)
        return Variable.retrieveWithTrailers(self.inst, self.trailers)[0]

class Symbol(Variable):
    __slots__ = [
        'name', 'trailers'
    ]

    def __init__(self, name):
        self.trailers = []
        self.name = name

    def __str__(self): # pragma: no cover
        return "SYMBOL<{0}>".format(str(self.name))

    def get(self):
        return Variable.retrieveWithTrailers(tupy.Interpreter.Interpreter.loadSymbol(self.name), self.trailers)[0]
