import turtle
def polygon(length, n1):
    t = turtle.Turtle()
    print(t)
    for i in range (n1):
        t.fd(length)
        t.lt(360/n1)
    turtle.mainloop()
l = float(input("What is the value for length? "))
n = int(input("How many sides does your polygon have? "))
polygon(l, n)
