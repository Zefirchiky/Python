import pygame as pg
from moves import *

'''Colors'''
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)

coord_vectors = ["X", "Y", "Z"]

'''3d to 2d matrix'''
projection_matrix = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
])     

class Figure:
    def __init__(self, dot_coords, lines):
        # [x, y, z]

        self.coords = dot_coords
        
        self.lines = lines
        
        self.coord_coords = np.array([
            [0, 0, 0], [1.5, 0, 0], [0, -1.5, 0], [0, 0, 1.5]
        ])
        
        self.coord_lines = np.array([
            [0, 1], [0, 2], [0, 3]
        ])
        
        self.translxy = [0, 0]       # Movement coords
        self.anglex = 0
        self.angley = 0
        self.anglez = 0
        self.scalec = 1
        
        '''Moves matrices'''
        self.transl_matrix = translation(self.translxy)
        self.rotatex = rotate_x(self.anglez)
        self.rotatey = rotate_y(self.anglez)
        self.rotatez = rotate_z(self.anglez)
        self.scale_matrix = scale_f(self.scalec)
    
    def transl(self, keys, speed):
        if keys[pg.K_UP]:
            self.translxy[1] -= speed
        if keys[pg.K_DOWN]:
            self.translxy[1] += speed
        if keys[pg.K_LEFT]:
            self.translxy[0] -= speed
        if keys[pg.K_RIGHT]:
            self.translxy[0] += speed
    
    def rotate(self, keys, speed):
        if keys[pg.K_s]:
            self.anglex += speed
            self.rotatex = rotate_x(self.anglex)
        if keys[pg.K_w]:
            self.anglex -= speed
            self.rotatex = rotate_x(self.anglex)
            
        if keys[pg.K_a]:
            self.angley += speed
            self.rotatey = rotate_y(self.angley)
        if keys[pg.K_d]:
            self.angley -= speed
            self.rotatey = rotate_y(self.angley)
            
        if keys[pg.K_q]:
            self.anglez += speed
            self.rotatez = rotate_z(self.anglez)
        if keys[pg.K_e]:
            self.anglez -= speed
            self.rotatez = rotate_z(self.anglez)
        
    def scale(self, keys):
        if keys[pg.K_z]:
            self.scalec /= 1.02
            self.scale_matrix = scale_f(self.scalec)
        if keys[pg.K_x]:
            self.scalec *= 1.02
            self.scale_matrix = scale_f(self.scalec)
        
    def mutation(self):
        '''3D coords change and 3D => 2D'''
        transform_matrix = self.rotatey @ self.rotatex @ self.rotatez @ self.scale_matrix
        project_dots = []
        project_coord_dots = []
        for i in self.coords:
            transformed_point = i @ transform_matrix
            project_dots.append(transformed_point)
            
        for i in self.coord_coords:
            transformed_point = i @ transform_matrix
            project_coord_dots.append(transformed_point)
            
        return project_dots, project_coord_dots
    
    def draw(self, surfes, line_size: int | float, col: list | tuple, coord_col: list | tuple, X, Y, font, project_dots, project_coord_dots, coords_on):
        x_col = 0
        for i in project_dots:                                      # Render cube dots
            x = int(i[0] * line_size + X + self.translxy[0])
            y = int(i[1] * line_size + Y + self.translxy[1])
            pg.draw.circle(surfes, col, (x, y), 5)
        if coords_on: 
            for i in project_coord_dots:                                # Render coord dots
                x = int(i[0] * line_size + X + self.translxy[0])
                y = int(i[1] * line_size + Y + self.translxy[1])
                pg.draw.circle(surfes, col, (x, y), 5)

        for i in self.lines:                                   # Render cube lines
            x1, y1 = project_dots[i[0]][0] * line_size + X + self.translxy[0], project_dots[i[0]][1] * line_size + Y + self.translxy[1]
            x2, y2 = project_dots[i[1]][0] * line_size + X + self.translxy[0], project_dots[i[1]][1] * line_size + Y + self.translxy[1]
            pg.draw.line(surfes, col, (x1, y1), (x2, y2))    
        if coords_on:    
            for i in self.coord_lines:                                  # Render coord lines with diferent colors + X, Y, Z
                x1, y1 = project_coord_dots[i[0]][0] * line_size + X + self.translxy[0], project_coord_dots[i[0]][1] * line_size + Y + self.translxy[1]
                x2, y2 = project_coord_dots[i[1]][0] * line_size + X + self.translxy[0], project_coord_dots[i[1]][1] * line_size + Y + self.translxy[1]
                pg.draw.line(surfes, coord_col[x_col], (x1, y1), (x2, y2))
                surfes.blit(font.render(coord_vectors[x_col], True, col), (x2+10, y2-15))
                x_col += 1
                
    def rendering(self, surfes, keys: list | tuple, size: int | float, X: int | float, Y: int | float, col: list | tuple, font, translation_speed: int | float, rotation_speed: int | float, *_, coords_on: bool = False, coords_col: list | tuple = (RED, BLUE, GREEN)):
        self.transl(keys, translation_speed)
        self.rotate(keys, rotation_speed)
        self.scale(keys)
        project_dots, project_coord_dots = self.mutation()
        self.draw(surfes, size, col, coords_col, X, Y, font, project_dots, project_coord_dots, coords_on)