##(c) Noah Andrew 2018
from math import *
from random import randint
def sqrt(a):
    x = randint(0,5)
    while True:
        y = (x + a/x)/2
        if y == x:
            break
        x = y
    return x
def test_square_root(i):
    for a in range(1,i):
        estimate = sqrt(a)
        actual = math.sqrt(a)
        difference = abs(estimate-actual)
