'''
Crie um programa que crie uma matriz de dimensão 3X3
e prencha com valores lidos pelo teclado
0 [ ] [ ] [ ]
1 [ ] [ ] [ ]
2 [ ] [ ] [ ]
    0   1   2
No final mostre a matriz na tela, com a formatação correta
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        number = int(input(f'Informe um numero para [{linha}] [{coluna}]:'))
        matriz[linha][coluna] = number
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end ='')
    print()