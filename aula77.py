# sets -  conjuntos em python (tipo set)
# Conjuntos são ensinados na matemática
# Represetados graficamente pelo diagrama de Venn
# Sets em python são mutáveis, porém aceitam apenas 
# tipós imutáveis como valor interno

# criando um set 
# set (iterável) ou {1,2,3}
s1 = set() # vazio
s1 = {'Elias',1,2,3}
s1 = {1,2,3,3,4,5,5,1,2}# naturalmente eliniman valores duplicados
l1 = [1,2,36,3,3,3,1,2]
s2 = set(l1)# remove valores duplicados
l2 = list(s2) #converte pra lista novamente
s1 = set('Elias')# não garatem ordem g.g
s1 = {1,2,3,4,}# nao aceita dados mutaveis la dentro no caso arrays obj  e assim por diante

print(3 in s1) # verificar se tem o numero dentro do set
for numero in s1:
    print(numero)
# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - eles não tem índixes;
# - eles não garatem ordem;
# - eles sao iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard