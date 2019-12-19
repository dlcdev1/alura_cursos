import random

inteiros = []

i = 0

while i < 5:
    numero = random.randrange(1, 101)
    inteiros.append(numero)
    i += 1
print(inteiros)