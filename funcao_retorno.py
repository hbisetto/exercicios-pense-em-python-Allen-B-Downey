
def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    elif x < y:
        return -1

primeiro = int(input("Qual o primeiro número?"))
segundo = int(input("Qual o segundo número?"))

retorno = compare(primeiro, segundo)
print(retorno)