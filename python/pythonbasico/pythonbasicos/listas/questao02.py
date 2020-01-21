import random

sorteio = []
lista_par = []
lista_impar = []
impar = 0
par = 0
i = 0

while i < 20:
    n = random.randrange(1, 100)
    sorteio.append(n)

    if sorteio[i] % 2 == 0:
        lista_par.append(sorteio[i])
    else:
        lista_impar.append(sorteio[i])
    i += 1
print('Total da lista é de: %d números' %len(sorteio))
print('Lista dos numeros:', sorteio)
print('Lista dos numeros pares:', lista_par)
print('Lista dos números impares: ', lista_impar)







