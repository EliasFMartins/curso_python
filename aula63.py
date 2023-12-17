"""
Introdução ás funções (def) em Python
Funções  sao trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
por padrão, funções Python retornam None (nada)
Funções podem usar parâmetros para receber valores. Parâmetro é o nome da "variável" dentro dos parênteses, argumento é o valor passado para o parâmetro no momento da execução da função.
"""
# def example( params, params)
# return print(params +parans)
# example(argumentos,argumentos)

def Print(param='teste'):
    print(param)


def soma(x, y):
    print(x + y)
soma(5,8)
soma(y=3,x=8) # poode alterar a ordem que envia-se os parametros