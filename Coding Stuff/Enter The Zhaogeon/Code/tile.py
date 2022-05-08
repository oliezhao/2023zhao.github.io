from pygame import *
from settings import *

class Tile(sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.surface = Surface((tilesize,tilesize))
        self.surface.fill("white")
        self.rect = self.surface.get_rect(topleft = pos)
        