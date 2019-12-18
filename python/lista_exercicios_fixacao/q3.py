'''
Faça um Programa que peça dois números e imprima a soma.
'''

i = 0
sum = 0
while i < 2:
    n1 = int(input('Pass number: '))
    sum += n1
    i += 1

print('Sum of two number {}'.format(sum))