import turtle

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360 / n)
    
lado = int(input('Quanto medirá cada lado?'))  
angulos = int(input('Quantos ângulos terá?'))

bob = turtle.Turtle()

polygon(bob, lado, angulos)
turtle.mainloop()