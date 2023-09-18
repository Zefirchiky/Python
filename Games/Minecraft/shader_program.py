from settings import *

class ShaderProgram:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.player = app.player

        # ----------- Shaders ----------- #
        self.chunk = self.get_program(shader_name='chunk')
        self.cross_hair = self.get_program(shader_name='cross_hair')
        self.voxel_marker = self.get_program(shader_name='voxel_marker')
        # ------------------------------- #

        self.set_uniform_on_init()

    def set_uniform_on_init(self):
        # chunk
        self.chunk['m_proj'].write(self.player.m_proj)
        self.chunk['m_model'].write(glm.mat4())
        self.chunk['u_texture_0'] = 0
        
        # marker
        self.voxel_marker['m_proj'].write(self.player.m_proj)
        self.voxel_marker['m_model'].write(glm.mat4())
        self.voxel_marker['u_texture_0'] = 0

    def update(self):
        self.chunk['m_view'].write(self.player.m_view)
        self.voxel_marker['m_view'].write(self.player.m_view)


    def get_program(self, shader_name):
        with open(f'shaders/{shader_name}.vert') as f:
            vert_shader = f.read()

        with open(f'shaders/{shader_name}.frag') as f:
            frag_shader = f.read()

        program = self.ctx.program(vertex_shader=vert_shader, fragment_shader=frag_shader)
        return program
