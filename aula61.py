"""
Cauculo do primeiro digito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma 
contagem regressiva começando de 10

Ex.: 746.824.890-70 (746824890)
    10  9  8  7  6  5   4  3   2
 *   7   4  6  8  2  4  8  9    0
 70  36  48  56 12 20 32 27 0

Somar todos os resultados :
70+37+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301*10 = 3010
obter o resto da divisao da conta anteriror por 11
3010 % 11 =7
Se o resultado anterir for maior que 9:
    resultado e 0
contrario disso :
    resultado e o valor da conta
O primeiro digito do cpf e 7
.replace('.','') da pra usar ele pra subistituir oque for colocado no primeiro parametro pelo segundo
"""
#validador de CPF
import re 
import sys

# cpf_enviado_usuario = '746.824.890-70'.replace('.','') 
cpf_enviado_usuario = re.sub(
    r'[^0-9]',#seleciona tudo que nao for um numero 
    '',#subistitui pra nada ou string vazia
    # '746.824.890-70'
    '111111111'
    )
entrada_e_sequencial = cpf_enviado_usuario == cpf_enviado_usuario[0] * len(cpf_enviado_usuario) 
if entrada_e_sequencial :
    print('Voce enviou dados sequenciais')
    sys.exit()
nove_digitos = cpf_enviado_usuario[:9]
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
if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} e Válido')
else:
    print('CPF Inválido')