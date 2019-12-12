quantidade_de_convidados = int(input('Informe a quantidade de convidados: '))
convidado = 0
lista_nomes = []

while convidado < quantidade_de_convidados:
    nomes = input('Informe o nome: ')
    lista_nomes.insert(convidado, nomes)

    convidado += 1

count = 1;
print('Lista de convidados:\n')
for nomes_confirmados in lista_nomes:
    print(count, '-', nomes_confirmados)
    count += 1

