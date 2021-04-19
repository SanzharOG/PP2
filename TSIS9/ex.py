import pygame
import sys
import random
import pygame_menu
pygame.init()

Color = (0, 255, 204)
HEADER_COLOR = (121, 85, 61)
SNAKE_COLOR = (0, 102, 0)
BLUE=(204, 255, 255)
WHITE=(255, 255, 255)
RED = (224, 0, 0)

MARGIN=1
SIZE_BLOCK = 20
COUNT_BLOCKS = 30
HEADER_MARGIN = 70
timer = pygame.time.Clock()
size=[SIZE_BLOCK*COUNT_BLOCKS + 2*SIZE_BLOCK + MARGIN*COUNT_BLOCKS, SIZE_BLOCK*COUNT_BLOCKS + 2*SIZE_BLOCK + MARGIN*COUNT_BLOCKS + HEADER_MARGIN]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("ZHYLAN")
courier = pygame.font.SysFont("courier", 36)

class SnakeBLock:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def is_inside(self):
        return 0<=self.x<30 and 0<=self.y<30
    
    def __eq__(self, other):
        return isinstance(other, SnakeBLock) and self.x == other.x and self.y == other.y

def get_random_empty_block():
    x = random.randint(0, 29)
    y = random.randint(0, 29)
    empty_block = SnakeBLock(x, y)
    while empty_block in snake_blocks:
        empty_block.x = random.randint(0, 29)
        empty_block.y = random.randint(0, 29)
    return empty_block

process=True
def draw_block(color, row, column):
    pygame.draw.rect(screen, color, [10+column*SIZE_BLOCK+MARGIN*(column+1), 20+row*SIZE_BLOCK + MARGIN*(row+1), SIZE_BLOCK, SIZE_BLOCK])

snake_blocks=[SnakeBLock(15, 15), SnakeBLock(15, 16)]
apple = get_random_empty_block()
d_row = 0
d_col = 1
total = 0
speed = 1
while process:
    for event in pygame.event.get(): 
      if event.type==pygame.QUIT:
          pygame.quit()
          sys.exit()
      elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP and d_col!=0:
              d_row = -1
              d_col = 0
          elif event.key == pygame.K_DOWN and d_col!=0:
              d_row = 1
              d_col = 0
          elif event.key == pygame.K_LEFT and d_row!=0:
              d_row = 0
              d_col = -1
          elif event.key == pygame.K_RIGHT and d_row!=0:
              d_row = 0
              d_col = 1

    screen.fill(Color)
    text_total = courier.render(f"Total: {total}", 0, WHITE)
    screen.blit(text_total, (SIZE_BLOCK, 700))
    text_speed = courier.render(f"Speed: {speed}", 0, WHITE)
    screen.blit(text_speed, (400, 700))
    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if(row+column)%2==0:
                color = BLUE
            else:
                color = WHITE

            draw_block(color, row, column)
    head = snake_blocks[-1]

    if not head.is_inside():
        print('crash')
        pygame.quit()
        sys.exit()
    draw_block(RED, apple.x, apple.y)
    for block in snake_blocks:
        draw_block(SNAKE_COLOR, block.x, block.y)
    
    if apple == head:
        total +=1
        speed = total//5 + 1
        snake_blocks.append(apple)
        apple = get_random_empty_block()
        
    
    new_head = SnakeBLock(head.x + d_row, head.y + d_col)
    
    if new_head in snake_blocks:
        print("crash yourself")
        pygame.quit()
        sys.exit()

    snake_blocks.append(new_head)
    snake_blocks.pop(0)
    pygame.display.flip()
    timer.tick(3+speed)