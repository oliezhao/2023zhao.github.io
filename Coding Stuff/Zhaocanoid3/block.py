import pygame
from pygame import *

class Block(sprite.Sprite):
    def __init__(self, color,width, height, pos):
        super().__init__()
        
        self.image = Surface((width, height))
        self.rect = self.image.get_rect(topleft = (pos))
        self.image.fill(color)
        
shape = ['----------',
         '----------',
         '----------',
         '----------',
         '----------',
         '----------',
         '----------',
         '----------',
         ]