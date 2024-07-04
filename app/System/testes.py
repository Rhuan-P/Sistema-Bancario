'''import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(dir_path,'..'))
'''
from Modelo import User
jao= User.PF(nome='jao',tipo='PF',dif=123,data_nasc='10/01/1999')
jao.mostrar()

#maria = Cliente(nome='Maria',dif='987.654.321-00', data_nasc='15/06/1990')
#pedro = Cliente(nome='Pedro',dif='111.222.333-44', data_nasc='10/03/1975')

# Criando instâncias da classe PJ com atributos específicos
'''empresa_a = PJ(nome='Empresa A', dif='12.345.678/0001-90', data_nasc='05/07/2000')
empresa_b = PJ(nome='Empresa B', dif='98.765.432/0001-10', data_nasc='20/11/2010')
empresa_c = PJ(nome='Empresa C', dif='11.22.33/0001-44', data_nasc='15/09/1998')

#login = filter( lambda cliente:cliente.cpf == 42, lista_clientes)
#acess= list(login)[0]'''