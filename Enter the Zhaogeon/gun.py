from pygame import *
from settings import *


font = font.Font(None, int(screenx/50))

class Gun(sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        
        
        self.image = font.render(str("gun"), True, "White")
        self.rect = self.image.get_rect(topleft = pos)
        