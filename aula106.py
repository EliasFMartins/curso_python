# Ordem dos decoradores
def parametros_decorador(nome):
    def decorador (func):
        print('Decorador: ',nome)
        
        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return sua_nova_funcao
    return decorador


@parametros_decorador(nome='Segundo')#funfa de baixo para cima diferente do fluxo padrao
@parametros_decorador(nome='Primeiro')
def soma(x, y):
    return x+y

dez_mais_cinco = soma(10,5)
print(dez_mais_cinco)