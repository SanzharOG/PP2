import pygame
import random
import time
screen = pygame.display.set_mode((800, 600))


def get_random_speed():
    speed = random.randint(1, 3)
    return speed


class Coin(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("123.jpg")
        self.surf = pygame.Surface((32, 32))
        self.rect = self.surf.get_rect(center=(random.randint(40, 600 - 40), 0))
        self.speed = get_random_speed()

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, 600 - 40), 0)
            self.speed = get_random_speed()


while True:
    C1 = Coin()
    entities = pygame.sprite.Group()
    entities.add(C1)
    screen.fill((50, 50, 50))
    for entity in entities:
        entity.move()
        screen.blit(entity.image, entity.rect)
    pygame.display.flip()