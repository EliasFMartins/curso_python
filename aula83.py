# Empacotament e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
print(a, b)

pessoa = {
    'nome':'Elias',
    'sobrenome':'Agnus'
}
a, b = pessoa.values()
(a1,a2), (b1,b2) = pessoa.items()# pega chave e valor
print(a1, b2)
#args e kwargs
#args (já vimos)
#kwargs - keyword arguments (argumentos nomeados)
for chave, valor in pessoa.items():
    print(chave, ':', valor)
    
pessoa = {
    'nome':'Elias',
    'sobrenome':'Agnus'
}
dados_pessoa = {
    ' idade':18,
    'aniversario':'Janeiro'
}
pessoa_completa = {**pessoa , **dados_pessoa,'quem e o gostosao daqui':'Sou eu sou eu '}
print( 
      
pessoa_completa
      )
def mostro_argumentos_nomeados(*args, **kwargs):
    #nomeados sempre vem em kwargs os  sem nomeacao vem em args
    print('Nao nomeados',args)
    for chave, valor in kwargs.items():#precisa dele pra pegar os valores
        print(chave, valor)
    
mostro_argumentos_nomeados(1,2,3,4,teste='biscoito', suco='tampico')
mostro_argumentos_nomeados(**pessoa_completa)
mostro_argumentos_nomeados(pessoa_completa)