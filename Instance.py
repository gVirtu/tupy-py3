from Type import Type

class Instance(object):
    __slots__ = [
        'value', 'type', 'heldtype', 'size', 'collection_size', 'array_dimensions', 'roottype'
    ]

    # TODO: Scope?

    def __init__(self, datatype, value):
        self.type = datatype
        self.heldtype = None # For arrays
        self.roottype = self.type # For arrays
        self.array_dimensions = 0 # For arrays

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

    def array_pad(self, size, literal):
        while self.array_length() < size:
            self.array_append(literal)
        self.heldtype = self.value[0].get().type

    def is_pure_array(self):
        return self.type == Type.ARRAY

    def is_subscriptable_array(self):
        return self.type in [Type.ARRAY, Type.STRING, Type.TUPLE]

    # UNUSED
    # def is_mutable_array(self):
        # return self.type in [Type.ARRAY, Type.STRING]
