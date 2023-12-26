# List comprehension em Python
# List comprehesion é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)
lista = [numero for numero in range(10)]
# print(lista)  
lista = [numero * 2 for numero in range(10)]
# print(lista)  
produtos = [
    {'nome':'p1','preco':20,},
    {'nome':'p2','preco':30,},
    {'nome':'p3','preco':40,},
    {'nome':'p4','preco':50,},
]
novos_produtos = [
    # {'nome': produto['nome'],'preco': produto['preco']*2} , #copia as chaves e faz alteracões
    {**produto, 'preco':produto['preco']*2}
    if produto['preco'] > 20 else {**produto}# copia tudo e rescreve um valor em especifico
    for produto in produtos
]
print(*novos_produtos, sep='\n')