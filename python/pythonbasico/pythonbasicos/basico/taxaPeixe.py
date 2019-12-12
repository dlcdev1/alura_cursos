while True:
    peso = int(input('- Infome o peso do Peixe:\n- Digite 0 para sair: '))

    if peso == 0:
        print('Programa finalizado: ')
        break
    if peso <= 50:
        taxa = 0
        print('Taxa: ', taxa)
    else:
        taxa = (peso - 50) * 4
        print('Total %d Reais' %taxa)
