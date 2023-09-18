from settings import *

class Texture:
    def __init__(self, filename, size, num, *, mult = glm.vec2(1, 1)):
        self.texture = pg.image.load(filename).convert_alpha()
        self.size = size
        self.w, self.h = size
        self.num = num
        self.mult = mult
        self.sprites = self.get_sprites()

    def get_sprite(self, x, y):
        sprite = pg.Surface((self.w, self.h))
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.texture, (0, 0), (x * self.w, y * self.h, self.w, self.h))
        return pg.transform.scale(sprite, self.mult * self.size)
    
    def get_sprites(self):
        sprites = {}
        u = 0

        for name, n in self.num.items():
            TEMP_R, TEMP_L = [], []
            sprites[name] = {}

            for i in range(n):
                TEMP_R.append(self.get_sprite(i, u))
            for sprite in TEMP_R:
                TEMP_L.append(pg.transform.flip(sprite, True, False))

            sprites[name]['right'] = TEMP_R
            sprites[name]['left'] = TEMP_L
            u += 1

        return sprites
    