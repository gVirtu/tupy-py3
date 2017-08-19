from Instance import Instance
from Type import Type
import Interpreter as ii

class Variable(object):
    def call(self, params):
        pass

    def subscript(self, subscript):
        pass

    def get(self):
        pass

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
        'inst'
    ]

    def __init__(self, instance):
        self.inst = instance

    def __str__(self):
        return "LITERAL<{0}>".format(str(self.inst))

    def call(self, params):
        raise TypeError("Literal object is not callable")

    def subscript(self, subscript):
        try:
            return self.inst.array_get(subscript)
        except TypeError:
            raise

    def get(self):
        return self.inst

class Symbol(Variable):
    __slots__ = [
        'name', 'scope'
    ]

    def __init__(self, name):
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
        return ii.Interpreter.loadSymbol(self.name)