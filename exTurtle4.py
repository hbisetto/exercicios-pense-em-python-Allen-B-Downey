import turtle
import math

def polygon(t, n, length):
    for i in range(n):
        t.fd(length)
        t.lt(360 / n)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n 
    polygon(t, n, length)
    
    
bob = turtle.Turtle()

circle(bob, 20)
turtle.mainloop()