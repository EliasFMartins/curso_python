"""
Lista em Python 
Tipo List -  Mutável
Suporta vários valores de qualquer tipo 
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del,, clear, extend, +
"""
number_list = [10, 20, 30, 40]
number_list[2] = 300
#methodo para deletar um elemento da lista  no entanto mudar o index de todos os  demais  consome muito processamento
del number_list[2]
print(number_list)
print(number_list[2]) 
number_list.append(50) # added to end of list
print(number_list)
number_list.pop(2) 

# remove element from list end or remove element from list with index with parameter pop( parameter )
ultimo_valor = number_list.pop(   ) # remove the  last element from list and return it
print(ultimo_valor)
print(number_list)
# if list is very large avoid removing element from start and mid point for avoid cossuming processament power