import time

import pygame
from random import randrange

RES = 800
SIZE = 20


def random_position():
    return randrange(0, RES, SIZE), randrange(0, RES, SIZE)


class Snake:
    def __init__(self):
        pygame.init()

        # window
        self.screen = pygame.display.set_mode((RES, RES))
        pygame.display.set_caption("Snake")

        self.snake_pos = self.generate_position()
        self.direction = [0, 0]
        self.food = []

    def generate_position(self):
        x, y = random_position()
        return [(x, y)]

    def start_game(self):
        fps = 10
        frametime = 1 / fps
        t = time.time()

        while True:
            sc.fill(pygame.Color("black"))
            # drawing snake
            [(pygame.draw.rect(sc, pygame.Color("green"), (i, j, SIZE, SIZE))) for i, j in self.snake_pos]
            # pygame.draw.rect(sc, pygame.Color("red"), (*apple, SIZE, SIZE))

            # moving snake
            x, y = self.snake_pos
            dx, dy = self.direction

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
            if key[pygame.K_w]:
                dx, dy = 0, -1
            elif key[pygame.K_s]:
                dx, dy = 0, 1
            elif key[pygame.K_a]:
                dx, dy = -1, 0
            elif key[pygame.K_d]:
                dx, dy = 1, 0


x, y = random_position()  # first position of the snake
apple = random_position()  # apple position

length = 1  # first length of the snake
snake = [(x, y)]  # list of snake body positions

dx, dy = 0, 0  # direction of the snake
fps = 10  # snake speed

sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()

