notas = []

i = 0
media = 0

while i < 4:
    nota = float(input(f'Informe a {i+1}ª notas: '))
    notas.append(nota)
    i += 1
print(f'A média é {sum(notas)/i}')
