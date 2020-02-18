'''
Crie um programa que vai ler varios numeros
e colocar em uma lista.

Depois disso, mostre:

a) Quantos numeros foram digitados

b) a lista de valoes ordenada de forma decrescente.

c) se o valor 5 foi digitado e esta ou não na lista.
'''

router = True
number_list = list()
keep = ' '

while router != False:
    number = (int(input('Pass a new number: ')))
    if number not in number_list:
        number_list.append(number)
    else:
        print('Invalid number')

    keep = input('Isert a new nubmer: [S/N]: ')
    if keep == 'n' or keep == 'N':
        router = False
        print('Exit program')

print(f'Foram digitados: {len(number_list)}')
number_list.sort(reverse=True)
print(f'Decrescente {number_list}')

if 5 in number_list:
   print('O valor 5 esta na lista')
else:
   print('O valor 5 não esta na lista')
