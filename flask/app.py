from flask import Flask

nome = input('Informe um nome: ')
valor = int(input('Informe  um valor'))
print(f'Seu nome é {nome}')


def verificar_valor(valor):
    if valor < 10:
        print(valor)
