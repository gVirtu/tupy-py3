class SymbolTable(object):
    def __init__(self, ctx):
        self.data = {}
        self.datatype = {}
        self.declaredDepth = {}
        self.context = ctx

    def declare(self, name, datatype):
        self.datatype[name] = datatype
        self.declaredDepth[name] = self.context.depth

    def put(self, name, instance):
        if self.hasKey(name):
            if self.datatype[name] == instance.type:
                depth = self.declaredDepth[name]
                self.data[(name, depth)] = instance
            else:
                raise TypeError("Assignment types do not match!")
        else:
            raise NameError(name+" is not defined!")

    def get(self, name):
        depth = self.declaredDepth[name]
        return self.data[(name, depth)]

    def hasKey(self, name):
        return name in self.declaredDepth

    def merge(self, symbolTable):
        # Only add the variables from outer scopes that were changed in inner scopes
        self.data.update({key:val for key,val in symbolTable.data.items() if key[1] <= self.context.depth})

    def __str__(self):
        return str(self.data)