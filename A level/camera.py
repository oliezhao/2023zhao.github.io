from pygame import *

from common import *

class Camera(sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.hitbox = Surface([100*scale, 50*scale])
        self.hitbox.fill("Green")
        self.rect = self.hitbox.get_rect(center = (screenx/2, screeny/2))