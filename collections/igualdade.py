class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        return self._codigo == outro._codigo

    def deposita(self, valor):
        self._saldo += valor
    def __str__(self):
        return f">>Codigo {self._codigo} Saldo {self._saldo}<<"

conta1 = ContaSalario(37)
conta2 = ContaSalario(37)

print(conta1 == conta2)

idades = [15, 87, 32, 65, 56, 32, 49, 37]

# for i in range(len(idades)):
#     print(i, '-', idades[i])

print(list(enumerate(idades)))

for indice, idade in enumerate(idades):
    print(indice, idade)

usuarios = {("Guilherme", 37, 1981),
            ("Daniela", 31, 1987),
            ("Paulo", 39, 1979)}

for nome, idade, nascimento in usuarios:
    print(nome)

print(idades.sort())
print(idades)