'''
Arpimore o desafio anterior, mostrando no final:
a - A soma de todos os valroes pares digitados
b - a soma do valores da terceira coluna
c - O maior valro da segunda linha.
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pair = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        number = int(input(f'Informe um numero na posição [{linha}] [{coluna}]: '))
        matriz[linha][coluna] = number
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

for linha in range(0, 3):
    for coluna in range(0, 3):
        if matriz[linha][coluna] % 2 == 0:
            pair += matriz[linha][coluna]
for linha in range(3, 3):
    for coluna in range(3, 3):
        coluna_tre = matriz[linha][coluna]


print(f'A soma dos valores pares é {pair}')
print(f'A soma dos valores da coluna 3 é {coluna_tre}')
print()


