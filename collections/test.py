from collections import counter
# conjunto = {"paulo", "david", "Antonio", "sandra"}
# print(conjunto)
#
# usuarios_data_science = {15, 23, 43, 56}
# usuarios_machine_learning = {13, 23, 56, 42}
#
# print(usuarios_data_science & usuarios_machine_learning)

usuarios = {"Guilherme" : 1, "Paulo" : 2, "Sandra" : 3, "Antonio" :4}
print([f"Palavara {chave}" for chave in usuarios.items()])
print(usuarios.get("Guilherme"))