class Subscript(object):
    def __init__(self, begin=0, 
                       end=0, 
                       isWildcard=False,
                       isSingle=False):
        self.begin = begin
        self.end = end+1
        if (self.end == 0): self.end = None
        self.isWildcard = isWildcard
        self.isSingle = isSingle

    def __repr__(self):
        if (self.isWildcard): return "*"
        elif (self.isSingle): return "{0}".format(self.begin)
        else: return "{0}..{1}".format(self.begin, self.end)
