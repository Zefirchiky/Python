import pygame as pg
import random as rd
from random import randint

pg.init()

'''-------------------- SETTINGS --------------------'''
WIDTH, HEIGHT = 500, 500
DIS = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Maze creator")

FPS = 60

MAZE_SIZE = 10      # (10)

'''------------------- NOT CHANGE -------------------'''

class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {"Top": True, "Bottom": True,
                      "Left": True, "Right": True}
        self.visited = False
        
    def draw(self):
        pass

class Maze:
    def __init__(self, size):
        self.size = size
        self.visited = []
        
    def matrix_create(self):
        x = int(WIDTH/self.size)
        self.matrix = [
            [0 for i in range(x+2)] for i in range(x+2)
        ]
        for i in self.matrix:
            print(i)
        print("------------------------------")
        for i in self.matrix[1:-2]:
            print(i)
        
    def maze_change(self):
        for i, row in enumerate(self.matrix[1:-2]):
            for u, num in enumerate(row[1:-2]):
                l = [self.matrix[i+1][u], self.matrix[i-1][u], self.matrix[i][u+1], self.matrix[i][u-1]]
                if all(l) == False:
                    self.matrix[i][u] = 1
                    self.visited.append([i, u])

clock = pg.time.Clock()

def main():
    run = True
    maze = Maze(MAZE_SIZE)
    maze.matrix_create()
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        maze.maze_change()
        
        pg.display.update()
    pg.quit()
        
if __name__ == "__main__":
    main()

