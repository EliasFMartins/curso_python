# Exercício - Unir listas
# Crie uma função zipper (como o ziper de roupas)
# O trabalho dessa função será unir duas listas na ordem.
# Use todos os valores da menor lista.
# ex.:
# ['Salvador','Ubatuba','Belo Horizonte']
# resutado
# [('Salvador', 'BA'),('Ubatuba','SP'),('Bello Horizonte','MG')]
# def zipper(lista1, lista2):

#     main_list = lista1 if len(lista1) < len(lista2) else lista2
#     return [ (item , lista2[indice] ) for indice, item in enumerate(main_list)]


l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

# resultado = zipper(l1, l2)
# print(resultado)

def zipper(lista1, lista2):
    #min pega o valor minimo
    #max pega o valor maximo
    intervalo_maximo = min(len(lista1), len(lista2))
    return[
        (lista1[i],lista2[i]) for i in range(intervalo_maximo)
    ]
print(zipper(l1,l2))
print (list(zip(l1,l2)))# faz a mesma coisa sem o list vai vir uma variavel na memoria com list meio q converte o valor
from itertools import zip_longest
print(list(zip_longest(l1,l2, fillvalue='Sem Cidade')))


