"""
args - Argumentos NÃO nomeados 
 *-* args (empacotamento e desempacotament)
 """
 # lembre-te de desempacotamento 
x, y, *resto = 1,2,3,4
print(x,y, resto)

# def soma (x, y):
 #   return x + y
def soma (*args):
    total = 0
    for numero in args:
        total +=  numero
    return total

soma(1,2,3,4,5,6,7)
print(sum((7,5,4,3,6,9,8,8,5))) # faz a soma no caso recebe 2 parametros po padrao  se quiser passar mas e preciso usar 
# uma tupla
numeros = 1,2,3,4,5,6,7,8,9
print(numeros)
print(*numeros)# o * desempacota os dados da tupla  no exemplo vc consegue ver  q ele funfa como spreed operator