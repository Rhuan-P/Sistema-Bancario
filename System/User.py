from Account import *

class User:
    def __init__(self, nome,dif, data_nasc):
        self.nome = nome
        self.dif = dif
        self.data_nasc = data_nasc
        
    def Criar_user(self, tipo, **kw):
        super().__init__(**kw)
        if tipo.upper() == 'PF':
            PF(**kw)
        elif tipo.upper() == 'PJ':
            PJ(**kw)

class PF(User):
    def __init__(self,**kw ):
        super().__init__(**kw)
        

class PJ(User):
    def __init__(self, **kw ):
        super().__init__(**kw)


        






