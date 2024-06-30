from User_List import *

class PF:
    def __init__(self, nome, cpf, data_nasc):
        self.NOME = nome
        self.__CPF = cpf
        self.DATA_NASC = data_nasc
        self.id = int( User_List.add_List(self))

class Cliente(PF):
        
    def __init__(self, cpf, **kw ):
        super().__init__(**kw)
        self.cpf = cpf


p1=PF('alex',1,1)

print(User_List.show(0))
print(User_List.list_dict(0))





list[
    0x000002186C09A7B0, 0x100102186C09A7B0
]