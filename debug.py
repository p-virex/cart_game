import pygame

pygame.init()

WHITE = (255, 255, 255)
RED = (225, 0, 50)
YELLOW = (225, 225, 0)
FPS = 6
SPEED = 5
WIN_WIDTH = 400
WIN_HEIGHT = 300

# Радиус и начальная позиция по y круга
r = 15
y = WIN_HEIGHT + (r * 2)

# Ширина квадрата
a = 30

sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("MyGame")
sc.fill(WHITE)
pygame.display.update()

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    if i.type == pygame.MOUSEBUTTONDOWN:
        if i.button == 1:
            pos = pygame.mouse.get_pos()
            while y > i.pos[1]:
                sc.fill(WHITE)
                pygame.draw.circle(sc, YELLOW, (i.pos[0], y), r)
                y -= SPEED
                pygame.display.update()

                clock.tick(FPS)

            sc.fill(WHITE)
            pygame.draw.rect(sc, RED, (i.pos[0] - (a / 2), y - (a / 2), a, a))
            y = WIN_HEIGHT + (r * 2)
            pygame.display.update()