
def swap(l,left,right):
    l[left],l[right] = l[right],l[left]
    
def bubble(l,key=None):
    """Sort by bubbling up maximum values, *in place*.

    >>> l = [3,7,9,6,22,-4,83.5]
    >>> sl = sorted(l)
    >>> bubble(l)
    >>> sl == l
    True
    >>> empty = []
    >>> bubble(empty)
    >>> empty == []
    True
    """
    if key is None:
        key = lambda x : x
    n = len(l)
    sorted = 0
    while sorted < n-1:
        swapped = False
        # perform a pass of finding the max:
        for left in range(0,n-sorted-1):    # number of values: n-sorted; nu. of compares n-sorted-1
            right = left+1
            if key(l[left]) > key(l[right]):
                swapped = True
                swap(l,left,right) # l[left],l[right] = l[right],l[left]
        # the maximum value is now clear to the right
        # we can reduce the problem
        sorted += 1
        if not swapped:
            break

def selectionSort(d,key=None):
    """A destructive sort of list d.
    Make several passes, each of which places the largest value into the
    rightmost free spot.

    >>> d = [3,7,9,6,22,-4,83.5]
    >>> sd = sorted(d)
    >>> selectionSort(d)
    >>> sd == d
    True
    >>> d = []
    >>> selectionSort(d)
    >>> d
    []
    """
    if key is None:
        key = lambda x : x # key is naturally ordered value
    n = len(d)
    sorted = 0
    while sorted < n-1:
        last = n - sorted - 1 # last possible location for current max
        maxLocation = 0
        for i in range(1,last+1):
            if d[maxLocation] <= d[i]:
                maxLocation = i
        swap(d,maxLocation,last)
        sorted += 1

def insertionSort(d,key=None):
    """A destructive sort of list d.
    Keep sorted values in the low indexed locations.  Then, make passes
    of pushing leftmost unsorted value into the sorted values into "natural"
    location.

    >>> d = [3,7,9,6,22,-4,83.5]
    >>> k = lambda x : -x
    >>> sd = sorted(d,key=k)
    >>> insertionSort(d,key=k)
    >>> sd == d
    True
    >>> d = []
    >>> insertionSort(d,key=k)
    >>> d
    []
    """
    if key is None:
        key = lambda x : x # key is naturally ordered value
    n = len(d)
    sorted = 1
    while sorted < n:
        i = sorted
        while (i > 0) and (key(d[i]) < key(d[i-1])):
            swap(d,i-1,i)
            i -= 1
        sorted += 1

def _partition(d, low, high):
    pivot = d[low]
    while low < high:
        # pivot is "on the left side" of the comparison
        while low < high and pivot <= d[high]:
            high -= 1
        if low < high:
            swap(d,low,high)
            low += 1
        # pivot is "on the right side" of the comparison
        while low < high and d[low] <= pivot:
            low += 1
        if low < high:
            swap(d,low,high)
            high -= 1
    return low # the final location of the pivot

def quicksort(d,low = None, high = None):
    low = low if low is not None else 0
    high = high if high is not None else len(d)-1
    n = high - low + 1
    if n >= 2:
        mid = _partition(d,low,high)
        quicksort(d,low,mid-1)
        quicksort(d,mid+1,high)

def mex(l):
    """Given a list, l, of non-negative values, return the smallest
    non-negative integer not in l --- the minimum excluded integer."""
    result = 0
    while result in l:
        result += 1
    return result

def test():
    from doctest import testmod
    testmod()
    
if __name__ == "__main__":
    test()
    from random import randint
    d = [ randint(0,99) for _ in range(4) ]

    
