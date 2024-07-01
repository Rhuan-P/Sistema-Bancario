class conta:
    def __init__(self):
        self.saldo = 0.00
        self.extrato = [] 

    def add_extrato(self,operacao,valor):
        operacao_tupla = operacao,valor
        self.extrato.append(operacao_tupla)

    def depositar(self,valor):
        print(self.saldo)
        self.saldo += valor
        print(self.saldo)
        self.add_extrato('Deposito', valor)
    
    def sacar(self,valor):
        print(self.saldo)

        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor

            else:
                print('sem saldo')

                print(self.saldo)
                self.add_extrato('Saque', valor)
        else: print('valor invalido')

    def mostrar_extrato(self):
        print(self.extrato)
        return self.extrato
        
        

  