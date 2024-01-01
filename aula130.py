# Exercicio - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instancias
# da classe com os dados salvos
# Faca em arquivos semparados.
import json
CAMINHO_ARQUIVO = 'aula130.json'


class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Elias', 'Martins')
p2 = Pessoa('Carla', 'Martins')
p3 = Pessoa('Emilia', 'Martins')

bd = [vars(p1), vars(p2), vars(p3)]


def fazer_o_dump():
    print('Fazer o dump')
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        json.dump(bd, arquivo, indent=2)


if __name__ == '__main__':
    print('Ele e o main')
    fazer_o_dump()
# traduzindo joguei db que sao os dados dentro de arquivo com a identacao 2
