from tupy.Context import Context
from tupy.Stack import Stack
from tupy.Type import Type

class CallStack(Stack):
    def __init__(self):
        super(CallStack, self).__init__()
        self.push(Context(0, returnable=True, breakable=True, funcName="<module>"))

    def lookup(self, name):
        storage_ctx = None
        for i, ctx in reversed(list(zip(range(len(self.items)), self.items))):
            if ctx.locals.hasKey(name):
                storage_ctx = ctx
                storage_index = i
                break
        if storage_ctx is None:
            raise NameError("O nome "+name+" não está definido!")
        return (storage_ctx, i)
