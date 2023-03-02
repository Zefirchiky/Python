import pygame as pg
from figure import *
import numpy as np
from moves import *

pg.init()

'''====================SETTINGS===================='''
WIDTH, HEIGHT = 1500, 1000                  # Screen size (1500, 1000)
DIS = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("3D Figures")           # Name of 'game'

COORDS_ON = True            # Create coordinate system? (True\False)

'''Colors'''
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)

FPS = 60

TRANSLATION_SPEED = 3       # (3)
ROTATE_SPEED = 0.015        # (0.015)
SIZE = 200                  # Figure size (200)

FONT_SIZE = 25          # Text size -_-         (25)
FONT = "Aharoni"        # Only windows fonts    ("Aharoni")

'''====================NON CHANGE===================='''

control_font = pg.font.SysFont(FONT, FONT_SIZE)                                 

def text(font):
    DIS.blit(font.render("Controll:", True, WHITE), (WIDTH-FONT_SIZE*14, FONT_SIZE/3))
    DIS.blit(font.render("A, D - Y Coords", True, WHITE), (WIDTH-FONT_SIZE*14, FONT_SIZE + FONT_SIZE/3))
    DIS.blit(font.render("W, S - X Coords", True, WHITE), (WIDTH-FONT_SIZE*14, 2*FONT_SIZE + FONT_SIZE/3))
    DIS.blit(font.render("Q, E - Z Coords", True, WHITE), (WIDTH-FONT_SIZE*14, 3*FONT_SIZE + FONT_SIZE/3))
    DIS.blit(font.render("Z, X - Scale (Less\More)", True, WHITE), (WIDTH-FONT_SIZE*14, 4*FONT_SIZE + FONT_SIZE/3))
    DIS.blit(font.render("UP, DOWN, LEFT, RIGHT - Translation", True, WHITE), (WIDTH-FONT_SIZE*14, 5*FONT_SIZE + FONT_SIZE/3))

def main():
    run = True
    clock = pg.time.Clock()
    cube = Figure(np.array([
            [-1, -1, -1], [-1, 1, -1], [1, 1, -1], [1, -1, -1],
            [-1, -1, 1], [-1, 1, 1], [1, 1, 1], [1, -1, 1]
        ]),
        
        np.array([
            [0, 1], [1, 2], [2, 3], [3, 0],
            [4, 5], [5, 6], [6, 7], [7, 4],
            [0, 4], [1, 5], [2, 6], [3, 7]
        ]))
    tr = Figure(np.array([
            [1, 1, 1], [0, -1, 0], [-1, 1, 1], [-1, 1, -1], [1, 1, -1]
        ]),
        
        np.array([
            [1, 0], [1, 2], [1, 3], [1, 4],
            [0, 2], [2, 3], [3, 4], [4, 0]
        ]))
    while run:
        clock.tick(FPS)
        DIS.fill(BLACK)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        keys = pg.key.get_pressed()
        cube.rendering(DIS, keys, SIZE, WIDTH/4, HEIGHT/2, WHITE, control_font, TRANSLATION_SPEED, ROTATE_SPEED, coords_on = COORDS_ON, coords_col = (RED, BLUE, GREEN))
        tr.rendering(DIS, keys, SIZE, WIDTH/2 + WIDTH/4, HEIGHT/2, WHITE, control_font, TRANSLATION_SPEED, ROTATE_SPEED, coords_on = COORDS_ON, coords_col = (RED, BLUE, GREEN))
        text(control_font)
        pg.display.update()
    
    pg.quit()

if __name__ == "__main__":
    main()