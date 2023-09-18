import random
import pygame as pg
import time
import os

pg.init()
# os.chdir("C:\AllArtem\Programer\Python\Games\Snake")

WIDTH, HEIGHT = 1000, 800
DIS = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Snake")

H_WIDTH, H_HEIGHT = WIDTH//2, HEIGHT//2

SNAKE_SPEED = 20
SNAKE_SCALE = 18
SNAKE_HITBOX_SCALE = 20

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

FPS = 60

if WIDTH % SNAKE_HITBOX_SCALE != 0 or HEIGHT % SNAKE_HITBOX_SCALE != 0:
    raise ValueError("The width and height must be multiples of the snake's hitbox")

squares_map = [[0 for _ in range(HEIGHT//SNAKE_HITBOX_SCALE)]
               for _ in range(WIDTH//SNAKE_HITBOX_SCALE)]

squares_map_size = {'height': len(squares_map),
                    'width': len(squares_map[0])}

class Snake:
    def __init__(self):
        self.color = WHITE

    def create(self):
        self.body = [
            [squares_map_size['width']//2 - 1, squares_map_size['height']//2],
            [squares_map_size['width']//2,     squares_map_size['height']//2],
            [squares_map_size['width']//2 + 1, squares_map_size['height']//2],
        ]
        self.direction = [1, 0]

    def ch_direct(self, keys):
        dx = keys[pg.K_d] - keys[pg.K_a]
        dy = keys[pg.K_s] - keys[pg.K_w]
        if dx or dy:
            self.direction = [dx, 0] if self.direction[1] else [0, dy]

    def move(self, keys):
        self.ch_direct(keys)
        del self.body[0]
        if self.body[-1][0] + self.direction[0] > squares_map_size['width']:    # if head more than display width, teleport on left
            self.body.append([0, self.body[-1][1] + self.direction[1]])
        elif self.body[-1][0] + self.direction[0] < 0:                          # if head less than display width, teleport on right
            self.body.append([squares_map_size['width'], self.body[-1][1] + self.direction[1]]) 
        elif self.body[-1][1] + self.direction[1] > squares_map_size['height']: # if head more than display height, teleport on top
            self.body.append([self.body[-1][0] + self.direction[0], 0])
        elif self.body[-1][1] + self.direction[1] > 0:                          # if head less than display width, teleport on bottom
            self.body.append([self.body[-1][0] + self.direction[0], squares_map_size['height']])
        else:
            self.body.append([self.body[-1][0] + self.direction[0], self.body[-1][1] + self.direction[1]])

    def draw(self):
        for x, y in self.body:
            pg.draw.rect(DIS, self.color, [x * SNAKE_HITBOX_SCALE, y * SNAKE_HITBOX_SCALE,
                                           SNAKE_HITBOX_SCALE, SNAKE_HITBOX_SCALE])

    


def main():
    run = True
    snake = Snake()
    tic = time.perf_counter()
    clock = pg.time.Clock()
    while run:
        DIS.fill(BLACK)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        dt = time.perf_counter() - tic
        tic = dt
        keys = pg.key.get_pressed()
        snake.create()
        snake.move(keys)
        snake.draw()
        pg.display.flip()
        clock.tick(FPS)

if __name__ == '__main__':
    main()