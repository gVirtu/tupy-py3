import Instance as im
import Type as tm

class Subscript(object):
    def __init__(self, begin=0, 
                       end=0, 
                       isWildcard=False):
        self.begin = begin
        self.end = end
        self.isWildcard = isWildcard