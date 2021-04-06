import pygame
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
road_rect = road_surf.get_rect()
DISPLAYSURF.blit(road_surf, road_rect)
process=True
while process:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            process = False
    while pygame.event.wait().type !=pygame.QUIT:
           pygame.display.flip()
    pygame.quit()