from pygame import *
from math import atan2, degrees

aspect_ratio = (16,9)
screenx = 1920
screeny = screenx * (aspect_ratio[1]/aspect_ratio[0])

scale = screenx/256

screen_resolution = (screenx, screeny)

def spritesheet_loader(filename, row, column, size):
    row -= 1
    column -= 1
    spritesheet = image.load(filename).convert_alpha()
    sprite = Surface((16,16))
    sprite.blit(spritesheet, (0,0), (column * 16, row * 16, size * 16, size * 16))
    sprite = transform.scale(sprite, (16 * scale, 16 * scale)).convert_alpha()
    
    sprite.set_colorkey((0,0,0))
    
    return sprite

def get_angle(rect1, rect2):
    dy = -(rect2[1] - rect1[1])
    dx = rect2[0] - rect1[0]
    
    angle = atan2(dy, dx)

    return degrees(angle)