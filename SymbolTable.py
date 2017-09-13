import Instance
import Variable
import Function
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

    def defineFunction(self, name, returnType, argumentList, code, builtIn=False):
        self.datatype[name] = Type.Type.FUNCTION
        self.subscriptlist[name] = None
        depth = self.context.depth
        self.declaredDepth[name] = depth
        try:
            entry = self.data[(name, depth)].value
        except Exception:
            entry = Function.Function(name)
            self.data[(name, depth)] = Instance.Instance(Type.Type.FUNCTION, entry)
        finally:
            if entry.is_ambiguous(argumentList):
                raise NameError("Overloaded function {0} is ambiguous!".format(name))
            else:
                entry.put(argumentList, returnType, code, builtIn)

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
        print("validateSizes({0},{1},{2},{3})".format(subscriptList, instance, rootType, sizeList))
        if len(subscriptList)>0:
            # We still aren't at the lowest level
            targetSubscript = subscriptList[0]
            targetSize = self.getTargetSize(subscriptList, instance, sizeList)

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
                # e.g.: inteiro A[2,2]; A[*,*] <- 4
                # means that 4 becomes [[4,4], [4,4]]

                if targetSubscript.isSingle:
                    valid = self.validateSizes(childSubscripts, instance, rootType, childSizes)
                else:
                    new_value = [Variable.Literal(Instance.Instance(instance.type, instance.value)) for i in range(targetSize)]
                    instance.__init__(Type.Type.ARRAY, new_value)
                    for child in instance.value:
                        valid = self.validateSizes(childSubscripts, child.get(), rootType, childSizes)
                
                return valid;
        else:
            # We are at the lowest level
            if instance.is_pure_array():
                # Going deeper than we expected
                return False;
            else:
                # Primitive type at deepest level is ok
                return True; 

    def getTargetSize(self, subscriptList, instance, sizeList):
        targetSubscript = subscriptList[0]
        if targetSubscript.isWildcard:
            if sizeList[0].isWildcard:
                return instance.array_length() if instance.is_pure_array() else 1
            else:
                return sizeList[0].begin
        elif targetSubscript.isSingle:
            if len(subscriptList)==1:
                return 1
            else:
                return self.getTargetSize(subscriptList[1:], instance, sizeList[1:])
        else:
            return targetSubscript.end - targetSubscript.begin

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
        # Also get "parent_triple", which contains the pair (DATA, SUBSCRIPT, DEPTH) which tells us
        # where the child data is contained.
        current_data, parent_triple = Variable.Variable.retrieveWithTrailers(current_data, trailers)
        target_data, target_subscript, target_depth = parent_triple

        is_subscripted = isinstance(target_subscript, Subscript.Subscript)

        # Copy only the very last trailer if it is a subscript list
        subscriptList = []
        for trailer in reversed(trailers):
            if trailer[0] == Type.TrailerType.SUBSCRIPT:
                subscriptList = subscriptList + trailer[1]

        # We need to be able to tell which sizes our INSTANCE should ideally have
        # Here we automatically fill every omitted subscript with a wildcard
        # e.g.: let A be a 2D matrix, if we want to access A[5], this would
        # be interpreted as A[5, *].
        applicable_subscripts = self.fillOmittedSizes(name, subscriptList) 
        declared_sizes = self.subscriptlist[name]

        root_type = self.datatype[name]
        print("Applicable subscripts: {0}".format(applicable_subscripts))

        # Next comes dimension validation. It digs inside instance's structure to find out
        # if it has the correct sizes according to applicable_subscripts. Root_type indicates
        # the primitive type being held at the lowest level of an array. The declared_sizes
        # are used when the subscripts are wildcards (figure out how large the current level is),
        # or single elements (figure out how large the next level is).
        if self.validateSizes(applicable_subscripts, instance, root_type, declared_sizes): 
            print("Instance turned into {0}".format(instance)) 
            print("Parent: {0} with subscript {1}".format(target_data, target_subscript))          
            if is_subscripted:
                self.updateChildren(target_data, target_subscript, target_depth, instance)
                print("hellooooo")
                self.data[(name, depth)].update_size(deep=True)
            else:
                self.data[(name, depth)] = instance
            return True
        else:
            raise TypeError("Assignment exceeds allocated space!")

    def updateChildren(self, target_data, target_subscript, depth, instance):
        print("updateChildren(target_data={0}, target_subscript={1}, depth={2}, instance={3})".format(target_data, target_subscript, depth, instance))
        if depth == 0:
            if target_subscript.isSingle:
                target_data.value[target_subscript.begin] = Variable.Literal(instance)
            elif target_subscript.isWildcard:
                target_data.value[:] = self.deepMerge(target_data.value[:], instance.value)
            else:
                target_data.value[target_subscript.begin:target_subscript.end] = \
                    self.deepMerge(target_data.value[target_subscript.begin:target_subscript.end], instance.value)
        else:
            # Here we assume target_data and instance will have the exact same structure
            for ind in range(len(target_data.value)):
                child = target_data.value[ind]
                inst_child = instance.value[ind]
                self.updateChildren(child.get(), target_subscript, depth-1, inst_child.get())

    def deepMerge(self, target_value, source_value):
        print("deepMerge({0}, {1})".format(target_value, source_value))
        updateLength = min(len(target_value), len(source_value))
        for ind in range(updateLength):
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
        ret = ""
        for key in self.data:
            ret += str(key)
            ret += " -> "
            ret += str(self.data[key])
            ret += "\n"
        return ret