class Tree(object):
    """A simple implementation of a binary tree."""
    
    __slots__ = [ '_value', '_left', '_right' ]
    def __init__(self, value, left = None, right = None):
        self._value = value
        self._left = left
        self._right = right

    @property
    def value(self):
        return self._value

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def isLeaf(self):
        return (self._left is None) and (self._right is None)

    def __str__(self):
        return "<value={!s},left={!s},right={!s}>".format(self.value, self.left, self.right)

    def __repr__(self):
        result = [ "Tree({!r}".format(self.value) ]
        if self.left or self.right:
            result.append( ",{!r}".format(self.left) )
            if self.right:
                result.append( ",{!r}".format(self.right) )
        result.append(")")
        return "".join(result)
    
if __name__ == "__main__":
    t2 = Tree(2)
    t3 = Tree(3)
    t = Tree(1,t2,t3)
    print(repr(t))
