class conta:
    def __init__(self):
        self.saldo = 0.00
        self.extrato = [] 

    def add_extrato(self,operacao,valor):
        operacao_tupla = operacao,valor
        self.extrato.append(operacao_tupla)

    def depositar(self,valor):
        self.saldo += valor
        self.add_extrato('Deposito', valor)
    
    def sacar(self,valor):
      

        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor

            else:
                print('sem saldo')

                print(self.saldo)
                self.add_extrato('Saque', valor)
        else: print('valor invalido')

    def mostrar(self):
        
        return self.extrato, self.saldo
        
        

  