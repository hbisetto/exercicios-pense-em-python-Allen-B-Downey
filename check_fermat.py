'''
Checar se não é meso possível a**n + b**n = c**n (último teorema de Fermat)
'''

def check_fermat(a, b, c, n):
    if (a**n + b**n == c**n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work")

def conferir_n(n):
    if n <= 2:
        print(f'{n} menor do que 2. Favor digitar outro número.')
        novo_numero = int(input('Digite um número inteiro referente a "n": ')) 
    if novo_numero <= 2:
        conferir_n(novo_numero)
        
print('Conferindo o último teorema de Fermat.')
print('a**n + b**n = c**n, sendo n > 2, não é possível.')   
a = int(input('Digite um número inteiro referente a "a": '))
b = int(input('Digite um número inteiro referente a "b": '))
c = int(input('Digite um número inteiro referente a "c": '))    
n = int(input('Digite um número inteiro referente a "n": '))    

conferir_n(n)

check_fermat(a, b, c, n)
# checar antes se n é maior que 2
    