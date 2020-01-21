texto = open('arquivo_strings.txt')
saida = open('textoSalvo2', 'w')
for linha in texto.readlines():
    for letra in linha:
        if letra in 'aeiou':
            saida.write('*')
        else:
            saida.write(letra)
texto.close()
saida.close()

with open('textoSalvo2') as f:
    print(f.read())
