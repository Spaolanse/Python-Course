import pygame
pygame.mixer.init()
pygame.mixer.music.load('music.mp3.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
