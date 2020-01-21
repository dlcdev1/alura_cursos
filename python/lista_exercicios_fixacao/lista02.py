import random

inteiros = []
inverte = []

i = 0


while i < 10:
    numeros = random.randrange(1, 10)
    inteiros.append(numeros)
    i += 1
print(inteiros)

while i >= 1:
    inverte.append(inteiros[i-1])
    i -=1
print(inverte)