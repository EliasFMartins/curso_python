# groupby - agrupando valores (itertools)
from itertools import groupby

alunos =[
    {'nome': 'Luiz', 'nota':'A'},
    {'nome': 'Leticia', 'nota':'B'},
    {'nome': 'Fabricio', 'nota':'A'},
    {'nome': 'Rosemary', 'nota':'C'},
    {'nome': 'Cremilda', 'nota': 'D'},
    {'nome': 'Joana', 'nota': 'A'},
    {'nome': 'Joao', 'nota': 'B'},
    {'nome': 'Andre', 'nota': 'A'},
    {'nome': 'Anderson', 'nota':'C'},
]
# print((lambda x, y : x + y)(3,5))
# alunos_agrupados = sorted(alunos, key=lambda a: a['nota'])#copia raza, precisa do parametro
# print(*alunos, sep='\n')
# alunos = [
#     'a','a','a','a','a','b','c'
# ]
# grupos = groupby((alunos))# os Dados precisam estar ordenados com sorted ou sort
def ordena(aluno):
    return aluno['nota']
alunos_agrupados = sorted(alunos, key=ordena)  
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:# separa por valores os grupos
    print(chave)
    for aluno in grupo:
        print(aluno)

