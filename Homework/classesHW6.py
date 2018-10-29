# queue/stack class
# (c) 2018 noah andrew

__all__ = [ "queue", "stack" ]

class queue(object):

    __slots__ = [ '_lst' ]

    def __init__(self):
        """Initilizes the queue."""
        self._lst = []

    def enqueue(self, v):
        self._lst.append(v)

    def dequeue(self):
        a = self._lst[0]
        del self._lst[0]
        return a

class stack(object):

    __slots__ = ['_tup']

    def __init__(self):
        self._tup = ()

    def push(self, v):
        self._tup += (v,)

    def pop(self):
        a = self._tup[-1]
        self._tup = self._tup[:-1]
        return a

    @property
    def isEmpty(self):
        return len(self._tup) == 0
