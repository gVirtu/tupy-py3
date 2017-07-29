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

class Instance(object):
    __slots__ = [
        'value', 'type'
    ]

    # TODO: Scope?

    def __init__(self, datatype, value):
        self.type = datatype
        if self.type == Type.INT:
            if not float(value).is_integer():
                self.type = Type.FLOAT
        '''elif self.type == Type.CHAR:
            if len(value)>1:
                self.type = Type.STRING'''
        self.value = value

    def __str__(self):
        return "INST({0}, {1})".format(self.type.name, self.value)