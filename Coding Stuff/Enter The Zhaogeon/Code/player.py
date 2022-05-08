from pygame import *
from settings import *

class Player(sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = image.load("../Graphics/White_Boy.aseprite")
        self.rect = self.image.get_rect(topleft = pos)