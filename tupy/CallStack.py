from tupy.Context import Context
from tupy.Stack import Stack
from tupy.Type import Type

class CallStack(Stack):
    def __init__(self):
        super(CallStack, self).__init__()
        self.push(Context(0, returnable=True, breakable=True, funcName="<module>"))
