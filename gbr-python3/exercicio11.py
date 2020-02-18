'''Faça um programa que leia a largura e a
altura de  uma parede em metros, calcule a sua área
e a quantidade de tinta necessaria para pintá-la, sabendo que cada litro de tinta,
pinta uma área de 2m'''

largura = int(input('Informe a largura da parede: '))
altura = int(input('Informe a altura da parede: '))

area = largura * altura

print(f'Serão necessário: {area / 2 } litros de tintas para pintar esta parede')

