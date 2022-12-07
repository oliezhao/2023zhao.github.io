from pygame import *
from common import *

from hitbox import *

list = [00, 10, 20, 30, 40, 19, 22, 50, 21]

class Tile(sprite.Sprite):
    def __init__(self, object, pos):
        super().__init__()
        
        filename = "graphics/spritesheets/WallSS.png"
        size = 16
        if object == 00: self.image = spritesheet_loader("graphics/spritesheets/WallSS.png", 1, 1, size)
        elif object == 10: self.image = spritesheet_loader("graphics/spritesheets/WallSS.png", 1, 2, size)
        elif object == 20: self.image = spritesheet_loader("graphics/spritesheets/WallSS.png", 1, 3, size)
        elif object == 30: self.image = spritesheet_loader("graphics/spritesheets/WallSS.png", 1, 4, size)
        elif object == 40: self.image = spritesheet_loader("graphics/spritesheets/WallSS.png", 1, 5, size)
        elif object == 50: self.image = spritesheet_loader("graphics/spritesheets/WallSS.png", 1, 6, size)
        elif object == 70: self.image = spritesheet_loader("graphics/spritesheets/WallSS.png", 1, 8, size)
        elif object == 18: self.image = spritesheet_loader("graphics/spritesheets/WallSS.png", 2, 1, size)
        elif object == 22: self.image = spritesheet_loader("graphics/spritesheets/WallSS.png", 2, 7, size)
        elif object == 32: self.image = spritesheet_loader("graphics/spritesheets/WallSS.png", 3, 1, size)
        elif object == 34: self.image = spritesheet_loader("graphics/spritesheets/WallSS.png", 3, 3, size)
        elif object == 19: self.image = spritesheet_loader("graphics/spritesheets/WallSS.png", 2, 4, size)
        elif object == 35: self.image = spritesheet_loader("graphics/spritesheets/WallSS.png", 3, 4, size)
        elif object == 36: self.image = spritesheet_loader("graphics/spritesheets/WallSS.png", 3, 5, size)
        elif object == 48: self.image = spritesheet_loader("graphics/spritesheets/WallSS.png", 4, 1, size)
        elif object == 21: self.image = spritesheet_loader("graphics/spritesheets/WallSS.png", 2, 5, size)
        else:
            self.image = Surface((16*scale, 16*scale))

        self.rect = self.image.get_rect(topleft = pos)
        
        if object == 48:
            self.hitbox = Hitox(self.rect.topleft[0], self.rect.topleft[1], 16*scale, 6 *scale)
        elif object in list:
            self.hitbox = Hitox(self.rect.midleft[0], self.rect.midleft[1], 16*scale, 8 *scale)
        else:
            self.hitbox = Hitox(self.rect.topleft[0], self.rect.topleft[1], 16 * scale, 16 * scale)
        
    def update(self):
        self.hitbox.update(self.rect.midleft)