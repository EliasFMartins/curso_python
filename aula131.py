# Métodos de classe + factores (fábricas)
# São métodos onde 'self' será 'cls', ou seja
# ao invés de receber a instância no primeiro
# parâmetro, recebemos a própia classe.
class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    # basicamente chamando esse methodo ele ja seta a idade pra 50 anos e vc n precisa digitar

    @classmethod
    def criar_sem_nome(cls ):
        return cls('beterraba', 50)
    # basicamente chamando esse methodo ele ja seta a idade pra 50 anos e vc n precisa digitar


print(Pessoa.ano)
p1 = Pessoa('Biscoutwi', 32)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa.criar_sem_nome()
Pessoa.metodo_de_classe()  # pode chamar diretamente sem ter q instaciar nenhuma class
print(p2.nome, p2.idade,p3.nome,p3.idade)
