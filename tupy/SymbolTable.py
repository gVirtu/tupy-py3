import tupy.Instance
import tupy.Interpreter
import tupy.Variable
import tupy.Function
import tupy.Type
import tupy.Subscript
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

    def declare(self, name, datatype, subscriptList, className, invisible):
        self.datatype[name] = datatype
        self.classname[name] = className
        self.subscriptlist[name] = subscriptList
        depth = self.context.depth
        self.declaredDepth[name] = depth
        if len(subscriptList) > 0:
            data = tupy.Variable.Variable.makeDefaultValue(tupy.Type.Type.ARRAY, subscriptList, datatype, className)
        else:
            data = tupy.Variable.Variable.makeDefaultValue(datatype, className=className)
        data.update_roottype(self.datatype[name])
        self.adjustArrayDimensions(data, len(subscriptList))
        data.class_name = className
        if (name, depth) in self.data:
            tupy.Interpreter.memRealloc(self.data[(name, depth)], data, invisible)
        else:
            self.data[(name, depth)] = tupy.Interpreter.memAlloc(data, invisible)

    def adjustArrayDimensions(self, data, dimensions):
        data.array_dimensions = dimensions
        if (data.type == tupy.Type.Type.ARRAY):
            for child in data.value:
                childInst = tupy.Interpreter.memRead(child)
                self.adjustArrayDimensions(childInst, dimensions-1)

    def defineFunction(self, name, returnType, argumentList, code, builtIn=False, isConstructor=False, overrideable=False):
        tupy.Interpreter.logger.debug("Declaring function "+name+" that returns "+str(returnType)+" with arguments "+str(argumentList))
        self.datatype[name] = tupy.Type.Type.FUNCTION
        self.classname[name] = None
        self.subscriptlist[name] = None
        depth = self.context.depth
        self.declaredDepth[name] = depth
        try:
            entry = tupy.Interpreter.memRead(self.data[(name, depth)]).value
        except Exception:
            entry = tupy.Function.Function(name)
            self.data[(name, depth)] = tupy.Interpreter.memAlloc(tupy.Instance.Instance(tupy.Type.Type.FUNCTION, entry))

        if entry.is_ambiguous(argumentList, depth):
            raise NameError("A função sobrecarregada {0} está ambígua!".format(name))
        else:
            entry.put(self.context, argumentList, returnType, code, builtIn, isConstructor, overrideable)

    def put(self, name, instance, trailerList):
        if self.hasKey(name):
            if self.hasValidType(name, instance, trailerList):
                self.updateData(name, instance, trailerList)
            else:
                raise TypeError("Tipos incompatíveis na atribuição!")
        else:
            raise NameError("O nome "+name+" não está definido!")

    def ref(self, name, cell):
        depth = self.declaredDepth[name]
        self.data[(name, depth)] = cell

    def get(self, name):
        try:
            depth = self.declaredDepth[name]
        except KeyError as e:
            if self.context.structName:
                raise NameError("O tipo {0} não possui o atributo {1}!".format(self.context.structName, name))
            else: # pragma: no cover
                raise e # unknown fallback
        
        return tupy.Interpreter.memRead(self.data[(name, depth)])

    def hasKey(self, name):
        return name in self.declaredDepth

    def merge(self, symbolTable):
        # Only add the variables from outer scopes that were changed in inner scopes
        self.data.update({key:val for key,val in symbolTable.data.items() if key[1] <= self.context.depth})

    def processDimensions(self, subscriptList, instance, rootType, sizeList, currentData, className):
        tupy.Interpreter.logger.debug("processDimensions({0},{1},{2},{3},{4})".format(subscriptList, instance, rootType, sizeList, currentData))
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
                                                   childSizes, tupy.Interpreter.memRead(currentData.value[targetIndex]), className)
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
                    tupy.Interpreter.logger.debug("TEST VALID SIZES: {0} <= {1} ??".format(levelSize, targetSize))

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
                        if (levelSize < targetSize and not isDynamicSize):
                            if childType is None: childType = rootType;
                            tupy.Interpreter.logger.debug("Padding {0} which holds {1} (our list is {2})".format(instance, childType, childSubscripts))
                            instance.array_pad(targetSize, tupy.Variable.Variable.makeDefaultValue, (childType, 
                                                                                            childSubscripts,
                                                                                            rootType, className))
                            levelSize = instance.array_length()
                            tupy.Interpreter.logger.debug("Instance is now {0}".format(instance))

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
                            currentData.array_pad(levelSize, tupy.Variable.Variable.makeDefaultValue, (childType, 
                                                                                               childSubscripts,
                                                                                               rootType, className))

                        offset = targetSubscript.begin
                        for targetIndex in range(offset, offset + levelSize):
                            child = instance.value[targetIndex - offset]
                            valid = self.processDimensions(childSubscripts, tupy.Interpreter.memRead(child), rootType, 
                                                       childSizes, tupy.Interpreter.memRead(currentData.value[targetIndex]), className)
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
                    if currentData.type == tupy.Type.Type.STRING:
                        valid = self.processDimensions(childSubscripts, instance, rootType, 
                                               childSizes, tupy.Instance.Instance(tupy.Type.Type.CHAR, currentData.value[targetIndex]), className)
                    else:
                        valid = self.processDimensions(childSubscripts, instance, rootType, 
                                               childSizes, tupy.Interpreter.memRead(currentData.value[targetIndex]), className)
                else:
                    if currentData.type == tupy.Type.Type.STRING:
                        if instance.type == tupy.Type.Type.STRING:
                            valid = len(instance.value) == targetSize
                        elif instance.type == tupy.Type.Type.CHAR:
                            new_value = chr(instance.value) * targetSize
                            instance.__init__(tupy.Type.Type.STRING, new_value)
                            valid = True
                    else:
                        new_value = [tupy.Interpreter.memAlloc(tupy.Instance.Instance(instance.type, instance.value, className=instance.class_name)) for i in range(targetSize)]
                        instance.__init__(tupy.Type.Type.ARRAY, new_value)
                        valid = True

                        for targetIndex in range(len(instance.value)):
                            offset = targetSubscript.begin
                            valid = self.processDimensions(childSubscripts, tupy.Interpreter.memRead(instance.value[targetIndex]), rootType, 
                                                    childSizes, tupy.Interpreter.memRead(currentData.value[targetIndex+offset]), className)
                
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
        tupy.Interpreter.logger.debug("getTargetSize({0},{1},{2})".format(subscriptList, currentData, sizeList))
        targetSubscript = subscriptList[0]
        if targetSubscript.isWildcard:
            if currentData.type == tupy.Type.Type.STRING:
                return len(currentData.value)
            else:
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
                                          tupy.Interpreter.memRead(currentData.value[targetIndex]), 
                                          sizeList[1:])
        else:
            if targetSubscript.end is None:
                if sizeList[0].isWildcard:
                    sz = currentData.array_length() if currentData.is_pure_array() else 1
                else:
                    sz = sizeList[0].begin
                return sz - targetSubscript.begin
            else:
                return targetSubscript.end - targetSubscript.begin

    def hasValidType(self, name, instance, trailerList):
        if (instance.roottype == tupy.Type.Type.NULL):
            return True
        else:
            depth = self.declaredDepth[name]
            current_data = tupy.Interpreter.memRead(self.data[(name, depth)])
            # self.data[(name, depth)].print_roottype()

            (inst, parent) = tupy.Variable.Variable.retrieveWithTrailers(current_data, trailerList)

            # An instance will only keep its roottype as Type.ARRAY if it's a literal has no elements
            if (instance.roottype == tupy.Type.Type.ARRAY and inst.is_pure_array()):
                return True

            tupy.Interpreter.logger.debug("HASVALIDTYPE - RETRIEVED {0} with roottype {1}, comparing against {2} ({3}) but decltype is {4}".format(inst, inst.roottype, instance, instance.roottype, self.datatype[name]))

            if (instance.type == tupy.Type.Type.INT and inst.type == tupy.Type.Type.FLOAT):
                # Very special case
                instance.__init__(tupy.Type.Type.FLOAT, instance.value)

            equivalent_types = (inst.roottype == instance.roottype) \
                               or (len(trailerList) > 0 and \
                                   trailerList[-1][0] == tupy.Type.TrailerType.SUBSCRIPT and \
                                   inst.roottype == tupy.Type.Type.STRING and \
                                   instance.roottype == tupy.Type.Type.CHAR) 

            if (inst.roottype == tupy.Type.Type.STRUCT and equivalent_types):
                tupy.Interpreter.logger.debug("CLASS NAMES are {0} and {1}".format(inst.class_name, instance.class_name))
                return tupy.Interpreter.Interpreter.areClassNamesCompatible(inst.class_name, instance.class_name) #inst.class_name == instance.class_name
            else:
                return equivalent_types
            # if instance.is_pure_array():
            #     if instance.array_length() > 0:
            #         return self.hasValidType(name, instance.array_get(0).get())
            #     else:
            #         return True
            # else:
            #     return instance.type == self.datatype[name] or instance.type == tupy.Type.Type.NULL

    def updateData(self, name, instance, trailers, visited=None):
        if visited is None: visited = {}
        tupy.Interpreter.logger.debug("Updating {0}{1} to {2} (visits={3})".format(name, trailers, instance, visited))
        # This is a call to assign some INSTANCE to some NAME
        # with a list of trailers. e.g.: A[5,5] <- 10
        # A is the NAME, 10 is the INSTANCE, and [(subscript, 5), (subscript, 5)] are the trailers.
        # Note that when a name is DECLARED, the trailers won't show up here.
        # e.g.: inteiro A[5,5] <- ... # No trailers! Equivalent to "inteiro A[5,5]; A <- ..."

        depth = self.declaredDepth[name]

        full_data = tupy.Interpreter.memRead(self.data[(name, depth)])
        target_subscript = None

        if (instance.type != tupy.Type.Type.STRUCT):
            old_instance = instance
            instance = copy.deepcopy(old_instance)

        for ind, trailer in enumerate(trailers):
            if trailer[0] == tupy.Type.TrailerType.MEMBER:
                # A special case is updating a member of some class instance.
                # We'll cutoff the trailers list here and have that instance's
                # SymbolTable take over.
                tupy.Interpreter.logger.debug("Found call to member {0} at index {1}".format(trailer[1], ind))
                class_instance, _ = tupy.Variable.Variable.retrieveWithTrailers(full_data, trailers[:ind])
                class_instance.value.locals.updateData(trailer[1], instance, trailers[(ind+1):], visited=visited)
                # self.updateRefs(name, depth, visited)
                return True

        if (self.classname[name]): #self.datatype[name] == tupy.Type.Type.STRUCT):
            instance.class_name = self.classname[name]

        # First, apply the trailers to the name to get what's currently stored there
        # Also get "parent_triple", which contains the pair (DATA, SUBSCRIPT, DEPTH) which tells us
        # where the child data is contained. This is useful in range assignments so that we know
        # exactly the locations where our new data will be placed.
        current_data, parent_triple = tupy.Variable.Variable.retrieveWithTrailers(full_data, trailers)
        target_data, target_subscript, target_depth = parent_triple

        is_subscripted = isinstance(target_subscript, tupy.Subscript.Subscript)
        root_type = current_data.roottype

        # The only trailers that matter for range assignments are the last ones, here we
        # separate them from the rest.
        # e.g.: alunos[5].listaNotas()[3][1] -> [1, 3]
        subscriptList = []
        for trailer in reversed(trailers):
            if trailer[0] == tupy.Type.TrailerType.SUBSCRIPT:
                subscriptList = subscriptList + trailer[1]
            else:
                # MEMBER trailertypes have already been handled above
                raise SyntaxError("Não é possível atribuir a chamadas de função!")

        # We need to be able to tell which sizes our INSTANCE should ideally have
        # Here we automatically fill every omitted subscript with a wildcard
        # e.g.: let A be a 2D matrix, if we want to access A[5], this would
        # be interpreted as A[5, *].
        instDepth = len(subscriptList)
        applicable_subscripts = self.fillOmittedSizes(name, subscriptList) 
        declared_sizes = self.subscriptlist[name]

        class_name = self.classname[name]
        # tupy.Interpreter.logger.debug("Applicable subscripts: {0}".format(applicable_subscripts))

        # Next comes dimension validation and corrections. 
        # It digs inside instance's structure to find out if it has the correct sizes according to 
        # applicable_subscripts. Root_type indicates the primitive type being held at the lowest 
        # level of an array. The declared_sizes are used when the subscripts are wildcards 
        # (figure out how large the current level is), or single elements (figure out how large the
        # next level is). Finally, full_data has the current value of NAME (without subscripts).

        if self.processDimensions(applicable_subscripts, instance, root_type, declared_sizes, full_data, class_name): 
            instance.update_roottype(root_type)
            tupy.Interpreter.logger.debug("Instance turned into {0}".format(instance)) 
            tupy.Interpreter.logger.debug("Parent: {0} with subscript {1}".format(target_data, target_subscript))          
            if is_subscripted:
                self.updateChildren(target_data, target_subscript, target_depth, instance)
                full_data.update_size(deep=True)
            else:
                tupy.Interpreter.memWrite(self.data[(name, depth)], instance)
            return True
        else:
            raise TypeError("Atribuição excede o espaço alocado!")

    def updateChildren(self, target_data, target_subscript, depth, instance):
        tupy.Interpreter.logger.debug("updateChildren(target_data={0}, target_subscript={1}, depth={2}, instance={3})".format(target_data, target_subscript, depth, instance))
        if depth == 0:
            if target_data.type == tupy.Type.Type.STRING:
                if target_subscript.isSingle:
                    orig_str = target_data.value
                    pos = target_subscript.begin
                    target_data.value = orig_str[:pos] + chr(instance.value) + orig_str[pos+1:]
                elif target_subscript.isWildcard:
                    target_data.value = instance.value
                else:
                    orig_str = target_data.value
                    pos_begin = target_subscript.begin
                    pos_end = target_subscript.end
                    target_data.value = orig_str[:pos_begin] + instance.value + orig_str[pos_end:]
            else:
                if target_subscript.isSingle:
                    tupy.Interpreter.memWrite(target_data.value[target_subscript.begin], instance)
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
                self.updateChildren(tupy.Interpreter.memRead(child), target_subscript, depth-1, tupy.Interpreter.memRead(inst_child))

    def deepMerge(self, target_value, source_value):
        tupy.Interpreter.logger.debug("deepMerge({0}, {1})".format(target_value, source_value))
        # Either the target_value or source_value would do as the updateLength, 
        # since they are guaranteed to be the same after processDimensions runs.
        updateLength = len(target_value)
        for ind in range(updateLength):
            child = tupy.Interpreter.memRead(target_value[ind])
            newchild = tupy.Interpreter.memRead(source_value[ind])
            if isinstance(child.value, list):
                self.deepMerge(child.value, newchild.value)
            else:
                tupy.Interpreter.memWrite(target_value[ind], newchild)
        tupy.Interpreter.logger.debug("Merged and became {0}".format(target_value))
        return target_value

    def fillOmittedSizes(self, name, subscripts):
        ret = subscripts
        target = len(self.subscriptlist[name])
        while len(ret) < target:
            ret.append(tupy.Subscript.Subscript(isWildcard=True))
        return ret        

    def __str__(self):
        ret = ""
        for key in self.data:
            (name, depth) = key
            # We shouldn't need to check this... TODO: Check why
            if name in self.datatype.keys() and \
                self.datatype[name] != tupy.Type.Type.FUNCTION:
                ret += str(key)
                ret += " -> "
                ret += str(self.data[key])
                ret += "\n"
        return ret

    def print_all_locals(self):
        ret = ""
        for key in self.data:
            (name, depth) = key
            if depth>0:
                ret += str(key)
                ret += " -> "
                ret += str(self.data[key])
                ret += "\n"
        return ret

