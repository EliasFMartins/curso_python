"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados :
    Exiba:
        Seu Nome é {}
        Seu nome Invertido é {nome invertido}
        seu nome contém (ou não) espaços
        seu nome tem {N} letras
        A primeira letra do seu nome é {letra}
         A ultima letra do seu nome é {letra}
se nada for digitado em nome ou idade :
....exiba "Desculpe, vc deixou campos vazios."
         Fatiamento  [i:f:p] [::]                                
"""
nome = input("digite seu nome ai fera :" )
idade = input("digite sua idade ai fera :")

if nome and idade:
  print(f'Seu nome Seu cretino  e {nome}')
  print(f'seu nome invertido e: {nome [::-1]}')
  if' ' in nome:
    print('Seu nome contém espaços')
  else:
    print('Seu nome NÃO contem espaços')
  print(f"Sua idade e {idade}")
  print(f'o comprimento do seu nome e: {len(nome)}')




if not nome or not idade:
  print('Viado ce tem q mandar os parametros arrombadinho')   