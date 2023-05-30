import pygame as pg
import logging as lgg
import loguru as lgr

pg.init()

font = pg.font.Font(None, 30)
def debug(info, y=10, x=10):
    display_surface = pg.display.get_surface()
    debug_surface = font.render(str(info), True, 'white')
    debug_rect = debug_surface.get_rect(topleft=(x, y))
    pg.draw.rect(display_surface, 'black', debug_rect)
    display_surface.blit(debug_surface, debug_rect)
    
lgg.basicConfig(format="%(levelname)s (%(asctime)s: %(message)s (Line: %(lineno)s [%(filename)s])",
                datefmt="%d-%m-%Y %I:%M:%S %p",
                level=lgg.DEBUG)
lgg.critical("LOL")