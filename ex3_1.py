def rigth_justify(palavra):
    tamanho = len(palavra)
    tamanho -= 1
    
    espaco = 70 - tamanho
    
    print((" " * espaco) + palavra)
        
rigth_justify('Henrique')
