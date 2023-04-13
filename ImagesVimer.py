from time import sleep
import pygame as pg

W, H = 1500, 1100
DIS = pg.display.set_mode((W, H))
pg.display.set_caption("LOL")

for i in range(9000):
    img = pg.image.load(f"D:\Artem\ijknhbg\Bests\{i}")
    img_s = img.get_size()
    DIS.blit(img, (W/2 - img_s[0]/2, H/2 - img_s[1]/2))

    