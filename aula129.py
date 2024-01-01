# __dict__ e vars para atributos de instancia
class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('Elias',28)
print(p1.__dict__)#todos os dados ficam visiveis dentro do __dict__
print(vars(p1))# vars faz a mema merda