class SymbolTable(object):
    def __init__(self):
        self.data = {}

    def put(self, name, variable):
        self.data[name] = variable

    def get(self, name):
        return self.data[name]

    def hasKey(self, name):
        return self.data.has_key(name)