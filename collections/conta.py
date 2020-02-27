class ContaCorrent:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposit(self, valor):
        self.saldo += valor

    def __str__(self):
        return f'Codigo {self.codigo} Saldo {self.saldo}'


conta_do_gui = ContaCorrent(15)
print(conta_do_gui)

conta_do_gui.deposit(500)
print(conta_do_gui)

conta_da_dani = ContaCorrent(47685)
conta_da_dani.deposit(1000)

contas = (conta_da_dani, conta_do_gui)
contas[0].deposit(350)
contas[1].deposit(2)


for conta in contas:
    print(conta)