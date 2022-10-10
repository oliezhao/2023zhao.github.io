from pygame import *

from settings import *

class Wall(sprite.Sprite):
    def __init__(self, size, pos):
        super().__init__()
        
        self.image = Surface([size, size])
        self.image.fill("Blue")
        self.rect = self.image.get_rect(topleft = pos)