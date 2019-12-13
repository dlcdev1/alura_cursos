import random

lista = []
i = 0
maior = 0
menor = 100


while i < 10:
    n = random.randrange(1, 101)
    print(n)
    lista.append(n)
    numero = lista[i]

    if numero > 0:
        if numero >= maior:
            maior = numero
        elif numero < menor:
            menor = numero
    i += 1
print(lista)
print('O maior número é: %d' %maior)
print('O menor número é: %d' %menor)



