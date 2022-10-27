from pygame import *

from settings import *

class Wall(sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        
        self.image = Surface([int(screenx * 15/256), int(screeny * 15/144)])
        self.image.fill("Blue")
        self.rect = self.image.get_rect(topleft = pos)