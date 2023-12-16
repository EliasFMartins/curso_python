"""
split e join com list e srt
split - divide uma string
join - une uma string
"""
frase = 'Olha so que ,  coisa interessante'
lista_palavras = frase.split(', ') # Separa string por padrao por spaces  se passar um parametro ex ',' ele vai separar por virgula e etc...
lista_palavras_fixed = []
for i, frase in enumerate(lista_palavras):
    print(lista_palavras[i].strip()) # remove os espacos do inicio and the end of phase
    lista_palavras_fixed.append(lista_palavras[i].strip())
print(lista_palavras_fixed)
print(lista_palavras)

frases_unidas = ', '.join(lista_palavras_fixed)
print('teste')
print(frases_unidas)