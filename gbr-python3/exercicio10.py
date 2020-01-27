'''
Crie um programa que leia quanto dinheiro uma pesoa
tem na carteira e mostre quantos Dólares ela pode comprar.
'''
money = float(input('Informe a quantidade de dinheiro: '))
dollar = float(input('Informe o valor atual do dolar: '))

print(f'Voce pode comprar: {round(money / dollar)} dollares')