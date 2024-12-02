
''' 
1) Começar a contar as palavras somente após o cabeçalho
2) Contar o número total de palavras do livro e a quantidade que elas aparecem
3) Comparar livros diferentes 

'''
import string 

def process_file(filename):
    hist = dict()
    with open(filename, 'r', encoding='utf-8', errors='ignore') as fp:
        pos_cab = False
        for line in fp:
            if line.strip() == '*** START OF THE PROJECT GUTENBERG EBOOK DON QUIJOTE ***':
                pos_cab = True
                pass
            elif pos_cab:
                process_line(line, hist)
        return hist

def process_line(line, hist):
    line = line.replace('-', ' ')
    
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1

def count_words(dicionario):
    words = sum(dicionario.values())
    return words
  
def different_words(dicionario):
    return len(dicionario)

    
hist = process_file('../ebooks_txt/Don_Quijote.txt')
#print(hist)

print('Número total de palavras:')
print(count_words(hist))
print('Número de vezes que cada palavra aparece: ')
print(hist)
print('Número de palavras diferentes:')
print(different_words(hist))