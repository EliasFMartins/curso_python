from functools import partial
# map -  mapear dados


def print_inter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)


# round e para arredondar o valor
aumentar_dez_procento = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)
# novos_produtos = [
#     # {**p} for p in produtos # p para cada p in produtos literalmente
#     {**p, 'preco':aumentar_dez_procento(p['preco'])} for p in produtos # p e uma chave 'preco'  como a chave ja existia sobreescreve o valor da mesma para cada p in produtos literalmente
# ]


def muda_preco_de_produtos(produto):
    return {
        **produto,
        'preco': aumentar_dez_procento(
            produto['preco']
        )
    }


novos_produtos = map(muda_preco_de_produtos,produtos)
# print_inter(novos_produtos)
print(*list(novos_produtos),sep='\n')

print(list(map(
    lambda n :n*3,
    [1,2,3,4]
)))
#atencao e preciso usar lista pra converter em um interador tem algum que  fica esgotado  dps que chega ao maximo e n pode chamar d nv ex com console ja teria esgotado e daria erro