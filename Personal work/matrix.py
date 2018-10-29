# class for matrices with included operations
# (c) 2018 noah andrew

class matrix(object):

    __slots__ = [ "_nrows", "_ncolumns", "dimensions", "_rows", "_rowentries" ]

    def __init__(self, nrows=3, ncolumns=3):
        self._nrows = nrows
        self._ncolumns = ncolumns
        self.dimensions = ("{}x{}".format(nrows,ncolumns))
        
