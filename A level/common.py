from pygame import *
import json

from math import atan2, degrees

aspect_ratio = (16,9)
screenx = 1920
screeny = screenx * (aspect_ratio[1]/aspect_ratio[0])

scale = screenx/256

screen_resolution = (screenx, screeny)

class SpriteSheet:
    def __init__(self, filename):
        super().__init__()

        self.filename = filename
        self.spritesheet = image.load(filename)
        self.meta_data = self.filename.replace("png", "json")
        
        with open(self.meta_data) as f:
            self.data = json.load(f)
        f.close()
        
    def parse_sprite(self, name):
        sprite = self.data["frames"][name]["frame"]
        x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        image = self.get_sprite(x, y, w, h)
        return image
        
    def get_sprite(self, x, y, w, h):
        sprite = Surface((w, h))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.spritesheet, (0,0), (x, y, w, h))
        sprite = transform.scale(sprite, (w * scale, h  * scale)).convert_alpha()

        return sprite


def get_angle(rect1, rect2):
    dy = -(rect2[1] - rect1[1])
    dx = rect2[0] - rect1[0]
    
    angle = atan2(dy, dx)

    return degrees(angle)

