import turtle
bob = turtle.Turtle()
def dotwice(a):
    a()
    a()
def dofour(a):
    dotwice(a)
    dotwice(a)
def move():
    bob.fd(100)
    bob.lt(90)
dofour(move)
turtle.mainloop()
