def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    tamanho = len(word)
    if first(word) == last(word):
        for i in range(2, tamanho): 
            if not word[i] == word[-i]:
                break
        print("Is palindrome")
    else:
        print('Is not palindrome')

is_palindrome('asaaddaasa')