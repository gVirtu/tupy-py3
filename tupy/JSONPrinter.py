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

    def trace(self, line, is_return=False):
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
            stack.append(self.process_stack_element(tupy.Interpreter.Interpreter.callStack.top(), True, heap))
        
        element["stack_to_render"] = stack

        tupy.Interpreter.Interpreter.outStream.seek(0)
        element["stdout"] = tupy.Interpreter.Interpreter.outStream.read()
        element["func_name"] = tupy.Interpreter.Interpreter.callStack.top().funcName

        self.format_heap(heap)
        element["heap"] = heap #self.format_heap(heap)
        element["line"] = line
        element["event"] = self.map_event_to_string(tupy.Interpreter.Interpreter.callStack.size(), 
                                                    is_return)

        # All done!
        self.data["trace"].append(element)

    # Encodes all non-function locals from a given context as references to
    # the trace heap. Stores the order in which the names appear session-wide.
    def scan_context_locals(self, context, locals_set, locals_order, heap):
        ret = {}
        for name, depth in context.locals.declaredDepth.items():
            if depth < context.depth:
                continue

            if context.locals.datatype[name] == tupy.Type.Type.FUNCTION:
                continue

            # Add to ordered_locals / globals
            if name not in locals_set:
                locals_set.add(name)
                locals_order.append(name)

            # Add to heap
            ret[name] = ["REF",
                            self.add_to_heap(heap, context.locals.data[(name, depth)]) ]
        return ret

    # Adds data from a memory cell to the global trace heap. The local heap
    # defines a subset of the global heap that is to be displayed at a certain step.
    def add_to_heap(self, heap, memoryCell):
        mcID = str(id(memoryCell))
        heap[mcID] = self.parse_memory_cell(memoryCell, heap)
        # heap.add(mcID)
        # if mcID not in self.globalHeap:
        #     ind = len(self.globalHeap)+1
        # else:
        #     (ind, _) = self.globalHeap[mcID]

        # self.globalHeap[mcID] = (ind, self.parse_memory_cell(memoryCell, heap))

        return mcID

    # Formats the output heap. To be rendered correctly, primitives need
    # to be in a HEAP_PRIMITIVE structure.
    def format_heap(self, heap):
        for k, v in heap.items():
            if (v[0] == "C_DATA"):
                #datatype = data[2]
                heap[k] = ["HEAP_PRIMITIVE", "primitivo", v]

    # Recursively extracts data from a memory cell and outputs the trace-ready
    # parsed data that goes into the heap. 
    def parse_memory_cell(self, memoryCell, heap):
        inst = memoryCell.data
        #print("Handling {0}".format(inst))

        if (inst.type == tupy.Type.Type.STRUCT):
            data = ["INSTANCE", inst.class_name]
            instLocals = inst.value.locals
            for name, depth in instLocals.declaredDepth.items():
                if depth == tupy.Interpreter.Interpreter.classContextDepth: 
                    attribute = []
                    subMemoryCell = instLocals.data[(name, depth)]
                    self.handle_submemory_cell(subMemoryCell, attribute, heap)  
                    attribute.append(name)
                    data.append(attribute)

        elif (inst.is_pure_array()):
            data = ["LIST"]
            for subMemoryCell in inst.value:
                self.handle_submemory_cell(subMemoryCell, data, heap)

        else: # Primitive data
            header = "C_DATA"
            address = str(id(inst))
            type_str = self.map_type_to_string(inst.type)
            value = inst.value
            data = [header, address, type_str, value]
        
        return data

    # Makes sure nested lists are stored separatedly
    def handle_submemory_cell(self, subMemoryCell, data_list, heap):
        subInst = subMemoryCell.data
        #print("Subhandling {0}, list is {1}".format(subInst, data_list))
        # Compound, link a REF.
        if (subInst.type == tupy.Type.Type.STRUCT or subInst.is_pure_array()):
            data_list.append(["REF", self.add_to_heap(heap, subMemoryCell)])
        else: # Primitive, just put the C_DATA inside the LIST
            data_list.append(self.parse_memory_cell(subMemoryCell, heap))

    def process_stack_element(self, context, is_highlighted, heap):
        stack_element = {}

        frame_id = id(context)
        if frame_id not in self.contextVars:
            self.contextVars[frame_id] = set()
            self.contextVarList[frame_id] = []

        stack_element["is_highlighted"] = is_highlighted
        stack_element["is_parent"] = False
        stack_element["parent_frame_id_list"] = []
        stack_element["encoded_locals"] = self.scan_context_locals(context, self.contextVars[frame_id], 
                                 self.contextVarList[frame_id], heap)
        stack_element["ordered_varnames"] = self.contextVarList[frame_id]
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
