from Instance import Instance
from Type import TrailerType, Type
import Interpreter as ii
import copy

class Variable(object):
    def __init__(self):
        self.trailers = []

    def call(self, params):
        pass

    def subscript(self, subscript):
        pass

    def get(self):
        pass

    @classmethod
    def retrieveWithTrailers(cls, inst, trailers):
        ret = inst
        # Parent is useful when we want to assign ranges
        # e.g.: A[5, 1..2] <- [10, 20]
        # We retrieveWithTrailers(A) but we want to change A[5] specifically
        # so we don't go down all the way to A[5, 1..2]
        parent = (inst, None) 
        for (ttype, tid) in trailers:
            if ttype == TrailerType.SUBSCRIPT:
                # Parse subscript list
                level = 0
                for ss in tid:
                    parent = (ret, ss)
                    if ss.isWildcard:
                        pass
                    elif ss.isSingle:
                        ret = Instance(inst.heldtype, cls.get_array_range(ret, ss.begin, ss.begin, level, True)) #ret = ret.array_get(ss.begin).get()
                    else:
                        ret = Instance(inst.type, cls.get_array_range(ret, ss.begin, ss.end, level))
                    level += 1
            else:
                pass
        return (ret, parent)

    @classmethod
    def get_array_range(cls, inst, begin, end, level, single=False):
        print("get_array_range({0}, {1}, {2}, {3})".format(inst, begin, end, level))
        if level == 0:
            try:
                if not inst.is_subscriptable_array():
                    raise TypeError("{0} cannot be subscripted.".format(inst.type))
                print("...returned {0}".format(inst.value[begin:end]))
                if (single):
                    return inst.value[begin].get().value
                else:
                    return inst.value[begin:end]
            except TypeError:
                raise
        else:
            ret = []
            print("Welp, first gotta check {0}".format(inst.value))
            for literal in inst.value:
                lower_inst = literal.get()
                lower_level = cls.get_array_range(lower_inst, begin, end, level-1, single)
                if (single and level==1):
                    new_inst = Instance(lower_inst.heldtype, lower_level)
                else:
                    new_inst = Instance(lower_inst.type, lower_level)
                ret.append(Literal(new_inst))
                
            print("...returned {0}".format(ret))
            return ret

    @classmethod
    def makeDefaultValue(cls, datatype, declSubscripts=[], heldType=None):
        if datatype == Type.ARRAY:
            return cls.array_init(declSubscripts, heldType)
        elif datatype == Type.STRING:
            return Instance(datatype, "")
        else:
            return Instance(datatype, 0)

    @classmethod
    def array_init(cls, declSubscripts, heldType):
        if len(declSubscripts)==0:
            # At lowest level, initialize an element
            ret = cls.makeDefaultValue(heldType)
            return ret
        else:
            subs = declSubscripts[0]
            sz = subs.begin
            element = Literal(cls.array_init(declSubscripts[1:], heldType))
            content = [(copy.deepcopy(element)) for i in range(sz)]
            ret = Instance(Type.ARRAY, content)
            return ret

    def power(self, rhs:'Variable'):
        typ = self.resultType(self.get().type, rhs.get().type)
        return Literal(Instance(typ, self.get().value ** rhs.get().value))

    def positive(self):
        return Literal(Instance(self.get().type, +self.get().value))

    def negative(self):
        return Literal(Instance(self.get().type, -self.get().value))

    def bitwise_flip(self):
        if (self.get().type != Type.INT):
            raise TypeError("Cannot do bit-wise NOT with non-integer type!")
        return Literal(Instance(Type.INT, ~self.get().value))

    def multiply(self, rhs:'Variable'):
        typ = self.resultType(self.get().type, rhs.get().type)
        return Literal(Instance(typ, self.get().value * rhs.get().value))

    def divide(self, rhs:'Variable'):
        typ = self.resultType(self.get().type, rhs.get().type)
        return Literal(Instance(typ, self.get().value / rhs.get().value))

    def modulo(self, rhs:'Variable'):
        typ = self.resultType(self.get().type, rhs.get().type)
        return Literal(Instance(typ, self.get().value % rhs.get().value))

    def integer_divide(self, rhs:'Variable'):
        typ = self.resultType(self.get().type, rhs.get().type)
        return Literal(Instance(typ, self.get().value // rhs.get().value))

    def add(self, rhs:'Variable'):
        typ = self.resultType(self.get().type, rhs.get().type)
        if typ == Type.STRING:
            return Literal(Instance(typ, self.stringConcat(self.get(), rhs.get())))
        else:
            return Literal(Instance(typ, self.get().value + rhs.get().value))

    def subtract(self, rhs:'Variable'):
        typ = self.resultType(self.get().type, rhs.get().type)
        return Literal(Instance(typ, self.get().value - rhs.get().value))

    def left_shift(self, rhs:'Variable'):
        if (self.get().type != Type.INT or rhs.get().type != Type.INT):
            raise TypeError("Cannot do bit-wise shift with non-integer types!")
        typ = Type.INT
        return Literal(Instance(typ, self.get().value << rhs.get().value))

    def right_shift(self, rhs:'Variable'):
        if (self.get().type != Type.INT or rhs.get().type != Type.INT):
            raise TypeError("Cannot do bit-wise shift with non-integer types!")
        typ = Type.INT
        return Literal(Instance(typ, self.get().value >> rhs.get().value))

    def bitwise_and(self, rhs:'Variable'):
        if (self.get().type != Type.INT or rhs.get().type != Type.INT):
            raise TypeError("Cannot do bit-wise AND with non-integer types!")
        typ = Type.INT
        return Literal(Instance(typ, self.get().value & rhs.get().value))

    def bitwise_or(self, rhs:'Variable'):
        if (self.get().type != Type.INT or rhs.get().type != Type.INT):
            raise TypeError("Cannot do bit-wise OR with non-integer types!")
        typ = Type.INT
        return Literal(Instance(typ, self.get().value | rhs.get().value))

    def bitwise_xor(self, rhs:'Variable'):
        if (self.get().type != Type.INT or rhs.get().type != Type.INT):
            raise TypeError("Cannot do bit-wise XOR with non-integer types!")
        typ = Type.INT
        return Literal(Instance(typ, self.get().value ^ rhs.get().value))

    def gt(self, rhs:'Variable'):
        return Literal(Instance(Type.BOOL, self.get().value > rhs.get().value))

    def lt(self, rhs:'Variable'):
        return Literal(Instance(Type.BOOL, self.get().value < rhs.get().value))

    def gt_eq(self, rhs:'Variable'):
        return Literal(Instance(Type.BOOL, self.get().value >= rhs.get().value))

    def lt_eq(self, rhs:'Variable'):
        return Literal(Instance(Type.BOOL, self.get().value <= rhs.get().value))

    def eq(self, rhs:'Variable'):
        return Literal(Instance(Type.BOOL, self.get().value == rhs.get().value))

    def neq(self, rhs:'Variable'):
        return Literal(Instance(Type.BOOL, self.get().value != rhs.get().value))

    def logic_not(self):
        return Literal(Instance(Type.BOOL, not self.get().value))

    def logic_and(self, rhs:'Variable'):
        return Literal(Instance(Type.BOOL, self.get().value and rhs.get().value))

    def logic_or(self, rhs:'Variable'):
        return Literal(Instance(Type.BOOL, self.get().value or rhs.get().value))

    def cardinality(self):
        return Literal(Instance(Type.INT, self.get().size))

    def resultType(self, a, b):
        if (a == Type.REFERENCE or b == Type.REFERENCE):
            raise TypeError("Cannot operate on instance of type REFERENCE!")
        elif (a == Type.NULL or b == Type.NULL):
            raise TypeError("Cannot operate on instance of type NULL!")
        elif (a == Type.RANGE or b == Type.RANGE):
            raise TypeError("Cannot operate on instance of type RANGE!")
        else:
            if (a == Type.STRING or b == Type.STRING):
                return Type.STRING
            elif (a == Type.FLOAT or b == Type.FLOAT):
                return Type.FLOAT
            elif (a == Type.INT or b == Type.INT):
                return Type.INT
            elif (a == Type.CHAR or b == Type.CHAR):
                return Type.CHAR
            elif (a == Type.BOOL or b == Type.BOOL):
                return Type.BOOL

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

    def call(self, params):
        raise TypeError("Literal object is not callable")

    def subscript(self, subscript):
        try:
            return self.inst.array_get(subscript)
        except TypeError:
            raise

    def get(self):
        return Variable.retrieveWithTrailers(self.inst, self.trailers)[0]

class Symbol(Variable):
    __slots__ = [
        'name', 'scope', 'trailers'
    ]

    def __init__(self, name):
        self.trailers = []
        self.name = name

    def __str__(self):
        return "SYMBOL<{0}>".format(str(self.name))

    #TODO
    def call(self, params):
        if (self.get().callable):
            return 0 #AST here?
        else:
            raise TypeError(self.name + " is not callable")

    def subscript(self, subscript):
        try:
            return self.inst.array_get(subscript)
        except TypeError:
            raise

    def get(self):
        return Variable.retrieveWithTrailers(ii.Interpreter.loadSymbol(self.name), self.trailers)[0]