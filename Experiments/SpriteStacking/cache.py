from settings import *

class Cache:
    def __init__(self):
        self.stacked_sprite_cache = {}
        self.v_angle = 360 / NUM_ANGLES
        self.get_stacked_sprite_cache()
        
    def get_stacked_sprite_cache(self):
        for name in STACKED_SPRITE_ATTRIBUTE:
            self.stacked_sprite_cache[name] = {
                "rotated_sprite": {}
            }
            attr = STACKED_SPRITE_ATTRIBUTE[name]
            layer_array = self.get_layer_array(attr)
            self.run_prerender(name, layer_array, attr)
            
    def run_prerender(self, name, layer_array, attr):
        for angle in range(NUM_ANGLES):
            # 1 layer size surface
            surf = pg.Surface(layer_array[0].get_size())
            surf = pg.transform.rotate(surf, angle * self.v_angle)
            # Sprite layers surface
            sprite_surf = pg.Surface((surf.get_width(), surf.get_height()
                                    + attr["num_layers"] * attr["scale"]))
            sprite_surf.fill('khaki')
            sprite_surf.set_colorkey('khaki')
            
            # Blit layers on sprite_surf
            for i, layer in enumerate(layer_array):
                layer = pg.transform.rotate(layer, angle * self.v_angle)
                sprite_surf.blit(layer, (0, i * attr["scale"]))
                
            # Flip sprite_surf
            image = pg.transform.flip(sprite_surf, True, True)
            self.stacked_sprite_cache[name]["rotated_sprite"][angle] = image
            
    def get_layer_array(self, attr):
        # Load all layers img
        sprite_sheet = pg.image.load(attr["path"]).convert_alpha()
        # Increment img scale
        sprite_sheet = pg.transform.scale(sprite_sheet,
                                          vec2(sprite_sheet.get_size()) * attr["scale"])
        sheet_width = sprite_sheet.get_width()
        sheet_height = sprite_sheet.get_height()
        sprite_height = sheet_height // attr["num_layers"]
        sheet_height = sprite_height * attr["num_layers"]
        # Cutting image
        layer_array = []
        for y in range(0, sheet_height, sprite_height):
            sprite = sprite_sheet.subsurface((0, y, sheet_width, sprite_height))
            layer_array.append(sprite)
        return layer_array[::-1]
            