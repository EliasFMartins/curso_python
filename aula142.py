# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
class MinhaString(str):
    def upper(self):
        print('CHAMOU UPPER')
        retorno = super(MinhaString, self).upper()
        print('DEPOIS DO UPPER')
        return retorno


string = MinhaString('Luiz')
print(string.upper())
# super() vc chama o methodo da super class tempoorariamente no caso chamaria metodos da str


class A:
    atributo_a = 'valor a'

    def __init__(self, value):
        self.value = value
    # esse methodo como os demais e passado pras class q herdaram como ele precisa de um parametro vai da erro em todos que chamarem sem parametro
    def methodo(self):
        print('A')


class B(A):
    atributo_b = 'valor b'

    def methodo(self):
        print('B')


class C(B):
    atributo_c = 'valor c'

    def methodo(self):
        # c, e self ja esta por padrao mesmo q n veja  o super vai busca o methodo acima que retorna print 'B'
        super(B, self).methodo()
        # c, e self ja esta por padrao mesmo q n veja  o super vai busca o methodo acima que retorna print 'B'
        super(C, self).methodo()
        # por padrao mesmo sem aparecer e o nome da class se eu colocar b ele vai busca o doa class acima no caso  class A

        # super e a super class em outras palavras de quem vc esta herdando as caracteristicas ele sempre busca o methodo de quem vc herdou as paradas
        print('C')


print(C.mro())  # mostra a cadeia em ordem
c = C()
print(C.atributo_a)
print(C.atributo_b)
print(C.atributo_c)
c.methodo()
