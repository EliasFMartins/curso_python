import json

# pessoa = {
#     'nome':'Elias',
#     'sobrenome':'F Martins',
#     'enderecos': [
#         {'rua':'R1','numero':22},
#         {'rua':'R2', 'numero':55}
#     ],
#     'altura':1.8,
#     'numero_preferido': (2,4,6,8,10),
#     'dev':True,
#     'nada':None
# }

# with open('aula117.json', 'w') as arquivo:#vai abrir com w e o json.dump( vai lancar o dicionario como json)
#     json.dump(
#         pessoa,
#         arquivo,
#         ensure_ascii=False, #padrao de codificacao
#         indent=2, # pra deixar o testo indentado no json
#         )

with open('aula117.json', 'r')  as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    print(pessoa['nome'])