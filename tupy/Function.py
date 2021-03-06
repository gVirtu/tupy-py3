import tupy.Interpreter
from tupy.Type import Type

_args_end = Type.RESERVED

class Function(object):
    def __init__(self, name):
        self.name = name
        self.argumentTree = {}

    def __repr__(self): # pragma: no cover
        return "F->{0}".format(str(self.argumentTree))

    def put(self, context, argumentList, returnType, code, builtIn=False, isConstructor=False, overrideable=False):
        current_level = self.argumentTree
        depth = context.depth

        if builtIn:
            codeAST = code
        else:
            codeAST = FunctionAST(code)

        for arg in argumentList:
            # If next argument is optional, we add the possibility to call the function without it.
            if arg.defaultValue is None:
                if arg.type == Type.TUPLE:
                    # Variadic
                    current_level[arg.type] = current_level
            else:
                current_level[_args_end] = (codeAST, depth, argumentList, returnType, 
                                            builtIn, isConstructor, overrideable)
            current_level = current_level.setdefault(arg.type, {})
            
        # Entry point for the function with all arguments
        current_level[_args_end] = (codeAST, depth, argumentList, returnType, 
                                    builtIn, isConstructor, overrideable)

    def get(self, instArgs):
        current_level = self.argumentTree
        for inst in instArgs:
            try:
                current_level = current_level[inst.roottype]
            except Exception:
                try:
                    done = False
                    if (inst.roottype == Type.INT):
                        # Try to convert INT to FLOAT in case of failure
                        try:
                            current_level = current_level[Type.FLOAT]
                            done = True
                        except Exception:
                            pass
                    if (inst.roottype == Type.ARRAY):
                        # Workaround for empty array literals, assume int
                        try:
                            current_level = current_level[Type.INT]
                            done = True
                        except Exception:
                            pass
                    if not done:
                        current_level = current_level[Type.TUPLE]
                except Exception:
                    raise TypeError("Argumento inesperado {0}!".format(inst.value))
        try:
            return current_level[_args_end]
        except Exception:
            raise TypeError("Faltam argumentos para a função {0}!".format(self.name))


    def is_ambiguous(self, argumentList, depth):
        # Trying to add argumentList to the possible signatures for function 'name'
        current_level = self.argumentTree
        overrideable_index = 6 #ugly

        for arg in argumentList:
            if arg.defaultValue is not None:
                if _args_end in current_level:
                    if current_level[_args_end][1] >= depth:
                        return (not current_level[_args_end][overrideable_index])
            if arg.type not in current_level:
                return False
            current_level = current_level[arg.type]
        
        if _args_end in current_level:
            return current_level[_args_end][1] >= depth and \
                   not current_level[_args_end][overrideable_index]
        else:
            return False

    def merge(self, function):
        self.merge_recurse(self.argumentTree, function.argumentTree)

    def merge_recurse(self, myNode, copyNode):
        for ret_type in copyNode.keys():
            # As this is intended to be used with lower-depth functions,
            # it won't override anything from above.
            if ret_type == _args_end:
                if ret_type in myNode:
                    continue
                else:
                    myNode[ret_type] = copyNode[ret_type] # copy?
                    nextOwnNode = myNode[ret_type]
            else:
                nextOwnNode = myNode.setdefault(ret_type, {})
            nextCopyNode = copyNode[ret_type]

            # Variadic = infinite recursion depth
            if ret_type != Type.TUPLE and isinstance(nextCopyNode, dict):
                self.merge_recurse(nextOwnNode, nextCopyNode)

class FunctionAST(object):
    def __init__(self, block):
        self.block = block

    def get(self):
        return self.block

    def __deepcopy__(self, memo):
        # Never ever deepcopy ASTs otherwise things get really out of control
        return self
