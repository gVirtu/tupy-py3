import Argument as a
import Interpreter as ii
from Type import Type

_args_end = Type.NULL

class Function(object):
    def __init__(self, name):
        self.name = name
        self.argumentTree = {}

    def __repr__(self):
        return "F->{0}".format(str(self.argumentTree))

    def put(self, argumentList, returnType, code, builtIn=False):
        current_level = self.argumentTree

        if builtIn:
            codeIndex = code
        else:
            codeIndex = ii.Interpreter.registerCodeTree(code)

        for arg in argumentList:
            # If next argument is optional, we add the possibility to call the function without it.
            if arg.defaultValue is None:
                if arg.type == Type.TUPLE:
                    # Variadic
                    current_level[arg.type] = current_level
            else:
                current_level[_args_end] = (codeIndex, argumentList, returnType, builtIn)
            current_level = current_level.setdefault(arg.type, {})
            
        # Entry point for the function with all arguments
        current_level[_args_end] = (codeIndex, argumentList, returnType, builtIn)

    def get(self, callArgs):
        current_level = self.argumentTree
        for literal in callArgs:
            try:
                current_level = current_level[literal.get().roottype]
            except Exception:
                try:
                    current_level = current_level[Type.TUPLE]
                except Exception:
                    raise TypeError("Unexpected argument {0}!".format(literal.get().value))
        try:
            return current_level[_args_end]
        except Exception:
            raise TypeError("Missing arguments for function {0}!".format(self.name))


    def is_ambiguous(self, argumentList):
        # Trying to add argumentList to the possible signatures for function 'name'
        current_level = self.argumentTree

        for arg in argumentList:
            if arg.defaultValue is not None:
                if _args_end in current_level:
                    return True
            if arg.type not in current_level:
                return False
            current_level = current_level[arg.type]
        
        if _args_end in current_level:
            return True
        else:
            return False



    