__all__ = ["LinkedList"]

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

    def pop(self,i):
        """Return and remove the ith item after self."""
        if i == 0:
            return (self.value,self.next)
        else:
            v,n = self.next.pop(i-1)
            self.next = n
            return (v,self)

    def reverse(self,newNext=None):
        """Reverse a list of elements."""
        oldNext = self.next
        self.next = newNext
        if oldNext is None:
            return self
        else:
            return oldNext.reverse(self)

    def orderedInsert(self,v):
        """Inserts v in ordered list, returns new list."""
        if v <= self.value:
            return Element(v,self)
        elif not self.next:
            self.next = Element(v)
            return self
        else:
            self.next = self.next.orderedInsert(v)
            return self

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

    def last(self):
        if self.next == None:
            return self
        else:
            return self.next.last()

    def sum(self):
        if self.next == None:
            return self.value
        else:
            return self.value + self.next.sum()

    def __contains__(self,v):
        if self.value == v:
            return True
        return (v in self.next) if self.next is not None else False

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

    def __contains__(self,v):
        return v in self._head if self._head else False

    def pop(self,i=None):
        """Remove and return element i."""
        if i is None:
            i = len(self)-1
        v,self._head = self._head.pop(i)
        return v

    def __delitem__(self,i):
        """Remove element i."""
        _ = self.pop(i)

    def reverse(self):
        """Reverse the list."""
        if self._head is not None:
            self._head = self._head.reverse()

    def __iter__(self):
        """Iterate across the elements of l."""
        current = self._head
        while current:
            yield current.value
            current = current.next


    def sort(self):
        """Sort a list of values."""
        newList = None
        for item in self:
            if newList is None:
                newList = Element(item)
            else:
                newList = newList.orderedInsert(item)
        self._head = newList

    def __str__(self):
        """Print this list."""
        results = [ str(v) for v in self ]
        return '[' + (', '.join(results)) + ']'

    def __repr__(self):
        """Compute representation of list."""
        return "LinkedList({!s})".format(self)

if __name__ == "__main__":
    from random import randint
    l = LinkedList([randint(0,100) for _ in range(20)])
    print(l)
    l.sort()
    print(l)
