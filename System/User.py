from Account import *

class User:
    def __init__(self, nome,dif, data_nasc):
        self.nome = nome
        self.dif = dif
        self.data_nasc = data_nasc
        

class PF(User):
    def __init__(self,**kw ):
        super().__init__(**kw)
        

class PJ(User):
    def __init__(self, **kw ):
        super().__init__(**kw)


        






