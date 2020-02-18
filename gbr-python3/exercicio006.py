'''
Crie um algoritmo que leia um numero e moestre
seu dobro, triplo e raiz quadrada
'''
import math
number = int(input('Informe um numero: '))

print(f'O dobro é: {number*2}')
print(f'O triplo é: {number*3}')
print(f'A raiz quadrada é: {round(math.sqrt(number))} ')