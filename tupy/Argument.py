class Argument(object):
    def __init__(self, name, 
                       datatype, 
                       arrayDimensions=0,
                       passByRef=False,
                       className=None,
                       defaultValue=None):
        self.name = name
        self.type = datatype
        self.arrayDimensions = arrayDimensions
        self.passByRef = passByRef
        self.className = className
        self.defaultValue = defaultValue

    def __repr__(self):
        strr = "{0} {1} {2}".format(self.name, self.type, "[]" * self.arrayDimensions)
        if (self.className): return self.className + strr
        if (self.passByRef): return "ref " + strr
        else: return "val " + strr
