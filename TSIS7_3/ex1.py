import pygame
import math
pygame.init()
size = width, height = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Trigonometric functions")
font = pygame.font.SysFont('times-new-roman', 20)
pygame.mixer.music.load('muz.mp3')
pygame.mixer.music.play(-1)

process=True
while process:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            process = False
    screen.fill('white')

    pygame.draw.rect(screen, 'black', (70, 10, 660, 540), 2) #borders
    pygame.draw.line(screen, 'black', (70, 280), (730, 280), 3)  # OX
    pygame.draw.line(screen, 'black', (400, 10), (400, 550), 3)  # OY
    pygame.draw.line(screen, 'black', (70, 40), (730, 40))  # Y first line
    pygame.draw.line(screen, 'black', (70, 520), (730, 520))  # Y last line
    pygame.draw.line(screen, 'black', (100, 10), (100, 550))  # X first line
    pygame.draw.line(screen, 'black', (700, 10), (700, 550))  # X last line
    pygame.draw.line(screen, 'red', (530, 60), (570, 60)) # line of color of sin function
    for x in range(530, 570, 7):                          # dotted line of color of cos function
            pygame.draw.line(screen, 'blue', (x, 90), (x + 3, 90))
    for x in range(100, 701, 100):                        # other OY lines
            if x != 500:                                  # place to mark functions 
               pygame.draw.line(screen, 'black', (x, 10), (x, 550))
            else:
               pygame.draw.line(screen, 'black', (x, 10), (x, 40))
               pygame.draw.line(screen, 'black', (x, 100), (x, 550))
    for x in range(100, 701, 50):                       # OX large strokes for a value of 0 or 1 for functions
        pygame.draw.line(screen, 'black', (x, 10), (x, 30))
        pygame.draw.line(screen, 'black', (x, 550), (x, 530))
    for x in range(100, 701, 25):                      # OX average size strokes for a value of 0 or 1 for functions
        pygame.draw.line(screen, 'black', (x, 10), (x, 20))
        pygame.draw.line(screen,'black', (x, 550), (x, 540))
#    for x in range(100, 701, 12):                      
#        pygame.draw.line(screen, 'black', (x, 10), (x, 13))
#        pygame.draw.line(screen,'black', (x, 550), (x, 547))
    for y in range(40, 521, 60):                       # OY other lines
        pygame.draw.line(screen, 'black', (70, y), (730, y))
    for y in range(40, 521, 30):                        # OY large strokes
        pygame.draw.line(screen, 'black', (70, y), (90, y))
        pygame.draw.line(screen, 'black', (710, y), (730, y))
    for y in range(40, 521, 15):                       # OY average size strokes
        pygame.draw.line(screen, 'black', (70, y), (80, y))
        pygame.draw.line(screen, 'black', (720, y), (730, y))
    for x in range(100, 700):                         # sin(x) function
        sin_y1 = 240 * math.sin((x - 100) / 100 * math.pi)
        sin_y2 = 240 * math.sin((x - 99) / 100 * math.pi)
        pygame.draw.aalines(screen, 'red', False, [(x, 280 + sin_y1), ((x + 1), 280 + sin_y2)])
        pygame.time.delay(10)                         # animation of sin(x)
        pygame.display.update()
    for x in range(100, 700, 3):                      # cos(x) function
        cos_y1 = 240 * math.cos((x - 100) / 100 * math.pi)
        cos_y2 = 240 * math.cos((x - 99) / 100 * math.pi)
        pygame.draw.aalines(screen, 'blue', False, [(x, 280 + cos_y1), ((x + 1), 280 + cos_y2)])
        pygame.time.delay(20)                        # animation of cos(x)
        pygame.display.update()
    screen.blit(font.render('sin(x)', False, 'black'), (475, 45)) # text in empty place
    screen.blit(font.render('cos(x)', False, 'black'), (475, 75))
    screen.blit(font.render('X', False, 'black'), (393, 575))
    x_numerator = ['-3п', ' 5п', '-2п', ' 3п', '-п ', ' п ', ' 0 ', ' п ', ' п ', ' 3п', ' 2п', ' 5п', ' 3п']
    x_division = ['', '_ __', '', '_ __', '', '_ _', '', '   _', '', '   __', '', '   __', '']
    x_denominator = ['', '  2', '', '  2', '', ' 2', '', ' 2', '', '  2', '', '  2', '']
    y_values = [' 1.00', ' 0.75', ' 0.50', ' 0.25', ' 0.00', '-0.25', '-0.50', '-0.75', '-1.00']
    for x in range(100, 701, 50):                  # OX values
        screen.blit(font.render(x_numerator[(x - 100) // 50], False, 'black'), (x - 10, 550))
        screen.blit(font.render(x_division[(x - 100) // 50], False, 'black'), (x - 20, 550))
        screen.blit(font.render(x_denominator[(x - 100) // 50], False, 'black'), (x - 10, 570))
        pygame.time.delay(300)
        pygame.display.update()
    for y in range(40, 521, 60):                   # OY values
        screen.blit(font.render(y_values[(y - 40) // 60], False, 'black'), (25, (y - 10)))
        pygame.time.delay(300)
        pygame.display.update()
    while pygame.event.wait().type !=pygame.QUIT:
           pygame.display.flip()
    pygame.quit()