import unittest
from app.Modelo.account import Conta

class TestConta(unittest.TestCase):
    def setUp(self):
        # Inicializa a Conta para os testes
        self.conta = Conta()

    def test_depositar(self):
        # Testando depósito válido
        self.conta.Depositar(100.0)
        self.assertEqual(self.conta.saldo, 100.0)

        # Testando depósito inválido
        with self.assertRaises(ValueError):
            self.conta.Depositar(-50.0)

    def test_sacar(self):
        # Testando saque válido
        self.conta.Depositar(200.0)
        self.conta.Sacar(50.0)
        self.assertEqual(self.conta.saldo, 150.0)

        # Testando saque maior que saldo
        with self.assertRaises(ValueError):
            self.conta.Sacar(200.0)

    def test_mostrar(self):
        # Testando método mostrar
        extrato, saldo = self.conta.Mostrar()
        self.assertEqual(saldo, self.conta.saldo)
        self.assertEqual(len(extrato), len(self.conta.extrato))

if __name__ == "__main__":
    unittest.main()
