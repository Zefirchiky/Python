import pygame as pg
import moderngl as mgl
import sys
from model import *
from camera import Camera

pg.init()

pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)

WIN_SIZE = WIDTH, HEIGHT = (1600, 900)
pg.display.set_mode(WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
pg.display.set_caption("OpenGL")

FPS = 60

class GraphicsEngine:
    def __init__(self):
        self.WIN_SIZE = WIN_SIZE
        self.ctx = mgl.create_context()
        self.clock = pg.time.Clock()
        #scene
        self.scene = Cube(self)
        #camera
        self.camera = Camera(self)
                
    def event_check(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.scene.destroy()
                pg.quit()
                sys.exit()
                
    def render(self):
        self.ctx.clear(color=(0.08, 0.16, 0.18))
        self.scene.render()
        pg.display.flip()
        
    def run(self):
        while True:
            self.event_check()
            self.render()
            self.clock.tick(FPS)
        

if __name__ == '__main__':
    app = GraphicsEngine ()
    app.run()
        
        