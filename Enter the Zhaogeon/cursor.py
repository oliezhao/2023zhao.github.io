from pygame import *
from settings import *

class Cursor(sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = image.load("graphics/cursor-6x6.png")
        self.image = transform.scale(self.image, (screenx * 6/256, screeny * 6/144))
        self.image
        self.rect = self.image.get_rect(center = mouse.get_pos())
    
    def update(self):
        self.rect.center = mouse.get_pos()