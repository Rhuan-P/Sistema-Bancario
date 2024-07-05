from app.Modelo.cliente import Cliente
from app.Utils.validador import validar_doc, validar_data

class Banco:
    def __init__(self):
        self.clientes = []

    def criar_cliente(self, nome, tipo, doc, data_nasc):
        # Exemplo simplificado de validação de documento
        if not doc.isdigit() or len(doc) != 11:  # Verifica se o documento tem 11 dígitos
            raise ValueError("Documento inválido.")
        
    def acessar(self, doc):
        return next((cliente for cliente in self.clientes if cliente.doc == doc), None)

    def add_cliente(self, cliente):
        self.clientes.append(cliente)

    def cliente_existe(self, doc):
        return any(cliente.doc == doc for cliente in self.clientes)

    def criar_cliente(self, nome, tipo, doc, data_nasc):
        if not validar_doc(doc):
            raise ValueError("Documento inválido.")
        if not validar_data(data_nasc):
            raise ValueError("Data de nascimento inválida.")
        if self.cliente_existe(doc):
            raise ValueError("Cliente com esse documento já existe.")
        
        cliente = Cliente(nome=nome, tipo=tipo, doc=doc, data_nasc=data_nasc)
        self.add_cliente(cliente)

    def __str__(self):
        return f"{self.clientes}"
