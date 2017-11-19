from SymbolTable import SymbolTable

class Context(object):
    def __init__(self, depth, returnable=False, returnType=(None, 0)):
        self.depth = depth
        self.locals = SymbolTable(self)
        self.returnable = returnable
        self.returnType = returnType
        self.functions = []
        self.refMappings = {}

    def __str__(self):
        return "CONTEXT<{0}> <<{1}>>".format(self.depth, str(self.locals))
