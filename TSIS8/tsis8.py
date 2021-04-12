import pygame
from pygame.locals import *
import random, time
import math

FPS = 60
FramePerSec = pygame.time.Clock()
pygame.init()
# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 650
SCREEN_HEIGHT = 840
SPEED = 5
SCORE = 0
COIN_SCORE = 0
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("1556547969.png")

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((840, 650))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("car.png")
        self.surf = pygame.Surface((42, 70))
        self.rect = self.surf.get_rect(center=(random.randint(100, SCREEN_WIDTH - 40)
                                               , 0))

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(100, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("tank.png")
        self.surf = pygame.Surface((40, 75))
        self.rect = self.surf.get_rect(center=(160, 550))

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    def get_random_speed(self):
        speed = random.randint(1, 3)
        return speed

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.surf = pygame.Surface((32, 32))
        self.rect = self.surf.get_rect(center=(random.randint(100, SCREEN_WIDTH - 40), 0))
        self.speed = self.get_random_speed()

    def move(self):
        global COIN_SCORE
        self.rect.move_ip(0, self.speed)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(100, SCREEN_WIDTH - 40), 0)
            self.speed = self.get_random_speed()
        if pygame.sprite.spritecollideany(P1, coins):
            COIN_SCORE += 1
            pygame.mixer.Sound('coin-drop-4.mp3').play()
            self.rect.top = 0
            self.rect.center = (random.randint(100, SCREEN_WIDTH - 40), 0)
            self.speed = self.get_random_speed()


# Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()
# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game Loop
process = True
while process:

    # Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.1
        if event.type == QUIT:
            pygame.quit()
            process = False

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render("SCORE: " + str(SCORE), True, RED)
    coinscore = font_small.render("COINS: " + str(COIN_SCORE), True, 'yellow')
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coinscore, (10, 30))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('gameover.mp3').play()
        time.sleep(0.5)
        stop = pygame.image.load("gameover1.jpg")
        DISPLAYSURF.blit(stop, (0, 0))
        DISPLAYSURF.blit(scores, (0, 0))
        DISPLAYSURF.blit(coinscore, (0, 30))
       
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(5)

    pygame.display.update()
    FramePerSec.tick(FPS)