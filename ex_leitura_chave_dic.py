''' 
Dicionário com cada palavra da lista como chave
''' 
dic = {}
def lista_dicionario():
    fin = open('words.txt')
    print('Arquivo words.txt - aberto')
    count = 0
    for line in fin:
        word = line.strip()
        count +=1
        dic[word] = count
    fin.close()
    print('Operação 1 - leitura -> dicionário - ok')
    
def countains(word):
    if word in dic:
        print(f'There is a {word} in the list in words.txt')
    else:
        print(f'There is no {word} in the list words.txt')

lista_dicionario()
countains('abuzz')
countains('zymurgy')
countains('abacate')
