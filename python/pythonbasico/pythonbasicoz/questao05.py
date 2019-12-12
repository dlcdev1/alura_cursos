mercadoria = int(input('Informe o preço da mercadoria: '))
desconto = int(input('Informe o valor de desconto: '))

porcentagem = desconto / 100

desconto = mercadoria * porcentagem

print('Valor do desconto é de: ', desconto)
print('Valor a pagar é de: ', mercadoria - desconto)