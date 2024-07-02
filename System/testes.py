from User_List import Cliente

# Criando instâncias da classe PF com atributos específicos
jao = Cliente('PJ','João','123.456.789-00', '01/01/1980')
maria = Cliente('Pf','Maria', '987.654.321-00', '15/06/1990')
pedro = Cliente('pf','Pedro', '111.222.333-44', '10/03/1975')

jao.Conta.depositar(100)
jao.Conta.sacar(9)

jao.Conta.mostrar_extrato()

maria.Conta.sacar(-100)
maria.Conta.mostrar_extrato()

jao.User.mostrar()
maria.User.mostrar()


#maria = Cliente(nome='Maria',dif='987.654.321-00', data_nasc='15/06/1990')
#pedro = Cliente(nome='Pedro',dif='111.222.333-44', data_nasc='10/03/1975')

# Criando instâncias da classe PJ com atributos específicos
'''empresa_a = PJ(nome='Empresa A', dif='12.345.678/0001-90', data_nasc='05/07/2000')
empresa_b = PJ(nome='Empresa B', dif='98.765.432/0001-10', data_nasc='20/11/2010')
empresa_c = PJ(nome='Empresa C', dif='11.22.33/0001-44', data_nasc='15/09/1998')



#login = filter( lambda cliente:cliente.cpf == 42, lista_clientes)
#acess= list(login)[0]'''