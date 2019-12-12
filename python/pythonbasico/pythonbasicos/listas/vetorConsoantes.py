'''
Faça um Programa que leia umvetor de 10
caracteres minúsculos, e diga quantas consoantes foram lidas.
'''


consoante = input("Informe a palavra com 10 letras")

if consoante.__contains__('a' and 'e' and 'i' and 'o' and 'u'):
        print('o total de consoantes é de:', consoante.count())

