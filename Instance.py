from Type import Type

class Instance(object):
    __slots__ = [
        'value', 'type', 'heldtype', 'size', 'collection_size', 'callable', 'dynamic'
    ]

    # TODO: Scope?

    def __init__(self, datatype, value, callable=False):
        self.type = datatype
        self.heldtype = None # For arrays
        self.callable = None # If true, value is an AST 

        if self.type == Type.INT:
            if not float(value).is_integer():
                self.type = Type.FLOAT
        #TODO: More type validations?
        
        self.value = value

        if self.type == Type.ARRAY and len(self.value)>0:
            self.heldtype = self.value[0].get().type
            if not all(element.get().type == self.heldtype for element in self.value):
                raise TypeError()

        if self.type == Type.STRING:
            self.size = len(self.value)
        elif self.type == Type.ARRAY or self.type == Type.TUPLE:
            self.size = sum([element.get().collection_size for element in self.value])
        elif self.type == Type.NULL:
            self.size = 0
        else:
            self.size = 1

        self.collection_size = 1 if self.type == Type.STRING else self.size

    #def __str__(self):
    #    return "INST({0}, {1})".format(self.type.name, self.value)

    def __repr__(self):
        return "{0}".format(self.value)

    def array_get(self, pos):
        try:
            if not self.is_subscriptable_array():
                raise TypeError("{0} cannot be subscripted.".format(self.type))
            return self.value[pos]
        except TypeError:
            raise

    def array_update(self, pos, literal):
        try:
            if not self.is_mutable_array():
                raise TypeError("{0} is immutable.".format(self.type))
            self.size -= self.value[pos].size
            self.value[pos] = literal
            self.size += literal.get().size
        except TypeError:
            raise

    def array_append(self, literal):
        try:
            if not self.is_mutable_array():
                raise TypeError("{0} cannot be appended.".format(self.type))
            self.value += [literal]
            self.size += literal.get().size
            self.collection_size += 1
        except TypeError:
            raise

    def array_length(self):
        return len(self.value)

    def array_pad(self, size, literal):
        while self.array_length() < size:
            self.array_append(literal)
        self.heldtype = self.value[0].get().type

    def array_merge(self, target, subscriptList):
        something = 2;
        #TODO: Merge

    def is_pure_array(self):
        return self.type == Type.ARRAY

    def is_subscriptable_array(self):
        return self.type in [Type.ARRAY, Type.STRING, Type.RANGE, Type.TUPLE]

    def is_mutable_array(self):
        return self.type in [Type.ARRAY, Type.STRING]
