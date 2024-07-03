from Modelo import User
from Modelo import Account
List = []    

class Cliente:
    def __init__(self,tipo,nome,dif,data_nasc):
        self.dif = dif
        self.data_nasc = data_nasc
        self.User = User.PF(nome=nome, tipo=tipo, dif = dif, data_nasc = data_nasc)
        self.Conta = Account.conta()   
        List.append(self)

#TODO move to Menu.py
def login(dif):
    #login = filter(lambda cliente:cliente.dif == dif, List)
    acess = list(filter(lambda cliente:cliente.dif == dif, List))[0]
    return acess
    #TODO return obj
