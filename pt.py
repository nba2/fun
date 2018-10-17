# A class for storing 2d coordinates: (x,y)
# (c) noah andrew 2018

class Pt(object):
    __slots__ = [ "_x", "_y"]

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __eq__(self, other):
        return (self._x == other._x) and (self._y == other._y)

    def __str__(self):
        return "({},{})".format(self._x, self._y)

    def __repr__(self):
        return "Pt({},{})".format(self._x, self._y)
