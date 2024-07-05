from app.Modelo.banco import Banco
from colorama import init, Fore, Style

# Inicializar colorama para uso de cores no console
init(autoreset=True)

def validar_tipo(tipo):
    return tipo.upper() in ["PF", "PJ"]

def validar_valor(valor):
    try:
        valor = float(valor)
        return valor > 0
    except ValueError:
        return False

def cadastrar_cliente(banco):
    print("\n" + Fore.CYAN + "=== Cadastro de Cliente ===" + Style.RESET_ALL)
    nome = input("Digite o nome: ")
    tipo = input("Digite o tipo de conta (PF ou PJ): ")
    while not validar_tipo(tipo):
        print(Fore.RED + "Tipo de conta inválido. Tente novamente." + Style.RESET_ALL)
        tipo = input("Digite o tipo de conta (PF ou PJ): ")

    doc = input("Digite o número do CPF ou CNPJ: ")
    data_nasc = input("Digite a data de nascimento (DD/MM/AAAA): ")
    
    try:
        banco.criar_cliente(nome=nome, tipo=tipo, doc=doc, data_nasc=data_nasc)
        print(Fore.GREEN + "Cliente cadastrado com sucesso!" + Style.RESET_ALL)
        return True
    except ValueError as e:
        print(Fore.RED + f"Erro: {e}" + Style.RESET_ALL)
        return False

def acessar_cliente(banco):
    print("\n" + Fore.CYAN + "=== Acesso a Cliente ===" + Style.RESET_ALL)
    doc = input("Digite o número do CPF ou CNPJ do cliente: ")
    cliente = banco.acessar(doc)
    if cliente:
        print(Fore.GREEN + f"Cliente encontrado: {cliente.user.nome}" + Style.RESET_ALL)
        return cliente
    else:
        print(Fore.RED + "Cliente não encontrado." + Style.RESET_ALL)
        return None

def realizar_operacoes(cliente):
    while True:
        print("\n" + Fore.CYAN + "=== Operações Bancárias ===" + Style.RESET_ALL)
        print("1. Depositar")
        print("2. Sacar")
        print("3. Mostrar Saldo e Extrato")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = input("Digite o valor para depósito: ")
            while not validar_valor(valor):
                print(Fore.RED + "Valor inválido. Tente novamente." + Style.RESET_ALL)
                valor = input("Digite o valor para depósito: ")
            try:
                cliente.conta.Depositar(float(valor))
                print(Fore.GREEN + f"Depósito de R$ {valor} realizado com sucesso!" + Style.RESET_ALL)
            except ValueError as e:
                print(Fore.RED + f"Erro: {e}" + Style.RESET_ALL)
        elif opcao == "2":
            valor = input("Digite o valor para saque: ")
            while not validar_valor(valor):
                print(Fore.RED + "Valor inválido. Tente novamente." + Style.RESET_ALL)
                valor = input("Digite o valor para saque: ")
            try:
                cliente.conta.Sacar(float(valor))
                print(Fore.GREEN + f"Saque de R$ {valor} realizado com sucesso!" + Style.RESET_ALL)
            except ValueError as e:
                print(Fore.RED + f"Erro: {e}" + Style.RESET_ALL)
        elif opcao == "3":
            extrato, saldo = cliente.conta.Mostrar()
            print("\n" + Fore.CYAN + "=== Saldo e Extrato ===" + Style.RESET_ALL)
            print(f"Saldo: {Fore.GREEN}R$ {saldo:.2f}" + Style.RESET_ALL)
            print("Extrato:")
            for operacao, valor in extrato:
                print(f"{operacao}: {Fore.GREEN}R$ {valor:.2f}" + Style.RESET_ALL)
        elif opcao == "4":
            break
        else:
            print(Fore.RED + "Opção inválida. Tente novamente." + Style.RESET_ALL)

def interface_principal():
    banco = Banco()
    
    while True:
        print("\n" + Fore.CYAN + "=== Menu Principal ===" + Style.RESET_ALL)
        print("1. Cadastrar novo cliente")
        print("2. Acessar cliente")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            if cadastrar_cliente(banco):
                print(Fore.GREEN + "Cadastro realizado com sucesso!" + Style.RESET_ALL)
        elif opcao == "2":
            cliente = acessar_cliente(banco)
            if cliente:
                realizar_operacoes(cliente)
        elif opcao == "3":
            print(Fore.YELLOW + "Saindo..." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Opção inválida. Tente novamente." + Style.RESET_ALL)

if __name__ == "__main__":
    interface_principal()
