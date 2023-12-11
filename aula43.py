# texto = 'Python'


# i = 0
# name = ''
# tamanho_string = len(texto)
# while i < tamanho_string:
#     name +=texto[i]
#     # print(texto[i])
#     print(name)
#     i+=1

texto = 'Python'
novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto+ '*')