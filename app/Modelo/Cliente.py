from .user import PF, PJ
from .account import Conta


class Cliente:
    def __init__(self, nome, tipo, doc, data_nasc):
        self.doc = doc
        self.data_nasc = data_nasc

        if tipo.upper() not in ["PF", "PJ"]:
            raise ValueError("Tipo de cliente inválido.")
        # Validando e criando o tipo de usuário (PF ou PJ)
        
        if tipo.upper() == "PF":
            self.user = PF(nome=nome, doc=doc, data_nasc=data_nasc)
        elif tipo.upper() == "PJ":
            self.user = PJ(nome=nome, doc=doc, data_nasc=data_nasc)
        else:
            raise ValueError("Tipo de cliente inválido.")

        # Criando a conta do cliente
        self.conta = Conta()

    def __str__(self):
        return f"Cliente: {self.user.nome}, Documento: {self.doc}"
