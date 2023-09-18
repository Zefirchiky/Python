from settings import *

class Attack:
    def __init__(self, app):
        self.app = app
        self.win = app.WIN

    def get_attack_degree(self):
        mouse_pos = H_WIN_REZ - pg.mouse.get_pos()
        mouse_deg = glm.atan(mouse_pos.x / mouse_pos.y)
        print(mouse_deg)
    
    def update(self):
        self.get_attack_degree()