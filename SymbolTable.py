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
        depth = self.context.depth
        self.declaredDepth[name] = depth
        if len(subscriptList) > 0:
            data = Variable.Variable.makeDefaultValue(Type.Type.ARRAY, subscriptList, datatype)
        else:
            data = Variable.Variable.makeDefaultValue(datatype)
        self.data[(name, depth)] = data

    def put(self, name, instance, trailerList):
        if self.hasKey(name):
            if self.hasValidType(name, instance):
                self.updateData(name, instance, trailerList)
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

    def hasValidSizes(self, subscriptList, instance, rootType):
        if instance.is_pure_array():
            if len(subscriptList)==0:
                # Going deeper than we expected
                    return False;

            targetSubscript = subscriptList[0]
            #TODO: FIX A[*] <- VALUE
            if targetSubscript.isWildcard:
                return True
            else:
                if targetSubscript.isSingle:
                    targetSize = targetSubscript.end
                else:
                    targetSize = targetSubscript.end - targetSubscript.begin + 1
                levelSize = instance.array_length()
                print("TEST VALID SIZES: {0} <= {1} ??".format(levelSize, targetSize))
                valid = (levelSize <= targetSize)
                if valid:
                    childSubscripts = subscriptList[1:]
                    if (levelSize < targetSize):
                        if (instance.is_pure_array()):
                            childType = instance.heldtype
                            if childType is None: childType = rootType;
                            print("Padding {0} which holds {1} (our list is {2})".format(instance, childType, childSubscripts))
                            instance.array_pad(targetSize, 
                                               Variable.Literal(Variable.Variable.makeDefaultValue(childType, 
                                                                                                   childSubscripts,
                                                                                                   heldType=rootType)))

                    for child in instance.value:
                        valid = self.hasValidSizes(childSubscripts, child.get(), rootType)
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
        # Puts instance in name[trailers]
        depth = self.declaredDepth[name]
        current_data = self.data[(name, depth)]
        target_subscript = None

        current_data, parent_pair = Variable.Variable.retrieveWithTrailers(current_data, trailers)
        target_data, target_subscript = parent_pair
        
        is_subscripted = isinstance(target_subscript, Subscript.Subscript)

        # Copy only the very last trailer if it is a subscript list
        if len(trailers) > 0 and trailers[-1][0] == Type.TrailerType.SUBSCRIPT:
            subscriptList = trailers[-1][1]
        else:
            subscriptList = []

        if is_subscripted:
            if target_subscript.isSingle:
                desired_depth = len(subscriptList)
            else:
                desired_depth = len(subscriptList)-1
        else:
            desired_depth = 0

        applicable_subscripts = self.overrideSizes(name, subscriptList) #self.subscriptlist[name][desired_depth:]

        root_type = self.datatype[name]
        print("Applicable subscripts: {0}".format(applicable_subscripts))

        if self.hasValidSizes(applicable_subscripts, instance, root_type): # might change instance (padding)            
            if is_subscripted:
                if target_subscript.isSingle:
                    target_data.value[target_subscript.begin] = instance
                    #Variable.Variable.deepMerge(target_data[target_subscript.begin], instance)
                elif target_subscript.isWildcard:
                    target_data.value[:] = instance.value
                    #Variable.Variable.deepMerge(target_data[:], instance)
                else:
                    print("For the record, instance is {0}".format(instance))
                    target_data.value[target_subscript.begin:target_subscript.end+1] = instance.value
                    #Variable.Variable.deepMerge(target_data[target_subscript.begin:target_subscript.end+1], 
                                                #instance)
                # if target_subscript.isSingle:
                    # target_element = target_data[target_subscript.begin]
                    # if instance.type == target_element.get().type
                # else:
                    # target_data[target_subscript.begin, target_subscript.end] = 
            else:
                self.data[(name, depth)] = instance
            return True
        else:
            raise TypeError("Assignment exceeds allocated space!")

    def overrideSizes(self, name, subscripts):
        ret = self.subscriptlist[name]
        override = subscripts
        print("Do override between "+str(ret)+" and "+str(subscripts))
        override_count = len(subscripts)
        ret[:override_count] = subscripts
        return ret

    def __str__(self):
        return str(self.data)