from settings import *
from player import Player
from attack import Attack

class App:
    def __init__(self):
        self.WIN = pg.display.set_mode(WIN_REZ)

        # ============ # Time # ============ #
        self.clock = pg.time.Clock()
        self.t = 0
        self.dt = 0
        self.tic = time.perf_counter()
        # ================================== #

        self.on_init()

    def on_init(self):
        self.player = Player(self)
        self.attack = Attack(self)

    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.on_quit()
            self.player.mouse_handler(event)

    def on_quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        self.t = pg.time.get_ticks() * .001
        self.dt = time.perf_counter() - self.tic
        self.tic = time.perf_counter()

        self.player.update()
        self.attack.update()

        pg.display.set_caption(f'{self.clock.get_fps():.3f} FPS')

    def render(self):
        self.WIN.fill(SUNRISE)

        self.player.render()
        
        pg.display.flip()

    def run(self):
        while True:
            self.event_handler()
            self.update()
            self.render()
            self.clock.tick(FPS)

if __name__ == "__main__":
    app = App()
    app.run()
