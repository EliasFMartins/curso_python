# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o valor para uma variavel e mostre o valor
# da variável.

#Crie uma função fala se um número é par ou ímpar.
#Retorne se o número é par ou ímpar.

def multiplica (*args):
    total = 1
    for  numero in args:
        total *=numero
    return total


def isPar (num):
    result = 'par' if num % 2==0 else 'inpar'
    return result
print(isPar(5))
print(multiplica(5,6,8))