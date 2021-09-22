class filanormal:
    codigo:int = 0
    fila = []
    clientesatendidos = []
    senhatual:str = ""

    def gerasenhaatual(self) -> None:
        self.senhatual = f"NM{self.codigo}"

    def resetafila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo+=1

    def atualizarfila(self) -> None:
        self.resetafila()
        self.gerasenhaatual()
        self.fila.append(self.senhatual)

    def chamaclient(self, caixa:int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientesatendidos.append(cliente_atual)
        return (f'Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}')