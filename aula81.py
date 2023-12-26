#Função lambda em python
#a função labda é uma funçao como qualquer 
#outra em python. Porém, são funções anônimas
#que contém apenas uma linha. Ou seja, tudo
#deve ser contido dentro de uma única
#expressão
lista = [
    {'nome': 'Luiz','sobrenome': 'Amirairanda'},
    {'nome': 'Maria','sobrenome': 'karaense'},
    {'nome': 'Bernadeth','sobrenome': 'bakeosu'},
    {'nome': 'Fraudinho','sobrenome': 'mnanimaa'},
    {'nome': 'Pistonho','sobrenome': 'Chorrong'},
] 

# lista = [4,2,1,3,5,4,6,8,7,9]
# lista.sort(reverse=True)#Ordena a lista reverse=True altera a ordem pra decrecente

def ordena(item):
    print(item)
    return item['nome'] #vai ordenar pela chave nome ordem alfabetica

# lista.sort(key=ordena)
# lista.sort(key=lambda item: item['sobrenome']) # basicamente uma funcao de uma linha ou anonima
# print(lista)
l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])
#sorted retorna um novo array
# lista.sort altera a ordem dos roles no proprio array
# retorna 2 lista cada uma ordenada por uma key diferente ex nome and sobrenome
print(l1)
print(l2)