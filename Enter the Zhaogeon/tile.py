import pygame
from pygame import *
from settings import *

class Tile(sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        
        size = 200
        
        self.image = Surface((size,size))
        self.image.fill("GREEN")
        self.rect = self.image.get_rect(topleft = pos)