import pygame
import math
import random
from pygame.locals import *

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

image_list = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']


class Ball:
    BALL_SIZE = 25

    def get_random_change(self):
        change = random.randint(-2, 3)
        while change == 0:
            change = random.randint(-2, 3)
        return change

    def init(self):
        self.x = random.randint(self.BALL_SIZE, SCREEN_WIDTH - self.BALL_SIZE)
        self.y = random.randint(self.BALL_SIZE, SCREEN_HEIGHT - self.BALL_SIZE)
        self.z = random.randint(0, 4)
        self.change_x = self.get_random_change()
        self.change_y = self.get_random_change()
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def move(self):
        self.x += self.change_x
        self.y += self.change_y
        if self.x > SCREEN_WIDTH - self.BALL_SIZE or self.x < self.BALL_SIZE:
            self.change_x *= -1
        if self.y > SCREEN_HEIGHT - self.BALL_SIZE or self.y < self.BALL_SIZE:
            self.change_y *= -1


size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ball Game")
done = False
clock = pygame.time.Clock()
ball_list = []
ball = Ball()
ball_list.append(ball)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            ball_list.append(Ball())
    for ball in ball_list:
        ball.move()
    screen.fill(BLACK)
    for ball in ball_list:
        image = pygame.image.load(image_list[ball.z])
        screen.blit(image, (ball.x, ball.y))
        pygame.draw.circle(screen, ball.color, [ball.x, ball.y], ball.BALL_SIZE)
    clock.tick(60)
    pygame.display.flip()
pygame.quit()