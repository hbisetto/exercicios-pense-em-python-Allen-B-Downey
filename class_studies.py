class Animal:
    '''Represents an animal'''
    def emitir_som(self):
        print('Som do animal')
    def comer(self):
        print('Comendo')
    def dormir(self):
        print('Dormindo')

class Mamifero(Animal):
    def mamar(self):
        print('Mamando')

class Cachorro(Mamifero):
    def emitir_som(self):
        print('Latindo!!')
    
class Gato(Mamifero):
    def arranhar(self):
        print('Arranhando')
    
    def emitir_som(self):
        print('Miando!')
        
cao = Cachorro()
cao.emitir_som()
cao.comer()
cao.mamar()
print()
gato = Gato()
gato.emitir_som()
gato.arranhar()
gato.comer()
gato.mamar()
gato.dormir()