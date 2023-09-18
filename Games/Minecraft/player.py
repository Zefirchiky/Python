from settings import *
from camera import Camera

class Player(Camera):
    def __init__(self, app, pos=PLAYER_POS, yaw=180, pitch = 0):
        self.app = app
        super().__init__(pos, yaw, pitch)

    def update(self):
        self.mouse_control()
        self.keyboard_control()
        super().update()

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            voxel_handler = self.app.scene.world.voxel_handler
            if event.button == 1:
                voxel_handler.remove_voxel()
                print("DESTROY")
            if event.button == 3:
                voxel_handler.add_voxel()
                print("CREATE")

    def mouse_control(self):
        mouse_dx, mouse_dy = pg.mouse.get_rel()
        
        if mouse_dx:
            self.rotate_yaw(dx=mouse_dx * MOUSE_SENSITIVITY)
        if mouse_dy:
            self.rotate_pitch(dy=mouse_dy * MOUSE_SENSITIVITY)

    def keyboard_control(self):
        key_state = pg.key.get_pressed()
        vel = PLAYER_SPEED * self.app.dt

        if key_state[pg.K_LCTRL]:
            vel *= 3
        if key_state[pg.K_w]:
            self.move_forward(vel)
        if key_state[pg.K_s]:
            self.move_back(vel)
        if key_state[pg.K_a]:
            self.move_left(vel)
        if key_state[pg.K_d]:
            self.move_right(vel)
        if key_state[pg.K_SPACE]:
            self.move_up(vel)
        if key_state[pg.K_LSHIFT]:
            self.move_down(vel)