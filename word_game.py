
def more_than_20():        
    fin = open('words.txt')
    for line in fin:
        if len(line) >= 20:
            word = line.strip()
            print(word)
    fin.close()
            
def has_no_e(word):
    if 'e' not in word:
        return True
    else:
        return False
    
def is_there_e():
    fin = open('words.txt')
    list_no_e = []
    count = 0
        
    for line in fin:
        word = line.strip()
        if has_no_e(word) and word != '':
            count += 1
            list_no_e.append(word)
    #print(list_no_e)
    fin.close()
    return list_no_e, count
    
def count_words():
    fin = open('words.txt')
    count = 0
    
    for line in fin:
        word = line.strip()
        count += 1
    
    fin.close()
    return count

def to_list(list_):
    for word in list_:
        print(word)    
        
def percent(total, part):
    percent = (int(part) * 100) / (int(total))
    return percent
            
# more_than_20()
# is_there_e()
# count_words()

no_e_list, count_no_e = is_there_e()
to_list(no_e_list)
print(f'Words without the letter "e" = {count_no_e}')
total_words = count_words()
print(f'Total words = {total_words}')

print('Calculating percent:')
percent = percent(total_words, count_no_e)
print(f'No "e" words represent {percent:.2f}% of the total words.')