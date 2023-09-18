import pygame as pg
import sys
import time
from settings import *
from debug import debug

pg.init()

DIS = pg.display.set_mode(DIS_REZ)
pg.display.set_caption("Chess")

class App:
    def __init__(self):
        self.clock = pg.time.Clock()
        self.tic = time.time()
        self.DIS = DIS
    
    def update(self):
        self.dt = time.time() - self.tic
        self.tic = time.time()
        self.keys_pressed = pg.key.get_pressed()
        self.clock.tick(FPS)
    
    def draw(self):
        DIS.fill(TURQUOISE)
        pg.display.flip()
    
    def event_handler(self):
        self.keys = []
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                
            if event.type == pg.KEYDOWN:
                self.keys.append(event.key)
    
    def run(self):
        while True:
            self.event_handler()
            self.update()
            self.draw()

print(CLEAR, CLEAR_AND_RETURN)
if __name__ == "__main__":
    app = App()
    app.run()
