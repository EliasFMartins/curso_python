# @property - um getter no modo Pythônico
# getter - 8um método para obter um atributo
# modo Pythônico  - modo do python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um atributo
# 🤯🤯🤯
# Geralmente é usada nas seguintes situações:
#  - como getter
# - p;/evitar quebrar o código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
 #Property  fazerm um methodo ficar como uma propriedade por isso o nome acredito eu
class Caneta:
    def __init__(self, cor):
        self.cor_foda = cor
        #o self cor foi definido  sempre q vc alterar daria merda se outras pessoas utilizacem seu codigo
        # utilizando get_cor eles chamam o methodo mesmo q vc mude oque ele retorna n iria quebrar codigo d ngmn
        
    def get_cor(self):
        print('GET COR')
        return self.cor
    
    @property
    def cor(self):
        return self.cor_foda
        
        
        
caneta = Caneta('Red')

print(caneta.cor)
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())