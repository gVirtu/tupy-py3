import Instance
import Variable
import Type
import Subscript

class SymbolTable(object):
    def __init__(self, ctx):
        self.data = {}
        self.datatype = {}
        self.subscriptlist = {}
        self.declaredDepth = {}
        self.context = ctx

    def declare(self, name, datatype, subscriptList):
        self.datatype[name] = datatype
        self.subscriptlist[name] = subscriptList
        self.declaredDepth[name] = self.context.depth

    def put(self, name, instance, trailerList):
        if self.hasKey(name):
            if self.hasValidType(name, instance):
                if self.hasValidSizes(name, instance): #might change instance (padding)
                    self.updateData(name, instance, trailerList)
                else:
                    raise TypeError("Assignment exceeds allocated space!")
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

    def hasValidSizes(self, name, instance, level=0):
        if instance.is_pure_array():
            if len(self.subscriptlist[name])<level+1:
                # Going deeper than we expected
                    return False;

            targetSubscript = self.subscriptlist[name][level]
            if targetSubscript.isWildcard:
                return True
            else:
                targetSize = targetSubscript.end
                levelSize = instance.array_length()
                print("TEST VALID SIZES: {0} <= {1} ??".format(levelSize, targetSize))
                valid = (levelSize <= targetSize)
                if valid:
                    if (levelSize < targetSize):
                        if (instance.is_pure_array()):
                            instance.array_pad(targetSize, self.defaultPadding(instance.heldtype))

                    for child in instance.value:
                        valid = self.hasValidSizes(name, child.get(), level+1)
                        if valid:
                            pass
                        else:
                            break

                return valid
        else:
            return True; # Primitive type, is ok

    def hasValidType(self, name, instance):
        if instance.is_pure_array():
            if instance.array_length() > 0:
                return self.hasValidType(name, instance.array_get(0).get())
            else:
                return True
        else:
            return instance.type == self.datatype[name]

    def defaultPadding(self, datatype):
        if datatype == Type.Type.STRING:
            return Variable.Literal(Instance.Instance(datatype, ""))
        elif datatype == Type.Type.BOOL:
            return Variable.Literal(Instance.Instance(datatype, False))
        elif datatype == Type.Type.ARRAY: 
            return Variable.Literal(Instance.Instance(datatype, []))
        else:
            return Variable.Literal(Instance.Instance(datatype, 0))

    def updateData(self, name, instance, trailers):
        depth = self.declaredDepth[name]
        current_data = self.data[(name, depth)]
        target_subscript = None
        if current_data is not None:
            target_data, target_subscript = Variable.Variable.retrieveWithTrailers(current_data, trailers)
            if isinstance(target_subscript, Subscript.Subscript):
                if target_subscript.isSingle:
                    Variable.Variable.deepMerge(target_data[target_subscript.begin], instance)
                elif target_subscript.isWildcard:
                    Variable.Variable.deepMerge(target_data[:], instance)
                else:
                    Variable.Variable.deepMerge(target_data[target_subscript.begin:target_subscript.end+1], 
                                                instance)
                # if target_subscript.isSingle:
                    # target_element = target_data[target_subscript.begin]
                    # if instance.type == target_element.get().type
                # else:
                    # target_data[target_subscript.begin, target_subscript.end] = 

        self.data[(name, depth)] = instance
        return True
        

    def __str__(self):
        return str(self.data)