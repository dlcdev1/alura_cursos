''''
Faça um programa que leia 5 valores
numericos e guarde os em uma lista.

No final, moestre qual foi o maio e o menos
valro digitado e as suas repectivas posiçoes na lista'''

list_number = list()

for count in range(0, 5):
    list_number.append(int(input('Pass a number:')))

print(max(list_number))
print(min(list_number))
