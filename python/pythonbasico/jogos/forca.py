def jogar():
    print("********************************")
    print("Bem vindo no jodo Forca ")
    print("********************************")

    palavra_secreta = 'banana'
    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        chute = input('Qual letra? ')
        chute = chute.strip().upper()
        index = 1
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                print('Encontrei a letra {} na posição {} '.format(letra, index))
            index += 1

    print('Fim do jogo')

if __name__ == '__main__':
    jogar()