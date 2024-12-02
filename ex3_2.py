def do_twice(funcao, argumento):
    resultado = funcao(argumento)
    print_twice(f"A soma de {argumento} + {argumento} é igual a {resultado}")
    
def soma_duas_vezes(num):
    resultado = num + num
    # print(f"A soma de {num} + {num} é igual a {resultado}")
    return resultado

def print_twice(word):
    print(word)
    print(word)
    
def do_four(funcao, valor):
    do_twice(funcao, valor)
    do_twice(funcao, valor)


print("Função do_twice(): ")
do_twice(soma_duas_vezes, 5)

print("Função do_four(): ")
do_four(soma_duas_vezes, 10)
