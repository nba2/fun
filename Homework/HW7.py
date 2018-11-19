def inorder(l,key=None):
    if key is None:
        key = lambda x : x
    for i in range(len(l)-1):
        if key(l[i+1]) < key(l[i]):
            return False
    return True
