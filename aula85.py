lista = [ ]
for x in range(3):
    for y in range(3):
        lista.append((x, y))
        
lista = [ 
         x
         for x in range(3)# altera o valor do x 3x
         for y in range(3)# como esta depois ele repete o valor 3x
         ]
print(lista)