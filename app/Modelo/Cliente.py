from .user import PF, PJ
from .account import Conta


class Cliente:
    def __init__(self, nome, tipo, doc, data_nasc):
        self.doc = doc
        self.data_dasc = data_nasc
        self.user = (
            PF(nome=nome, doc=doc, data_nasc=data_nasc)
            if tipo.upper() == "PF"
            else PJ(nome=nome, doc=doc, data_nasc=data_nasc)
        )
        self.conta = Conta()
