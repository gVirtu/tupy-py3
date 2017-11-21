from SymbolTable import SymbolTable
import copy

# The Context object
# ------------------
# Each code block spawns a new Context, nested from the global one.
# They are stored in the Call Stack.

class Context(object):
    def __init__(self, depth, returnable=False, returnType=(None, 0), struct=None):
        # Depth describes how nested the current code block is.
        # Global context has a depth of 0.
        self.depth = depth

        # Locals is the current context's Symbol Table. 
        self.locals = SymbolTable(self)

        # When a RETURN is found, contexts are popped from the Call Stack
        # until a returnable context is found. An example of a non-returnable
        # context is a code block inside an if/else clause.
        self.returnable = returnable

        # When a returnable context (e.g. a function) is found, its returnType
        # is stored so that type checks can be made before returning.
        self.returnType = returnType

        # Functions is a list of ASTs. The array indices are referenced when
        # an actual Function object is stored in a SymbolTable.
        self.functions = []

        # RefMappings is used within function contexts. Whenever a parameter X
        # is declared as pass-by-reference, its name is mapped to the name and 
        # depth of the passed symbol. Whenever an update occurs, the mapped
        # symbol is then updated to point to the same instance reference.
        self.refMappings = {}

        # Dict of classes (TODO)
        self.classes = {}

        # In Class Contexts, this is the name of the class this belongs to
        self.structName = struct

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        # Only locals needs deepcopying
        setattr(result, 'depth', copy.copy(self.depth, memo))
        setattr(result, 'locals', copy.deepcopy(self.locals, memo))
        setattr(result, 'returnable', copy.copy(self.returnable, memo))
        setattr(result, 'functions', copy.copy(self.functions, memo))
        setattr(result, 'refMappings', copy.copy(self.refMappings, memo))
        setattr(result, 'classes', copy.copy(self.classes, memo))
        setattr(result, 'structName', copy.copy(self.structName, memo))
        return result

    def __str__(self):
        return "CONTEXT<{0}> <<{1}>>".format(self.depth, str(self.locals))
