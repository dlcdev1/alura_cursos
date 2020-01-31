'''crie um progrma onde 4 jogadores
joguem um DADO e tenha resultados aleatorios.
Guarde esses resultados em um dicionario. no final, coloque esse dicionário em ordem, sabendoque o
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
jogadas = { }
for numbers in range(0, 4):
    print(numbers)
    jogadas = {f"Jogador{numbers}": random.randrange(1, 6)}

print(jogadas)