# Méthodos úteis:
s1 =set()
s1.add('Elias')
#s1 .add(1,2)# so aceita 1 valor por vez e possivel mandar varias vezes seguidas
s1.add(1)
# s1.update('Olar mundo')#add mas fode com a poha toda vai letra por letra ao invez da palavra
s1.update(('Olar mundo',1,2,3,4))# passar em forma de tupla q e interavel resolve
# s1.clear()#Limpa o set
s1.discard('Olar mundo')# como não tem indice ele  compara o valor e remove o mesmo
# print(s1)
# add, update, clear, discard

# Operadores úteis:
# união | união(union) - Une
# interesecção & (intersection) - Itens  presentes em ambos
# diferença - Items presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estçao em ambos lados
s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 | s2 # ele une o sets os que tem valor igual vao pro krlh
s3 = s1 & s2 #retorna os items presentes em abos sets
s3 = s1 - s2 #retorna os itens disponiveis apenas no primeiro set no caso o da esquerda
s3 = s1 ^ s2 #retorna os itens  unicos de ambos os lados no caso o 1 e o 4
print(s3)