# fatiamento de strings
"""
 0  1  2  3  4
 e  l  i  a  s
-5 -4 -3 -2 -1

Fatiamento [i:f:p] [::]
inicio 
fim
passo
obs.: a função len retorna a qtd
de caracteres da str
"""
variavel = 'Olá mundo'      
print(variavel[4:])
#dessa forma vai fatirar do indice 4 ate o fim
print(len(variavel))
#mostra o valor tipo .length
print(variavel[0:len(variavel)])
# nesse caso , vai pegar do inicio ate o fim por causa do len
print(variavel[0:9:2])
# vai de 0  9 no passo 2 pegando basicamente 1 letra e pulando a outra 
print(variavel[::-1])
# nesse caso ja inverte a string do inicio ao final no passo negativo inverte o role
     