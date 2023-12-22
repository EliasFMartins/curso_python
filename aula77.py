# sets -  conjuntos em python (tipo set)
# Conjuntos são ensinados na matemática
# Represetados graficamente pelo diagrama de Venn
# Sets em python são mutáveis, porém aceitam apenas 
# tipós imutáveis como valor interno

# criando um set 
# set (iterável) ou {1,2,3}
s1 = set() # vazio
s1 = {'Elias',1,2,3}
print(s1)
# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - eles não tem índixes;
# - eles não garatem ordem;
# - eles sao iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard