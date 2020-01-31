'''
Arpimore o desafio anterior, mostrando no final:

a - A soma de todos os valroes pares digitados
b - a soma do valores da terceira coluna\
c - O maior valro da segunda linha.
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pair = 0
col = 0
maior = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}] [{coluna}]: '))
print('=-=' * 30)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            pair += matriz[linha][coluna]
    col += matriz[linha][2]
    maior = max(matriz[1])
    print()


print(f'A soma dos numeros pares: {pair}')
print(f'A soma da terceira colunas é: {col}')
print(f'O maior valor da linha 2 é: {maior}')
print('=-=' * 10)

