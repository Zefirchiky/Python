from settings import *

class CrossHair:
    def __init__(self, HUD):
        self.app = HUD.app
        self.hud = HUD
        self.pos = glm.vec3(0.0)