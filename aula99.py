from sys import path 
from aula99_package.modulo import soma_do_modulo
import aula99_package.modulo
from aula99_package.modulo import *# importar tudo
from aula99_package import modulo

# print(*path, sep='\n')# diretorios que esse modulo tem acesso

# import aula99_package

# print(soma_do_modulo(2,5))
# print(aula99_package.modulo.soma_do_modulo(2,5))
# print(modulo.soma_do_modulo(2,5))
# print(variavel)
# from aula99_package.modulo import fala_oi
# fala_oi()
from aula99_package import fala_oi,soma_do_modulo,variavel
print(aula99_package.fala_oi())