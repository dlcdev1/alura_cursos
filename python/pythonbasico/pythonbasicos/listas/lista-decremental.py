vetor = []
vetor_inverso = []
i = 0
while i < 10:
    n = int(input('Informe um numero:'))
    vetor.append(n)
    i += 1

print(vetor)
inverso = i-1

while inverso >= 0:
    vetor_inverso.append(vetor[inverso])
    inverso -= 1
print(vetor_inverso)
