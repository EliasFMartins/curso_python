#Funções decoradoras e decoradores
#Decorar =Adicionar/ Remover / Restrigir / Alterar
#Funções decoradoras são usados para fazer o Python
#usar as funções decoradoras em outras funções.
def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou lhe decorar')
        for arg in args:
                e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}')
        print('Ok, agora voce foi decorada')
        return resultado
    return interna
@criar_funcao
def invert_string(string):
    print(f'{invert_string.__name__}')
    return string[::-1]

def e_string(param):
    if not isinstance(param ,str):
        raise TypeError('Param deve ser uma string')
    
    
invertida = invert_string('123')
print(invertida)