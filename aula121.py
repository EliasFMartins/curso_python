# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar = )
# todo = [] -> lista de tarefas
# todo = ['fazer cafe'] => adicionar fazer cafe
# todo = ['fazer cafe','caminhar',] -> adicionar caminhar
# desfazer = ['fazer cafe',] -> Refazer ['caminhar']
# desfazer = [] -> REfazer ['caminhar', fazer cafe']
# refazer= todo ['fazer cafe']
# refazer = todo['fazer cafe,'caminhar]
# list_tarefas = []
# while True:
#     comando = input('Digite oque vc gostaria de fazer: ').lower()
#     if comando == 'adicionar':
#         tarefa = input('Digite a tarefa aqui ferinha: ')
#         list_tarefas.append(tarefa)
#         continue
#     elif comando=='listar':
#         print(list_tarefas, sep='\n')
#         continue
#     elif comando == 'remover':
#         list_tarefas.pop()
#         print(f'Lista atual ta assim: {list_tarefas}')
#         continue
#     else:
#         print('Comando invalido sorry')
#         print('DIgite novamente e.,e')
#         continue
import os

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return
    print('Tarefas: ')
    for tarefa in tarefas:
        print(f'\t{tarefa}')  # \t e um tab
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer ')
        return
    tarefa = tarefas.pop()
    print('a tarefa', tarefa, ' foi removida da lista de tarefas')
    tarefas_refazer.append(tarefa)
    print()


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer ')
        return
    tarefa = tarefas_refazer.pop()
    print('a tarefa', tarefa, ' foi adicionada a lista de tarefas')

    tarefas.append(tarefa)
    print()


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('voce nao digitou nada meu consagraido ')
        return
    tarefas.append(tarefa)
    print('a tarefa', tarefa, ' foi adicionada a lista de tarefas')
    print()


tarefas = []
tarefas_refazer = []
while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')
    if tarefa == 'listar':
        listar(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'clear':
        os.system('clear')
        continue
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue
