import time

import pygame
import random
from pygame.locals import * 
from sys import exit


pygame.init() 

largura = 800
altura = 600
x = altura/2
y = altura/2


tela = pygame.display.set_mode((largura, altura))
nome_tela = pygame.display.set_caption('Jogo') 
relogio = pygame.time.Clock()
xMoeda = 60
yMoeda = 60
Moeda = True

while True:
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == WINDOWCLOSE:
            print('CONSOLE LOGS')
            print('Janela fechada')
        if event.type == KEYDOWN: 
            if event.key == K_s: 
                y = y + 5
            if event.key == K_w:
                y = y - 5
            if event.key == K_d:
                x = x + 5
            if event.key == K_a:
                x = x - 5
        if x and y == xMoeda and yMoeda:
            Moeda = False
    relogio.tick(75)
    if Moeda == True:
        pygame.draw.rect(tela, (255, 0, 0), (xMoeda, yMoeda, 40, 50))
    else:
        pass
    pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))
    pygame.display.update()
