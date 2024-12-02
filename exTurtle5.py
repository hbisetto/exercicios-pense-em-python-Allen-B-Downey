import turtle
import math

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    print(f'A função arc chama a função polyline({t}, {n}, {step_length}, {step_angle})')
    polyline(t, n, step_length, step_angle)
        
def polyline(t, n, length, angle):
    print(f'Função polyline está sendo executada com os parâmetros({t}, {n}, {length}, {angle})')
    for i in range(n):
        t.fd(length)
        t.lt(angle)
        
#def polygon(t, n, length):
#    angle =  360.0 / n
#    polyline(t, n, length, angle)

def circle(t, r):
    print(f'A função circle chama a função arc({t}, {r}, 360)')
    arc(t, r, 360)

def various(t, n):
    print(f'Função various({t}, {n}) chama a função circle({t}, {n})')
    circle(t, n)
    circle(t, n * 2)
    circle(t, n * 4)
    
bob = turtle.Turtle()
n = 30
# polygon(bob, 50, 50)
print(f'Função __main__ chama a função various({bob}, {n})')
various(bob, n)
