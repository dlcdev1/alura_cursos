while True:
    sair = input('Para sair digite s: ')

    if sair == 's':
        break
    n1 = int(input('Informe o primeiro numero'))
    n2 = int(input('Informe o segundo numero'))
    n3 = int(input('Informe o terceiro numero'))

    if(n1 > n2 and n1 > n3):
        print('%d é o maior numero!' %n1)
    elif(n2 > n1 and n2 > 3):
        print('%d é o maior numero!' %n2)
    else:
        print('%d é o maior numero!' %n3)



