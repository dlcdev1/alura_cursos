'''mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril',
       'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
       'Outubro', 'Novembro', 'Dezembro']

print(len(mes))

data_nascimento = input('Informe a sua data de nascimento:')

resultado = int(data_nascimento[3:5]) - 1

print('A data é:', data_nascimento[0:2], 'de', mes[resultado], 'de', data_nascimento[6:11])
'''

dia, mes, ano = input('Informo a data: ').split('/')

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril'
       'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
       'Outubro', 'Novembro', 'Dezembro']
print('Voce nasceu em:')
print('%s de %s de %s' %(dia, meses[int(mes) -1], ano))