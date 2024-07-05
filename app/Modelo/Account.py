class Conta:
    def __init__(self):
        self.saldo = 0.00
        self.extrato = []

    def add_extrato(self, operacao, valor):
        operacao_tupla = (operacao, valor)
        self.extrato.append(operacao_tupla)

    def Depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor de depósito deve ser positivo.")
        self.saldo += valor
        self.add_extrato("Depósito", valor)

    def Sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor de saque deve ser positivo.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente.")
        self.saldo -= valor
        self.add_extrato("Saque", valor)

    def Mostrar(self):
        return self.extrato, self.saldo
