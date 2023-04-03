import pygame as pg
import random as rd
from pygame import gfxdraw

pg.init()

DIS_SIZE = WIDTH, HEIGHT = 1500, 900
DIS = pg.display.set_mode(DIS_SIZE)
pg.display.set_caption("FIREEE!!!")

FPS = 60

COLORS = ["black", "red", "orange", "yellow", "white"]
STEPS = 9
SIZE = 5

class Fire:
    def __init__(self):
        self.fire_width = WIDTH//SIZE+1
        self.fire_height = HEIGHT//SIZE
        self.pallet = self.get_pallet()
        self.fire_array = self.fire_array_create()
    
    @staticmethod
    def get_pallet():
        pallet = []
        for u, col in enumerate(COLORS[:-1]):
            c1, c2 = col, COLORS[u+1]
            for i in range(STEPS):
                pallet.append(pg.Color(c1).lerp(c2, (i+0.5) / STEPS))
        return pallet
                
    def pallet_draw(self):
        posx = SIZE
        posy = HEIGHT//2 - SIZE//2
        for i, col in enumerate(self.pallet):
            gfxdraw.box(DIS, (i * posx + 20, posy, SIZE - 5, SIZE - 5), col)
    
    def fire_array_create(self):
        fire_array = [[0 for _ in range(self.fire_width)] for _ in range(self.fire_height)]
        for i in range(self.fire_width):
            fire_array[self.fire_height-1][i] = len(self.pallet)-1
        return fire_array
                           
    def do_fire(self):
        for x in range(self.fire_width):
            for y in range(1, self.fire_height):
                color_index = self.fire_array[y][x]
                if color_index:
                    rnd = rd.randint(0, 3)
                    self.fire_array[y - 1][(x - rnd + 1) % self.fire_width] = color_index - rnd % 2
                else:
                    self.fire_array[y - 1][x] = 0
                           
    def draw(self):
        for y, row in enumerate(self.fire_array):
            for x, color_index in enumerate(row):
                if color_index:
                    color = self.pallet[color_index]
                    gfxdraw.box(DIS, (x*SIZE, y*SIZE,
                                      SIZE, SIZE), color)
       
clock = pg.time.Clock()     
def main():
    run = True
    fire = Fire()
    while run:
        clock.tick(FPS)
        DIS.fill((0, 0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        fire.do_fire()
        fire.draw()    
        pg.display.update()
        
    pg.quit()
    
if __name__ == "__main__":
    main()
                