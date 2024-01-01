# Relações entre classes: associação, agregação e composição
# Composicao e uma especializacao da agregacao.
# Mas nela, quando o objeto 'Pai' for apagado, todas
# as referencias dos objetos filhos tbm sao apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print('Apagando', self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('Apagando', self.rua, self.numero)


cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Av dos coqueiros', 54)
cliente1.inserir_endereco('chapadinha', 5284)

print(cliente1.enderecos[0].rua)
print(cliente1.enderecos[1].rua)

endereco_externo = Endereco('Av Saudade', 1231245)
cliente1.inserir_endereco_externo(endereco_externo)
cliente1.listar_enderecos()
del cliente1  # quando apaga client o edereco vai de base tbm
print('#'*50)
