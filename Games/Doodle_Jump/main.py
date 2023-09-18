from random import randint
import pygame as pg
from math import *
import json

pg.init()

'''------------------Settings------------------'''
WIDTH, HEIGHT = 600, 900                    # Display size  (600, 900)
DIS = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("NoName")            # Game name

'''COLORS'''
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

FPS = 60
FONT_SIZE = 40                      # Score font size   (40)
DEATH_FONT_SIZE = 90                # Death font size   (90)
TEXT_DEATH = f"Press F to restart"  # Death text

PLATF_H = 20    # Platform height           (20)
PLATF_W = 100   # Platform width            (100)
PLATFS_H = 120  # Len between platforms     (120)
MAP_SPEED = 4   # Map speed                 (4)

PLAYER_AD_SPEED = 5 # Right\Left player speed  (5)
PLAYER_H = 75       # Player height            (75)
PLAYER_W = 55       # Player width             (55)

GRAVI = .3 # Gravity            (.2)
JUMP_H = 10 # Jump height       (10)

'''------------------ NOT CHANGE ------------------'''
lol = True

score_font = pg.font.SysFont("bahnschrift", FONT_SIZE)
death_font = pg.font.SysFont("Arial", DEATH_FONT_SIZE)

doodle_right = pg.transform.scale(pg.image.load("img/doodle-right.png"), (PLAYER_W, PLAYER_H))
doodle_left = pg.transform.scale(pg.image.load("img/doodle-left.png"), (PLAYER_W, PLAYER_H))
platform_img = pg.transform.scale(pg.image.load("img/1jump_panel.png"), (PLATF_W, PLATF_H))


class Map:
    def __init__(self):
        self.map_move_y = 50
        self.platfsx = [
            randint(20, WIDTH - PLATF_W - 20) for _ in range(19)]                                  # Firsts platforms X coords
        self.platfsy = [
            HEIGHT - 50 - randint(i*round(PLATFS_H/(1 + 0.2 / (i+1))),
                                  i*round(PLATFS_H*(1 + 0.2 / (i+1)))) for i in range(19)]         # Firsts platforms Y coords (with random range 0.4)
        self.platfsx[0] = int(WIDTH/2 - PLATF_W/2)                                                 # First platform in center
        self.score = 0
        self.bgcol1 = WHITE
        self.bgcol2 = BLACK
    
    def create(self): # Add/Delete platforms
        if len(self.platfsx) <= 20:
            self.platfsx.append(randint(20, WIDTH - PLATF_W - 20))                          # Create platforms X coords
            self.platfsy.append(self.platfsy[-1] - randint(PLATFS_H/1.2, PLATFS_H*1.2))     # Create platforms Y coords (with random range 0.4)
        elif self.platfsy[0] > HEIGHT:
            del self.platfsx[0], self.platfsy[0]
            self.score += 1
            if self.score % 40 == 0 and self.score != 0:                    # BG change every 40 score
                self.bgcol2, self.bgcol1 = self.bgcol1, self.bgcol2
        
    def map_move(self, playery):
        if playery < HEIGHT/8:
            self.map_move_y -= 2.5*MAP_SPEED
            for i in range(len(self.platfsy)):          # Move every Y platforms
                self.platfsy[i] += 2.5*MAP_SPEED
            return 2.5*MAP_SPEED                        # Move player Y
        elif playery < HEIGHT/4:
            self.map_move_y -= 1.5*MAP_SPEED
            for i in range(len(self.platfsy)):
                self.platfsy[i] += 1.5*MAP_SPEED
            return 1.5*MAP_SPEED
        elif playery < HEIGHT/2:
            self.map_move_y -= MAP_SPEED
            for i in range(len(self.platfsy)):
                self.platfsy[i] += MAP_SPEED
            return MAP_SPEED
        return 0
        
    def platf_draw(self):                       # Platforms render
        for i in range(len(self.platfsx)):
            DIS.blit(platform_img, (self.platfsx[i], self.platfsy[i]))
            
    def texts(self, font, text, color_outline, color, x, y):            # Score text with outlines
        DIS.blit(font.render(text, True, color_outline), [x-2, y-2])
        DIS.blit(font.render(text, True, color_outline), [x-2, y+2])
        DIS.blit(font.render(text, True, color_outline), [x+2, y-2])
        DIS.blit(font.render(text, True, color_outline), [x+2, y+2])
        DIS.blit(font.render(text, True, color), [x, y])
            
    def background(self):
        DIS.fill(self.bgcol2)
    
    
