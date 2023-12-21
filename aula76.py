# Exercícios  - sistema de perguntas e respostas

perguntas = [
 {
     'Pergunta': 'Quanto e 2+2 ?',
     'Opções':['1','2','3','4'],
     'Resposta':'4'
 },
 {
     'Pergunta': 'Quanto e 5*5 ?',
     'Opções':['25','45','55','15'],
     'Resposta':'25'
 },
 {
     'Pergunta': 'Quanto e 10/2 ?',
     'Opções':['3','5','2','1'],
     'Resposta':'5'
 },
]

# running = True
# count = 0
# questoes = 0
# running2 = True
# while running:
#     running2 = True
#     print('Pergunta:',  perguntas[questoes]['Pergunta'])
#     print('Opções :')
    
#     for indice,pergunta in enumerate(perguntas[questoes]['Opções']):
#         print(f'{indice}) {pergunta}')
#     print('Escolha uma opção: ')
#     indice_resposta = input('Digite a resposta: ')
#     try:
#         int_resposta = int(indice_resposta)
#         if int_resposta > 3 :
#             raise
#     except:
#         print('vc deve enviar um numero inteiro de 0 a 3 ')
#         questoes = 0
#         count =0
#         continue
#     if perguntas[questoes]['Opções'][int_resposta] == perguntas[questoes]['Resposta']:
#         print('💪 Resposta correta gafanhoto 🦗')
#         count += 1
#     else:
#         print('❌ Imundo nem isso tu sabe seu verme')
#         count = count
#     questoes +=1
#     if questoes == 3:
#         if count > 0:
#             print(f'vc acertou {count} de {len(perguntas)}')
#         elif count == 2:
#             print('vc acertou todas as questoes !!!')
#         else:
#             print('Errou tudo ai fera mals')
#     else:
#         continue
    
#     while running2:
#         jogar_novamente = input('Quer Jogar novamente meu consagrado [S]im [N]ão ').lower()
#         if jogar_novamente == 's':
#             questoes=0
#             count=0
#             running2 = False
#             continue
#         elif jogar_novamente =='n':
#             running = False
#             running2 = False
#             break
#         elif jogar_novamente != 's' and jogar_novamente != 'n':
#              print('Vc deve escolher entre [S]im ou [N]ão')
#              questoes=0
#              count=0
qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta: ',pergunta['Pergunta'])
    print()
    opcoes = pergunta['Opções']
    for i,opcao in enumerate(opcoes):
        print(f'{i})',opcao)
    print()
    escolha = input('Escolha uma opção: ')
    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)
    if escolha.isdigit():
       escolha_int = int(escolha)
    if escolha_int is not None:
        if escolha_int >=0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True
    print()
    if acertou:
        qtd_acertos +=1
        print('Acertou Mizeravi 💪')
    else:
        print('❌ Errou Covardy')
    print()

print(f'vc acertou {qtd_acertos}')
print(f'de  {len(perguntas)} perguntas')

