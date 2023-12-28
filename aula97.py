# Entendendo os seus própios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a ásta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ pror 
# padrão
# O python conhece todos os módulos e pacotes presentes 
# nos caminhos de sys.path
import aula97_m # importa a poha toda
from aula97_m import variavel_modulo, soma #importar so 1 variavel
print('Este módulo se chama', __name__)

print(aula97_m.variavel_modulo)
print(soma(2,3))
