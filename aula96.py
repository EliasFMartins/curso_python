# Módulos padrão do Python (import, from, as e *)
# inteiro - import nome_modulo
# Vantagens: você tem o nomespace do módulo
# Desvatagens: nomes grandes
import sys
print(sys.platform)

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