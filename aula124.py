# class - Casses sao moldes para criar novos objetos
# As classes geram novos objetos (instancias) que
# podem ter seus proprios atrubutos e metodos.
#Os objetos gerados pela classe podem usar seus dados
#internos para realizar varias acoes.
#por convecao usamos PascalCase para nomes de 
#classes
string ='Elias'
print(string.upper())
print(isinstance(string,str))

class Pessoa:
    ...
p1  = Pessoa()
p1.nome = 'Elias'
p1.sobrenome='Martins'


p2  = Pessoa()
p2.nome = 'Pao'
p2.sobrenome='Frances'
print(p1)
print(p1.nome)#atributo sempre  sem parenteses por serem dados
print(p1.sobrenome)

print(p2)
print(p2.nome)#atributo sempre  sem parenteses por serem dados
print(p2.sobrenome)