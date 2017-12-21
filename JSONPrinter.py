import Interpreter as ii
import Type

class JSONPrinter(object):
    def __init__(self, codeString):
        self.globalVars = set()
        self.globalVarList = []
        self.contextVars = {}
        self.contextVarList = {}
        self.data = {"code": codeString, "trace": []}

    def trace(self, line, is_call=False):
        element = {}
        heap = {}

        element["globals"] = self.scan_context_locals(ii.Interpreter.callStack.items[0], self.globalVars, 
                                 self.globalVarList, heap)
        element["ordered_globals"] = self.globalVarList

        ii.Interpreter.outStream.seek(0)
        element["stdout"] = ii.Interpreter.outStream.read()
        element["func_name"] = ii.Interpreter.callStack.top().funcName #TODO: Resume from here
        element["heap"] = heap
        element["line"] = line
        element["event"] = self.map_event_to_string(is_call)

        # All done!
        self.data["trace"].append(element)

    def scan_context_locals(self, context, locals_set, locals_order, heap):
        ret = {}
        for name, depth in context.locals.declaredDepth.items():
            # Add to ordered_locals / globals
            if name not in locals_set:
                locals_set.add(name)
                locals_order.append(name)

                # Add to heap
                ret["name"] = ["REF",
                               self.add_to_heap(heap, context.locals.data[(name, depth)]) ]
        return ret

    def add_to_heap(self, heap, memoryCell):
        mcID = id(memoryCell)
        if mcID not in heap:
            ind = len(heap)+1
            heap[mcID] = (ind, self.parse_memory_cell(memoryCell, heap))
        else:
            (ind, _) = heap[mcID]
        return ind

    def parse_memory_cell(self, memoryCell, heap):
        inst = memoryCell.data

        if (inst.className is not None):
            data = ["INSTANCE", inst.className]
            instLocals = inst.value.locals
            for name, depth in instLocals.declaredDepth.items():
                if depth == ii.Interpreter.classContextDepth: 
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
            address = id(inst)
            type_str = self.map_type_to_string(inst.type)
            value = inst.value
            data = [header, address, type_str, value]
        
        return data

    def handle_submemory_cell(self, subMemoryCell, data_list, heap):
        subInst = subMemoryCell.data
        # Compound, link a REF.
        if (subInst.className is not None or inst.is_pure_array()):
            data_list.append(["REF", self.add_to_heap(self, heap, subMemoryCell)])
        else: # Primitive, just put the C_DATA inside the LIST
            data_list.append(self.parse_memory_cell(self, subMemoryCell, heap))

    def map_event_to_string(self, is_call):
        if (is_call): return "call"
        elif ii.Interpreter.flow == ii.FlowEvent.RETURN: return "return"
        else: return "step_line"

    def map_type_to_string(self, type):
        return {
            Type.Type.INTEGER: "inteiro",
            Type.Type.FLOAT: "real",
            Type.Type.CHAR: "caracter",
            Type.Type.STRING: "cadeia",
            Type.Type.BOOLEAN: "lógico",
            Type.Type.STRUCT: "estrutura"
        }.get(type, "???")
