
x = '0123456789'
print(x)
print(x[0:2])
data = '25/11/1982'
print(data[0:2])
print(x[2:4])
print(x[0:5])
print(x[1:8])

print('=====')
print(x[:2])
print(x[4:])
print(x[4:-1])
print(x[-4:-1])
print(x[:])


texto = 'batatinha quando nasce'
print(texto[::2])
print(texto[::-1])



palavra = input('Palavra')

if palavra == palavra[::-1]:
    print('%s é palíndrome' %palavra)
else:
    print('%s não é palindrome' %palavra)