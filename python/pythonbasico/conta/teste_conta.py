from cliente import Cliente
from contaC import Conta

joao = Cliente('João da silva', '777-1234')
maria = Cliente('Maria da Silva', '555-4321')

print('Nome: %s. Telefone: %s.' %(joao.nome, joao.telefone))
print('Nome: %s. Telefone: %s.' %(maria.nome, maria.telefone))

conta1 = Conta([joao], 1, 1000)
conta2 = Conta([maria, joao], 2, 500)
conta1.resumo()
conta2.resumo()
