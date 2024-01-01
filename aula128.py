# Atributos de classe
class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('Elias',28)
print(p1.get_ano_nascimento())