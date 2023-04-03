import pygame as pg
import time
import math
from debug import debug

pg.init()

vec2 = pg.math.Vector2

'''----------------------- SETTINGS -----------------------'''
DIS_REZ = WIDTH, HEIGHT = 1200, 900
CENTER = H_WIDTH, H_HEIGHT = vec2(DIS_REZ)//2

FPS = 144

NUM_ANGLES = 90     # multiple to 360

STACKED_SPRITE_ATTRIBUTE = {
    "van": {
        "path": "assets/stacked_sprites/van.png",
        "num_layers": 20,
        "scale": 8
    },
    "tank": {
        "path": "assets/stacked_sprites/tank.png",
        "num_layers": 17,
        "scale": 13
    }
}

'''COLORS'''
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

'''---------------------- NOT CHANGE ----------------------'''
FORMAT_CLEAR = "\033[0m"
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

BLACK_TEXT = "\033[30m"
RED_TEXT = "\033[31m"
GREEN_TEXT = "\033[32m"
YELLOW_TEXT = "\033[33m"
BLUE_TEXT = "\033[34m"
MAGENTA_TEXT = "\033[35m"
CYAN_TEXT = "\033[36m"
WHITE_TEXT = "\033[37m"