'''arquivo = open('numero.txt', 'r')
for linha in arquivo.readlines():
    print(linha.rstrip())
arquivo.close()'''

with open('numeros2.txt') as f:
    print(f.read())