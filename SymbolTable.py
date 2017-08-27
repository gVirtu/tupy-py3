import Instance
import Variable
import Type
import Subscript
import copy

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

    def validateSizes(self, subscriptList, instance, rootType, sizeList):
        if len(subscriptList)>0:
            # We still aren't at the lowest level
            targetSubscript = subscriptList[0]

            if targetSubscript.isWildcard:
                if sizeList[0].isWildcard:
                    targetSize = instance.array_length() if instance.is_pure_array() else 1
                else:
                    targetSize = sizeList[0].begin
            elif targetSubscript.isSingle:
                targetSize = 1
            else:
                targetSize = targetSubscript.end - targetSubscript.begin

            childSubscripts = subscriptList[1:]
            childSizes = sizeList[1:]

            if instance.is_pure_array():
                levelSize = instance.array_length()
                print("TEST VALID SIZES: {0} <= {1} ??".format(levelSize, targetSize))
                valid = (levelSize <= targetSize) or (sizeList[0].isWildcard)
                if valid:
                    if (levelSize < targetSize):
                        if (instance.is_pure_array()):
                            childType = instance.heldtype
                            if childType is None: childType = rootType;
                            print("Padding {0} which holds {1} (our list is {2})".format(instance, childType, childSubscripts))
                            instance.array_pad(targetSize, 
                                                Variable.Literal(Variable.Variable.makeDefaultValue(childType, 
                                                                                                    childSubscripts,
                                                                                                    heldType=rootType)))

                    if targetSubscript.isSingle:
                        valid = self.validateSizes(childSubscripts, instance, rootType, childSizes)
                    else:
                        for child in instance.value:
                            valid = self.validateSizes(childSubscripts, child.get(), rootType, childSizes)
                            if valid:
                                pass
                            else:
                                break

                return valid
            else:
                # Primitive not at lowest level, let's clone it into an array
                # e.g.: 4 -> [[4,4], [4,4]]

                if targetSubscript.isSingle:
                    valid = self.validateSizes(childSubscripts, instance, rootType, childSizes)
                else:
                    new_value = [Variable.Literal(Variable.Instance(instance.type, instance.value)) for i in range(targetSize)]
                    instance.__init__(Type.Type.ARRAY, new_value)
                    for child in instance.value:
                        valid = self.validateSizes(childSubscripts, child.get(), rootType, childSizes)
                        if valid:
                            pass
                        else:
                            break
                
                return valid;
        else:
            # We are at the lowest level
            if instance.is_pure_array():
                # Going deeper than we expected
                return False;
            else:
                # Primitive type at deepest level is ok
                return True; 

    def hasValidType(self, name, instance):
        if instance.is_pure_array():
            if instance.array_length() > 0:
                return self.hasValidType(name, instance.array_get(0).get())
            else:
                return True
        else:
            return instance.type == self.datatype[name] or instance.type == Type.Type.NULL

    def updateData(self, name, instance, trailers):
        # This is a call to assign some INSTANCE to some NAME
        # with a list of trailers. e.g.: A[5,5] <- 10
        # A is the NAME, 10 is the INSTANCE, and [(subscript, 5), (subscript, 5)] are the trailers.
        # Note that when a name is DECLARED, the trailers won't show up here.
        # e.g.: inteiro A[5,5] <- ... # No trailers! Equivalent to inteiro A[5,5]; A <- ...

        depth = self.declaredDepth[name]
        current_data = self.data[(name, depth)]
        target_subscript = None

        # Make sure we aren't overwriting anything important
        old_instance = instance
        instance = copy.deepcopy(old_instance)

        # First, apply the trailers to the name to get what's currently stored there
        # Also get "parent_pair", which contains the pair (DATA, SUBSCRIPT) which tells us
        # where the child data is contained.
        current_data, parent_pair = Variable.Variable.retrieveWithTrailers(current_data, trailers)
        target_data, target_subscript = parent_pair

        is_subscripted = isinstance(target_subscript, Subscript.Subscript)

        # Copy only the very last trailer if it is a subscript list
        if len(trailers) > 0 and trailers[-1][0] == Type.TrailerType.SUBSCRIPT:
            subscriptList = trailers[-1][1]
        else:
            subscriptList = []

        # We need to be able to tell which sizes our INSTANCE should ideally have
        applicable_subscripts = self.fillOmittedSizes(name, subscriptList) 
        declared_sizes = self.subscriptlist[name]

        root_type = self.datatype[name]
        print("Applicable subscripts: {0}".format(applicable_subscripts))

        if self.validateSizes(applicable_subscripts, instance, root_type, declared_sizes): # might change instance (padding) 
            print("Instance turned into {0}".format(instance)) 
            print("Parent: {0} with subscript {1}".format(target_data, target_subscript))          
            if is_subscripted:
                if target_subscript.isSingle:
                    target_data.value[target_subscript.begin] = Variable.Literal(instance)
                elif target_subscript.isWildcard:
                    target_data.value[:] = self.deepMerge(target_data.value[:], instance.value)
                    #target_data.value[:] = instance.value
                else:
                    print("For the record, instance is {0}".format(instance))
                    target_data.value[target_subscript.begin:target_subscript.end] = \
                        self.deepMerge(target_data.value[target_subscript.begin:target_subscript.end], instance.value)
                    #target_data.value[target_subscript.begin:target_subscript.end] = instance.value
            else:
                self.data[(name, depth)] = instance
            return True
        else:
            raise TypeError("Assignment exceeds allocated space!")

    def deepMerge(self, target_value, source_value):
        for ind in range(len(target_value)):
            child = target_value[ind].inst
            newchild = source_value[ind].inst
            if isinstance(child.value, list):
                self.deepMerge(child.value, newchild.value)
            else:
                target_value[ind].inst = source_value[ind].inst
        for ind in range(len(target_value), len(source_value)):
            print("NEW ELEMENT {0}".format(source_value[ind]))
            target_value.append(source_value[ind])
        return target_value

    def fillOmittedSizes(self, name, subscripts):
        ret = subscripts
        target = len(self.subscriptlist[name])
        while len(ret) < target:
            ret.append(Subscript.Subscript(isWildcard=True))
        return ret        

    def __str__(self):
        return str(self.data)