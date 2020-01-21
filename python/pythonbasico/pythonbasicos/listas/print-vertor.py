'''vetor = [8, 10, 20, 9 , 50]
numeros = 0

while numeros < len(vetor):
    print('Vetor', numeros, 'é igua a %d' %vetor[numeros])
    numeros += 1
'''

vetor = []
i = 1

while i <= 5:
    n = int(input('Digite um número: '))
    vetor.append(n)
    i +=1
print('Vetor lido: ', vetor)