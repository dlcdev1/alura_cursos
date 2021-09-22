from fila_normal import filanormal
from fila_prioritaria import FilaPrioritaria

# fila_test = filanormal()
#
# fila_test.atualizarfila()
# fila_test.atualizarfila()
# fila_test.atualizarfila()
# fila_test.atualizarfila()
# fila_test.atualizarfila()
#
#
# print(fila_test.chamaclient(6))
# print(fila_test.chamaclient(10))

fila_test2 = FilaPrioritaria()
fila_test2.atualizar_fila()
fila_test2.atualizar_fila()
fila_test2.atualizar_fila()
fila_test2.atualizar_fila()
print(fila_test2.chama_cliente(10))
print(fila_test2.chama_cliente(1))
print(fila_test2.estatisticas('10/01/1993', 198, 'detail'))