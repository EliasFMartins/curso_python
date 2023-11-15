"""
Faca um programa que peca ao usuario pra digitar um numero inteiro, informe se este numero e par ou impar
. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""


# numero = input('Digite um numero inteiro !')

# if numero.isdigit():
#   numero_int = int(numero)
#   par_inpar = numero_int % 2 == 0
#   numero_text = 'numero par' if par_inpar else 'numero impar'
#   print(f'O numero {numero_int} e um {numero_text}')
# else:
#   print('vc nao digitou um numero inteiro')

# other solucao
entrada = input ('Digite um Numero inteiro')
try:
  entrada_int = int(entrada)
  par_inpar = entrada_int % 2 == 0
  par_inpar_texto = 'Inpar'
  if par_inpar:
    par_inpar_texto = 'par'
  print(f'O numero {entrada_int} e {par_inpar_texto}')
except:
  print('Voce nao digitou um numero inteiro')