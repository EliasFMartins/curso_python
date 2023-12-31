
# Criando arquivos com Python
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# Write, read (escrever e ler)
# Writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os , masÇ
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

# caminho_arquivo='/home/elias/workspace/curso_python/'
caminho_arquivo = 'aula118.txt'

# arquivo=open(caminho_arquivo, 'w')
# arquivo.close()

# with open(caminho_arquivo, 'w+') as arquivo:  # with  open abre e fecha o arquivo
#     # w so da a possibilidade de escrever se vc tentar ler vai da ruim se vc colocar + com  w  ex: w+ consegue ler e escrever
#     arquivo.write('Pao dia saude e alegria\n')
#     arquivo.write('Pao dia saude e alegria\n')
#     arquivo.writelines(  # e possivel mandar varias linhas mas vc q deve quebrar las \n e  interavel no caso tuplas
#         ('Linha3\n', 'Linha4\n', 'Linha5\n')
#     )
#     arquivo.seek(0, 0)
#     print(arquivo.read())
#     arquivo.seek(0, 0)
#     # em tipo um next muito cuidado se o cursor estiver em baixo n tera nada pra ler mover o cursor nesses casos
#     print(arquivo.readline().strip())
#     print(arquivo.readline(), end='')
#     print(arquivo.readline(), end='')
#     print(arquivo.readline(), end='')
#     # dessa forma n le pois o cursor esta no final do documento pra fazer ele voltar pra posicao inicial
#     print('READLINES')
#     arquivo.seek(0, 0)
#     for linha in arquivo.readlines():
#         print(linha.strip())
# print('*'*30)
# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())


with open(caminho_arquivo, 'w+', encoding='utf8') as arquivo:# se vc executar so o w ele apaga o documento inteiro...
    # esse enconding no windows tava dando merda 
    # ja o 'a' nao apaga nada e comeca a escrever do final do aquivo
    arquivo.write('Pão dia saude e alegria\n')
    arquivo.write('Pço dia saude e alegria\n')
    arquivo.writelines(
        ('Linha3\n', 'Linha4\n', 'Linha5\n'))