class Player(object):
    def __init__(self):
        self.player_name = input("Name:")
        self.playerx = int(WIDTH/2 - PLAYER_W/2)        # First player X coord
        self.playery = HEIGHT - PLAYER_H - 30           # First player Y coord
        self.y_change = 0
        self.jump = False
        self.doodle = doodle_right
        self.data_death = 0
        try:
            with open("data.json", "r") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {}
            
        self.DEATH = True
        self.data_load = True
    
    def create(self):               # Player render
        DIS.blit(self.doodle, [self.playerx, self.playery])
    
    def collision(self, game_map, j):                                                   # Collision player\platforms
        self.player_rect = pg.Rect(self.playerx, self.playery, PLAYER_W, PLAYER_H)      # Player rect
        for i in range(len(game_map.platfsx)):                                          # All platforms
            '''Player touch platform   AND   player don`t jump   AND   player go down'''
            if self.player_rect.colliderect(pg.Rect(game_map.platfsx[i],
                                                    game_map.platfsy[i],
                                                    PLATF_W, PLATF_H)) \
                and self.jump == False \
                and self.y_change >= 0:
                j = True
        return j
    
    def move(self, keys, playerMAP_SPEED):
        if self.jump:
            self.y_change = -JUMP_H             # Jump
            self.jump = False
        self.playery += playerMAP_SPEED         # Graviti
        self.playery += self.y_change
        self.y_change += GRAVI
        
        if keys[pg.K_a] and self.playerx > 0:           # Move left
            self.playerx -= PLAYER_AD_SPEED
            self.doodle = doodle_left
        elif keys[pg.K_d] and self.playerx < WIDTH - PLAYER_W:     # Move right
            self.playerx += PLAYER_AD_SPEED
            self.doodle = doodle_right
            
    def death(self, keys):
        if self.playery > HEIGHT and keys[pg.K_f] == False:                # If player touch ground
            DIS.blit(death_font.render(TEXT_DEATH, True, RED), [10, HEIGHT/2 - DEATH_FONT_SIZE/2])
            if self.DEATH:
                self.death_data_add()
                self.DEATH = False
            return True
        elif self.playery > HEIGHT and keys[pg.K_f]:
            self.DEATH = True
            return False
        else:
            return True
    
    def score_read(self, score):
        open("data.json", "x")

        with open("data.json", "r") as f:
            if self.data_load:
                self.data = json.load(f)
        
        if self.player_name in self.data:
            if self.data[self.player_name]["Score"] < score:
                self.data[self.player_name]["Score"] = score
                
        else:
            self.data[self.player_name] = {"Score": 0,
                                        "Death": self.data_death}
            
        with open("data.json", "w") as f:
            json.dump(self.data, f, indent=4)
        
        self.data_load = True
        return self.data[self.player_name]["Score"]
        
    def death_data_add(self):
        self.data_load = False
        self.data[self.player_name]["Death"] += 1

def main():
    run = True
    
    while run:
        clock = pg.time.Clock()
        game_map = Map()
        player = Player()
        not_rest = True
        while not_rest:
            clock.tick(FPS)
            game_map.background()
            keys_pressed = pg.key.get_pressed()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    not_rest = False
                    run = False
            playerMAP_SPEED = game_map.map_move(player.playery)
            game_map.platf_draw()
            game_map.create()
            player.create()
            player.jump = player.collision(game_map, player.jump)
            player.move(keys_pressed, playerMAP_SPEED)
            score_data = player.score_read(game_map.score)
            game_map.texts(score_font, f"Score: {game_map.score}", WHITE, BLACK, 50, 100)
            game_map.texts(score_font, f"Record: {score_data}", WHITE, BLACK, 50, 50)
            not_rest = player.death(keys_pressed)
            pg.display.update()

    
    pg.quit()


if __name__ == "__main__":
    main()