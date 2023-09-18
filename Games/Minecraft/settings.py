from numba import njit
import numpy as np
import pygame as pg
import moderngl as mgl
import math
import glm
import time
import sys
import os

# resolution
WIDTH, HEIGHT = 1600, 900
WIN_RES = glm.vec2(WIDTH, HEIGHT)

# world
SEED = 76543

# cross_hair
CROSS_HAIR_SIZE = 0.000008
CROSS_HAIR_COLOR = glm.vec3(0.0)

# ray casting
MAX_RAY_DIST = 12

# chunk
CHUNK_SIZE = 48
H_CHUNK_SIZE = CHUNK_SIZE // 2
CHUNK_AREA = CHUNK_SIZE ** 2
CHUNK_VOL = CHUNK_SIZE ** 3
CHUNK_SPHERE_RADIUS = H_CHUNK_SIZE * math.sqrt(3)

# world
WORLD_W, WORLD_H = 20, 3
WORLD_D = WORLD_W
WORLD_AREA = WORLD_D * WORLD_W
WORLD_VOL = WORLD_AREA * WORLD_H

# world center
CENTER_XZ = WORLD_W * H_CHUNK_SIZE
CENTER_Y = WORLD_H * H_CHUNK_SIZE

# camera
ASPECT_RATIO = WIN_RES.x / WIN_RES.y
FOV_DEG = 50
V_FOV = glm.radians(FOV_DEG) # vertical FOV
H_FOV = 2 * math.atan(math.tan(V_FOV * .5) * ASPECT_RATIO) #horizontal FOV
NEAR = 0.1
FAR = 2000.0
PITCH_MAX = glm.radians(89)

# player
PLAYER_SPEED = 20
PLAYER_ROT_SPEED = 0.003
PLAYER_POS = glm.vec3(CENTER_XZ, 3 * CHUNK_SIZE, CENTER_XZ)
MOUSE_SENSITIVITY = 0.002

# colors
BG_COLOR = glm.vec3(0.1, 0.16, 0.25)