from SymbolTable import SymbolTable

class Context(object):
    def __init__(self, parent=None):
        if (parent is None):
            self.locals = SymbolTable()
        else:
            self.locals = parent.locals

    