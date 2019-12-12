while True:
    sair = input('Informe s para sair: ')
    if sair == 's':
        print('Fim do programa: ')
        break

    n1 = int(input('Informe o primeiro numero: '))
    n2 = int(input('Informe o segundo numero: '))
    n3 = int(input('Informe o terceiro numero: '))

    if n1 > n2 and n1 > n3:
        print('%d é o maior numero: ' %n1)
        if n2 < n3:
            print('%d é o menor numero:' %n2)
        else:
            print('%d é o menor numero' %n3)
    elif n2 > n3:
        print('%d é o maior numero' %n2)
        if n1 < n3:
            print('%d é o menor numero' %n1)
        else:
            print('%d é o menor numero' %n3)
    else:
        print('%d é o maior numero ' %n3)
        if(n1 < n2):
            print('%d é o menor numero' %n1)
        else:
            print('%d é o menor numero' %n2)
