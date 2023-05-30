import random
import pygame as pg
import time
import os

pg.init()
os.chdir("C:\AllArtem\Programer\Python\Snake")

WIDTH, HEIGHT = 1000, 800
DIS = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Snake")

H_WIDTH, H_HEIGHT = WIDTH//2, HEIGHT//2
SNAKE_SCALE = 18
SNAKE_HITBOX_SCALE = 20

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

FPS = 60

if WIDTH % SNAKE_HITBOX_SCALE != 0 or HEIGHT % SNAKE_HITBOX_SCALE != 0:
    raise ValueError("The width and height must be multiples of the snake's hitbox")

squares_map = (WIDTH//SNAKE_HITBOX_SCALE, HEIGHT//SNAKE_HITBOX_SCALE)

class Snake:
    def __init__(self, scale, hitbox_scale, speed):
        self.scale = scale
        self.hb_scale = hitbox_scale
        self.speed = speed

    def snake_create(self):
        self.body = [
            [squares_map[0] - 1, squares_map[1]],
            [squares_map[0], squares_map[1]],
            [squares_map[0] + 1, squares_map[1]],
        ]

    def move(self, keys):
        dx = keys[0]


def main():
    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        keys = pg.key.get_pressed()
        print(keys)
        DIS.fill(BLACK)

if __name__ == '__main__':
    main()