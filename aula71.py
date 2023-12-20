# Manipulando chaves e valores em dicionários
pessoa = {
    
}
##
##
pessoa['nome'] = 'Elias Fodão'# criando chave no dicionario
pessoa['teste'] = 'testando'
print(pessoa['nome'])
print(pessoa)
del pessoa['teste'] #apagar um campo do dicionario no caso uma chave
print(pessoa)
#verificar se a chave não existir
if pessoa.get('nome',None):
    print('Existe')
    
if pessoa.get('nome') is None:
    print('Não Existe')
    