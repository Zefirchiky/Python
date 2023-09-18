from enum import Enum
import pygame as pg
import time
import glm
import sys
import os

pg.init()
os.chdir("C:\AllArtem\Programer\Python\Games\IDK_NAME")

# WIN
WIDTH, HEIGHT = 1600, 900
WIN_REZ = glm.vec2(WIDTH, HEIGHT)
H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2
H_WIN_REZ = glm.vec2(H_WIDTH, H_HEIGHT)

# Player
PLAYER_SIZE = glm.vec2(1.3)
PLAYER_WIDTH, PLAYER_HEIGHT = 160, 128
PLAYER_WH = glm.vec2(PLAYER_WIDTH, PLAYER_HEIGHT)
PLAYER_POS = glm.vec2(WIDTH // 2, HEIGHT // 2)
PLAYER_SPEED = 10
PLAYER_TEXTURE = 'necromancer_(128x128).png'

# Animation
ANIMATION_SPEED = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
VIOLET = (178, 102, 255)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)
SKY_COL = (135, 206, 235)
SUNRISE = (255, 153, 51)

FPS = 144