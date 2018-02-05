from tupy.Type import TrailerType, Type
import tupy.Interpreter #as ii
import copy
import tupy.Instance
import tupy.Context

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
                ret = tupy.Interpreter.Interpreter.executeBlock(ret.value, tid)
                # except Exception:
                    # raise TypeError("{0} is not callable!".format(ret.type))
            elif ttype == TrailerType.MEMBER:
                tupy.Interpreter.Interpreter.callStack.push(ret.value)
                parent = (ret, tid, -2)
                if ret.type == Type.NULL:
                    raise RuntimeError("Tentativa de acessar o campo {0} de instância não inicializada!".format(tid))
                ret = ret.value.locals.get(tid)
                classContextsPushed = classContextsPushed+1

        for i in range(classContextsPushed):
            tupy.Interpreter.Interpreter.popFrame()

        return (ret, parent)

    @classmethod
    def get_array_range(cls, inst, begin, end, level, single=False):
        tupy.Interpreter.logger.debug("get_array_range({0}, {1}, {2}, {3})".format(inst, begin, end, level))
        if level == 0:
            if not inst.is_subscriptable_array():
                raise TypeError("{0} não contém elementos para acesso posicional!".format(inst.type))
            
            if (single):
                if inst.type == Type.STRING:
                    tupy.Interpreter.logger.debug("...returned {0}".format(inst.value[begin]))
                    return (ord(inst.value[begin]), Type.CHAR)
                else:
                    tupy.Interpreter.logger.debug("...returned {0}".format(tupy.Interpreter.memRead(inst.value[begin]).value))
                    return (tupy.Interpreter.memRead(inst.value[begin]).value, tupy.Interpreter.memRead(inst.value[begin]).type)
            else:
                tupy.Interpreter.logger.debug("...returned {0}".format(inst.value[begin:end]))
                return (inst.value[begin:end], inst.type)
        else:
            ret = []
            tupy.Interpreter.logger.debug("Welp, first gotta check {0}".format(inst.value))
            for memoryCell in inst.value:
                lower_inst = tupy.Interpreter.memRead(memoryCell)
                lower_level = cls.get_array_range(lower_inst, begin, end, level-1, single)[0] #Not interested in type
                if (single and level==1):
                    new_inst = tupy.Instance.Instance(lower_inst.heldtype, lower_level)
                else:
                    new_inst = tupy.Instance.Instance(lower_inst.type, lower_level)
                ret.append(tupy.Interpreter.memAlloc(new_inst))
                
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
            return tupy.Instance.Instance(Type.NULL, 0, className=className) #tupy.Interpreter.Interpreter.newClassInstance(className)
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
        typ = self.resultType(self.get().type, rhs.get().type)
        return Literal(tupy.Instance.Instance(typ, self.get().value ** rhs.get().value))

    def positive(self):
        return Literal(tupy.Instance.Instance(self.get().type, +self.get().value))

    def negative(self):
        return Literal(tupy.Instance.Instance(self.get().type, -self.get().value))

    def bitwise_flip(self):
        if (self.get().type != Type.INT):
            raise TypeError("Não é possível fazer negação de bits com tipo não-inteiro!")
        return Literal(tupy.Instance.Instance(Type.INT, ~self.get().value))

    def multiply(self, rhs:'Variable'):
        typ = self.resultType(self.get().type, rhs.get().type)
        return Literal(tupy.Instance.Instance(typ, self.get().value * rhs.get().value))

    def divide(self, rhs:'Variable'):
        typ = self.resultType(self.get().type, rhs.get().type)
        return Literal(tupy.Instance.Instance(typ, self.get().value / rhs.get().value))

    def modulo(self, rhs:'Variable'):
        typ = self.resultType(self.get().type, rhs.get().type)
        return Literal(tupy.Instance.Instance(typ, self.get().value % rhs.get().value))

    def integer_divide(self, rhs:'Variable'):
        typ = self.resultType(self.get().type, rhs.get().type)
        return Literal(tupy.Instance.Instance(typ, self.get().value // rhs.get().value))

    def add(self, rhs:'Variable'):
        typ = self.resultType(self.get().type, rhs.get().type)
        if typ == Type.STRING:
            return Literal(tupy.Instance.Instance(typ, self.stringConcat(self.get(), rhs.get())))
        else:
            return Literal(tupy.Instance.Instance(typ, self.get().value + rhs.get().value))

    def subtract(self, rhs:'Variable'):
        typ = self.resultType(self.get().type, rhs.get().type)
        return Literal(tupy.Instance.Instance(typ, self.get().value - rhs.get().value))

    def left_shift(self, rhs:'Variable'):
        if (self.get().type != Type.INT or rhs.get().type != Type.INT):
            raise TypeError("Não é possível fazer deslocamento de bits para a esquerda com tipo não-inteiro!")
        typ = Type.INT
        return Literal(tupy.Instance.Instance(typ, self.get().value << rhs.get().value))

    def right_shift(self, rhs:'Variable'):
        if (self.get().type != Type.INT or rhs.get().type != Type.INT):
            raise TypeError("Não é possível fazer deslocamento de bits para a direita com tipo não-inteiro!")
        typ = Type.INT
        return Literal(tupy.Instance.Instance(typ, self.get().value >> rhs.get().value))

    def bitwise_and(self, rhs:'Variable'):
        if (self.get().type != Type.INT or rhs.get().type != Type.INT):
            raise TypeError("Não é possível fazer E (AND) de bits com tipo não-inteiro!")
        typ = Type.INT
        return Literal(tupy.Instance.Instance(typ, self.get().value & rhs.get().value))

    def bitwise_or(self, rhs:'Variable'):
        if (self.get().type != Type.INT or rhs.get().type != Type.INT):
            raise TypeError("Não é possível fazer OU (OR) de bits com tipo não-inteiro!")
        typ = Type.INT
        return Literal(tupy.Instance.Instance(typ, self.get().value | rhs.get().value))

    def bitwise_xor(self, rhs:'Variable'):
        if (self.get().type != Type.INT or rhs.get().type != Type.INT):
            raise TypeError("Não é possível fazer OU EXCLUSIVO (XOR) de bits com tipo não-inteiro!")
        typ = Type.INT
        return Literal(tupy.Instance.Instance(typ, self.get().value ^ rhs.get().value))

    def gt(self, rhs:'Variable'):
        return Literal(tupy.Instance.Instance(Type.BOOL, 
                                              self.validateComparisonTypes(self.get().type,
                                                                           rhs.get().type) and
                                              self.get().value > rhs.get().value))

    def lt(self, rhs:'Variable'):
        return Literal(tupy.Instance.Instance(Type.BOOL, 
                                              self.validateComparisonTypes(self.get().type,
                                                                           rhs.get().type) and
                                              self.get().value < rhs.get().value))

    def gt_eq(self, rhs:'Variable'):
        return Literal(tupy.Instance.Instance(Type.BOOL, 
                                              self.validateComparisonTypes(self.get().type,
                                                                           rhs.get().type) and
                                              self.get().value >= rhs.get().value))

    def lt_eq(self, rhs:'Variable'):
        return Literal(tupy.Instance.Instance(Type.BOOL,
                                              self.validateComparisonTypes(self.get().type,
                                                                           rhs.get().type) and
                                              self.get().value <= rhs.get().value))

    def eq(self, rhs:'Variable'):
        return Literal(tupy.Instance.Instance(Type.BOOL, 
                                              self.validateComparisonTypes(self.get().type,
                                                                           rhs.get().type) and
                                              self.get().value == rhs.get().value))

    def neq(self, rhs:'Variable'):
        return Literal(tupy.Instance.Instance(Type.BOOL, 
                                              not self.validateComparisonTypes(self.get().type,
                                                                           rhs.get().type) or
                                              self.get().value != rhs.get().value))

    def logic_not(self):
        return Literal(tupy.Instance.Instance(Type.BOOL, not self.get().value))

    def logic_and(self, rhs:'Variable'):
        return Literal(tupy.Instance.Instance(Type.BOOL, rhs.get().value))

    def logic_or(self, rhs:'Variable'):
        return Literal(tupy.Instance.Instance(Type.BOOL, rhs.get().value))

    def cardinality(self):
        return Literal(tupy.Instance.Instance(Type.INT, self.get().size))

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
            raise TypeError("Uma tupla somente pode ser comparada com outras listas!")
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
        # elif (a == Type.RANGE or b == Type.RANGE):
            # raise TypeError("Cannot operate on instance of type RANGE!")
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
        if (lhs.type == Type.CHAR): a = chr(lhs.value)
        else: a = str(lhs.value)

        if (rhs.type == Type.CHAR): b = chr(rhs.value)
        else: b = str(rhs.value)

        return a + b


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
