# palavra = 'biscoito'
# render = '*******'

# while True:
#     try:
#         letra = input('Digite uma letra: ')
#         if len(letra) > 1:
#             print('Não é possível enviar mais de uma letra por vez.')
#             continue  # Volta para o início do loop

#         if letra in palavra:
#             for index, letter in enumerate(palavra):
#                 if letter == letra:
#                     render = render[:index] + letra + render[index+1:]

#             print(f'Palavra: {render}')

#             if render == palavra:
#                 print('Parabéns! Você acertou a palavra!')
#                 break  # Sai do loop, pois a palavra foi adivinhada

#         else:
#             print('Letra não encontrada na palavra.')
        
#     except Exception as e:
#         print(f'Ocorreu um erro: {e}')

palavra = 'teste'
print(f'Palavra: {palavra[:2]}')
print(f'Palavra: {palavra[2:]}')
print(f'Palavra: {palavra[::-1]}')