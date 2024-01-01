# Mantendo estados dentro da classe
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} ja esta filmando...')
            return

        print(f'{self.nome} esta filmando...')
        self.filmando = True

    def para_filmar(self):
        if not self.filmando:
            print(f'{self.nome} nao esta filmando...')
            return

        print(f'{self.nome} esta parando de filmar...')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} nao pode fotografar enquanto esta filmando...')
            return
        print(f'{self.nome} esta fotografando ...')


c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()
c1.filmar()
c1.fotografar()
c1.para_filmar()
c1.para_filmar()
c1.fotografar()

