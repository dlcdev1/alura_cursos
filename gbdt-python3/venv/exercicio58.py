'''Melhore o jogo, onde o computador vai pensar
em um numero entre 0 e 10. Só que agora o jogador vai tentar adivinhar
até acertar, mostrando no final quantos palpites foram necessários para vencer
- computador pensa em um numero entre 0 e 10
- o jogador tem que tentar acetar para parar o programa
- mostrando no final quantos palpites foram necessários para vencer
'''
import random
computador = random.randrange(0, 10)
# print(computador)

count = 0
n = 1
while n != 0:
    jogador = int(input("Chute um número: [0 a 10 ] ?"))
    if jogador != computador:
        print("Você errou! Tente novamente!")
        count +=1
    else:
        print('Você acertou!')
        print(f'Foram: {count} tentativa!' )
        n = 0

