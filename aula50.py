"""
Tipo tupla - Uma lista imutável 

"""
# se não colocar os [] ja sera a tuple for stand
# nao e possivel reatribuir valores a tuple ela e mais rapida que a lista  no entanto nao permite reatribuição de valores
# e Imutavel
nomes = ['Maria', 'Hellena', 'Luiz'] #list
nomes = (tuple(nomes)) #convertendo list for tuple
nomes = list(nomes) #convertendo tuple for list
print(nomes)
print(nomes[1])
