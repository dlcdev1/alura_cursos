salario = int(input('Informe o valor do seu salario: '))
aumento = int(input('Informe a porcentagem do aumento: %'))

porcentagem = aumento / 100
aumento = porcentagem * salario

print('O valor do aumento é de: ', aumento)
print("O novo salario é de: ", salario + aumento)


