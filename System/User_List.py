from User import *
from Account import *
List = []    




class Cliente:
    def __init__(self,nome,dif,data_nasc):
        self.dif = dif
        self.data_nasc = data_nasc
        self.nome = nome
        self.User = PF(nome=nome, dif = dif, data_nasc = data_nasc)
        self.Conta = conta()   
        List.append(self)
      


def login(dif):
    #login = filter(lambda cliente:cliente.dif == dif, List)
    acess = list(filter(lambda cliente:cliente.dif == dif, List))[0]
    return acess

