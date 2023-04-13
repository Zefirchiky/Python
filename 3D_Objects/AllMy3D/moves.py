import numpy as np
from math import sin, cos

def translation(coords):
    dx, dy = coords
    return np.array([
        [1, 0, 0],
        [0, 1, 0],
        [dx, dy, 1]
    ])

def rotate_x(a):
    return np.array([
        [1, 0, 0],
        [0, cos(a), -sin(a)],
        [0, sin(a), cos(a)]
    ])
    
def rotate_y(a):
    return np.array([
        [cos(a), 0, sin(a)],
        [0, 1, 0],
        [-sin(a), 0, cos(a)]
    ])

def rotate_z(a):
    return np.array([
        [cos(a), -sin(a), 0],
        [sin(a), cos(a), 0],
        [0, 0, 1]
    ])
    
def scale_f(k):
    return np.array([
        [k, 0, 0],
        [0, k, 0],
        [0, 0, 1]
    ])