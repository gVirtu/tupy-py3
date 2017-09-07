from SymbolTable import SymbolTable

class Context(object):
    def __init__(self, depth):
        self.depth = depth;
        self.locals = SymbolTable(self)
        self.functions = []

    def setDepth(self, depth):
        self.depth = depth;

    def __str__(self):
        return "CONTEXT<{0}> <<{1}>>".format(self.depth, str(self.locals))