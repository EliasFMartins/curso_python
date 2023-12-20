# get - obtém uma chave
# pop - Apaga um item com a chave especificada(del)
# popitem - Apagao último item adicionado

p1 = {
    'nome':'Elias',
    'sobrenome':'Martins',
    'removido':'coitado'
}
print(p1.get('nome'))# vem o nome se n tivesse veria por padrao None

print(p1.get('nome','Fodao'))
nome = p1.pop('nome')# remove a chave e retonar o valor que foi removido no caso Elias
print(nome)
print(p1)

nome2= p1.popitem()# remove a ultima chave e retonar o seu valor
print(nome2)
print(p1)


# p1.update({
#     'nome':'Novo Valor',#atualiza valor da chave ja existente
#     'idade':18 # cria uma nova chave com valor  caso nao exista
# })
# da pra usar assim tbm
p1.update(nome='novo valor', idade=30)
print(p1)

print(p1)