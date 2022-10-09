from pygame import *
from settings import *

#The Cursor is decalred in Main
class Cursor(sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = image.load("graphics/cursor-9x9.png")
        self.image = transform.scale(self.image, (int(screenx * 5/256), int(screeny * 5/144)))
        self.rect = self.image.get_rect(center = mouse.get_pos())
    
    def update(self):
        self.rect.center = mouse.get_pos()