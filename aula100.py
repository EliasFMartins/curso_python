# Exercícios
# copy, sorted, lista.sort
# Aumente os preços dos protudos a seguir im 10%
# Gere novos_produtos por deep Copy(cópia profunda)

# Ordene os produtos porm nome decrescente (do maior para o menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente  (do menor para o maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
from dados import produtos
import copy
novos_produtos = [
    {**produto, 'preco':round(produto['preco']*1.1,2)}
    for produto in
    copy.deepcopy(produtos)

]


produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p :p['nome']
)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p :p['preco'],
    reverse=False
)
print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n') 
