# Dictionary comprehension e set comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria':'Escritório',
}

dc = {
    chave: valor
    if isinstance(valor, (int, float)) else valor.upper()#deu erro pois tem um numero no produto e  feito a verificação pelo 
    #isintace passa o valor e verifica se o mesmo e uma string caso nao seja recebe o valor 
    for chave, valor in produto.items()
    if chave != 'categoria'# FUNCIONA COMO FILTER SO INCLUE SE FOR CATEGORIA 
}
print(dc)

s1 = {i for i in range (10)}
print(s1)