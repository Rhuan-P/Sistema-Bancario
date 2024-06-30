class ContaBancaria:
    def __init__(self):
        self.saldo = 00.00  # Saldo inicial da conta
        self.extrato = []  # Lista para armazenar as operações no extrato

   

    def operacao(self, tipo_operacao, valor):
        # Registra uma operação no extrato
        operacao_tuple = (tipo_operacao, valor, self.saldo)
        self.extrato.append(operacao_tuple)

    def depositar(self, valor):
        # Deposita um valor na conta e registra a operação
        self.saldo += valor
        self.operacao('deposito', valor)

    def sacar(self, valor):
        if valor <= self.saldo:
            # Realiza um saque da conta e registra a operação
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

def interface(conta):
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
            return
        else:
            print("Opção inválida. Tente novamente.")

    print("Encerrando a aplicação.")

class Usuario:
    def __init__(self, cpf, nome, tel, senha):
        self.cpf = cpf
        self.nome = nome
        self.tel = tel
        self.senha = senha
        self.conta = ContaBancaria()

    def verificar_senha(self, senha):
        return senha == self.senha

def criar_usuario(cpf):

    nome = input("Digite o nome do usuário: ")
    tel = input("Digite o telefone do usuário: ")
    senha = input("Digite a senha do usuário: ")
    return Usuario(cpf, nome, tel, senha)

def interface_user():
    usuarios = []

    while True:
        print("Selecione uma opção:")
        print("1 - Acessar conta")
        print("2 - Criar conta")
        print("3 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            if not usuarios:
                print("Nenhum usuário cadastrado. Crie uma conta primeiro.")
            else:
                cpf = input("Digite o CPF do usuário: ")
                senha = input("Digite a senha do usuário: ")
                for usuario in usuarios:
                    if usuario.cpf == cpf:
                        if usuario.verificar_senha(senha):
                            interface(usuario.conta)
                            break
                        else:
                            print("Senha incorreta.")
                            break
                else:
                    print("Usuário não encontrado.")
                    continue

        elif opcao == "2":
            cpf = input("Digite o CPF do usuário: ")
            
            for usuario in usuarios:
                if usuario.cpf == cpf:
                    print("Usuário já existe.")
                    break
            else:
                usuario = criar_usuario(cpf)
                usuarios.append(usuario)
                print("Usuário criado com sucesso!")
        elif opcao == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")

    print("Encerrando a aplicação.")

interface_user()