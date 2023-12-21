frase = 'O python é uma linguagem de programação '\
    'multiparadigma.'\
    'Python foi criado por Guido van Rossum. '
    #methodo pra contar quantas vezes a palavra que eu colocar dentro se repete na variavel
i = 0
apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]
    quantas_verzes_letra_apareceu_atual = frase.count(letra_atual)
    if letra_atual == ' ':
        i += 1
        continue
    if apareceu_mais_vezes < quantas_verzes_letra_apareceu_atual:
        apareceu_mais_vezes = quantas_verzes_letra_apareceu_atual
        letra_que_apareceu_mais_vezes = letra_atual
        
    i += 1
print(
    'A letra que apareceu mais vezes foi '
    f'{letra_que_apareceu_mais_vezes} que apareceu'
    f' {apareceu_mais_vezes}x'
)

