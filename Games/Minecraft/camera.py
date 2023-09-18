from settings import *
from frustum import Frustum

class Camera:
    def __init__(self, pos, yaw, pitch):
        self.pos = glm.vec3(pos)
        self.yaw = glm.radians(yaw)
        self.pitch = glm.radians(pitch)

        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)

        self.m_proj = glm.perspective(V_FOV, ASPECT_RATIO, NEAR, FAR)
        self.m_view = glm.mat4()

        self.frustum = Frustum(self)

    def update(self):
        self.update_vectors()
        self.update_view_matrix()

    def update_view_matrix(self):
        self.m_view = glm.lookAt(self.pos, self.pos + self.forward, self.up)

    def update_vectors(self):
        self.forward.x = glm.cos(self.yaw) * glm.cos(self.pitch)
        self.forward.y = glm.sin(self.pitch)
        self.forward.z = glm.sin(self.yaw) * glm.cos(self.pitch)

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    def rotate_pitch(self, dy):
        self.pitch -= dy
        self.pitch = glm.clamp(self.pitch, -PITCH_MAX, PITCH_MAX)

    def rotate_yaw(self, dx):
        self.yaw += dx

    def move_left(self, velocity):
        self.pos -= self.right * velocity

    def move_right(self, velocity):
        self.pos += self.right * velocity

    def move_up(self, velocity):
        self.pos += self.up * velocity

    def move_down(self, velocity):
        self.pos -= self.up * velocity

    def move_forward(self, velocity):
        self.pos += self.forward * velocity

    def move_back(self, velocity):
        self.pos -= self.forward * velocity