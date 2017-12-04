from Type import Type
import Variable

class Instance(object):
    __slots__ = [
        'value', 'type', 'heldtype', 'size', 'collection_size', 'array_dimensions', 'roottype', 'class_name'
    ]

    def __init__(self, datatype, value, className=None):
        self.type = datatype
        self.heldtype = None # For arrays
        self.roottype = self.type # For arrays, set at declare time
        self.array_dimensions = 0 # For arrays
        self.class_name = className # For structs

        if self.type == Type.INT:
            if not float(value).is_integer():
                self.type = Type.FLOAT
        #TODO: More type validations?
        
        self.value = value

        if self.type == Type.ARRAY and len(self.value)>0:
            self.heldtype = self.value[0].get().type
            self.roottype = self.value[0].get().roottype
            self.array_dimensions = self.value[0].get().array_dimensions + 1
            if not all(element.get().type == self.heldtype for element in self.value):
                raise TypeError()

        if self.type == Type.STRING:
            self.heldtype = Type.CHAR

        self.update_size()

    #def __str__(self):
    #    return "INST({0}, {1})".format(self.type.name, self.value)

    def __repr__(self):
        return "I{0}".format(self.value)

    def update_size(self, deep=False):
        if self.type == Type.STRING:
            self.size = len(self.value)
        elif self.type == Type.ARRAY or self.type == Type.TUPLE:
            if deep:
                self.size = sum([element.get().update_size() for element in self.value])
            else:
                self.size = sum([element.get().collection_size for element in self.value])
        elif self.type == Type.NULL:
            self.size = 0
        else:
            self.size = 1

        self.collection_size = 1 if self.type == Type.STRING else self.size
        return self.collection_size

    def update_roottype(self, new_type):
        print("Updating root type of {0} to {1}".format(self.value, new_type))
        self.roottype = new_type
        if self.type == Type.ARRAY or self.type == Type.TUPLE:
            for element in self.value:
                element.get().update_roottype(new_type)

    def print_roottype(self):
        print("The root type of {0} is {1}".format(self.value, self.roottype))
        if self.type == Type.ARRAY or self.type == Type.TUPLE:
            for element in self.value:
                element.get().print_roottype()

    def array_get(self, pos):
        return self.value[pos]

    # UNUSED
    # def array_update(self, pos, literal):
        # if not self.is_mutable_array():
            # raise TypeError("{0} is immutable.".format(self.type))
        # self.size -= self.value[pos].size
        # self.value[pos] = literal
        # self.size += literal.get().size

    def array_append(self, literal):
        self.value += [literal]
        self.size += literal.get().size
        self.collection_size += 1

    def array_length(self):
        return len(self.value)

    def array_pad(self, size, generator, args):
        while self.array_length() < size:
            self.array_append(Variable.Literal(generator(*args)))
        if len(self.value) > 0:
            self.heldtype = self.value[0].get().type

    def is_pure_array(self):
        return self.type == Type.ARRAY

    def is_subscriptable_array(self):
        return self.type in [Type.ARRAY, Type.STRING, Type.TUPLE]

    # UNUSED
    # def is_mutable_array(self):
        # return self.type in [Type.ARRAY, Type.STRING]
