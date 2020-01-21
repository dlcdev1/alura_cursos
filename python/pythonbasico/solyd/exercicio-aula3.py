

router = 1

while (router > 0):

    idade = int(input('Idade:'))
    peso = float(input('Peso:'))
    altura = float(input('Altura:'))

    if(idade >= 18 and peso >= 60 and altura >= 1.79):
        print('Você esta apto!')
        print('Idade: ', idade,
              '\nPeso', peso,
              '\nAltura', altura)
        break
    else:
        print("Você não esta apto")
        print('Idade: ', idade,
              '\nPeso', peso,
              '\nAltura', altura)
        break


