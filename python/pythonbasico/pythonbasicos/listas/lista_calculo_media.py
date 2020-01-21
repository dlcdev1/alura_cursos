
while True:

    fim = input('Informe s para sair')
    if fim == 's':
        break

    n1 = int(input('Informe a primeira nota: '))
    n2 = int(input('Informe a segunda nota: '))
    n3 = int(input('Informe a terceira nota: '))
    n4 = int(input('Informe a quarta nota: '))
    n5 = int(input('Informe a quinta nota: '))

    notas = [n1, n2, n3, n4, n5]

    total = 0
    for soma in notas:
        total += soma

    print('A média é de %d' %(total / len(notas)))



