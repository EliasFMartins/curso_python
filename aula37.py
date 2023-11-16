"""Repetições      
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""
contador = 0
while contador <= 100:
  contador +=1
  if contador >=27 and contador <= 45:
    print(f' nao vou mostrar o {contador}')
    continue
  if contador == 40:
    break
  print(contador)
print('TErminou')