from settings import *
from meshes.cross_hair_mesh import CrossHairMesh

class HUD:
    def __init__(self, app):
        self.app = app
        self.cross_hair_mesh = CrossHairMesh(app)

    def update(self):
        pass

    def render(self):
        self.cross_hair_mesh.render()