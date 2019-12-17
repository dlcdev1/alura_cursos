import forca
import advinhacao

print("********************************")
print("*****Escolha o seu Jogo*********")
print("********************************")

print("1 - Forca:\n2 - Advinnhação: ")
jogo = int(input('Qual o jogo?'))

if jogo == 1:
    print('Jogando forca')
    forca.jogar()
else:
    print('Jogando advinhação')
    advinhacao.jogar()