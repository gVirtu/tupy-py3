from enum import Enum

class Type(Enum):
    NULL = 0
    INT = 1
    FLOAT = 2
    STRING = 3
    CHAR = 4
    BOOL = 5
    REFERENCE = 6
    # RANGE = 7
    ARRAY = 8
    TUPLE = 9
    FUNCTION = 10
    STRUCT = 11
    RESERVED = 12

class TrailerType(Enum):
    SUBSCRIPT = 0
    CALL = 1
    MEMBER = 2
