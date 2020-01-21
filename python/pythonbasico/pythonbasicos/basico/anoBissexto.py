
while True:
    ano = int(input('- Informe o ano: \n- Para sair digite 0 para sair: '))
    if ano == 0:
        break
    if ano % 4 == 0 and ano % 100 !=0 or ano% 400 == 0:
        print('%d É um ano bissexto possui 29 dias' %ano)
    else:
        print('Não é um ano bissexto o ano %d 28 dias' %ano)