

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print('Construindo objeto....{}'.format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print('Saldo {} do titula {}'.format(self.saldo, self.titular))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.valor -= valor
    datas.d
