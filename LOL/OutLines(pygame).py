import pygame

def texts(self, DIS, font, text, color_outline, size_outline, color, x, y):
    DIS.blit(font.render(text, True, color_outline), [x-size_outline, y-size_outline])
    DIS.blit(font.render(text, True, color_outline), [x-size_outline, y+size_outline])
    DIS.blit(font.render(text, True, color_outline), [x+size_outline, y-size_outline])
    DIS.blit(font.render(text, True, color_outline), [x+size_outline, y+size_outline])
    DIS.blit(font.render(text, True, color), [x, y])