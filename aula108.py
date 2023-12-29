# Considerando duas listas de inteiros ou floats (listaA e listaB)
# Some os valores nas listas retornado uma nova lista com o valores somados:

# se uma lista for maior que a outra, a soma so vai cosiderar o tamanho da menor.
# exemplo:


# resultado
# lista_soma = [2, 4 , 6, 8]

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]


def soma_lista(lista1, lista2):
    result = []
    min_len = min(len(lista1), len(lista2))
    for i in range(min_len):
        result.append(lista1[i] + lista2[i])
    return result


print(soma_lista(lista_a, lista_b))


lista_soma = [x + y for x, y in zip(lista_a, lista_b)] # o segundo x, y esta desenpacotando
print(lista_soma)


# No exercício anterior, fizemos a soma de duas listas usando várias soluções diferentes.

# Uma delas foi usando zip para unir duas listas e utilizar list comprehension para fazer a conta:

lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)  # Saída: [22, 4, 6, 10, 55]
# O problema é que zip só une as listas até o tamanho da menor lista (como proposto no exercício).

# Uma outra possibilidade é usar zip_longest para capturar os valores da lista maior.

# A ideia é a mesma, veja:

from itertools import zip_longest
 
lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_soma)  # [22, 4, 6, 10, 55, 60, 70]
# Neste caso, usamos o "fillvalue" como 0 (zero), assim conseguimos capturar os valores restantes da lista maior, realizando contas, sem obter um erro em nosso programa.

# from random import randint
# numeros_mega=[]
# for numero in range(7):
#     numeros_mega .append(randint(0,60))
    
# print(numeros_mega)
