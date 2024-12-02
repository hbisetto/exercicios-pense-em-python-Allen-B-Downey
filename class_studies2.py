
class Pneu:
    def __init__(self, tipo, tamanho):
        self.tipo = tipo
        self.tamanho = tamanho
        
    def calibrar(self):
        print(f'Pneu {self.tipo} de tamanho {self.tamanho} CALIBRADO.')
        
    def __str__(self):
        return f'Pneu {self.tipo}, tamanho {self.tamanho}'
    
class Motor:
    def __init__(self, potencia, status):
        self.potencia = potencia
        self.status = bool(status)
    
    def funcionando(self):
        if self.status:
            print('Motor funcionando.')
        else:
            print('Motor sem funcionar')
            
class Freios:
    def __init__(self, estado):
        self.estado = bool(estado)
        
    def conferir_freio(self):
        if self.estado:
            print('Freio ok')
        else:
            print('Freio não ok')
            
    def frear(self):
        if self.estado:
            print('Freando')
        else:
            print('Não foi possivel frear')
            
class Combustivel:
    def __init__(self, estado):
        self.estado = bool(estado)
        
    def encher(self):
        self.estado = True
        print('Combustível ok')
        
    def consumir(self):
        self.estado = False
        print('Combustível faltando, favor colocar')
        
class Carro:
    '''Formado por: pneus, motor, freios, combustivel'''
    def __init__(self, modelo, pneus, motor, freios, combustivel):
        self.modelo = modelo
        self.pneus = pneus
        self.motor = motor
        self.freios = freios
        self.combustivel = combustivel
        
    def partida(self):
        print('Tentando ligar o carro ', self.modelo)
        if self.motor.status and self.combustivel.estado:
            self.motor.funcionando()
        else: 
            print('Não foi possível dar a partida. Verificar combustível e motor')

    def __str__(self):
        pneus_str = ', '.join(str(pneu) for pneu in self.pneus)
        x = f'Carro de modelo {self.modelo}, Pneus: {pneus_str}, Status do motor: {self.motor.status}, Status dos freios: {self.freios.estado}, Status do combustível: {self.combustivel.estado}'
        return x
        
pneu1 = Pneu('d1', 17)
pneu2 = Pneu('d2', 17)
pneu3 = Pneu('t1', 18)
pneu4 = Pneu('t2', 18)

pneus = [pneu1, pneu2, pneu3, pneu4]

motor = Motor('7 cavalos', False)

freios = Freios(True)

combustivel = Combustivel(True)

carro1 = Carro('Celta', pneus, motor, freios, combustivel)
print(carro1)

carro1.motor.status = False

print(carro1)

print()

carro1.partida()
carro1.motor.status = True
carro1.partida()

carro1.combustivel.consumir()
carro1.partida()
carro1.combustivel.encher()
carro1.partida()