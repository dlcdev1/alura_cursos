'''
Cria um programa que leia nome e duas notas de várias alunos e guarde tudo em uma lista composta
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
notas de cada aluno individualmente
'''
dados = list()
alunos = list()
media_list = list()
router = True
media = 0
count = 0
soma = 0
while router != False:
    count +=1
    nome = input('Informe o nome: ')
    dados.append(nome)
    for linha in range(0, 2):
        nota = int(input(f'Infome a {linha+1}º nota: '))
        dados.append(nota)
    alunos.append(dados[:])
    dados.clear()

    keep = input('Deseja continuar [S/N]: ')
    if keep == 'n' or keep == 'N':
        router = False
        print('Fim do programa')

print("-="*20)
print("Boletim Escolar")

for linha in range(0, count):
    soma = sum(alunos[linha][1:2] + alunos[linha][2:3])
    print(f'Nome:{alunos[linha][0:1]}')
    print(f'A media é {soma/2}')
    print("=="*20)

