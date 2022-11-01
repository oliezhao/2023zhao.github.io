from pygame import *
from settings import *


font = font.Font(None, int(screenx/50))

class Gun(sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        
        self.image = Surface([screenx/10, screenx/20])
        self.rect = self.image.get_rect(topleft = pos)
        self.image.fill("Red")
        self.text = font.render(str("gun"), True, "White")
        self.text_rect = self.text.get_rect(topleft = pos)
    