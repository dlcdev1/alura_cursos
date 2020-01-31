'''
Faça um program que ajude um jogador da MEGA SENA a criar palpites
O programa vai perguntar quantos jogos serão gerados e vair sortear 6 númereos
entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta.
'''

import random
sorted_list = list()
list_number = list()
count_list = int(input('Informe a quantidade jogos? '))

for list in range(0, count_list):
    for numbers in range(0, 6):
        list_number.append(random.randrange(1, 60))
    sorted_list.append(list_number[:])
    list_number.clear()

for linha in range(0, count_list):
    print(f'{sorted(sorted_list[linha])}')