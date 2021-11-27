import pygame
from random import randrange

RES = 800
SIZE = 20


def random_position():
    return randrange(0, RES, SIZE), randrange(0, RES, SIZE)


x, y = random_position()  # first position of the snake
apple = random_position()  # apple position

length = 1  # first length of the snake
snake = [(x, y)]  # list of snake body positions

dx, dy = 0, 0  # direction of the snake
fps = 10  # snake speed

pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()

while True:
    sc.fill(pygame.Color("black"))
    # drawing snake
    [(pygame.draw.rect(sc, pygame.Color("green"), (i, j, SIZE, SIZE))) for i, j in snake]
    pygame.draw.rect(sc, pygame.Color("red"), (*apple, SIZE, SIZE))

    # moving snake
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]

    # eating apple
    if snake[-1] == apple:
        apple = random_position()
        length += 1

    # game over out of sandbox
    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE:
        break

    # game over eaten itself
    if len(snake) != len(set(snake)):
        break

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        # control
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            dx, dy = 0, -1
        elif key[pygame.K_DOWN]:
            dx, dy = 0, 1
        elif key[pygame.K_LEFT]:
            dx, dy = -1, 0
        elif key[pygame.K_RIGHT]:
            dx, dy = 1, 0