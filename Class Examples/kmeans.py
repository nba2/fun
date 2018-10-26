# A clustering data structure implementing k-means
# (c) 2018 noah andrew

from random import randint

__all__ [ "KMeans" ]

def fdist(a,b):
    return abs(a-b)

def meanf(s):
    return sum(s)/len(s)

class KMeans(object):
    """An implementation of k-means clustering. Typical use:
    data = [ randint(0,1000000) for _ in range (1000) ]
    cl = KMeans(data, k = 10)
    for rep in cl.means():
        print ("Cluster {}:".format(rep))
        for value in cl.cluster(rep):
            print("  {}".format(value))
    """

    __slots__ = [ "_means", "_k", "_clusters", "_distf", "_meanf", "_data" ]

    def __init__(self, data, k = 5, distf = None, meanf = None):
        self._distf = fdist if distf is None else distf
        self._meanf = fmean if meanf is None else meanf
        self._k = k
        self._data = list(data)
        self._cluster()

    def _pickMeans(self):
        """Select k "representative values" from the data."""
        n = len(self._data)
        locations = []
        means = []
        for _ in range(self._k):
            loc = randint(0,n-1)
            while loc in locations:
                loc = randint(0,n-1)
            locations.append(loc)
            means.append(self._data[loc])
        return means

    def _findClosest(self, value):
        min = 0
        for ind in range (self._k):
            rep = self._means[ind]
            if self._distf(rep, value) < self._means[min]:
                min = ind
        return self._means[min]

    def _classify(self):
        for value in self._data:
            rep = self._findClosest(value)
            self._cluster[rep].append(value)

    def _cluster(self):
        self._means = self.pickMeans()
        for _ in range(10):
            self._classify()
            self._adjustMeans()

if __name__ == "__main__":
    data = [ randint(0,1000000) for _ in range(1000) ]
    cl = KMeans(data, k = 10)
    for rep in cl.means():
        print("Cluster {}:".format(rep))
        for value in cl.cluster(rep):
            print("  {}".format(value))
    # rep = cl.classify(value)
