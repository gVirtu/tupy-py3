from tupy.SymbolTable import SymbolTable
import copy

# The Context object
# ------------------
# Each code block spawns a new Context, nested from the global one.
# They are stored in the Call Stack.

class Context(object):
    def __init__(self, depth, returnable=False, breakable=False, 
                 funcName=None, returnType=(None, 0), struct=None):
        # Depth describes how nested the current code block is.
        # Global context has a depth of 0.
        self.depth = depth

        # Locals is the current context's Symbol Table. 
        self.locals = SymbolTable(self)

        # When a RETURN is found, contexts are popped from the Call Stack
        # until a returnable context is found. An example of a non-returnable
        # context is a code block inside an if/else clause. Similar handling
        # is done for BREAK/CONTINUE: for/while loops are breakable but not
        # returnable.
        self.returnable = returnable
        self.breakable = breakable

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
        # self.refMappings = {}

        # Dict of classes (TODO)
        self.classes = {}

        # In Class Contexts, this is the name of the class this belongs to
        self.structName = struct

        # In Function Contexts, this is the name of the function being ran
        self.funcName = funcName

    def inheritSymbolTable(self, otherContext):
        self.locals.data = copy.copy(otherContext.locals.data)
        self.locals.datatype = copy.copy(otherContext.locals.datatype)
        self.locals.classname = copy.copy(otherContext.locals.classname)
        self.locals.subscriptlist = copy.deepcopy(otherContext.locals.subscriptlist)
        self.locals.declaredDepth = copy.copy(otherContext.locals.declaredDepth)

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        # Only locals needs deepcopying
        setattr(result, 'depth', copy.copy(self.depth))
        setattr(result, 'locals', copy.deepcopy(self.locals, memo))
        setattr(result, 'returnable', copy.copy(self.returnable))
        setattr(result, 'breakable', copy.copy(self.breakable))
        setattr(result, 'functions', copy.copy(self.functions))
        # setattr(result, 'refMappings', copy.copy(self.refMappings))
        setattr(result, 'classes', copy.copy(self.classes))
        setattr(result, 'funcName', copy.copy(self.funcName))
        setattr(result, 'structName', copy.copy(self.structName))
        return result

    def __str__(self):
        return "CONTEXT<{0}> <<{1}>>".format(self.depth, str(self.locals))