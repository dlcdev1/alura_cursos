from collections import defaultdict
usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = []
assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)


# print(assistiram)
# print(len(assistiram))
#
# print(set(assistiram))

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}


# print("Here", usuarios_machine_learning - usuarios_data_science)
# print("Here", usuarios_machine_learning | usuarios_data_science)
# print("Here", usuarios_machine_learning + usuarios_data_science)

usuarios = {"Guilherme" : 1, "Paulo" : 2, "Sandra" : 3, "Antonio" :4}
print(type(usuarios))

print([f"Palavara {chave}" for chave in usuarios.items()])

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()

# default
aparicoes = defaultdict(int)

for palavra in meu_texto.split():
    aparicoes[palavra] += 1
print(aparicoes)

