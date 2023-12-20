# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como paramêtro.

# def duplicar(numero):
#     return numero * 2
# def duplicar_2(numero):
#     return numero * 2
# def duplicar_3(numero):
#     return numero * 2

def criar_multiplicador (multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

print(criar_multiplicador(2)(10))# eu estava colocando um dentro do outro e estava dando erro  tem q ser nesse formato