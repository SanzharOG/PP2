import pygame
import time
from pygame.locals import *
import random, time
pygame.init()
pygame.mixer.music.load('rap.mp3')
pygame.mixer.music.play(-1)
FPS = 60
FramePerSec = pygame.time.Clock()
size=(840, 650)
DISPLAYSURF = pygame.display.set_mode(size)
DISPLAYSURF.fill('white')
pygame.display.set_caption("Game runner")
pygame.display.update()
FramePerSec.tick(FPS)
road_surf = pygame.image.load('1556547969.png')
car=pygame.image.load('tank.png')
x_car=355
y_car=530

process=True
while process:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            process = False
        keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x_car>125:
        x_car-=1
    if keys[pygame.K_RIGHT] and x_car<600:
        x_car+=1

    DISPLAYSURF.blit(road_surf, (0, 0))
    DISPLAYSURF.blit(car, (x_car, y_car))
    
    
    pygame.display.update()