'''
Crie um programa onde o usuario possa digitar cinco valores
numericos e cadastre-os em uma lista, ja na posição correta de inserçao (sem usar o sort())

No final, mostre a lista ordenada na tela.
'''

valores = []

for i in range(0, 5):
    num = int(input('Informe um numero: '))

    if i == 0:
        valores.append(num)
    elif num <= min(valores):
        valores.insert(0, num)
    elif num >= max(valores):
        valores.append(num)
    else:
        for j in range(0, len(valores)):
            if num <= valores[j]:
                valores.insert(j, num)
                break
    print(valores)
print(f'Os valores são: {valores}')