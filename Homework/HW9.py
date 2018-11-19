class Tree(object):

    __slots__ = [ "_value", "_left", "_right" ]

    def __init__(self, value, left=None, right=None):
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

    def __len__(self):
        if (self.right is None) and (self.left is None):
            return 1
        elif self.right is None:
            return 1 + len(self.left)
        elif self.left is None:
            return 1 + len(self.right)
        else:
            return 1 + len(self.right) + len(self.left)

    @property
    def sum(self):
        if (self.right is None) and (self.left is None):
            return self.value
        elif self.right is None:
            return self.value + self.left.sum
        elif self.left is None:
            return self.value + self.right.sum
        else:
            return self.value + self.right.sum + self.left.sum
