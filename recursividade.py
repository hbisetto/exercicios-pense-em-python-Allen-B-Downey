# def countdown(n):
#     if n <= 0:
#         print('Blastoff!')
#     else:
#         print(n)
#         countdown(n - 1)
        
def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n - 1)
        
def do_n(funcao, n):
    if n <= 0:
        return
    funcao('Hello', 2)        
    do_n(funcao, n-1)
        
# countdown(30)
#print_n('Hello', 2)
do_n(print_n, 4)