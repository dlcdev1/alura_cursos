'''Faça um programa em Python qu eabra e reproduza o áudio de um arquivo MP3'''
import pygame
import os

# Inicializando o PyGame
pygame.init()


pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
pygame.event.wait()

#
# # Carregando o arquivo MP3 e executando
# if os.path.exists('music.mp3'):
#     pygame.mixer.music.load('music.mp3')
#     pygame.mixer.music.play()
#     pygame.mixer.music.set_volume(1)
#
#     clock = pygame.time.Clock()
#     clock.tick(1)
#
#     while pygame.mixer.music.get_busy():
#         pygame.event.poll()
#         clock.tick(10)
# else:
#     print('O arquivo musica.mp3 não está no diretório do script Python')