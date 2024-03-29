import pygame, random
pygame.display.set_caption("PAINT")
def drawLine(screen, start, end, width, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2
    
    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, color, (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, color, (x, y), width)
def main():
    screen = pygame.display.set_mode((800, 600))
    screen.fill('white')
    mode = 'random'
    draw_on = False
    last_pos = (0, 0)
    color = (255, 128, 0)
    radius = 10

    colors = {
        'red': (255, 0, 0),
        'blue': (0, 0, 255),
        'green': (0, 255, 0),
        'white': (255, 255, 255),
        'orange': (255, 91, 0),
        'yellow':(255, 255, 0),
        'dark' : (0, 0 ,0),
        'brown':(121,85,61)
    }

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_r:
                    mode = 'red'
                if event.key == pygame.K_b:
                    mode = 'blue'
                if event.key == pygame.K_g:
                    mode = 'green'
                if event.key == pygame.K_e:
                    mode = 'white'
                if event.key == pygame.K_o:
                    mode = 'orange'
                if event.key == pygame.K_y:
                    mode = 'yellow'
                if event.key == pygame.K_d:
                    mode = 'dark'
                if event.key == pygame.K_q:
                    mode = 'brown'
                if event.key == pygame.K_s:
                    pygame.image.save(screen, "Screenshot.jpg")
                if event.key == pygame.K_UP:
                    radius += 1
                if event.key == pygame.K_DOWN:
                    radius -= 1
                if event.key == pygame.K_z and ctrl_held:
                    print("YOUR COORDINATES")
                    z1 = int(input())
                    w1 = int(input())
                    z2 = int(input())
                    w2 = int(input())
                    pos = pygame.mouse.get_pos()
                    pygame.draw.rect(screen, mode, (z1, w1, z2, w2), radius)
                if event.key == pygame.K_x and ctrl_held:
                    pos = pygame.mouse.get_pos()
                    pygame.draw.circle(screen, mode, pos, radius, 1)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mode == 'random':
                    color = (random.randrange(256), random.randrange(256), random.randrange(256))
                else:
                    color = colors[mode]
                pygame.draw.circle(screen, color, event.pos, radius)
                draw_on = True
            if event.type == pygame.MOUSEBUTTONUP:
                draw_on = False
            if event.type == pygame.MOUSEMOTION:
                if draw_on:
                    drawLine(screen, last_pos, event.pos, radius, color)
                    #pygame.draw.circle(screen, color, event.pos, radius)
                last_pos = event.pos
        pygame.display.flip()

    pygame.quit()

main()
rect = pygame.Rect(10, 20, 30, 50)
# print(rect.bottom)
# print(rect.top)
# print(rect.left)
# print(rect.right)
# print(rect.bottomleft)
print(rect.bottomright)
print(rect.center)
