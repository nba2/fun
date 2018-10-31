# A clustering data structure implementing k-means.
# (c) 2018

from random import randint

__all__ = [ "KMeans", "fdist", "fmean" ]

def fdist(a,b):
    """A distance function for float values."""
    return abs(a-b)

def fmean(s):
    """A Mean function for float values."""
    assert(s)
    return sum(s)/len(s)

class KMeans(object):
    """An implementation of k-means clustering.  Typical use:
    data = [ randint(0,1000000) for _ in range(1000) ]
    cl = KMeans(data, k = 10)
    for rep in cl.means():
        print("Cluster {}:".format(rep))
        for value in cl.cluster(rep):
            print("  {}".format(value))
    """
    __slots__ = [ "_means", "_k", "_clusters", "_distf", "_meanf", "_data" ]

    def __init__(self, data, k = 5, distf = None, meanf = None):
        """Load a cluster data into k clusters.  The distf and meanf
           functions, if not specified, default to distance and mean
           computations on floating point values."""
        self._distf = fdist if distf is None else distf
        self._meanf = fmean if meanf is None else meanf
        self._k = k
        self._data = list(data)
        # values we compute
        self._clusters = []
        self._cluster()

    def _pickMeans(self):
        """Select some initial means.  Here, we pick k random values from
        the original dataset.  We try to avoid repeats."""
        n = len(self._data)
        locations = []
        means = []
        for _ in range(self._k):
            loc = randint(0,n-1)
            while loc in locations:
                loc = randint(0,n-1)
            locations.append(loc)
            means.append(self._data[loc])
        self._means = means

    def _findClosest(self,value):
        """Find the cluster number that has a representative that is closest
           to value."""
        mindex = 0
        minDist = self._distf(value,self._means[0])
        for ind in range(1,self._k):
            d = self._distf(value,self._means[ind])
            if d < minDist:
                mindex = ind
                minDist = d
        return mindex

    def _classify(self):
        """For each data value, place it in a cluster which best represents
           it; all data in a cluster are closest to their representative."""
        self._clusters = [ [] for _ in range(self._k) ]
        for value in self._data:
            repIndex = self._findClosest(value)
            self._clusters[repIndex].append(value)

    def _adjustMeans(self):
        """Compute means based on the current clustering."""
        self._means = []
        for i in range(self._k):
            self._means.append(self._meanf(self._clusters[i]))

    def _cluster(self):
        """Iteratively find representative values, classify data and iterate."""
        self._pickMeans()
        self._classify()
        for _ in range(10):
            self._adjustMeans()
            self._classify()

    def means(self):
        return self._means.copy()

    def classify(self, value):
        repIndex = self._findClosest(value)
        return self._means[repIndex]

    def cluster(self,rep):
        if rep not in self._means:
            rep = self.classify(rep)
        return self._clusters[self._means.index(rep)]


if __name__ == "__main__":
    data = [ randint(0,1000000) for _ in range(1000) ]
    cl = KMeans(data, k = 10)
    for rep in cl.means():
        print("Cluster {}:".format(rep))
        for value in cl.cluster(rep):
            print("  {}".format(value))
     # rep = cl.classify(value)
