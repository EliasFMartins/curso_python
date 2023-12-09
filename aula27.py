# .<numero de digitos> f
# (Caractere) (><^)(quantidade)
# > - esquerda
# < - direita
variavel =  'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel:%^10}.')
print(f'{1000.4873648123746:0>+10,.1f}.')
print(f'o hexadecimal de 1500 e {1500:08X}')
print(f'o hexadecimal de 1500 e {1500:X}')