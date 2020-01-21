import random

vetor1 = []
vetor2 = []
vetor3 = []

i = 0

while i < 10:
    n = random.randrange(1, 100)
    vetor1.append(n)
    vetor2.append(n + 1)
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])
    i += 1

print('Vetor 1: ', vetor1)
print('Vetor 2: ', vetor2)
print('Vetor 3: ', vetor3)