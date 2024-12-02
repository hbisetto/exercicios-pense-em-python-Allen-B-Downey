def b(z):
    print(f'b.Inicio da função b({z})')
    print(f'b.A variavel prod = a chamada da função a({z}, {z})')
    prod = a(z, z)
    print(f'b.A variável prod agora, após a chamada de a(z, z), vale = {prod}')
    print('b.Abaixo está impresso z, prod') 
    print(z, prod)
    print(f'b.E segue o return da funcao b(z) com o valor de prod = {prod}')
    return prod

def a(x, y):
    print(f'a.Chamada da função a({x},{y})')
    print(f'a.{x} = {x} + 1')
    x = x + 1
    print(f'a.Novo valor de x = {x}')
    print(f'a.O retorno da função será de {x} * {y}')
    print('a.', x * y)
    return x * y

def c(x, y, z):
    print('x = 1; y = 2.')
    print('Valores recebidos:')
    print(f'x = {x}, y = {y} e z = {z}')
    total = x + y + z
    print(f'A soma destes elementos é igual a = {total}')
    print('(Chamada da função b com parâmetro total) e o resultado de retorno será elevado a 2' )
    print('Ou seja square = b(total)**2')
    square = b(total)**2
    print(f'De volta  na função c, agora com o resultado de square = b(total)**2 igual a {square}')
    return square

x = 1
y = x + 1
print(c(x, y+3, x+y))