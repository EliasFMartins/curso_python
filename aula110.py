# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutção - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product

def print_iter(interator):
    print(*list((interator)),sep='\n')
    print()
pessoas = [
    'João',  'Joana', 'Elias', 'Letícia'
]
camisetas = [
    ['preta', 'branca'],
    ['p','m','g'],
    ['masculino','feminino']
]
print_iter(combinations(pessoas, 2))
print_iter(permutations(pessoas, 2))

print_iter(product(*camisetas))
# interadores  precisa usar o for ou uma lista
#* foi pra desetruturar meio q abrir o array