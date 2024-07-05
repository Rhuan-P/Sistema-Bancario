import unittest

def run_tests():
    # Descobre e carrega todos os testes do diretório 'app/test'
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('app/test', pattern='test_*.py')

    # Cria um TestRunner com saída detalhada
    test_runner = unittest.TextTestRunner(verbosity=2)
    
    # Executa a suíte de testes
    test_runner.run(test_suite)

if __name__ == '__main__':
    run_tests()
