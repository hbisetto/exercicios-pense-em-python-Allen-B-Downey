'''
rotate_string(string, number, op)
Ex:
rotate_string('Henrique', 5, 1)
5 = letter rotate 
a rotate 1 = b
a rotate 2 = c etc
op is 1 for cript
      2 for descript


'''

def string_to_code(letter):
    number = ord(letter)
    return number

def num_string(list_num, num):
    list_numbers = []
    for number in list_num:
        if isinstance(number, str) and number.startswith('[.') and number.endswith('.]'):
            list_numbers.append(number)
        else:
            list_numbers.append(int(number) - num)
    print(list_numbers)
    string_ok(list_numbers)

def string_ok(list_):
    list_converted = []
    print('String converted: ')
    for obj in list_:
        if isinstance(obj, str) and obj.startswith('[.') and obj.endswith('.]'):
            print(obj[2:-2], end="")
        elif obj == " ":
            print(" ", end="")
        else:
            print(chr(obj), end="")
    
def rotate_string(string, num, op):
   list_words = []
   
   #print(list_words)
   if op == 1:
       for letter in string.lower():
            if letter.isalpha():
                list_words.append(string_to_code(letter))
            else:
                list_words.append('[.' + letter + '.]')
       num_string(list_words, num) #criptografar
   elif op == 2:
       for letter in string.lower():
           if letter.startswith('[.') and letter.endswith('.]'):
               list_words.append('[.' + letter + '.]')
           elif letter == ' ':
               list_words.append(' ')
           else:
               list_words.append(string_to_code(letter))
       num_string_back(list_words, num)  #descriptografar
            
def num_string_back(list_num, num):
    list_numbers = []
    for number in list_num:
        if isinstance(number, str) and number.startswith('[.') and number.endswith('.]'):
            list_numbers.append(number)
        elif number == ' ':
            list_numbers.append(' ')
        else:
            list_numbers.append(int(number) + num)
    #print(list_numbers)
    string_ok(list_numbers)
      
rotate_string('Henrique 4523 ahsdushaud!', 5, 1)
rotate_string('c`imdlp` 4523 \cn_pnc\p_!', 5, 2) 
# I need to fix the problem with some characters like numbers and !
