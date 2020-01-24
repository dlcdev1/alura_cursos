# n = 1
# while n != 0:
#     n = int(input('Digite um valor: '))
#
# print('Fim')

''' Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores m ou f. Caso esteja errado faça a digitação novamente ate ter um valor correto'''

n = 1
while n != 0:
    sexo = input('Informe o sexo: ').upper()
    if sexo == 'F' or sexo == 'M':
        n = 0
        print('Fim do programa')
    else:
        print('Entrou aqui')
        n = 1