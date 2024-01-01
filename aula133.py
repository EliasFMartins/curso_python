# method vs @ classmethod vs @staticmethod
# method - self , método de instância
# @classmethod -cls, método de classe
# @staticmethod - método estático (❌self,❌cls)

class Connection:
    #sempre que usar alguma coisa de self e um method de instancia
    #methodo normal recebe a self
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password
        
    @classmethod
    #methodo de class recebe a class
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    #n tem acesso a nada n faz poha nnehuma e uma funcao enfeitadinha 
    def soma(x,y):
        return x + y

c1 = Connection.create_with_auth('Elias',123)
# c1 = Connection()
# c1.set_user('Elias')
# c1.set_password('senha')
print(c1.user)
print(c1.password)
