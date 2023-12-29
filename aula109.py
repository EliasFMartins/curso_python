# count é um iterador sem fim(itertools)
from itertools import count

c1 = count(step=8, start=8)
#da pra passar o start q e o inicio e o passo que nesse caso e 8 step
print(next(c1))
for i in c1:
    if i>50:
        break
    print(i)
