# A clustering data structure implementing k-means
# (c) 2018 noah andrew

from random import randint

__all__ [ "KMeans" ]

class KMeans(object):
    pass

if __name__ == "__main__":
    data = [ randint(0,1000000) for _ in range(1000) ]
    cl = KMeans(data, k = 10)
    for rep in cl.means():
        print("Cluster {}:".format(rep))
        for value in cl.cluster(rep):
            print("  {}".format(value))
