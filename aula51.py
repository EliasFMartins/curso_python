"""
enumerate - enumera iteráveis (índices)

"""
lista  = ['Maria', 'Helena', 'Luiz']
lista.append('João')
lista_enumerada = enumerate(lista)
lista_enumerada = list(enumerate(lista))
#basicamente retorna uma tupla com indece and values
print(lista_enumerada)# retorna uma lista com tuplas e chaves de index e valor 

for item in lista_enumerada:
    print(item)
    #depois de consumido os valores do inumerete os valores vão pra casa do krlh '-'
    #se tentar fazer outro for com lista_enumerada vai retornar nada pois ja foi consumido
    # a forma de usar ele e nao passando pra uma variavel e sim chamando o metodo toda vez q for feito 
    # o for  vai abrir uma nova instacia basicamente falando
for item in enumerate(lista): # versão extendida
    indice,nome = item
    print(indice,nome)
    
for indice,nome in enumerate(lista): # versão clean AKA mais usada
    print(indice,nome)