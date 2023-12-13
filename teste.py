#calc com soma divisão e multiplicação potenciação subitracao


first_number = input('Digite o primeiro numero para executar uma operação: ')
second_number = input('Digite o segundo numero para executar a operação: ')
operador =input('Digite um operador (+-/* **): ' )
operadores = '+-/* **'
verificade_operador = operador

try:
    first_number_int = int(first_number)
    second_number_int = int(second_number)
    if operador in operadores:
        verificade_operador = operador
    if verificade_operador:
            
        if operador== '+':
            print(f'o {first_number_int} + {second_number_int} = {first_number_int+second_number_int}')
        elif operador== '*':
            print(f'o {first_number_int} * {second_number_int} = {first_number_int*second_number_int}')
        elif operador== '-':
            print(f'o {first_number_int} - {second_number_int} = {first_number_int-second_number_int}')
        elif operador== '/':
            print(f'o {first_number_int} / {second_number_int} = {first_number_int/second_number_int}')
        elif operador== '**':
            print(f'o {first_number_int} ** {second_number_int} = {first_number_int**second_number_int}')
    
    
except:
    print('algum erro com os numeros ou com ambos numeros')

    