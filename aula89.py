# dir, hasattr e getattr em Python

string  ='Elias'
metodo = 'upper'

if hasattr (string, metodo):
    print('Existe Upper')
    print(getattr(string, metodo)())
    print(string)
else:
    print('Não existe o método', metodo)