from moves import *
from OBJ_reader import *
from figure import *
import pygame as pg
import numpy as np
import itertools as itt

pg.init()

'''====================SETTINGS===================='''
WIDTH, HEIGHT = 1500, 1000                  # Screen size (1500, 1000)
DIS = pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE)
pg.display.set_caption("3D Figures")           # Name of 'game'

COORDS_ON = True            # Create coordinate system? (True\False)

'''Colors'''
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)

FPS = 60

TRANSLATION_SPEED = 10       # (10)
ROTATE_SPEED = 0.02        # (0.02)
SIZE = 100                  # Figure size (100)

FONT_SIZE = 25          # Text size -_-         (25)
FONT = "Aharoni"        # Only windows fonts    ("Aharoni")

'''====================NON CHANGE===================='''

control_font = pg.font.SysFont(FONT, FONT_SIZE)                                 
inp = [0, 0, 0]
setts = [SIZE, TRANSLATION_SPEED, ROTATE_SPEED]

class InputDIS:
    def __init__(self, text, col, x, y, font):
        self.col = col
        self.x = x
        self.y = y
        self.font = font
        self.inp_text = ""
        self.text = text
        self.in_input = False
        self.text_surfase = self.font.render(self.text, True, self.col)
        self.text_w = self.text_surfase.get_width()
        self.inp_surfase = self.font.render(self.inp_text, True, self.col)
        
    def input_handle(self, event):
        mouse = pg.mouse.get_pos()
        mouse_press = pg.mouse.get_pressed()
        if (mouse[0] > self.x-2 + self.text_w and 
            mouse[0] < max(self.x + 40, self.x + self.inp_surfase.get_width()+5) and 
            mouse[1] > self.y-4 and 
            mouse[1] < self.y + FONT_SIZE) or self.in_input:
            if mouse_press[0]:
                self.in_input = True
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_BACKSPACE:
                        self.inp_text = self.inp_text[0:-1]
                    else:
                        self.inp_text += event.unicode
        else:
            if mouse_press[0]:
                self.in_input = False

    def input_render(self, surfes):
        surfes.blit(self.text_surfase, (self.x, self.y))
        surfes.blit(self.inp_surfase, (self.x + self.text_w, self.y))
        pg.draw.rect(surfes, WHITE, (self.x-2 + self.text_w, self.y-4, max(40, self.inp_surfase.get_width()+5), FONT_SIZE), 1)
        

def text(font):
    DIS.blit(font.render("Controll:", True, WHITE), (DIS.get_width()-FONT_SIZE*14, FONT_SIZE/3))
    DIS.blit(font.render("A, D - Y Coords", True, WHITE), (DIS.get_width()-FONT_SIZE*14, FONT_SIZE + FONT_SIZE/3))
    DIS.blit(font.render("W, S - X Coords", True, WHITE), (DIS.get_width()-FONT_SIZE*14, 2*FONT_SIZE + FONT_SIZE/3))
    DIS.blit(font.render("Q, E - Z Coords", True, WHITE), (DIS.get_width()-FONT_SIZE*14, 3*FONT_SIZE + FONT_SIZE/3))
    DIS.blit(font.render("Z, X - Scale (Less\More)", True, WHITE), (DIS.get_width()-FONT_SIZE*14, 4*FONT_SIZE + FONT_SIZE/3))
    DIS.blit(font.render("UP, DOWN, LEFT, RIGHT - Translation", True, WHITE), (DIS.get_width()-FONT_SIZE*14, 5*FONT_SIZE + FONT_SIZE/3))
    
def settings_input(x, y, text, step, standart, font, num):
    mouse = pg.mouse.get_pos()
    mouse_press = pg.mouse.get_pressed()
    if mouse[0] > x and mouse[0] < x+200 and mouse[1] > y+15 and mouse[1] < y+42:
        if mouse_press[0]:
            mouse_in_x = mouse[0] - x
            global inp
            inp[num] = mouse_in_x - 100
    stand_set = 100 + inp[num]
    speed = round(standart + step*inp[num], 4)
    DIS.blit(font.render(f"{text}: {speed}", True, WHITE), (x, y))
    pg.draw.rect(DIS, WHITE, (x, y + 25, 200, 7), 1, border_radius=100)
    pg.draw.rect(DIS, WHITE, (x, y + 25, stand_set, 7), border_radius=100)
    
    return speed
    
def settings(font):
    setts = []
    counter = itt.count()
    DIS.blit(font.render(f"--Settings--", True, WHITE), (DIS.get_width()-FONT_SIZE*14, 7*FONT_SIZE + FONT_SIZE/3))
    setts.append(settings_input(DIS.get_width()-FONT_SIZE*14, 8*FONT_SIZE + FONT_SIZE/3, "Scale", SIZE/100, SIZE, font, next(counter)))
    setts.append(settings_input(DIS.get_width()-FONT_SIZE*14, 10*FONT_SIZE + FONT_SIZE/3, "Translation", TRANSLATION_SPEED/100, TRANSLATION_SPEED, font, next(counter)))
    setts.append(settings_input(DIS.get_width()-FONT_SIZE*14, 12*FONT_SIZE + FONT_SIZE/3, "Rotation speed", ROTATE_SPEED/100, ROTATE_SPEED, font, next(counter)))
    return setts

def main():
    run = True
    clock = pg.time.Clock()
    tea_cop = vertices_from_obj("objects/Tea_cop.obj")
    # tea_cop_f = faces_from_obj("objects/Tea_cop.obj")
    human_coords = vertices_from_obj("objects /FinalBaseMesh.obj")
    # tree_coords = vertices_from_obj("objects/Tree.obj")
    # tree_lines = lines_from_obj("objects/Tree.obj")
    cube = Figure(np.array(human_coords))
    tr = Figure(np.array([
            [1, 1, 1], [0, -1, 0], [-1, 1, 1], [-1, 1, -1], [1, 1, -1]
        ]),
        
        np.array([
            [1, 0], [1, 2], [1, 3], [1, 4],
            [0, 2], [2, 3], [3, 4], [4, 0]
        ]))
    
    rotate_input = InputDIS("Rotate speed: ", WHITE, DIS.get_width()-FONT_SIZE*14, 15*FONT_SIZE + FONT_SIZE/3, control_font)
    
    while run:
        clock.tick(FPS)
        DIS.fill(BLACK)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            rotate_input.input_handle(event)
        keys = pg.key.get_pressed()
        global setts
        cube.rendering(DIS, keys,
                       DIS.get_width()/4, HEIGHT/2,
                       WHITE, control_font,
                       setts[0], setts[1], setts[2],
                       coords_on = COORDS_ON, coords_col = (RED, BLUE, GREEN))
        
        tr.rendering(DIS, keys,
                     DIS.get_width()/2 + DIS.get_width()/4, HEIGHT/2,
                     WHITE, control_font,
                     setts[0], setts[1], setts[2],
                     coords_on = COORDS_ON, coords_col = (RED, BLUE, GREEN))
        
        text(control_font)
        rotate_input.input_render(DIS)
        setts = settings(control_font)
        pg.display.update()
        print(F"{clock.get_fps():.2f} FPS", end="\r")
    
    pg.quit()

if __name__ == "__main__":
    main()