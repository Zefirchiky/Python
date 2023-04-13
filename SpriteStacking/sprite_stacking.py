from settings import *
import pygame as pg

class StackedSprite(pg.sprite.Sprite):
    def __init__(self, app, name, pos):
        self.app = app
        self.name = name
        self.pos = pos
        # Auto group append
        self.group = app.main_group
        super().__init__(self.group)
        
        self.attr = STACKED_SPRITE_ATTRIBUTE[name]
        # Cache load
        self.cache = app.cache.stacked_sprite_cache
        self.v_angle = app.cache.v_angle
        self.rotated_sprites = self.cache[name]["rotated_sprite"]
        self.angle = 0
        
    def update(self):
        self.get_image()
        self.get_angle()
        
    def get_angle(self):
        self.angle = -math.degrees(self.app.time) // self.v_angle
        self.angle = int(self.angle % NUM_ANGLES)
        
    def get_image(self):
        self.image = self.rotated_sprites[self.angle]
        self.rect = self.image.get_rect(center=self.pos + CENTER)

        