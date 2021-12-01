import pygame
from pygame import *

class Laser(sprite.Sprite):
    def __init__(self,playerx, playery, pos):
        super().__init__()
        
        self.x = playerx / 20
        self.y = playery * 5
        
        self.image = Surface((self.x, self.y))
        self.image.fill('Red')
        self.rect = self.image.get_rect(midbottom = (pos))
        self.velocity = 50
    
    def deload(self):
        if self.rect.bottom < 0:
            self.kill()
    
    def update(self):
        self.deload()
        self.rect.y -= self.velocity
    
    
    