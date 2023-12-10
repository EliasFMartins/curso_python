"""Calculadora com while """
# valor1 = input('Digite o primeiro valor: ')
# valor2 = input('Digite o segundo valor: ')
# operação = input('Digite o operador desejando para efetuar a operação')

# try:
#     valor_int1 = int(valor1)
#     valor_int2 = int(valor2)
#     if operação == '+' or operação == '-' or operação == '*' or operação =='/':
#         if operação == '+':
#          print(f'{valor_int1} + {valor_int2} = {valor_int1+valor_int2}')
#         elif operação == '-':
#          print(f'{valor_int1} - {valor_int2} = {valor_int1 - valor_int2}')
#         elif operação == '*':
#          print(f'{valor_int1} * {valor_int2} = {valor_int1 * valor_int2}')
#         elif operação == '/':
#          print(f'{valor_int1} / {valor_int2} = {valor_int1 / valor_int2}')
#     else:
#      print('operador não reconhecido meu consagrado!')			
# except:
#     print('vc nao digitou numneros validos')

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador(+-/*): ')
    
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
        
    except:
       numeros_validos = None
    if numeros_validos is None:
        print('Um ou ambos os Numeros digitados são invalidos')
        continue
    
    operadores_permitidos = '+-/*'
    
    if operador not in operadores_permitidos:
        print('Operador não e valido')
        continue
    if len(operador) > 1:
        print('Operador não deve ter mais de um caracter')
        
    print(' Realizando sua conta. confira o resultado abaixo: ')
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = { num_1_float + num_2_float}')
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} = { num_1_float - num_2_float}')
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} = { num_1_float / num_2_float}')
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} = { num_1_float * num_2_float}')
    else :
        print(f'era pra tu ter chegado aqui n fera serio mesmo')
        
    sair= input('Quer sair ? [S]im: ').lower().startswith('s')
    if sair is True:
        break