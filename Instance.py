from enum import Enum

class Type(Enum):
    NULL = 0
    INT = 1
    FLOAT = 2
    STRING = 3
    CHAR = 4
    BOOL = 5
    REFERENCE = 6
    RANGE = 7
    ARRAY = 8
    TUPLE = 9

class Instance(object):
    __slots__ = [
        'value', 'type', 'heldtype', 'size', 'collection_size'
    ]

    # TODO: Scope?

    def __init__(self, datatype, value):
        self.type = datatype
        self.heldtype = None # For arrays

        if self.type == Type.INT:
            if not float(value).is_integer():
                self.type = Type.FLOAT
        #TODO: More type validations?
        
        self.value = value

        if self.type == Type.ARRAY and len(self.value)>0:
            self.heldtype = self.value[0].type
            if not all(element.type == self.heldtype for element in self.value):
                raise TypeError()

        if self.type == Type.STRING:
            self.size = len(self.value)
        elif self.type == Type.ARRAY or self.type == Type.TUPLE:
            self.size = sum([element.collection_size for element in self.value])
        elif self.type == Type.NULL:
            self.size = 0
        else:
            self.size = 1

        self.collection_size = 1 if self.type == Type.STRING else self.size

    def __str__(self):
        return "INST({0}, {1})".format(self.type.name, self.value)

    def array_update(self, pos, inst):
        self.size -= self.value[pos].size
        self.value[pos] = inst
        self.size += inst.size

    def array_append(self, inst):
        self.value.append(inst)
        self.size += inst.size

    def array_length(self):
        return len(self.value)
