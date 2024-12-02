def rotate_word(word, num):
    word_num = []
    word_lower = word.lower()
    for letter in word_lower:
        word_num.append(ord(letter))
    print(word_num)
    rotate(word_num, num)
    
def rotate(cod_num, num):
    new_list = []
    for number in cod_num:
        new_list.append(number - num)
    print(new_list) 
    caractere(new_list)

def caractere(cod_num):
    new_list = []
    print("New word: ")
    for number in cod_num:
        new_list.append(chr(number))
    for letter in new_list:
        print(letter, end="")

#def rotate_string(string, num):
#    for letter in string:
#        if isalpha(letter):
            
      
rotate_word('Henrique', 5)