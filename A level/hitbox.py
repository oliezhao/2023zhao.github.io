from pygame import *

class Hitox(sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()

        self.image = Surface((w,h))
        self.rect = self.image.get_rect(topleft = (x, y))

    def update(self, pos):
        self.rect.topleft = pos