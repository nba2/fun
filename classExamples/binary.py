def bs(d,v):
    low = 0
    high = len(d)
    while low < high:
        mid = (low+high)//2
        if v <= d[mid]:
            high = mid
        else:
            low = mid+1
    return low
