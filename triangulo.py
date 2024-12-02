import turtle

# Inicializa a tela e a tartaruga
t = turtle.Turtle()

# Define o lado do triângulo
lado = 100

# Desenha o triângulo equilátero
for _ in range(3):
    t.forward(lado)  # Move para frente o comprimento do lado
    t.left(120)      # Gira a tartaruga 120 graus para a esquerda

# Finaliza o desenho
turtle.done()