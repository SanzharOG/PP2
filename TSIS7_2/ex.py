import pygame
import math
pygame.init()
size = width, height = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Trigonometric functions")
font = pygame.font.SysFont('times-new-roman', 20)
pygame.mixer.music.load('muz.mp3')
pygame.mixer.music.play(-1)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
PI = math.pi

x_axis_points = ['-3п', ' 5п', '-2п', ' 3п', '-п ', ' п ', ' 0 ', ' п ', ' п ', ' 3п', ' 2п', ' 5п', ' 3п']
x_axis_points_extra1 = ['', '_ __', '', '_ __', '', '_ _', '', '   _', '', '   __', '', '   __', '']
x_axis_points_extra2 = ['', '  2', '', '  2', '', ' 2', '', ' 2', '', '  2', '', '  2', '']
y_axis_points = [' 1.00', ' 0.75', ' 0.50', ' 0.25', ' 0.00', '-0.25', '-0.50', '-0.75', '-1.00']
is_going=True
while is_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_going = False
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, (70, 10, 660, 540), 2)  # Borders
    pygame.draw.line(screen, BLACK, (70, 280), (730, 280), 3)  # X-Axis
    pygame.draw.line(screen, BLACK, (400, 10), (400, 550), 3)  # Y-Axis
    pygame.draw.line(screen, BLACK, (70, 40), (730, 40))  # H_line 1
    pygame.draw.line(screen, BLACK, (70, 520), (730, 520))  # H_line 2
    pygame.draw.line(screen, BLACK, (100, 10), (100, 550))  # V_line 1
    pygame.draw.line(screen, BLACK, (700, 10), (700, 550))  # V_line 2
    pygame.draw.line(screen, RED, (530, 60), (570, 60))
    for x in range(530, 570, 7):
        pygame.draw.line(screen, BLUE, (x, 90), (x + 3, 90))
    for x in range(100, 701, 100):
        if x != 500:
            pygame.draw.line(screen, BLACK, (x, 10), (x, 550))
        else:
            pygame.draw.line(screen, BLACK, (x, 10), (x, 40))
            pygame.draw.line(screen, BLACK, (x, 100), (x, 550))
    for x in range(100, 701, 50):
        pygame.draw.line(screen, BLACK, (x, 10), (x, 30))
        pygame.draw.line(screen, BLACK, (x, 550), (x, 530))
    for x in range(100, 701, 25):
        pygame.draw.line(screen, BLACK, (x, 10), (x, 20))
        pygame.draw.line(screen, BLACK, (x, 550), (x, 540))

    for y in range(40, 521, 60):
        pygame.draw.line(screen, BLACK, (70, y), (730, y))
    for y in range(40, 521, 30):
        pygame.draw.line(screen, BLACK, (70, y), (90, y))
        pygame.draw.line(screen, BLACK, (710, y), (730, y))
    for y in range(40, 521, 15):
        pygame.draw.line(screen, BLACK, (70, y), (80, y))
        pygame.draw.line(screen, BLACK, (720, y), (730, y))

    for x in range(100, 700):
        sin_y1 = 240 * math.sin((x - 100) / 100 * PI)
        sin_y2 = 240 * math.sin((x - 99) / 100 * PI)
        pygame.draw.aalines(screen, RED, False, [(x, 280 + sin_y1), ((x + 1), 280 + sin_y2)])
        pygame.time.delay(10)
        pygame.display.update()

    for x in range(100, 700, 3):
        cos_y1 = 240 * math.cos((x - 100) / 100 * PI)
        cos_y2 = 240 * math.cos((x - 99) / 100 * PI)
        pygame.draw.aalines(screen, BLUE, False, [(x, 280 + cos_y1), ((x + 1), 280 + cos_y2)])
        pygame.time.delay(20)
        pygame.display.update()
    
    screen.blit(font.render('sin(x)', False, BLACK), (475, 45))
    screen.blit(font.render('cos(x)', False, BLACK), (475, 75))
    screen.blit(font.render('X', False, BLACK), (393, 575))

    for x in range(100, 701, 50):
        screen.blit(font.render(x_axis_points[(x - 100) // 50], False, BLACK), (x - 10, 550))
        screen.blit(font.render(x_axis_points_extra1[(x - 100) // 50], False, BLACK), (x - 20, 550))
        screen.blit(font.render(x_axis_points_extra2[(x - 100) // 50], False, BLACK), (x - 10, 570))
        pygame.time.delay(300)
        pygame.display.update()
    for y in range(40, 521, 60):
        screen.blit(font.render(y_axis_points[(y - 40) // 60], False, BLACK), (25, (y - 10)))
        pygame.time.delay(300)
        pygame.display.update()

    while pygame.event.wait().type !=pygame.QUIT:
           pygame.display.flip()
    pygame.quit()