import os

def try_open(file):
    if os.path.isfile(file):
        fn = open(file, 'w')
    elif not os.path.isfile(file):
        fn = open(file, 'w')
    return fn

def sed(s1, s2, fn1, fn2):
    try:
        fn_ = open('palavras1.txt', 'r')
        ler = fn_.read()
        words = ler.split()
        # print(words)
        if s1.strip() in words:
            for word in words:
                if word == s1.strip():
                    indice = words.index(s1.strip())
                    words[indice] = s2
            
        fn2_ = try_open(fn2)
        words_string = ' '.join(words)
        fn2_.write(words_string)
        fn_.close()
        fn2_.close()
    except:
        print('Oh no, something went wrong')
        
sed('abacate', 'tamandua', 'palavras1.txt', 'palavras2.txt')