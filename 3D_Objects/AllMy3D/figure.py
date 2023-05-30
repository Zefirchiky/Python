import pygame as pg
from moves import *
import itertools as itt
import numba

'''Colors'''
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)

coord_vectors = itt.cycle(["X", "Y", "Z"])

'''3d to 2d matrix'''
projection_matrix = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
])     

class Figure:
    def __init__(self, dot_coords, 
                 lines = np.array([]),
                 faces = np.array([])):
        # [x, y, z]

        self.coords = dot_coords
        self.lines = lines
        self.faces = faces
        
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
        
        self.transformations_changed = True
        self.screen_size = pg.display.Info()
    
    def transl(self, keys, speed):
        dx = (keys[pg.K_RIGHT] - keys[pg.K_LEFT]) * speed
        dy = (keys[pg.K_DOWN] - keys[pg.K_UP]) * speed
        self.translxy[0] += dx
        self.translxy[1] += dy
    
    def rotate(self, keys, speed):
        dax = float((keys[pg.K_s] - keys[pg.K_w]) * speed)
        day = float((keys[pg.K_d] - keys[pg.K_a]) * speed)
        daz = float((keys[pg.K_e] - keys[pg.K_q]) * speed)
        self.anglex += dax
        self.angley += day
        self.anglez += daz
        self.rotatex = rotate_x(self.anglex)
        self.rotatey = rotate_y(self.angley)
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
        transform_matrix = np.dot(self.rotatey, self.rotatex)
        transform_matrix = np.dot(transform_matrix, self.rotatez)
        transform_matrix = np.dot(transform_matrix, self.scale_matrix)
        project_dots = np.dot(self.coords, transform_matrix)                # Transform main figure
        project_coord_dots = np.dot(self.coord_coords, transform_matrix)    # Transform coord sys
            
        return project_dots, project_coord_dots

    @numba.jit
    def draw(self, surface, line_size: int | float, 
             col: list | tuple, coord_col: list | tuple, 
             X, Y, font, project_dots, 
             project_coord_dots, coords_on):
        Xtransl = X + self.translxy[0]
        Ytransl = Y + self.translxy[1]
        for i, num in enumerate(project_dots):                                      # Render cube dots
            x = int(num[0] * line_size + Xtransl)
            y = int(num[1] * line_size + Ytransl)
            if x > -50 and x < self.screen_size.current_w + 50 and y > -50 and y < self.screen_size.current_h:
                pg.draw.circle(surface, col, (x, y), 1)
                
        if coords_on: 
            for i, dot in enumerate(project_coord_dots):                                # Render coord dots
                x = int(dot[0] * line_size + Xtransl)
                y = int(dot[1] * line_size + Ytransl)
                pg.draw.circle(surface, col, (x, y), 4)
                

        for i in self.faces:                                   # TODO Render cube faces
            x1, y1 = project_dots[i[0]][0] * line_size + Xtransl, project_dots[i[0]][1] * line_size + Ytransl
            x2, y2 = project_dots[i[1]][0] * line_size + Xtransl, project_dots[i[1]][1] * line_size + Ytransl
            #print(i, len(project_dots))
            x3, y3 = project_dots[i[2]][0] * line_size + Xtransl, project_dots[i[2]][1] * line_size + Ytransl
            x4, y4 = project_dots[i[3]][0] * line_size + Xtransl, project_dots[i[3]][1] * line_size + Ytransl
            pg.draw.polygon(surface, WHITE, ((0, 0), (50, 0), (25, 50), (0, 50)))
            pg.draw.polygon(surface, col, ((x1, y1), (x2, y2), (x3, y3), (x4, y4)))
        
        for i in self.lines:                                   # Render cube lines
            x1, y1 = project_dots[i[0]][0] * line_size + Xtransl, project_dots[i[0]][1] * line_size + Ytransl
            x2, y2 = project_dots[i[1]][0] * line_size + Xtransl, project_dots[i[1]][1] * line_size + Ytransl
            pg.draw.line(surface, col, (x1, y1), (x2, y2))

        cols = itt.cycle(coord_col)
        if coords_on:    
            for i, dot in enumerate(self.coord_lines):                                  # Render coord lines with different colors + X, Y, Z
                x1, y1 = project_coord_dots[dot[0]][0] * line_size + Xtransl, project_coord_dots[dot[0]][1] * line_size + Ytransl
                x2, y2 = project_coord_dots[dot[1]][0] * line_size + Xtransl, project_coord_dots[dot[1]][1] * line_size + Ytransl
                pg.draw.line(surface, next(cols), (x1, y1), (x2, y2))
                surface.blit(font.render(next(coord_vectors), True, col), (x2+10, y2-15))
                
    def rendering(self, surface, keys: list | tuple, 
                  X: int | float, Y: int | float, 
                  col: list | tuple, font, 
                  size: int | float, 
                  translation_speed: int | float, 
                  rotation_speed: int | float, *_, 
                  coords_on: bool = False, coords_col: list | tuple = (RED, BLUE, GREEN)):
        self.transl(keys, translation_speed)
        self.rotate(keys, rotation_speed)
        self.scale(keys)
        project_dots, project_coord_dots = self.mutation()
        self.draw(surface, size, col, coords_col, X, Y, font, project_dots, project_coord_dots, coords_on)