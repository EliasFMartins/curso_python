# Problema dos parametros mutaveis em funcoes Python
# def adiciona_clientes(nome, lista=[]):
#     lista.append(nome)
#     return lista
# para dados mutaveis o python sempre usa a mesma lista ao invez de criar uma nova a cada execucao
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista=[]
    lista.append(nome)
    return lista

#nesse caso foi modificado o parametro pro corpo da funcao pois o corpo sempre e executado novamente 
# assim sendo criando uma nova lista sempre q for none

cliente1 = adiciona_clientes('Elias')
adiciona_clientes('joana',cliente1)
print(cliente1)

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria',cliente2)
print(cliente2)