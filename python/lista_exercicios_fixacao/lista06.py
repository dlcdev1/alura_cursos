
class Alunos:

    def __init__(self, nome, notas):
        print('Construtor aluno')
        self.nome = nome
        self.notas = notas

    def somar_notas(self, notas):
        self.notas += notas

    def devolver_calculo_notas(self, media):
       media = self.notas / 4
       return media

i = 0
a = 0
notas = []

aluno1 = Alunos('Paulo', 10)
print(aluno1.nome)
print(aluno1.notas)