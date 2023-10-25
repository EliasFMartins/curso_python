# Operadores in e not in
# String sao iteraveis
#  0 1 2 3 4 =>
#  E l i a s
# -5-4-3-2-1

nome = 'Elias'
print(nome[2])
print(10*'----')
print('a' in nome)
# mostra se tem o caracter na variavel o not in faz o inverso se tiver fala que nao e assim por diante


nome2 = input('digite seu nome :')
encontrar = input('Digite o que deseja encontrar: ')
if encontrar in nome2:
  print(f'{encontrar} esta em {nome2}')
else:
  print(f' ta aqui nao fera fods')