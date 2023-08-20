class ContaBancaria:
    def __init__(self):
        self.saldo = 1000.00
        self.extrato = []

    def operacao(self, tipo, valor):
        operacao_tuple = (tipo, valor, self.saldo)
        self.extrato.append(operacao_tuple)

    def depositar(self, valor):
        self.saldo += valor
        self.operacao('deposito', valor)

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.operacao('saque', valor * -1)
        else:
            print("Saldo insuficiente. Não é possível realizar o saque.")

    def mostrar_extrato(self):
        print("Extrato:")
        print("{:<12} {:<12} {:<12}".format("Tipo", "Valor", "Saldo"))
        for operacao in self.extrato:
            tipo, valor, saldo = operacao
            if tipo == 'deposito':
                print("{:<12} {:<12.2f} {:.2f}".format("Depósito", valor, saldo))
            elif tipo == 'saque':
                print("{:<12} {:<12.2f} {:.2f}".format("Saque", valor * -1, saldo))
        print("\n Saldo atual: {:.2f}".format(self.saldo))


def interface():
    conta = ContaBancaria()

    while True:
        print("Selecione uma opção:")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Extrato")
        print("4 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor a ser depositado: "))
            conta.depositar(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor a ser sacado: "))
            conta.sacar(valor)
        elif opcao == "3":
            conta.mostrar_extrato()
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

    print("Encerrando a aplicação.")


interface()