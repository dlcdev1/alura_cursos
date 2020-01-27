'''
Faça um algoritmo que leia a preço de um produto e mostre
seu novo preço, com 5% de desconto
'''

produto = int(input('Informe o valor do produto: '))

print(f'O valor do produto com 5% de deconto é: {produto - (produto * 0.05)}')