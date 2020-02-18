'''
Um professor quer sortear  um dos seus quatro alunos
para apgar o quadro. Faça um programa que ajude ele, lendo o nome deles
e escrevendo o nome do escolhido
'''
import random
name1 = 'Paulo'
name2 = 'Antonio'
name3 = 'Maria'
name4 = 'Pedro'

sorteado = random.choice([name1, name2, name3, name4])

print(f'O sorteador foi: {sorteado}')
