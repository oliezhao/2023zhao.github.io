from pygame import *

from settings import *

class Wall(sprite.Sprite):
    def __init__(self,size, pos):
        super().__init__()
        
        self.image = Surface([int(size), int(size)])
        self.image.fill("#3d3244")
        self.rect = self.image.get_rect(topleft = pos)