# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Pessoa:
    cpf = 1234
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('Nao sai da class client')
        print(self.nome, self.__class__.__name__)


class Client(Pessoa):
    pass


class Aluno(Pessoa):
    pass


client = Client('Elias', 'Martins')
print(client.nome)
print(client.sobrenome)
client.falar_nome_classe()
print(client.cpf)
