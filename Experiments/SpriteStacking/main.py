from settings import *
import pygame as pg
import time
from sprite_stacking import StackedSprite
from cache import Cache

DIS = pg.display.set_mode(DIS_REZ, pg.RESIZABLE)
pg.display.set_caption("IDK")


class App:
    def __init__(self):
        self.run = True
        self.clock = pg.time.Clock()
        self.tic = time.time()
        self.dt = 0.0
        self.time = 0
        self.main_group = pg.sprite.Group()
        
        self.cache = Cache()
        
        StackedSprite(self, "van", (-HEIGHT // 3, 0))
        StackedSprite(self, "tank", (HEIGHT // 3, 0))
    
    def update(self):
        self.time_update()
        self.main_group.update()
    
    def draw(self):
        DIS.fill((0, 70, 35))
        self.main_group.draw(DIS)
        debug(self.clock.get_fps())
        pg.display.update()
    
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                        self.run = False
                        
    def time_update(self):
        self.dt = time.time() - self.tic
        self.tic = time.time()
        self.time = pg.time.get_ticks() * .001
        
    def main(self):
        while self.run:
            self.clock.tick(FPS)
            self.check_events()
            self.update()
            self.draw()
                    
        pg.quit()
        
if __name__ == "__main__":
    print(CLEAR)
    app = App()
    app.main()