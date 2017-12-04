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
        self.classname = {}
        self.subscriptlist = {}
        self.declaredDepth = {}
        self.context = ctx

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        # Make sure we do not call deepcopy on our context
        setattr(result, 'data', copy.deepcopy(self.data, memo))
        setattr(result, 'datatype', copy.deepcopy(self.datatype, memo))
        setattr(result, 'classname', copy.deepcopy(self.classname, memo))
        setattr(result, 'subscriptlist', copy.deepcopy(self.subscriptlist, memo))
        setattr(result, 'declaredDepth', copy.deepcopy(self.declaredDepth, memo))
        setattr(result, 'context', self.context)
        return result

    def declare(self, name, datatype, subscriptList, className):
        self.datatype[name] = datatype
        self.classname[name] = className
        self.subscriptlist[name] = subscriptList
        depth = self.context.depth
        self.declaredDepth[name] = depth
        if len(subscriptList) > 0:
            data = Variable.Variable.makeDefaultValue(Type.Type.ARRAY, subscriptList, datatype, className)
        else:
            data = Variable.Variable.makeDefaultValue(datatype, className=className)
        data.update_roottype(self.datatype[name])
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
            if self.hasValidType(name, instance, trailerList):
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

    def processDimensions(self, subscriptList, instance, rootType, sizeList, currentData, className):
        print("processDimensions({0},{1},{2},{3},{4})".format(subscriptList, instance, rootType, sizeList, currentData))
        # Because subscriptList tells us how the passed 'instance' will fit in
        # our current data, we need to verify it all the way to the end to make
        # sure our array dimensions are correct.
        # e.g.: inteiro A[3,3] <- ...; 
        #       A[2] <- [0,1,0];
        #
        # Means that [0,1,0] is placed with subscripts [2,*] into A.
        # (omitted subscripts from A in A[2] default to *)
        #
        # rootType is the stored type at the lowest possible level. It is the
        # same as the instance type when it's not an array.
        #
        # sizeList and currentData describe the symbol that is going to be
        # updated.
        #TODO: Finish documenting this mess

        # A positive length of subscriptList means we still haven't reached the lowest level of
        # an array.

        if len(subscriptList)>0:
            targetSubscript = subscriptList[0]
            targetSize = self.getTargetSize(subscriptList, currentData, sizeList)

            childSubscripts = subscriptList[1:]
            childSizes = sizeList[1:]

            if instance.is_pure_array():
                if targetSubscript.isSingle:
                    # Inserting an array, current subscript is a single index
                    # means we need to go further before reaching the correct depth.
                    # e.g.: inteiro A[2,2] <- [[0, 0], [0, 0]]
                    #       A[0,*] <- [1,2]
                    # Clearly we don't want [1,2] to override the top level, so we
                    # retrieve A[0] (which is [0, 0]) before processing the assignment.

                    targetIndex = targetSubscript.begin
                    return self.processDimensions(childSubscripts, instance, rootType, 
                                                   childSizes, currentData.value[targetIndex].get(), className)
                else:
                    # Inserting an array, current subscript is a range or wildcard.
                    #
                    # e.g.: inteiro A[2,3,3]
                    #       A[1,0..1,1..2] <- [[2, 4], [5, 6]]
                    #   results in
                    #       [ [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                    #         [[0, 2, 4], [0, 5, 6], [0, 0, 0]] ]
                    levelSize = instance.array_length()
                    isDynamicSize = sizeList[0].isWildcard
                    print("TEST VALID SIZES: {0} <= {1} ??".format(levelSize, targetSize))

                    # We don't need to validate the passed instance's length when the current
                    # dimension is dynamic, because in this case it can simply be updated
                    # to the new length.
                    valid = (levelSize <= targetSize) or (isDynamicSize)

                    if valid:
                        childType = instance.heldtype
                        # Make sure we pad the instance so that it will have exactly the same
                        # size as the target
                        # e.g.: inteiro A[5]
                        #       A <- [1, 2, 3]
                        #           result is [1, 2, 3, 0, 0]
                        if (levelSize < targetSize):
                            if childType is None: childType = rootType;
                            print("Padding {0} which holds {1} (our list is {2})".format(instance, childType, childSubscripts))
                            instance.array_pad(targetSize, Variable.Variable.makeDefaultValue, (childType, 
                                                                                            childSubscripts,
                                                                                            rootType, className))
                            levelSize = instance.array_length()
                            print("Instance is now {0}".format(instance))

                        # In some edge cases the currentData might not have the current size,
                        # especially when dealing with dynamic-sized arrays. Most notably,
                        # the bottommost size doesn't necessarily have to be dynamic, this also
                        # happens in some scenarios such as:
                        #   inteiro A[*,2]
                        #   A <- A + [[1, 2]]
                        # If we are in a dynamically-sized dimension, we have a free pass to
                        # resize the currentData. Otherwise, we have made sure the levelSize is
                        # not larger than the currentSize (aka our static size) and then padded
                        # the instance so that our levelSize is equal to our capacity. Thus, all
                        # we need to do in these cases is pad the currentData to levelSize.

                        currentSize = currentData.array_length()
                        if (isDynamicSize or currentSize < levelSize) and targetSubscript.isWildcard:
                            currentData.array_pad(levelSize, Variable.Variable.makeDefaultValue, (childType, 
                                                                                               childSubscripts,
                                                                                               rootType, className))

                        offset = targetSubscript.begin
                        for targetIndex in range(offset, offset + levelSize):
                            child = instance.value[targetIndex - offset]
                            valid = self.processDimensions(childSubscripts, child.get(), rootType, 
                                                       childSizes, currentData.value[targetIndex].get(), className)
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
                    targetIndex = targetSubscript.begin
                    valid = self.processDimensions(childSubscripts, instance, rootType, 
                                               childSizes, currentData.value[targetIndex].get(), className)
                else:
                    new_value = [Variable.Literal(Instance.Instance(instance.type, instance.value)) for i in range(targetSize)]
                    instance.__init__(Type.Type.ARRAY, new_value)

                    for targetIndex in range(len(instance.value)):
                        offset = targetSubscript.begin
                        valid = self.processDimensions(childSubscripts, instance.value[targetIndex].get(), rootType, 
                                                   childSizes, currentData.value[targetIndex+offset].get(), className)
                
                return valid;
        else:
            # We are at the lowest level
            if instance.is_pure_array():
                # Going deeper than we expected
                return False;
            else:
                # Primitive type at deepest level is ok
                return True; 

    # Utility function for dimension processing. 
    # It returns the desired size for the data to be inserted in the range/index
    # given by the first element of subscriptList. Having currentData is useful
    # in case we have variable (wildcard) dimensions, in which case we just
    # use the current amount of stored items.
    # Example: 
    # inteiro A[2, 3]
    # A[1] <- [2, 1]
    #   the above line yields:
    #       getTargetSize([1, *], [[0, 0, 0], [0, 0, 0]], [2, 3])
    #           -> getTargetSize([*], [0, 0, 0], [3])
    #               -> 3
    #   so we know that [2,1] must be padded to have size 3.
    #
    # Finally, A will be [[0, 0, 0], [2, 1, 0]].
    #

    def getTargetSize(self, subscriptList, currentData, sizeList):
        print("getTargetSize({0},{1},{2})".format(subscriptList, currentData, sizeList))
        targetSubscript = subscriptList[0]
        if targetSubscript.isWildcard:
            if sizeList[0].isWildcard:
                return currentData.array_length() if currentData.is_pure_array() else 1
            else:
                return sizeList[0].begin
        elif targetSubscript.isSingle:
            if len(subscriptList)==1:
                return 1
            else:
                targetIndex = targetSubscript.begin
                return self.getTargetSize(subscriptList[1:], 
                                          currentData.value[targetIndex].get(), 
                                          sizeList[1:])
        else:
            return targetSubscript.end - targetSubscript.begin

    def hasValidType(self, name, instance, trailerList):
        if (instance.roottype == Type.Type.NULL):
            return True
        else:
            depth = self.declaredDepth[name]
            current_data = self.data[(name, depth)]
            self.data[(name, depth)].print_roottype()

            (inst, parent) = Variable.Variable.retrieveWithTrailers(current_data, trailerList)

            # An instance will only keep its roottype as Type.ARRAY if it has no elements
            if (instance.roottype == Type.Type.ARRAY and inst.is_pure_array()):
                return True

            print("HASVALIDTYPE - RETRIEVED {0} with roottype {1}, comparing against {2} but decltype is {3}".format(inst, inst.roottype, instance.roottype, self.datatype[name]))

            return inst.roottype == instance.roottype
            # if instance.is_pure_array():
            #     if instance.array_length() > 0:
            #         return self.hasValidType(name, instance.array_get(0).get())
            #     else:
            #         return True
            # else:
            #     return instance.type == self.datatype[name] or instance.type == Type.Type.NULL

    def updateData(self, name, instance, trailers):
        # This is a call to assign some INSTANCE to some NAME
        # with a list of trailers. e.g.: A[5,5] <- 10
        # A is the NAME, 10 is the INSTANCE, and [(subscript, 5), (subscript, 5)] are the trailers.
        # Note that when a name is DECLARED, the trailers won't show up here.
        # e.g.: inteiro A[5,5] <- ... # No trailers! Equivalent to "inteiro A[5,5]; A <- ..."

        depth = self.declaredDepth[name]
        full_data = self.data[(name, depth)]
        target_subscript = None

        # An assignment should be a copy. Otherwise if we assign B to A without copying,
        # (i.e. a reference of B) whenever A is changed, B will also be.
        old_instance = instance
        instance = copy.deepcopy(old_instance)

        for ind, trailer in enumerate(trailers):
            if trailer[0] == Type.TrailerType.MEMBER:
                # A special case is updating a member of some class instance.
                # We'll cutoff the trailers list here and have that instance's
                # SymbolTable take over.
                print("Found call to member {0} at index {1}".format(trailer[1], ind))
                class_instance, _ = Variable.Variable.retrieveWithTrailers(full_data, trailers[:ind])
                return class_instance.value.locals.updateData(trailer[1], instance, trailers[(ind+1):])

        # First, apply the trailers to the name to get what's currently stored there
        # Also get "parent_triple", which contains the pair (DATA, SUBSCRIPT, DEPTH) which tells us
        # where the child data is contained. This is useful in range assignments so that we know
        # exactly the locations where our new data will be placed.
        current_data, parent_triple = Variable.Variable.retrieveWithTrailers(full_data, trailers)
        target_data, target_subscript, target_depth = parent_triple

        is_subscripted = isinstance(target_subscript, Subscript.Subscript)
        root_type = current_data.roottype

        # The only trailers that matter for range assignments are the last ones, here we
        # separate them from the rest.
        # e.g.: alunos[5].listaNotas()[3][1] -> [1, 3]
        subscriptList = []
        for trailer in reversed(trailers):
            if trailer[0] == Type.TrailerType.SUBSCRIPT:
                subscriptList = subscriptList + trailer[1]
            else:
                break

        # We need to be able to tell which sizes our INSTANCE should ideally have
        # Here we automatically fill every omitted subscript with a wildcard
        # e.g.: let A be a 2D matrix, if we want to access A[5], this would
        # be interpreted as A[5, *].
        instDepth = len(subscriptList)
        applicable_subscripts = self.fillOmittedSizes(name, subscriptList) 
        declared_sizes = self.subscriptlist[name]

        class_name = self.classname[name]
        print("Applicable subscripts: {0}".format(applicable_subscripts))

        # Next comes dimension validation and corrections. 
        # It digs inside instance's structure to find out if it has the correct sizes according to 
        # applicable_subscripts. Root_type indicates the primitive type being held at the lowest 
        # level of an array. The declared_sizes are used when the subscripts are wildcards 
        # (figure out how large the current level is), or single elements (figure out how large the
        # next level is). Finally, full_data has the current value of NAME (without subscripts).

        if self.processDimensions(applicable_subscripts, instance, root_type, declared_sizes, full_data, class_name): 
            instance.update_roottype(root_type)
            print("Instance turned into {0}".format(instance)) 
            print("Parent: {0} with subscript {1}".format(target_data, target_subscript))          
            if is_subscripted:
                self.updateChildren(target_data, target_subscript, target_depth, instance)
                print("hellooooo")
                self.data[(name, depth)].update_size(deep=True)
            else:
                self.data[(name, depth)] = instance
            # Update pass-by-reference mappings
            if name in self.context.refMappings:
                (refName, refDepth) = self.context.refMappings[name]
                self.data[(refName, refDepth)] = self.data[(name, depth)]
            self.data[(name, depth)].print_roottype()
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
        print("Merged and became {0}".format(target_value))
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
