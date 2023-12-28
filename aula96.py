# Módulos padrão do Python (import, from, as e *)
# inteiro - import nome_modulo
# Vantagens: você tem o nomespace do módulo
# Desvatagens: nomes grandes
import sys
print(sys.platform)# fa;a o nome do sistema operacional
#importa o pacote inteiro e seleciona qual funcionalidade utilizar
from sys import exit, platform
print(platform)
import sys as s # altera o nome  do pacote  quando vc faz a importação
from sys import platform as pf, exit as ex # alterando o nome da modulo do pacote na importação
from sys import *# basicamente importa tudo  e fica all sem a proteção do sys. vc consegue consumir diretamente

# seleciona oque vc quer do pacote e importa apenas eles vc pode utilizar diretamente

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvatagens: Sem o namespace do módulo

# alias 1 - import nome_modulo as apelido
# alias 2 - from nome_mmodulo import objeto as apelido
# Vantagens : você pode rreservar nomes para seu códico
# Desvatagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagens: impoorta tudo de um módulo
# Desvantagens: importa tudo de um módulo