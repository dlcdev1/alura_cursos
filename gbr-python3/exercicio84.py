'''
Faça um programa que leia nome e pseso de várias pessoas,
guardando tudo em uma lista. No final, mostre
a - Quantas pessoas foram cadastradas
b - uma listagem com as pessoas mais pesadas
c - um lista com as pessoas maisleves.
'''

route = True
keep = ''
pessoas = list()
dados = list()
pessoas_pesadas = list()
pessoas_leves = list()
while route != False:
    dados.append(str(input('Informe o nome: ')))
    dados.append(int(input('Informe o peso: ')))
    pessoas.append(dados[:])
    dados.clear()

    keep = input('Continuer [S/N] ')
    if keep == 'n' or keep == 'N':
        route = False
        print(f'Exit program')

for peso in pessoas:
    print(peso[1])
    if peso[1] >= 90:
        pessoas_pesadas.append(peso)
    elif peso[1] <= 70:
        pessoas_leves.append(peso)



print(f'Quatidade de pessoas cadastradas foram: {len(pessoas)}')
print(f'Pessoas mais pesadas são: {pessoas_pesadas}')
print(f'Pessoas mais leves são: {pessoas_leves}')