list1 = ['Pedro', 24]
list2 = ['Maria', 19]
list3 = ['João', 32]

pessoas = list()
pessoas.append(list1)
pessoas.append(list2)
pessoas.append(list3)


print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])
totmai = totmen = 0
for p in pessoas:
    print(p[0])

galera = list()
dado = list()

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade:')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de didade.')
        totmai +=1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen +=1
        print(f'Temos {totmai} maiores e {totmen} menores de idade.')