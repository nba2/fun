__all__ = ["LinkeList"]

class Element(object):
    """A private class for holding data values."""
    __slots__ = [ "_value", "_nxt" ]

    def __init__(self, value, next = None):
        """Build an empty Element with a value; next optionally
           points to another element."""
        self._value = value
        self._nxt = next

    @property
    def value(self):
        """Value accessor method."""
        return self._value

    @property
    def next(self):
        """Next accessor method."""
        return self._nxt

    @next.setter
    def next(self,v):
        """Next mutator method."""
        self._nxt = v

    def __len__(self):
        """Compute the length of the list headed by self."""
        if self.next is None:
            return 1
        else:
            return 1 + len(self.next)
        
    def __getitem__(self,i):
        """Get the ith item after self."""
        if i == 0:
            return self.value
        else:
            return self.next[i-1]

    def __setitem__(self,i,v):
        """Set the ith item after self to v."""
        if i == 0:
            self._value = v
        else:
            self.next[i-1] = v

    def append(self,v):
        """Append this item to the end of list headed by self."""
        if self.next is None:
            self.next = Element(v)
        else:
            self.next.append(v)
            
    def __str__(self):
        """Print Elements of this list."""
        return "(value={!s},next={!s})".format(self.value,self.next)

    def __repr__(self):
        """Return representations of this list's elements."""
        return "Element({!r},next={!r})".format(self.value,self.next)
        

class LinkedList(object):
    """A linked-list alternative to lists."""
    __slots__ = [ "_head" ]

    def __init__(self,s):
        """Initialize list to empty."""
        self._head = None
        self.extend(s)

    def __len__(self):
        """Compute length of list."""
        if self._head is None:
            return 0
        else:
            return len(self._head)

    def __getitem__(self,i):
        """Get the ith element of list."""
        return self._head[i]

    def __setitem__(self,i,v):
        """Set the ith element of list to v."""
        self._head[i] = v

    def append(self,v):
        """Add v to end of list."""
        if self._head is None:
            self._head = Element(v)
        else:
            self._head.append(v)

    def extend(self,s):
        """Extend list by adding elements of s."""
        for item in s:
            self.append(item)

    def __iter__(self):
        """Iterate across the elements of l."""
        current = self._head
        while current:
            yield current.value
            current = current.next

    def __str__(self):
        """Print this list."""
        results = [ str(v) for v in self ]
        return '[' + (', '.join(results)) + ']'

    def __repr__(self):
        """Compute representation of list."""
        return "LinkedList({!s})".format(self)

if __name__ == "__main__":
        l = LinkedList(range(10))
        print(l)
