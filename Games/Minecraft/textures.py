from settings import *

class Textures:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx

        self.texture_0: mgl.Texture = self.load('image.jpg')

        self.texture_0.use(location=0)

    def load(self, filename):
        texture = pg.image.load(f'assets/{filename}')
        texture = pg.transform.flip(texture, True, False)

        texture = self.ctx.texture(
            size=texture.get_size(),
            components=4,
            data=pg.image.tostring(texture, 'RGBA')
        )
        texture.anisotropy = 32.0
        texture.build_mipmaps()
        texture.filter = (mgl.NEAREST, mgl.NEAREST)
        return texture