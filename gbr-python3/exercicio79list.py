'''
Crie um progrma onde o usuario possa digitar vários valores numéricos e cadastre-os
em  uma lista. Caso o numero já exista lá dentro, ele não sera adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

'''

router = True
number_list = list()
keep = ' '
while router != False:
    number = int(input('Pass a number: '))
    if number not in number_list:
        number_list.append(number)
    else:
        print('This number not exist:')
    keep = input('Insert a new nubmer: [S/N]')
    if keep  == 'n' or keep == 'n':
        router = False
        print('Exit program!!!!')
print(sorted(number_list))

