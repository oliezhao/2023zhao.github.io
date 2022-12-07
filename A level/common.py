from pygame import *
from math import atan2, degrees

aspect_ratio = (16,9)
screenx = 1000
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

testlevel = [
    [00,10,10,10,10,10,10,10,10,10,10,10,20,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [18,48,48,48,48,48,48,48,48,48,48,48,18,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [18,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,18,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [18,-1,-1,19,21,-1,-1,-1,19,21,-1,-1,70,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,20],
    [18,-1,-1,35,36,38,-1,-1,35,36,-1,-1,18,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,18],
    [18,-1,-1,48,48,-1,-1,-1,48,48,-1,-1,18,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,18],
    [18,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,18,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,18],
    [18,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,18,-1,-1,-1,19,21,-1,-1,-1,-1,-1,-1,-1,-1,-1,19,21,-1,-1,-1,18],
    [18,-1,-1,19,21,-1,-1,-1,19,21,-1,-1,18,-1,-1,-1,35,36,-1,-1,-1,-1,-1,-1,-1,-1,-1,35,36,-1,-1,-1,18],
    [18,-1,-1,35,36,-1,-1,-1,35,36,-1,-1,18,-1,-1,-1,48,48,-1,-1,-1,-1,-1,-1,-1,-1,-1,48,48,-1,-1,-1,18],
    [18,-1,-1,48,48,-1,-1,-1,48,48,-1,-1,18,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,18],
    [70,10,10,10,40,-1,-1,-1,30,10,10,10,34,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,18],
    [18,48,48,48,48,-1,-1,-1,48,48,48,48,48,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,18],
    [18,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,18],
    [18,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,18],
    [70,10,10,10,10,40,-1,30,10,10,10,10,20,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,18],
    [18,48,48,48,48,48,-1,48,48,48,48,48,18,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,18],
    [18,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,18,-1,-1,-1,19,21,-1,-1,-1,-1,-1,-1,-1,-1,-1,19,21,-1,-1,-1,18],
    [18,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,18,-1,-1,-1,35,36,-1,-1,-1,-1,-1,-1,-1,-1,-1,35,36,-1,-1,-1,18],
    [18,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,18,-1,-1,-1,48,48,-1,-1,-1,-1,-1,-1,-1,-1,-1,48,48,-1,-1,-1,18],
    [18,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,18,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,18],
    [18,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,70,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,34],
    [18,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,18,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [18,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,18,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [32,10,10,10,10,10,10,10,10,10,10,10,34,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
]