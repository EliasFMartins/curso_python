# @property - um getter no modo Pythônico
# getter - 8um método para obter um atributo
# modo Pythônico  - modo do python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um atributo
# 🤯🤯🤯
# Geralmente é usada nas seguintes situações:
#  - como getter
# - p;/evitar quebrar o código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que comecem com um ou 2 __ nao devem ser alterados de forma algumaaaaaa foira da classe

# Property  fazerm um methodo ficar como uma propriedade por isso o nome acredito eu
class Caneta:
    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        print('Property')
        return self._cor

    @cor.setter
    def cor(self, valor):
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


def mostrar(caneta):
    return caneta.cor


caneta = Caneta('Red')
print(caneta._cor)
caneta.cor = 'Draconico'
caneta.cor = 'Dorado'

print(caneta._cor)
print(caneta.cor_tampa)
caneta.cor_tampa = 'Black'
print(caneta.cor_tampa)