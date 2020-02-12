'''crie um programa onde 4 jogadores
joguem um DADO e tenha resultados aleatorios.
Guarde esses resultados em um dicionario. no final,
coloque esse dicionário em ordem, sabendoque o
vencedor tirou o maior número no dado

PRINT
VALORES SORTEADOS
 SLEEP
 O JOGADOR 1 TIROU X
 O JOGADOR 2 TIROU X
 O JOGADOR 3 TIROU X
 O JOGADOR 4 TIROU X
 O JOGADOR 5 TIROU X

 RANKING DOS JOGAROES:
 1 LUGAR: JOGADOR X COM X
 2 LUGAR: JOGADOR X COM X
 3 LUGAR
 4 LUGAR
 5 LUGAR
'''
import random
jogadas = {}
resultados = {}
ranking = {}

for numbers in range(0, 4):
    jogadas = {f"Jogador {numbers+1}": random.randint(1, 6)}
    resultados.update(jogadas)
    # print(resultados)

for k, v in resultados.items():
    print(f'O {k} Tirou: {v}')

for item in sorted(resultados, key = resultados.get):
    print(resultados.keys())
    print(f'{resultados[item]}')

print('=-='*20)
for k, v in resultados.items():
    print(k, v)

