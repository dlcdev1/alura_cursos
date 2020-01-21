class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes +=1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        print(f'{self._nome} - {self.ano} - {self._likes}')


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super(Filme, self).__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.duracao} min - {self.ano} - {self._likes}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super(Serie, self).__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.temporadas} temporadas - {self.ano} - {self._likes}'

class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    @property
    def __len__(self):
        return len(self._programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em panico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()

demolidor.dar_like()
vingadores.dar_like()
vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playslist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'{len(playslist_fim_de_semana)}')

print(vingadores in playslist_fim_de_semana)
for programa in filmes_e_series:
    #(if ternario) detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
    print(programa)


# for programa in playslist_fim_de_semana.listagem:
#     print(programa)
