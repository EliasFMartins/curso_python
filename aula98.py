import aula98_m
import importlib
# módulos sao carregados apenas uma vez a menos que vc use o reload
print (aula98_m.variavel)
for i in range(10):
    print(i)
    importlib.reload( aula98_m)
print('FIm')
