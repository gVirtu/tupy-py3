from tupy.Type import Type
import tupy.Variable
import tupy.Interpreter
import copy

class Instance(object):
    __slots__ = [
        'value', 'type', 'heldtype', 'size', 'collection_size', 'array_dimensions',
        'roottype', 'class_name'
    ]

    def __init__(self, datatype, value, className=None, array_dimensions=0):
        self.type = datatype
        self.heldtype = None # For arrays
        self.roottype = self.type # For arrays, set at declare time
        self.array_dimensions = array_dimensions # For arrays
        self.class_name = className # For structs
        if self.class_name:
            self.roottype = Type.STRUCT # Useful during type validation with uninitialized structs

        if self.type == Type.INT:
            if not float(value).is_integer():
                self.type = Type.FLOAT

        self.value = value

        if self.type == Type.ARRAY:
            if len(self.value)>0:
                for element in self.value:
                    self.heldtype = tupy.Interpreter.memRead(element).type
                    if (self.heldtype != Type.NULL):
                        break
                self.roottype = tupy.Interpreter.memRead(self.value[0]).roottype
                self.array_dimensions = tupy.Interpreter.memRead(self.value[0]).array_dimensions + 1
                if not all(tupy.Interpreter.memRead(element).type == self.heldtype or
                           tupy.Interpreter.memRead(element).type == Type.NULL for element in self.value):
                    raise TypeError("Os tipos dos elementos de uma lista devem ser consistentes!")
                heldclasses = [element for element in self.value if tupy.Interpreter.memRead(element).type == Type.STRUCT]
                if len(heldclasses) > 0:
                    if not self.class_name:
                        self.class_name = tupy.Interpreter.memRead(heldclasses[0]).class_name
                    if not all(tupy.Interpreter.Interpreter.areClassNamesCompatible(self.class_name,
                                                                        tupy.Interpreter.memRead(element).class_name) \
                                for element in heldclasses):
                        raise TypeError("As classes de todos os elementos de uma lista que contém tipos compostos devem ser compatíveis!")
            else:
                self.array_dimensions = 1

        if self.type == Type.STRING:
            self.heldtype = Type.CHAR

        self.update_size()

    #def __str__(self):
    #    return "INST({0}, {1})".format(self.type.name, self.value)

    def __repr__(self):
        if self.class_name:
            return "I|C{0}".format(self.class_name)
        else:
            return "I{0}".format(self.value)

    def update_size(self, deep=False):
        if self.type == Type.STRING:
            self.size = len(self.value)
        elif self.type == Type.ARRAY or self.type == Type.TUPLE:
            if deep:
                self.size = sum([tupy.Interpreter.memRead(element).update_size() for element in self.value])
            else:
                self.size = sum([tupy.Interpreter.memRead(element).collection_size for element in self.value])
        elif self.type == Type.NULL:
            self.size = 0
        else:
            self.size = 1

        self.collection_size = 1 if self.type == Type.STRING else self.size
        return self.collection_size

    def update_roottype(self, new_type):
        #print("Updating root type of {0} to {1}".format(self.value, new_type))
        self.roottype = new_type
        if self.type == Type.ARRAY or self.type == Type.TUPLE:
            for element in self.value:
                tupy.Interpreter.memRead(element).update_roottype(new_type)

    # def print_roottype(self):
    #     print("The root type of {0} is {1}".format(self.value, self.roottype))
    #     if self.type == Type.ARRAY or self.type == Type.TUPLE:
    #         for element in self.value:
    #             element.get().print_roottype()

    # UNUSED
    # def array_update(self, pos, literal):
        # if not self.is_mutable_array():
            # raise TypeError("{0} is immutable.".format(self.type))
        # self.size -= self.value[pos].size
        # self.value[pos] = literal
        # self.size += literal.get().size

    def array_append(self, memCell):
        self.value += [memCell]
        self.size += tupy.Interpreter.memRead(memCell).size
        self.collection_size += 1

    def array_length(self):
        return len(self.value)

    def array_pad(self, size, generator, args):
        while self.array_length() < size:
            self.array_append(tupy.Interpreter.memAlloc(generator(*args)))
        if len(self.value) > 0:
            self.heldtype = tupy.Interpreter.memRead(self.value[0]).type

    def to_python_repr(self):
        if self.type == Type.ARRAY:
            return [tupy.Interpreter.memRead(elem).to_python_repr() for elem in self.value]
        if self.type == Type.TUPLE:
            return tuple([tupy.Interpreter.memRead(elem).to_python_repr() for elem in self.value])
        else:
            return self.value

    def is_pure_array(self):
        return self.type == Type.ARRAY

    def is_subscriptable_array(self):
        return self.type in [Type.ARRAY, Type.STRING, Type.TUPLE]

    def __deepcopy__(self, memo:dict):
        my_id = id(self)
        if my_id not in memo:
            cls = self.__class__
            result = cls.__new__(cls)
            memo[my_id] = result
            if self.type != Type.STRUCT or "structCopy" in memo:
                memo.pop("structCopy", None)
                setattr(result, 'value', copy.deepcopy(self.value, memo))
            else:
                setattr(result, 'value', self.value)
            setattr(result, 'type', self.type)
            setattr(result, 'heldtype', self.heldtype)
            setattr(result, 'size', self.size)
            setattr(result, 'collection_size', self.collection_size)
            setattr(result, 'array_dimensions', self.array_dimensions)
            setattr(result, 'roottype', self.roottype)
            setattr(result, 'class_name', self.class_name)
        else:
            result = memo[my_id] # necessary? not currently covered
        return result

    # UNUSED
    # def is_mutable_array(self):
        # return self.type in [Type.ARRAY, Type.STRING]
