#Gerador de CPF
import random
nove_digitos = ''
for i in range(9):
    nove_digitos +=str( random.randint(0,9))
contador_regressivo_1 = 10
resultado_digito_1 = 0
for digito in nove_digitos:
   resultado_digito_1 += int(digito) * contador_regressivo_1
   contador_regressivo_1 -=1
first_digito = ((resultado_digito_1 * 10) % 11)
first_digito = first_digito if first_digito <= 9 else 0


dez_digitos = nove_digitos + str(first_digito)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 +=  int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
second_digito = (resultado_digito_2 * 10 % 11)
second_digito = second_digito if second_digito <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{first_digito}{second_digito}'
print(cpf_gerado_pelo_calculo)