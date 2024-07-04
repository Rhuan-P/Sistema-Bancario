
class User:
    def __init__(self, nome, tipo, dif, data_nasc):
        self.nome = nome
        self.tipo = tipo
        self.dif = dif
        self.data_nasc = data_nasc

class PF(User):
    def __init__(self,**kw ):
        super().__init__(**kw)
    def mostrar(self):
        print(self.tipo)

class PJ(User):
    def __init__(self, **kw ):
        super().__init__(**kw)
    def mostrar(self):
        print(self.tipo)

        






