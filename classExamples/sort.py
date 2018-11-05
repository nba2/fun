
def swap(l,left,right):
    l[left],l[right] = l[right],l[left]

def bubble(l,key=None):
    if key is None:
        key = lambda x : x
    n = len(l)
    sorted = 0
    done = False
    while (sorted < n-1) and (not done):
        swapped = False
        for left in range(0,n-sorted-1):
            right = left+1
            if key(l[left]) > key(l[right]):
                swapped = True
                l[left],l[right] = l[right],l[left]
