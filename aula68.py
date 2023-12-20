"""
higher Order Functions
Funções de primeira classe
Closure e funções que retornam outras funções 
"""
def criar_saudacao (saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome} !'
    return saudar

s1 = criar_saudacao('bom dia')
s2 = criar_saudacao('boa Noite')
print(s1('Jao'))
print(s2("Bernadeth"))

for nome in ['Jao', 'Fernades', 'Kennety', 'Biscoitanio']:
    print( s1(nome))
    print( s2(nome))