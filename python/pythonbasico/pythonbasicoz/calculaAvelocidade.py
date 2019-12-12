velocidade = int(input('Informe a velocidade do carro: '))
multa = 5
limit = 110
calculo = velocidade

if(velocidade == 110):
    print(' ', multa)
elif(velocidade > 110):
    print(calculo)
    print('Você recebeu uma muta no valor de:', (velocidade - limit) * multa)
else:
    print('Não há multa')

