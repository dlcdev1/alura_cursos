class FilaPrioritaria():
    codigo: int = 0
    fila = []
    clientes_atentidos = []
    senha_atual: str = ""


    def gera_senha_atual(self) -> None:
        self.senha_atual = f"PR:{self.codigo}"


    def reseta_fila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def atualizar_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atentidos.append(cliente_atual)
        return (f'Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}')

    def estatisticas(self, dia: str, agencia: int, flag: str) -> dict:
        if flag  != "detail":
            estatistica = {f'{agencia}-{dia}' : len(self.clientes_atentidos)}
        else:
            estatistica = {}
            estatistica['dia'] = dia
            estatistica['agencia'] = agencia
            estatistica['clientes_atendidos'] = self.clientes_atentidos
            estatistica['quantidade_clientes_atendidos'] = len(self.clientes_atentidos)
        return estatistica