'''
Crie um programa onde o usuário possa digitar sete valroes numericos
e cadastre-os em um alista unica que mantenha separadas os valroes pares e impares.
No final mostre os valroes pares e imprares em ordem crescente
'''

number_list = list()
number_list_odd = list()
number_list_pair = list()

for c in range(0, 6):
    number = (int(input(f'Informe o {c}º numero: ')))
    if number % 2 == 0:
        number_list_pair.append(number)
    else:
        number_list_odd.append(number)

number_list.append(sorted(number_list_pair))
number_list.append(sorted(number_list_odd))
print(number_list)

