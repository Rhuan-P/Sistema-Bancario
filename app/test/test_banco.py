import unittest
from app.Modelo.banco import Banco

class TestBanco(unittest.TestCase):
    def setUp(self):
        self.banco = Banco()

    def test_criar_cliente(self):
        # Testando criação de cliente válida
        self.banco.criar_cliente(nome="Fulano", tipo="PF", doc="123.456.789-00", data_nasc="01/01/1990")
        self.assertEqual(len(self.banco.clientes), 1)

        # Testando tentativa de criação de cliente com mesmo documento
        with self.assertRaises(ValueError):
            self.banco.criar_cliente(nome="Ciclano", tipo="PF", doc="123.456.789-00", data_nasc="02/02/1995")

    def test_acessar_cliente(self):
        # Testando acesso a cliente existente
        self.banco.criar_cliente(nome="Beltrano", tipo="PF", doc="987.654.321-00", data_nasc="03/03/1980")
        cliente = self.banco.acessar("987.654.321-00")
        self.assertIsNotNone(cliente)
        self.assertEqual(cliente.user.nome, "Beltrano")

        # Testando acesso a cliente inexistente
        cliente = self.banco.acessar("111.222.333-44")
        self.assertIsNone(cliente)

if __name__ == "__main__":
    unittest.main()
