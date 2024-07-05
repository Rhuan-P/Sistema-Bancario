from app.Modelo.cliente import Cliente


class Banco:
    # TODO create a singleton
    def __init__(self):
        self.clientes = []

    def acessar(self, doc):
        return next((cliente for cliente in self.clientes if cliente.doc == doc), None)

    def add_cliente(self, cliente):
        self.clientes.append(cliente)

    def ciar_cliente(self, nome, tipo, doc, data_nasc):
        cliente = Cliente(nome=nome, tipo=tipo, doc=doc, data_nasc=data_nasc)
        self.add_cliente(cliente)

    def __str__(self):
        return f"{self.clientes}"
