import pygame
import sys
import random
import pygame_menu
pygame.init()

bg_image = pygame.image.load("unnamed.jpg")
Color = (0, 255, 204)
HEADER_COLOR = (121, 85, 61)
SNAKE_COLOR = (0, 102, 0)
BLUE=(204, 255, 255)
WHITE=(255, 255, 255)
RED = (224, 0, 0)
#pygame.mixer.Sound('music.mp3').play(-1)
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

class SnakeBLock1:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def is_inside(self):
        return 0<=self.x<30 and 0<=self.y<30
    
    def __eq__(self, other):
        return isinstance(other, SnakeBLock) and self.x == other.x and self.y == other.y



process=True
NO=[[15, 1], [15, 2], [15, 3], [15, 4], [15, 5], [15, 6], [15, 0], [15, 29], [15, 28], [15, 27], [15, 26], [15, 25], [15, 24], [15, 23], [0, 15],
        [1, 15], [2, 15], [3, 15], [4, 15], [5, 15], [6, 15], [7, 15], [8, 15], [9, 15], [10, 15], [11, 15], [12, 15], [13, 15], [14, 15], [29, 15], [28, 15], [27, 15], [26, 15], [25, 15], [24, 15], [23, 15], [22, 15], [21, 15], [20, 15]]
def draw_block(color, row, column):
    if [10+column*SIZE_BLOCK+MARGIN*(column+1), 20+row*SIZE_BLOCK + MARGIN*(row+1), SIZE_BLOCK, SIZE_BLOCK] not in NO:
     pygame.draw.rect(screen, color, [10+column*SIZE_BLOCK+MARGIN*(column+1), 20+row*SIZE_BLOCK + MARGIN*(row+1), SIZE_BLOCK, SIZE_BLOCK])

def start_the_game():

    def get_random_empty_block():
        x = random.randint(0, 29)
        y = random.randint(0, 29)
        empty_block = SnakeBLock(x, y)
        while empty_block in snake_blocks:
           empty_block.x = random.randint(0, 29)
           empty_block.y = random.randint(0, 29)
        return empty_block

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
            pygame.mixer.Sound('gameover.mp3').play()
            print('crash')
            break
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
            pygame.mixer.Sound('gameover.mp3').play()
            print("crash yourself")
            break
        snake_blocks.append(new_head)
        snake_blocks.pop(0)
        pygame.display.flip()
        timer.tick(3+speed)
def start_the_game1():
    
    def get_random_empty_block():
        x = random.randint(0, 29)
        y = random.randint(0, 29)
        empty_block = SnakeBLock(x, y)
        while empty_block in snake_blocks:
           empty_block.x = random.randint(0, 29)
           empty_block.y = random.randint(0, 29)
        return empty_block
    def get_random_empty_block1():
        x = random.randint(0, 29)
        y = random.randint(0, 29)
        empty_block1 = SnakeBLock1(x, y)
        while empty_block1 in snake_blocks1:
           empty_block1.x = random.randint(0, 29)
           empty_block1.y = random.randint(0, 29)
        return empty_block1

    snake_blocks=[SnakeBLock(15, 15), SnakeBLock(15, 16)]
    snake_blocks1=[SnakeBLock(20, 20), SnakeBLock(20, 21)]
    apple = get_random_empty_block()
    apple = get_random_empty_block1()
    d_row = 0
    d_col = 1
    d_row1 = 0
    d_col1 = 1
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
            elif event.key == pygame.K_w and d_col1!=0:
                    d_row1 = -1
                    d_col1 = 0
            elif event.key == pygame.K_s and d_col1!=0:
                    d_row1 = 1
                    d_col1 = 0
            elif event.key == pygame.K_d and d_row1!=0:
                    d_row1 = 0
                    d_col1 = 1
            elif event.key == pygame.K_a and d_row1!=0:
                    d_row1 = 0
                    d_col1 = -1   
            

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
        head1 = snake_blocks1[-1]

        if not head.is_inside():
            pygame.mixer.Sound('gameover.mp3').play()
            print('crash')
            break
        if not head1.is_inside():
            pygame.mixer.Sound('gameover.mp3').play()
            print('crash')
            break
        draw_block(RED, apple.x, apple.y)
        draw_block(RED, apple.x, apple.y)
        for block in snake_blocks:
            draw_block(SNAKE_COLOR, block.x, block.y)
        for block1 in snake_blocks1:
            draw_block(SNAKE_COLOR, block1.x, block1.y)
        
        if apple == head:
            total +=1
            speed = total//5 + 1
            snake_blocks.append(apple)
            apple = get_random_empty_block()

        if apple == head1:
            total +=1
            speed = total//5 + 1
            snake_blocks1.append(apple)
            apple = get_random_empty_block1()
            
        
        new_head = SnakeBLock(head.x + d_row, head.y + d_col)
        new_head1 = SnakeBLock1(head.x + d_row1, head.y + d_col1)
        
        if new_head in snake_blocks:
            pygame.mixer.Sound('gameover.mp3').play()
            print("crash yourself")
            break
        if new_head1 in snake_blocks1:
            pygame.mixer.Sound('gameover.mp3').play()
            print("crash yourself")
            break
        if new_head in snake_blocks1:
            pygame.mixer.Sound('gameover.mp3').play()
            print("crash yourself")
            break
        if new_head1 in snake_blocks:
            pygame.mixer.Sound('gameover.mp3').play()
            print("crash yourself")
            break
        snake_blocks.append(new_head)
        snake_blocks.pop(0)
        snake_blocks1.append(new_head1)
        snake_blocks1.pop(0)
        pygame.display.flip()
        timer.tick(3+speed)
