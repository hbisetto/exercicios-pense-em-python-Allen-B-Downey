# Só devolve True se a palavra não tiver as letras a serem evitadas

def avoids(word, list_):
    for letter in word:
        if letter.lower() in list_:
            return False
    return True

def avoids_list(list_):
    fin = open('words.txt')
    for word in fin:
        if avoids(word, list_):
            print(word)
    fin.close()
        
lista = ['b', 'd', 'e', 'h']
palavra1 = "Henrique"
palavra2 = "jaca"

print(f"Executando a função avoids(word, list_) com {palavra1} e {lista}")
print(avoids(palavra1, lista))
print()
print(f"Executando a função avoids(word, list_) com {palavra2} e {lista}")
print(avoids(palavra2, lista))
print()
print("Ok. Agora vamos buscar as informações em uma lista com mais de mil palavras. Digite as 5 letras a serem evitadas:")
i = 0
lista2 = [] 
for i in range(5):
    letra = input(f'Qual a {i+1}ª letra?:')
    lista2.append(letra)
    i += 1
#print(lista2)
avoids_list(lista2)
    

            
            
            
    