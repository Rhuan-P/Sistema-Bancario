class User:
    def __init__(self, nome, doc, data_nasc):
        self.nome = nome
        self.doc = doc
        self.data_nasc = data_nasc


class PF(User):
    def __init__(self, **kw):
        super().__init__(**kw)


class PJ(User):
    def __init__(self, **kw):
        super().__init__(**kw)
