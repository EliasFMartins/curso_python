from aula130 import CAMINHO_ARQUIVO, Pessoa, fazer_o_dump
import json

#Então, a diferença está no que é desempacotado: * desempacota as chaves, enquanto ** desempacota os valores associados às chaves

with open(CAMINHO_ARQUIVO,'r') as arquivo:
   pessoas =  json.load(arquivo)
   p1 = Pessoa(*pessoas[0])
   p2 = Pessoa(*pessoas[1])#dessa forma puxa apenas o nome da chave
   p3 = Pessoa(**pessoas[2])#dessa forma puxa o valor da chave 
   print(pessoas)
   print(*pessoas)
#    print(p1)
   
print(p1.nome,p1.sobrenome)
print(p2.nome)
print(p3.nome)
print(vars(p1))