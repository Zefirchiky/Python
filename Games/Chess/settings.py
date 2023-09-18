import pygame as pg

'''----------------------- SETTINGS -----------------------'''
DIS_REZ = WIDTH, HEIGHT = 1200, 900
HALF_REZ = HALF_WIDTH, HALF_HEIGHT = WIDTH//2, HEIGHT//2

FPS = 60

vec2 = pg.math.Vector2

'''COLORS'''
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
