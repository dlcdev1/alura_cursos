consoantes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']

count = 0
i = 0
while i < len(consoantes):
    if consoantes[i] not in 'aeiou':
        count +=1
    i +=1
print(f'O total de consoantes é de: {count}')
