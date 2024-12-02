
lista = []
dicionario = {}
dict_to_list = []
def list_letters(s):
    letters_list = []
    for letter in s:
        if letter != ' ' and letter != '\n':
            letters_list.append(letter)
    return letters_list

def count(s):
    words_count = {}
    for item in s:
        if item not in words_count:
            words_count[item] = 1
        elif item in words_count:
            words_count[item] += 1
    return words_count

def dict_to_list(d):
    global dicionario
    t = list(d.items())
    return t

def inverse(l):
    new_list = []
    for item, value in l:
        add = value, item
        new_list.append(add)
    return new_list
    
def criterio(tupla):
    return tupla[0]
    
def order(d):
    global dicionario
    ordenado = sorted(d, key=criterio, reverse=True)   
    return ordenado 

def count_word(s):
    return inverse(        
        order(
            inverse(
                dict_to_list(
                    count(
                        list_letters(s)
                        )
                    )
                )
            )
        )

def many_words(file):
    file2 = open(file, "r")
    global dicionario
    for word in file2:
        temp = count_word(word)
        for letter, value in temp:
            if letter not in dicionario.keys():
                dicionario[letter] = value
            elif letter in dicionario.keys():
                dicionario[letter] += value
    file2.close()
    #print(dicionario)

def order_many_words(path):
    global dicionario, dict_to_list
    many_words(path)
    dict_to_list = dict_to_list(dicionario)
    list_inversed = inverse(dict_to_list)
    list_ordered = order(list_inversed)
    list_reverse = inverse(list_ordered)
    return dict(list_reverse)

x = order_many_words('words.txt')
print(x)