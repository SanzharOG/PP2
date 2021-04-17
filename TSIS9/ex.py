import pygame
Color = (0, 255, 204)
BLUE=(204, 255, 255)
WHITE=(255, 255, 255)
size=[800, 800]
SIZE_BLOCK = 20
COUNT_BLOCKS = 30
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Zhylan")
MARGIN=1
process=True
while process:
    for event in pygame.event.get(): 
      if event.type==pygame.QUIT:
          pygame.quit()

    screen.fill(Color)
    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if(row+column)%2==0:
                color = BLUE
            else:
                color = WHITE
            pygame.draw.rect(screen, color, [10+column*SIZE_BLOCK+MARGIN*(column+1), 20+row*SIZE_BLOCK + MARGIN*(row+1), SIZE_BLOCK, SIZE_BLOCK])
    pygame.display.flip()