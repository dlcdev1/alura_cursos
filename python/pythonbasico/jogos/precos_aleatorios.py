import random
precos = []

i = 0
while i <= 10:
    numeros = random.randrange(1, 1000)
    precos.append(numeros)
    i += 1
print(precos)

print('O maior preço é %d' %max(precos))
print('O menor preço é %d' %min(precos))
print('Total de numeros é %d' %len(precos))
