from pygame import *

class hitbox(sprite.Sprite):
    def __init__(self, w, h, x, y):
        super().__init__()
        
        self.image = 