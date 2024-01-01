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
    def __init__(self,nome, sobrenome) :
        self.nome = nome
        self.sobrenome = sobrenome
        pass



p1  = Pessoa('Elias', 'Martins')

print(p1.sobrenome)
print(p1.nome)

# p2  = Pessoa()

