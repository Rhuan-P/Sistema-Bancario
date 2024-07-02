from Account import *

class User:
    def __init__(self, nome,dif, data_nasc):
        self.nome = nome
        self.dif = dif
        self.data_nasc = data_nasc
        
    def Criar_user(tipo, **kw):
        if tipo.upper() == 'PF':
            return PF(**kw)
        elif tipo.upper() == 'PJ':
            return PJ(**kw)

class PF(User):
    def __init__(self,**kw ):
        super().__init__(**kw)
    def mostrar(self):
        print('PF')

class PJ(User):
    def __init__(self, **kw ):
        super().__init__(**kw)
    def mostrar(self):
        print('Pj')

        






