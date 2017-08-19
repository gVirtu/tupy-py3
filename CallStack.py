from Context import Context
from Stack import Stack

class CallStack(Stack):
    def __init__(self):
        super(CallStack, self).__init__()
        self.push(Context())