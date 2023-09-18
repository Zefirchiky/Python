from settings import *
from shader_program import ShaderProgram
from scene import Scene
from player import Player
from textures import Textures
from HUD import HUD

pg.init()
os.chdir("C:\AllArtem\Programer\Python\Games\Minecraft")

pg.display.set_mode(WIN_RES, flags=pg.OPENGL | pg.DOUBLEBUF)

FPS = 60

class App:
    def __init__(self):
        self.ctx: mgl.Context = mgl.create_context()

        self.ctx.enable(mgl.DEPTH_TEST | mgl.CULL_FACE | mgl.BLEND)
        self.ctx.gc_mode = 'auto'

        self.clock = pg.time.Clock()
        self.dt = 0
        self.t = 0
        self.tic = time.perf_counter()

        pg.event.set_grab(True)
        pg.mouse.set_visible(False)

        self.is_run = True
        self.on_init()

    def on_init(self):
        self.textures = Textures(self)
        self.player = Player(self)
        self.shader_program = ShaderProgram(self)
        self.scene = Scene(self)
        self.hud = HUD(self)

    def update(self):
        self.dt = time.perf_counter() - self.tic
        self.tic = time.perf_counter()
        self.t = pg.time.get_ticks() * 0.001
        pg.display.set_caption(f'{self.clock.get_fps():04.1f} FPS')

        self.player.update()
        self.shader_program.update()
        self.scene.update()

    def render(self):
        self.ctx.clear(color=BG_COLOR)
        self.scene.render()
        self.hud.render()
        pg.display.flip()

    def handle_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_run = False
            self.player.handle_event(event)

    def run(self):
        while self.is_run:
            self.handle_event()
            self.update()
            self.render()
            self.clock.tick()
        pg.quit()
        sys.exit()


if __name__ == "__main__":
    app = App()
    app.run()