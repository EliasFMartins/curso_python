# Métodos em instâncias de classes Python
# hard coded - E algo que foi escrito diretamente no codigo

class Carro:
    def __init__(self, nome):
        self.nome = nome
    def acelerar(self):
        print(f'{self.nome} esta acelerando ...')
    
fusca = Carro('Fuskinha')
print(fusca.nome)
fusca.acelerar()