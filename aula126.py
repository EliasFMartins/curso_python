# Escopo da classe e de metodos da classe
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def acao(self):
        print(f'{self.nome} esta executando uma acao')
    
    def comendo(self, alimento):
        print(f'{self.nome} esta comendo {alimento}')
    
    def executar(self, *args, **kwargs):
      print(self.comendo(*args, **kwargs))
gepardo = Animal('Gepardo')
print(gepardo.nome)
gepardo.acao()
gepardo.comendo('comida ')
gepardo.executar('todin')