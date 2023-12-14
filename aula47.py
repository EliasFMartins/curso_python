"""
Lista em Python 
Tipo List -  Mutável
Suporta vários valores de qualquer tipo 
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del,, clear, extend, +
        append - Adiciona um item ao final
        insert - Adiciona um item no índice escolhido 
        pop - Remove do final ou do índice escohido
        del - Apaga um índice
        clear - Limpa a lista
        extend - estende a lista
        + - concatena listas
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (crud)

"""

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a+lista_b
lista_d = lista_a.extend(lista_b)
print(lista_d)