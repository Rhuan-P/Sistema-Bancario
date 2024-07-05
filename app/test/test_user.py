import unittest
from app.Modelo.user import PF, PJ

class TestPF(unittest.TestCase):
    def test_criar_pf(self):
        # Testando criação de pessoa física (PF)
        pf = PF(nome="João", doc="123.456.789-00", data_nasc="01/01/1990")
        self.assertEqual(pf.nome, "João")
        self.assertEqual(pf.doc, "123.456.789-00")
        self.assertEqual(pf.data_nasc, "01/01/1990")

class TestPJ(unittest.TestCase):
    def test_criar_pj(self):
        # Testando criação de pessoa jurídica (PJ)
        pj = PJ(nome="Empresa XYZ", doc="98.765.432/0001-00", data_nasc="01/01/2000")
        self.assertEqual(pj.nome, "Empresa XYZ")
        self.assertEqual(pj.doc, "98.765.432/0001-00")
        self.assertEqual(pj.data_nasc, "01/01/2000")

if __name__ == "__main__":
    unittest.main()
