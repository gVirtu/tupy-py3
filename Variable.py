from Type import TrailerType, Type
import Interpreter as ii
import copy
import Instance
import Context

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
                        ret = Instance.Instance(newtype, newvalue)
                        ret.roottype = orig_root_type
                    else:
                        (newvalue, newtype) = cls.get_array_range(ret, ss.begin, ss.end, depth)
                        orig_root_type = ret.roottype
                        ret = Instance.Instance(newtype, newvalue)
                        ret.roottype = orig_root_type
                        depth += 1
            elif ttype == TrailerType.CALL:
                # try:
                # ii.logger.debug("tid {0}".format(tid))
                ret = ii.Interpreter.executeBlock(ret.value, tid)
                # except Exception:
                    # raise TypeError("{0} is not callable!".format(ret.type))
            elif ttype == TrailerType.MEMBER:
                ii.Interpreter.callStack.push(ret.value)
                ret = ret.value.locals.get(tid)
                classContextsPushed = classContextsPushed+1
            else:
                pass

        for i in range(classContextsPushed):
            ii.Interpreter.popFrame()

        return (ret, parent)

    @classmethod
    def get_array_range(cls, inst, begin, end, level, single=False):
        ii.logger.debug("get_array_range({0}, {1}, {2}, {3})".format(inst, begin, end, level))
        if level == 0:
            if not inst.is_subscriptable_array():
                raise TypeError("{0} cannot be subscripted.".format(inst.type))
            
            if (single):
                if inst.type == Type.STRING:
                    ii.logger.debug("...returned {0}".format(inst.value[begin]))
                    return (ord(inst.value[begin]), Type.CHAR)
                else:
                    ii.logger.debug("...returned {0}".format(inst.value[begin].get().value))
                    return (inst.value[begin].get().value, inst.value[begin].get().type)
            else:
                ii.logger.debug("...returned {0}".format(inst.value[begin:end]))
                return (inst.value[begin:end], inst.type)
        else:
            ret = []
            ii.logger.debug("Welp, first gotta check {0}".format(inst.value))
            for literal in inst.value:
                lower_inst = literal.get()
                lower_level = cls.get_array_range(lower_inst, begin, end, level-1, single)[0] #Not interested in type
                if (single and level==1):
                    new_inst = Instance.Instance(lower_inst.heldtype, lower_level)
                else:
                    new_inst = Instance.Instance(lower_inst.type, lower_level)
                ret.append(Literal(new_inst))
                
            ii.logger.debug("...returned {0}".format(ret))
            return (ret, inst.heldtype)

    @classmethod
    def makeDefaultValue(cls, datatype, declSubscripts=None, heldType=None, className=None):
        if declSubscripts is None:
            declSubscripts = []
        if datatype == Type.ARRAY:
            return cls.array_init(declSubscripts, heldType)
        elif datatype == Type.STRING:
            return Instance.Instance(datatype, "")
        elif datatype == Type.TUPLE:
            return Instance.Instance(datatype, ())
        elif datatype == Type.STRUCT:
            return Instance.Instance(Type.NULL, None, className=className) #ii.Interpreter.newClassInstance(className)
        else:
            return Instance.Instance(datatype, 0)

    @classmethod
    def array_init(cls, declSubscripts, heldType, className=None):
        if len(declSubscripts)==0:
            # At lowest level, initialize an element
            ret = cls.makeDefaultValue(heldType, className=className)
            return ret
        else:
            subs = declSubscripts[0]
            sz = subs.begin
            element = Literal(cls.array_init(declSubscripts[1:], heldType, className))
            content = [(copy.deepcopy(element)) for i in range(sz)]
            ret = Instance.Instance(Type.ARRAY, content)
            return ret

    def power(self, rhs:'Variable'):
        typ = self.resultType(self.get().type, rhs.get().type)
        return Literal(Instance.Instance(typ, self.get().value ** rhs.get().value))

    def positive(self):
        return Literal(Instance.Instance(self.get().type, +self.get().value))

    def negative(self):
        return Literal(Instance.Instance(self.get().type, -self.get().value))

    def bitwise_flip(self):
        if (self.get().type != Type.INT):
            raise TypeError("Cannot do bit-wise NOT with non-integer type!")
        return Literal(Instance.Instance(Type.INT, ~self.get().value))

    def multiply(self, rhs:'Variable'):
        typ = self.resultType(self.get().type, rhs.get().type)
        return Literal(Instance.Instance(typ, self.get().value * rhs.get().value))

    def divide(self, rhs:'Variable'):
        typ = self.resultType(self.get().type, rhs.get().type)
        return Literal(Instance.Instance(typ, self.get().value / rhs.get().value))

    def modulo(self, rhs:'Variable'):
        typ = self.resultType(self.get().type, rhs.get().type)
        return Literal(Instance.Instance(typ, self.get().value % rhs.get().value))

    def integer_divide(self, rhs:'Variable'):
        typ = self.resultType(self.get().type, rhs.get().type)
        return Literal(Instance.Instance(typ, self.get().value // rhs.get().value))

    def add(self, rhs:'Variable'):
        typ = self.resultType(self.get().type, rhs.get().type)
        if typ == Type.STRING:
            return Literal(Instance.Instance(typ, self.stringConcat(self.get(), rhs.get())))
        else:
            return Literal(Instance.Instance(typ, self.get().value + rhs.get().value))

    def subtract(self, rhs:'Variable'):
        typ = self.resultType(self.get().type, rhs.get().type)
        return Literal(Instance.Instance(typ, self.get().value - rhs.get().value))

    def left_shift(self, rhs:'Variable'):
        if (self.get().type != Type.INT or rhs.get().type != Type.INT):
            raise TypeError("Cannot do bit-wise shift with non-integer types!")
        typ = Type.INT
        return Literal(Instance.Instance(typ, self.get().value << rhs.get().value))

    def right_shift(self, rhs:'Variable'):
        if (self.get().type != Type.INT or rhs.get().type != Type.INT):
            raise TypeError("Cannot do bit-wise shift with non-integer types!")
        typ = Type.INT
        return Literal(Instance.Instance(typ, self.get().value >> rhs.get().value))

    def bitwise_and(self, rhs:'Variable'):
        if (self.get().type != Type.INT or rhs.get().type != Type.INT):
            raise TypeError("Cannot do bit-wise AND with non-integer types!")
        typ = Type.INT
        return Literal(Instance.Instance(typ, self.get().value & rhs.get().value))

    def bitwise_or(self, rhs:'Variable'):
        if (self.get().type != Type.INT or rhs.get().type != Type.INT):
            raise TypeError("Cannot do bit-wise OR with non-integer types!")
        typ = Type.INT
        return Literal(Instance.Instance(typ, self.get().value | rhs.get().value))

    def bitwise_xor(self, rhs:'Variable'):
        if (self.get().type != Type.INT or rhs.get().type != Type.INT):
            raise TypeError("Cannot do bit-wise XOR with non-integer types!")
        typ = Type.INT
        return Literal(Instance.Instance(typ, self.get().value ^ rhs.get().value))

    def gt(self, rhs:'Variable'):
        return Literal(Instance.Instance(Type.BOOL, self.get().value > rhs.get().value))

    def lt(self, rhs:'Variable'):
        return Literal(Instance.Instance(Type.BOOL, self.get().value < rhs.get().value))

    def gt_eq(self, rhs:'Variable'):
        return Literal(Instance.Instance(Type.BOOL, self.get().value >= rhs.get().value))

    def lt_eq(self, rhs:'Variable'):
        return Literal(Instance.Instance(Type.BOOL, self.get().value <= rhs.get().value))

    def eq(self, rhs:'Variable'):
        return Literal(Instance.Instance(Type.BOOL, self.get().value == rhs.get().value))

    def neq(self, rhs:'Variable'):
        return Literal(Instance.Instance(Type.BOOL, self.get().value != rhs.get().value))

    def logic_not(self):
        return Literal(Instance.Instance(Type.BOOL, not self.get().value))

    def logic_and(self, rhs:'Variable'):
        return Literal(Instance.Instance(Type.BOOL, self.get().value and rhs.get().value))

    def logic_or(self, rhs:'Variable'):
        return Literal(Instance.Instance(Type.BOOL, self.get().value or rhs.get().value))

    def cardinality(self):
        return Literal(Instance.Instance(Type.INT, self.get().size))

    def resultType(self, a, b):
        if (a == Type.REFERENCE or b == Type.REFERENCE):
            raise TypeError("Cannot operate on instance of type REFERENCE!")
        elif (a == Type.STRUCT or b == Type.STRUCT):
            raise TypeError("Cannot operate on STRUCTS!")
        elif (a == Type.FUNCTION or b == Type.FUNCTION):
            raise TypeError("Cannot operate on FUNCTIONS!")
        elif (a == Type.NULL or b == Type.NULL):
            raise TypeError("Cannot operate on instance of type NULL!")
        # elif (a == Type.RANGE or b == Type.RANGE):
            # raise TypeError("Cannot operate on instance of type RANGE!")
        elif (a == Type.ARRAY or b == Type.ARRAY):
            if (a == Type.ARRAY and b == Type.ARRAY):
                return Type.ARRAY
            else:
                raise TypeError("ARRAY cannot operate with other types!")
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
        'name', 'scope', 'trailers'
    ]

    def __init__(self, name):
        self.trailers = []
        self.name = name

    def __str__(self):
        return "SYMBOL<{0}>".format(str(self.name))

    def get(self):
        return Variable.retrieveWithTrailers(ii.Interpreter.loadSymbol(self.name), self.trailers)[0]
