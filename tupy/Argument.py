class Argument(object):
    def __init__(self, name, 
                       datatype, 
                       arrayDimensions=0,
                       passByRef=False,
                       className=None,
                       invisible=False,
                       defaultValue=None):
        self.name = name
        self.type = datatype
        self.arrayDimensions = arrayDimensions
        self.passByRef = passByRef
        self.className = className
        self.defaultValue = defaultValue
        self.invisible = invisible

    def __repr__(self):
        strr = "{0} {1} {2}={3}".format(self.name, self.type, "[]" * self.arrayDimensions, self.defaultValue)
        if (self.className): strr = self.className + strr
        if (self.passByRef): strr = "ref " + strr
        else: strr = "val " + strr
        if (self.invisible): strr = strr + " invisivel"
        return strr
