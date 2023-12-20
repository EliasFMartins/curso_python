# Métodos úteis dos dicion´´arios em Python
# len - quantas chaves
# keys - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe 
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada(del)
# popitem - Apagao último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Elias -.- ',
    'sobrenome':'Fodão',
    'year':2050,
}
print(len(pessoa))# mostra quantidade de chaves
print(tuple(pessoa.keys()))# converte em tupla lista oque ce bota na frente e pega as chaves keys
print(tuple(pessoa.values()))# converte em tupla lista oque ce bota na frente e pega os values
print(tuple(pessoa.items()))# converte em tupla lista oque ce bota na frente e pega os values e as chaves

for chave, valor  in pessoa.items():
    print(chave,valor)
pessoa.setdefault('idade',None)
pessoa.get('year',2024)
print(pessoa['idade'])
# print(pessoa['year'])
print(pessoa.get('year',2024))#o get vai buscar o valor se n houver ele lanca o que vc passar
