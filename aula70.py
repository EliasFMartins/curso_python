# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Cha ves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: srt, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: srt, int, float, bool, tuple
# Mutável: dict, list
pessoa = {
'nome': 'Elias',  
'sobrennome': 'F. Martins',
'idade': 18,
'altura': 1.8,
'endereços': [
    {'rua':'Tal tal', 'numero':178},
    {'rua':'Tal tal', 'numero':178}
]
}

# pessoa ={
#     'nome':'Elias'
# }

print(pessoa,type(pessoa))
print(pessoa['nome'])
for chave in pessoa:
    print(chave, pessoa[chave])