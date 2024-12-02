# As funções daqui foram escritas a partir dos exercícios da página 139
# As funções anteriores foram utilizadas nos próprios scripts
# Para utilizar estas funções: import [nome_do_script sem '.py'] e chamar a função
import os

def nested_sum(list_):
    soma = 0
    for i in list_:
        for item in i:
            soma += item
    return soma

def cumsum(list_):
    soma_elementos = 0
    nova_lista = []
    for i in list_:
        if i is list_[0]:
            soma_elementos = i
            nova_lista.append(i)
        else:
            result = soma_elementos + i
            soma_elementos += i
            nova_lista.append(result)
    return nova_lista

def histogram(s):
    #Histogarm é um termo estatístico para uma coleção de contadores (ou frequências).
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def print_hist(h):
    for c in h:
        print(c, h[c])
        
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v: 
            return k
    raise LookupError('value does not appear in the dictionary')
    
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse
# Para debug:
# h = histogram('Henrique Bisetto')
# print(invert_dict(h))

def fibonacci(n):
    # if n == 0: 
    #     return 0
    # elif n == 1:
    #     return 1
    # else:
    #     return fibonacci(n-1) + fibonacci(n-2)
    # A versão acima fica lenta a medida que o número aumenta
    # Para isso, usar a versão abaixo
    known = {0:0, 1:1}
    if n in known:
        return known[n]
    
    res = fibonacci(n - 1) + fibonacci(n - 2)
    known[n] = res
    return res

def min_max(t):
    return min(t), max(t)

def printall(*args):
    print(args)
    
def sumall(*args):
    resultado = 0
    for arg in args:
        resultado += arg
    return resultado

def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False

def process_file(filename):
    hist = dict()
    fp = open(filename)
    for line in fp:
        process_line(line, hist)
    return hist

def process_line(line, hist):
    line = line.replace('-', ' ')
    
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1
    
def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)
            
