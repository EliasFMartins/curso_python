# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 'Eduarda', 'Flavinha', 'IsabellaS2']
tupla = 'python', 'é', 'Legal'

# a,b,c = lista
a, b, *_, S2 = lista
# operador *_ indica que vc esta pegando o resto da lista   se vc colocar alguma coisa dps do resto ele pegara o ultimo valor  e assim por diante
# for nome in lista:
#     print (nome, end=' ')
print(*lista) # intera com os elementos e deixa o nome apenas
print(lista)