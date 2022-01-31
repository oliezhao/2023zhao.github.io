import pygame
from pygame import *

class Laser(sprite.Sprite):
    def __init__(self, color, playerwidth, playermidtop, speed):
        super().__init__()
        
        self.image = Surface((playerwidth/50, playerwidth/5))
        self.rect = self.image.get_rect(midbottom = (playermidtop))
        self.image.fill(color)
        
        self.spd = speed
    
    def move(self):
        self.rect.y -= self.spd
    
    def deload(self):
        if self.rect.bottom < 0:
            self.kill()
    
    def update(self):
        self.move()
        self.deload()
        
        