def start_the_game2():
    
    def get_random_empty_block():
        x = random.randint(0, 29)
        y = random.randint(0, 29)
        empty_block = SnakeBLock(x, y) 
        while empty_block in snake_blocks:
           empty_block.x = random.randint(0, 29)
           empty_block.y = random.randint(0, 29)
        return empty_block

    snake_blocks=[SnakeBLock(15, 15), SnakeBLock(15, 16)]
    apple = get_random_empty_block()
    d_row = 0
    d_col = 1
    total = 0
    speed = 2
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
        def wall():
         for row in range(15):
            draw_block('black', row, 15)
         for row in range (10):
            draw_block('black', 29-row, 15)
         for column in range (7):
            draw_block('black', 15, column)
         for column in range (7):
            draw_block('black', 15, 29-column)
        wall()    
        head = snake_blocks[-1]

        if not head.is_inside():
            pygame.mixer.Sound('gameover.mp3').play()
            print('crash')
            break
        draw_block(RED, apple.x, apple.y)
        for block in snake_blocks:
            draw_block(SNAKE_COLOR, block.x, block.y)
        
        if apple == head:
            total +=1
            speed = total//3 + 2
            snake_blocks.append(apple)
            apple = get_random_empty_block()
            
        
        new_head = SnakeBLock(head.x + d_row, head.y + d_col)
        
        if new_head in snake_blocks:
            pygame.mixer.Sound('gameover.mp3').play()
            print("crash yourself")
            break
        if new_head in NO:
            pygame.mixer.Sound('gameover.mp3').play()
            print("crash yourself")
            break
        snake_blocks.append(new_head)
        snake_blocks.pop(0)
        pygame.display.flip()
        timer.tick(3+speed)


menu = pygame_menu.Menu(300, 400, "WELCOME", theme=pygame_menu.themes.THEME_BLUE)
menu.add_text_input("NAME: ", default = "Sanzhar")
menu.add_button("EASY 1 PLAYER", start_the_game)
menu.add_button("EASY 2 PLAYERS", start_the_game1)
menu.add_button("MEDIUM 1 PLAYER", start_the_game2)
menu.add_button("MEDIUM 2 PLAYERS", start_the_game2)
menu.add_button("HARD 1 PLAYER", start_the_game)
menu.add_button("HARD 2 PLAYERS", start_the_game1)


menu.add_button("EXIT", pygame_menu.events.EXIT)

while True:
   screen.blit(bg_image, (0, 0))

   events = pygame.event.get()
   for event in events:
        if event.type == pygame.QUIT:
           exit()
   if menu.is_enabled():
       menu.update(events)
       menu.draw(screen)
   pygame.display.update()
