minutos = int(input('Informe a quantidade de minutos: '))

if minutos <= 200:
    preco = 0.20
    print('0.20 caculo')
elif minutos <= 400:
        preco = 0.18
        print('0.18 caculo')
elif minutos < 800:
        preco = 0.15
        print('0.15 caculo')
elif minutos >= 800:
        preco = 0.08
        print('0.08 caculo')

print('O valor a ser pago é de:', preco * minutos)

