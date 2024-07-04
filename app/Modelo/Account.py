class Conta:
    def __init__(self):
        self.saldo = 0.00
        self.extrato = []

    def Add_Extrato(self, operacao, valor):
        operacao_tupla = operacao, valor
        self.extrato.append(operacao_tupla)

    def Depositar(self, valor):
        self.saldo += valor
        self.add_extrato("Deposito", valor)

    def Sacar(self, valor):

        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor

            else:
                print("sem saldo")

                print(self.saldo)
                self.add_extrato("Saque", valor)
        else:
            print("valor invalido")

    def Mostrar(self):

        return self.extrato, self.saldo
