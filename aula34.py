name = input('Digite o seu Nome : ')
try:
  name_text = str(name)
  if len(name_text) <= 4:
     print('seu nome e muito curto')
  if len(name_text) >4 and  len(name_text) < 7:
     print('Seu nome e normal')
  if len(name_text) > 6:
     print('seu nome e grande heim fera')
except:
  print('vc digitou um numerou  ou outro caracter')