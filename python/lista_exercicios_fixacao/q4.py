'''
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
'''

i = 0
media = 0

while i < 4:
    print('Pass the {} note: '.format(i+1))
    number = int(input())
    media += number
    i += 1
print(i)
print('Avarage of number is: {}'.format(media/i))