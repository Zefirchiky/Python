import pygame as pg

pg.init()

'''----------------------- SETTINGS -----------------------'''
DIS_REZ = WIDTH, HEIGHT = 1200, 900

FPS = 60

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