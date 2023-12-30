# filter e um filtro funcional
def print_inter(iterador):
    print(*list(iterador),sep='\n')
    print()
    
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
novos_produtos = [
    p for p in produtos
    if p['preco'] > 10#dpois vc coloca a condicao
]
novos_produtos2 = list(filter(
    lambda p : p['preco']>10,
    produtos)
)
print_inter(novos_produtos)
print(*novos_produtos2,sep='\n')