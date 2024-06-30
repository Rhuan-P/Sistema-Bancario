class conta:
    def __init__(self):
        self.saldo = 0.00
        self.extrato = []

    def depositar(self,valor):
        print(self.saldo)
        self.saldo += valor
        print(self.saldo)

        
        

  