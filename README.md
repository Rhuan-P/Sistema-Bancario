## Introdução
O projeto Sistema Bancário é uma aplicação simples implementada em Python, que permite a criação de contas bancárias, realização de depósitos e saques, e visualização de saldos e históricos de transações. O sistema suporta contas individuais (PF) e empresariais (PJ).

## Proposta
A proposta do Sistema Bancário é oferecer uma solução prática e eficiente para gerenciamento de contas bancárias. Ele facilita a criação e o gerenciamento de contas, permitindo aos usuários realizar operações básicas de forma segura e organizada.

## Funcionalidade
### Menu Principal
- **Cadastrar novo cliente:** Permite registrar um novo cliente no sistema.
- **Acessar cliente:** Permite acessar a conta de um cliente existente.
- **Sair:** Encerra a aplicação.

### Cadastro de Novo Cliente
- Solicita o nome do cliente, tipo de conta (PF ou PJ), CPF ou CNPJ, e data de nascimento.

### Acesso à Conta do Cliente
- Solicita o CPF ou CNPJ do cliente.
- Após o acesso, permite realizar depósitos, saques, visualizar saldo e histórico de transações.

## Construção
### Estrutura do Projeto
O projeto está organizado em vários módulos:

- **app/Modelo:** Contém as classes e a lógica principal.
  - **cliente.py:** Define a classe `Cliente`.
  - **user.py:** Define as classes `User`, `PF`, e `PJ`.
  - **account.py:** Define a classe `Conta`.
  - **banco.py:** Define a classe `Banco`.

- **app/interface.py:** Fornece a interface de usuário para interação com o sistema.

- **app/test:** Contém os casos de teste.
  - **test_account.py:** Testes para a classe `Conta`.
  - **test_banco.py:** Testes para a classe `Banco`.
  - **test_cliente.py:** Testes para a classe `Cliente`.
  - **test_user.py:** Testes para as classes `User`, `PF`, e `PJ`.
