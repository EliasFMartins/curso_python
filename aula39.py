"""
Iterando strings com while
"""
nome = 'Elias F Martins'
indice = 0
novo_nome =''
while indice < len(nome):
  letra = nome[indice]
  novo_nome+= f'*{letra}'
  print(novo_nome)
  indice +=1

print('finished')