"""
lista de lista e seus indices
"""
salas = [
    ['Maria', 'Helena',],
    ['Elaine', 'Beatriz'],
    ['Tony', 'Cleitin',]
]

for sala in salas:
    print(sala)
    for aluno in sala:
        print(aluno)