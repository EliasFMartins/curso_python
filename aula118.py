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
#vamos falar mais sobre o módulo json, mas:
#json.dump = Gera um arquivo json
# json.load

caminho_arquivo='/home/elias/workspace/curso_python/'
caminho_arquivo += 'aula118.txt'

# arquivo=open(caminho_arquivo, 'w')

# arquivo.close()
with open(caminho_arquivo,'w') as arquivo:
    print('Hello World')
    print('Aqruivo vai ser fechado x.x')