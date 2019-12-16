arquivo = open('numero.txt', 'r')
for linha in arquivo.readlines():
    print(linha.strip())
arquivo.close()

'''with open('numero2.txt') as f:
    print(f.read())'''