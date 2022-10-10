from pygame import *

from settings import *

class Camera(sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.hitbox = Surface([int(screenx * 4/10),int(screeny * 4/10)])
        self.hitbox.fill("Green")
        self.rect = self.hitbox.get_rect(topleft = (int(screenx * 3/10),int(screeny*3/10)))