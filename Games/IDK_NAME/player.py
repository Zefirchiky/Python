from settings import *
from textures import Texture

class Attack(Enum):
    NONE = 0
    NR1 = 1
    NR2 = 2
    NR3 = 3

class Player:
    def __init__(self, app):
        self.app = app
        self.WIN = app.WIN
        self.size = PLAYER_WH
        self.pos = glm.vec2(PLAYER_POS.x - self.size.x // 2, PLAYER_POS.y - self.size.y)
        print(self.pos)
        self.speed = PLAYER_SPEED

        self.state = 'stand'
        self.prev_state = self.state
        self.direction = 'right'

        self.is_moving = False
        self.attack = Attack.NONE
        self.state_can_change = True
        self.animation_i = 0

        self.sprites_num = {
                                'stand': 8,
                                'run': 8,
                                'attack_NR1': 13,
                                'attack_NR2': 13,
                                'attack_NR3': 17,
                                'hurt': 5,
                                'death': 10
                            }

        self.texture = Texture(f'assets/entities/{PLAYER_TEXTURE}', PLAYER_WH, self.sprites_num, mult=PLAYER_SIZE)

    def mouse_handler(self, event: pg.event.Event):
        if event.type == pg.MOUSEBUTTONDOWN:
            match event.button:
                case 1:
                    self.attack = Attack.NR1
                case 3:
                    self.attack = Attack.NR2

    def update(self):
        self.move()
        self.update_cur_state()

    def update_cur_state(self):
        if self.attack != Attack.NONE:
            self.state = f'attack_{self.attack.name}'
            self.state_can_change = False

        elif self.state_can_change:
            if self.is_moving:
                self.state = 'run'
            else:
                self.state = 'stand'

        if self.prev_state != self.state or self.animation_i >= self.sprites_num[self.state] - 1:
            self.animation_i = 0
        else:
            self.animation_i += ANIMATION_SPEED * self.app.dt

        self.prev_state = self.state

    def get_cur_sprite(self):
        if self.attack != Attack.NONE and self.animation_i >= self.sprites_num[self.state] - 1:
            self.state_can_change = True
            self.attack = Attack.NONE
            
        return self.texture.sprites[self.state][self.direction][int(self.animation_i)]

    def render(self):
        self.WIN.blit(self.get_cur_sprite(), self.pos)

    def move(self):
        key_state = pg.key.get_pressed()
        vel = PLAYER_SPEED * self.app.dt * 20
        self.is_moving = any((key_state[pg.K_d], key_state[pg.K_a], key_state[pg.K_s], key_state[pg.K_w]))

        if key_state[pg.K_d]:
            self.pos.x += vel
            self.direction = 'right'
        if key_state[pg.K_a]:
            self.pos.x -= vel
            self.direction = 'left'

        self.pos.y += (key_state[pg.K_s] - key_state[pg.K_w]) * vel
