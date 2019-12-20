import random
par = []
impar = []
numeros = []

i = 0

while i < 20:
    n = random.randrange(1, 1000)
    recebe_numeros = numeros.append(n)
    i += 1
i -= 1
while i >= 0 :
    recebe_numeros = numeros[i]

    if recebe_numeros % 2 == 0:
        par.append(recebe_numeros)
    else:
        impar.append(recebe_numeros)
    i -= 1
print(f'Numeros: {numeros}')
print(f'Números pares: {par}')
print(f'Numeros impares: {impar}')