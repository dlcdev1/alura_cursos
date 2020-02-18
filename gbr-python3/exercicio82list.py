'''
Crie um programa que vai ler vários números e colocar em uma lista

Depis disso, crie duas listas extras que vão conter apenas os valroes PARES e os valores IMPARES digitados, respectivamente

Ao final, mostre o conteúdo das tres listas geradas.
'''
number_list = list()
list_pair = list()
list_odd = list()
router = True
# keep = ' '
while router != False:
    number = int(input('Passa a new number: '))
    number_list.append(number)

    keep = input('Continue [S / N]')
    if keep == 'n' or keep == 'N':
        router = False
        print('Exite program')

for number_pair_or_odd in number_list:
    if number_pair_or_odd % 2 == 0:
        list_pair.append(number_pair_or_odd)
    else:
        list_odd.append(number_pair_or_odd)

print(f'List number all: {number_list}')
print(f'List number pair: {list_pair}')
print(f'List number odd: {list_odd}')