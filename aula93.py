# Try, exept, else e finally

try:
    a = 18
    print('Linha 01')
    b = 0
    print('linha1'[1000])
    c = a / b
    print('Linha 02')

except ZeroDivisionError: 
    print('Dividiu por 0')
except( NameError, IndexError) as error: #tratar mais de um erro de uma vez
    print('Name ',error.__class__.__name__)
except Exception:
    print('Fodeu a poha toda ')
print('Continuar')