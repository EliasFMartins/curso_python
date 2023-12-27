
# Generator expression, Iterables e Iterators em Python
import sys 

iterable =['Eu', 'tenho', '__iter__']
iterator = iter(iterable)    #.__iter__() # tem __iter__ e __next__
lista = [n for n in range(10)]# executa o codigo e gera a lista de numerod dentro do range toda dentro da memoria
generator= (n for n in range(10)) # o valor fica marcado pra chamar o proximo quando vc chama apenas o valor n fica na memoria n tem index nem len ne nada 
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))
print((lista))
print(next(generator))