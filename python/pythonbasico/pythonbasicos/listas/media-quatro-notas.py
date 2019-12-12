vetor = []

i = 1
media = 0
while i <= 4:
    notas = int(input("Digite a nota: "))
    vetor.append(notas)
    media += notas
    i += 1
print('As notas são: ', vetor)
print('A média é: ', media / len(vetor))
