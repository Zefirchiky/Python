from settings import *
from meshes.base_mesh import BaseMesh
from settings import np

class CrossHairMesh(BaseMesh):
    def __init__(self, app):
        super().__init__()

        self.app = app
        self.ctx = app.ctx
        self.program = app.shader_program.cross_hair

        self.vbo_format = '3f 3f'
        self.attrs = ['in_pos', 'in_col']
        self.vao = self.get_vao()

    def get_vertex_data(self) -> np.array:
        sx, sy = WIDTH * CROSS_HAIR_SIZE / ASPECT_RATIO / 2, HEIGHT * CROSS_HAIR_SIZE
        vertices = [
            (sx, sy, 0.0), (-sx, sy, 0.0), (-sx, -sy, 0.0), 
            (sx, sy, 0.0), (-sx, -sy, 0.0), (sx, -sy, 0.0)
        ]

        colors = [
            (0, 0, 0), (0, 0, 0), (0, 0, 0),
            (0, 0, 0), (0, 0, 0), (0, 0, 0)
        ]

        vertex_data = np.hstack([vertices, colors], dtype='float32')
        return vertex_data
