import unittest
from app.Modelo.cliente import Cliente
from app.Modelo.account import Conta

class TestCliente(unittest.TestCase):
    def setUp(self):
        # Inicializa o Cliente para os testes
        self.cliente = Cliente(nome="Fulano", tipo="PF", doc="12345678900", data_nasc="01/01/1990")

    def test_criar_cliente(self):
        # Testando criação de cliente com dados válidos
        self.assertEqual(self.cliente.user.nome, "Fulano")
        self.assertEqual(self.cliente.user.doc, "12345678900")
        self.assertEqual(self.cliente.user.data_nasc, "01/01/1990")
        self.assertEqual(self.cliente.conta.saldo, 0.00)

    def test_validacao_tipo(self):
        # Testando validação de tipo de conta
        self.assertRaises(ValueError, Cliente, nome="Ciclano", tipo="PP", doc="98765432100", data_nasc="02/02/1995")

    def test_acesso_conta(self):
        # Testando acesso ao objeto de conta
        self.assertIsNotNone(self.cliente.conta)
        self.assertIsInstance(self.cliente.conta, Conta)

if __name__ == "__main__":
    unittest.main()
