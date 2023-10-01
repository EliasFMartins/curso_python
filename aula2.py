altura = 1.85
nome = 'Elias F Martins'
peso = 78

# IMC = peso/ (altura x altura).
imc = peso/(altura * altura)
print(nome, 'tem', altura, 'de altura')
print('pesa', peso, 'quilos e seu imc é')
print(imc)
# com F strings
print(f'{peso} e algo desnecessario e {altura:.2f}')