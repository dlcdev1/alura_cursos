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
maior = men = 0
while route != False:
    dados.append(str(input('Informe o nome: ')))
    dados.append(int(input('Informe o peso: ')))
    if len(pessoas) == 0:
        maior = men = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
    pessoas.append(dados[:])
    dados.clear()

    keep = input('Continuer [S/N] ')
    if keep == 'n' or keep == 'N':
        route = False
        print(f'Exit program')



print(f'Quatidade de pessoas cadastradas foram: {len(pessoas)}')
print(f'Pessoas mais pesadas são: {maior}')
print(f'Pessoas mais leves são: {men}')