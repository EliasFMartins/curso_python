"""
Repetições      
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""
valor = True

while valor:
  name = input('Qual seu nome Coleginha ?')
  print(f'vai ser executado ate o breack ser ativado')
  if name =='biscoito':
    break



  contador  = 0 
  while contador <= 10 :
    contador  = contador + 1
    print(contador)
print('acabou')