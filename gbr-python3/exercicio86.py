'''
Crie um programa que crie uma matriz de dimensão 3X3
e prencha com valores lidos pelo teclado
0 [ ] [ ] [ ]
1 [ ] [ ] [ ]
2 [ ] [ ] [ ]
    0   1   2
No final mostre a matriz na tela, com a formatação correta
'''
<<<<<<< HEAD

=======
>>>>>>> c08013a3dd70cecbb2497efbae2231f45a03ad76
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
<<<<<<< HEAD
        number = int(input(f'Informe um numero para [{linha}] [{coluna}]:'))
        matriz[linha][coluna] = number
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end ='')
    print()
=======
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}] [{coluna}]: '))
print('=-=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('=-=' * 10)
>>>>>>> c08013a3dd70cecbb2497efbae2231f45a03ad76
