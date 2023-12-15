"""
Cuidados com dados mutáveis
= - copiando o valor (imutáveis)
= - aponta para o mesmo valor na menória ( mutável)
"""
nome = 'Luiz'
lista_a = ['Elias', 'The Fodão']
lista_b = lista_a.copy()
lista_a[0] = 'Pão com fejão'
print(lista_b)
lista = ['Gabriel alonbadinho', 'Elias The Fodão','Ademais']
lista.append('Froster')
indices = range(len(lista))
for indice in indices:
    print(indice,lista[indice])
    