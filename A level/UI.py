from pygame import *
from common import *

class Cursor(sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = image.load("graphics/sprites/cursor-9x9.png").convert_alpha()
        self.image = transform.scale(self.image, (6 * scale, 6 * scale)).convert_alpha()
        self.rect = self.image.get_rect(center = mouse.get_pos())
    
    def update(self):
        self.rect.center = mouse.get_pos()
        
class Button(sprite.Sprite):
    def __init__(self, text, color, size, pos, font_file):
        super().__init__()
        
        self.font = font.Font(font_file, size)
        self.image = self.font.render(text, True, color)
        self.rect = self.image.get_rect(center = pos)

        
