"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudaçao apropriada . EX.
bom dia 0-11, boa tarde 12-17 e Boa noite 18-23.


"""
hora = input('Digite a hora atual e receba a saudacao ')
try:
  hora_number = int(hora)
  if hora_number >= 0 and hora_number < 12:
    print(f'Bom dia sao  {hora_number} horas  ')
  elif hora_number >= 12 and hora_number < 18:
    print(f'Boa Tarde sao {hora_number} horas')
  elif hora_number>=18 and   hora_number <= 24:
    print(f'Boa noite sao {hora_number} horas')
  else:
    print(f'hora digitada nao coresponde')
except:
  print('vc n digitou um numero')