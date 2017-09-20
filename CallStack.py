from Context import Context
from Stack import Stack
from Type import Type

class CallStack(Stack):
    def __init__(self):
        super(CallStack, self).__init__()
        self.push(Context(0, returnable=True))