# Métodos úteis dos dicion´´arios em Python
# len - quantas chaves
# keys - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe 
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada(del)
# popitem - Apagao último item adicionado

d1 = {
    'c1':1,
    'c2':2
}
#d2['c1'] = 1000# esta simplimente linkado o local da memoria quando altera 1 altera os 2
#d2 = d1
d2 = d1.copy()# copia o obj  agora da pra alterar 1 se mexer no outro copia raza apenas dados imutaveis array ja vai pro krlh array vai pra mesmo luga na memoria

# pra copiar tudo tem q importar o copy
import copy
d2 = copy.deepcopy(d1)
#agora copiou de verdade

print(d1)
