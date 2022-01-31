import pygame
from pygame import *

class Block(sprite.Sprite):
    def __init__(self, width, height, x ,y):
        super().__init__()
        self.image = Surface(( width, height))
        self.rect = self.image.get_rect(topleft = (x, y))
        self.image.fill('White')