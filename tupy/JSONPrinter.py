import tupy.Interpreter
import json
import copy
import tupy.Type

class JSONPrinter(object):
    def __init__(self, codeString):
        self.globalVars = set()
        self.globalVarList = []
        self.contextVars = {}
        self.contextVarList = {}
        self.data = {"code": codeString, "trace": []}
        self.globalHeap = {}
        self.lastContextCount = 1

    def dump(self):
        return json.dumps(self.data, indent=None)

    def trace(self, line, returnData=None, exception=None):
        tupy.Interpreter.logger.debug("----------------TRACE----------------")
        element = {}
        heap = {}

        element["globals"] = self.scan_context_locals(tupy.Interpreter.Interpreter.callStack.items[0], self.globalVars, 
                                 self.globalVarList, heap)
        element["ordered_globals"] = copy.copy(self.globalVarList)

        stack = []

        it_callstack = iter(tupy.Interpreter.Interpreter.callStack.items[:-1]) # all except top frame
        try:
            next(it_callstack) # except global frame as well
            for context in it_callstack:
                stack.append(self.process_stack_element(context, False, heap))
        except StopIteration as e:
            pass

        if (tupy.Interpreter.Interpreter.callStack.size() > 1):
            # process highlighted frame
            stack.append(self.process_stack_element(tupy.Interpreter.Interpreter.callStack.top(), True, heap, returnData))
        elif returnData:
            if (self.instance_is_compound(returnData)): rd = ["REF", self.add_to_heap(heap, returnData)]
            else: rd = self.parse_instance(returnData, heap)

            element["globals"]["__return__"] = rd
            element["ordered_globals"].append("__return__")
        
        element["stack_to_render"] = stack

        tupy.Interpreter.Interpreter.outStream.seek(0)
        element["stdout"] = tupy.Interpreter.Interpreter.outStream.read()
        element["func_name"] = tupy.Interpreter.Interpreter.callStack.top().funcName

        if element["func_name"].startswith("Construtor de"):
            # Hack to slightly improve visualization: any constructor would have an empty
            # instance context pop up above it which turns the line step harder to understand
            del stack[-2]

        self.format_heap(heap)
        element["heap"] = heap #self.format_heap(heap)
        element["line"] = line
        if (exception):
            element["event"] = "exception"
            element["exception_msg"] = exception
        else:
            element["event"] = self.map_event_to_string(tupy.Interpreter.Interpreter.callStack.size(), 
                                                    returnData is not None)

        # All done!
        self.data["trace"].append(element)

    # Encodes all non-function locals from a given context as references to
    # the trace heap. Stores the order in which the names appear session-wide.
    def scan_context_locals(self, context, locals_set, locals_order, heap):
        ret = {}
        for name in sorted(context.locals.declaredDepth.keys()):
            depth = context.locals.declaredDepth[name]
            if context.structName is None and depth < context.depth:
                continue

            if context.locals.datatype[name] == tupy.Type.Type.FUNCTION:
                continue

            heap_ind = self.add_to_heap(heap, context.locals.data[(name, depth)].data)

            if name not in locals_set:
                locals_set.add(name)
                locals_order.append(name)

            # Add to heap
            ret[name] = ["REF", heap_ind]

        return ret

    # Adds data from a memory cell to the global trace heap. The local heap
    # defines a subset of the global heap that is to be displayed at a certain step.
    def add_to_heap(self, heap, instance):
        iid = id(instance)
        if iid not in self.globalHeap:
            self.globalHeap[iid] = str(len(self.globalHeap)+1)
        
        ind = self.globalHeap[iid]
        heap[ind] = self.parse_instance(instance, heap)
        # heap.add(mcID)
        # if mcID not in self.globalHeap:
        #     ind = len(self.globalHeap)+1
        # else:
        #     (ind, _) = self.globalHeap[mcID]

        # self.globalHeap[mcID] = (ind, self.parse_memory_cell(memoryCell, heap))

        return ind

    # Formats the output heap. To be rendered correctly, primitives need
    # to be in a HEAP_PRIMITIVE structure.
    def format_heap(self, heap):
        for k, v in heap.items():
            if (v and v[0] == "C_DATA"):
                #datatype = data[2]
                heap[k] = ["HEAP_PRIMITIVE", "primitivo", v]

    # Recursively extracts data from an instance and outputs the trace-ready
    # parsed data that goes into the heap. 
    def parse_instance(self, inst, heap):
        tupy.Interpreter.logger.debug("PARSE_INSTANCE {0}".format(inst))
        if (inst.type == tupy.Type.Type.STRUCT):
            header = "C_STRUCT"
            address = str(id(inst))
            data = [header, address, inst.class_name]
            instLocals = inst.value.locals
            tupy.Interpreter.logger.debug("Here's a {0}: {1}".format(inst.class_name, inst.value))
            for (name, depth) in sorted(instLocals.data.keys()):
                tupy.Interpreter.logger.debug("Found {0} at depth {1}".format(name, depth))
                if depth >= tupy.Interpreter.Interpreter.instContextDepth and \
                   instLocals.datatype[name] != tupy.Type.Type.FUNCTION: 
                    attribute = []
                    subMemoryCell = instLocals.data[(name, depth)]
                    attribute.append(name)
                    #print("ADDED NAME = {0} DEPTH = {1}".format(name, depth))
                    self.handle_submemory_cell(subMemoryCell, attribute, heap)  
                    data.append(attribute)
                #else:
                    #print("WELP, NAME = {0} DEPTH = {1} WAS NOT ADDED".format(name, depth))

        elif (inst.is_pure_array()):
            data = ["LIST"]
            for subMemoryCell in inst.value:
                self.handle_submemory_cell(subMemoryCell, data, heap)

        elif (inst.type == tupy.Type.Type.TUPLE):
            data = ["TUPLE"]
            for subMemoryCell in inst.value:
                self.handle_submemory_cell(subMemoryCell, data, heap)

        else: # Primitive data
            header = "C_DATA"
            address = str(id(inst))
            type_str = self.map_type_to_string(inst.type)
            if (inst.type == tupy.Type.Type.NULL):
                value = "<NULL>"
            else:
                value = inst.value
            data = [header, address, type_str, value]
        
        return data

    # Makes sure nested lists are stored separatedly
    def handle_submemory_cell(self, subMemoryCell, data_list, heap):
        subInst = subMemoryCell.data
        #print("Subhandling {0}, list is {1}".format(subInst, data_list))
        # Compound, link a REF.
        if (self.instance_is_compound(subInst)):
            data_list.append(["REF", self.add_to_heap(heap, subMemoryCell.data)])
        else: # Primitive, just put the C_DATA inside the LIST
            data_list.append(self.parse_instance(subMemoryCell.data, heap))

    def instance_is_compound(self, instance):
        return instance.type == tupy.Type.Type.STRUCT or \
               instance.type == tupy.Type.Type.TUPLE or \
               instance.type == tupy.Type.Type.ARRAY

    def process_stack_element(self, context, is_highlighted, heap, returnData=None):
        stack_element = {}

        frame_id = id(context)
        unique_id = (frame_id, returnData is None)
        if unique_id not in self.contextVars:
            self.contextVars[unique_id] = set()
            self.contextVarList[unique_id] = []

        stack_element["is_highlighted"] = is_highlighted
        stack_element["is_parent"] = False
        stack_element["parent_frame_id_list"] = []
        stack_element["encoded_locals"] = self.scan_context_locals(context, self.contextVars[unique_id], 
                                 self.contextVarList[unique_id], heap)
        stack_element["ordered_varnames"] = copy.copy(self.contextVarList[unique_id])
        if is_highlighted and returnData:
            if (self.instance_is_compound(returnData)): rd = ["REF", self.add_to_heap(heap, returnData)]
            else: rd = self.parse_instance(returnData, heap)

            stack_element["encoded_locals"]["__return__"] = rd
            stack_element["ordered_varnames"].append("__return__")
        stack_element["is_zombie"] = False
        stack_element["frame_id"] = frame_id
        stack_element["func_name"] = context.funcName
        stack_element["unique_hash"] = "{0}_{1}".format(stack_element["func_name"], 
                                                        stack_element["frame_id"])

        return stack_element


    def map_event_to_string(self, contextCount, is_return):
        if contextCount > self.lastContextCount: 
            self.lastContextCount = contextCount
            return "call"
        elif is_return:
            return "return"
        else:
            return "step_line"
        # if (is_call): return "call"
        # elif tupy.Interpreter.Interpreter.flow == tupy.Interpreter.FlowEvent.RETURN: return "return"
        # else: return "step_line"

    def map_type_to_string(self, type):
        return {
            tupy.Type.Type.INT: "inteiro",
            tupy.Type.Type.FLOAT: "real",
            tupy.Type.Type.CHAR: "caracter",
            tupy.Type.Type.STRING: "cadeia",
            tupy.Type.Type.BOOL: "lógico",
            tupy.Type.Type.NULL: "nulo",
            tupy.Type.Type.STRUCT: "estrutura"
        }.get(type, "???")
