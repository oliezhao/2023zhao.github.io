import pygame
from pygame import *

class Ball(sprite.Sprite):
    def __init__(self, windowsize, color, pos, spd):
        super().__init__()
    
        #-- ball image
        self.image = Surface((windowsize[0]/100, windowsize[0]/100))
        self.rect = self.image.get_rect(midbottom = (pos))
        self.image.fill(color)
        
        #-- ball parameters
        self.max_x = windowsize[0]
        self.max_y = windowsize[1]
        self.spd = spd
        self.spdx = 0
        self.spdy = spd
        
    def checkBorder(self):
        if self.rect.top < 0:
            self.rect.top = 0
            self.spdy =  abs(self.spdy)
        # if self.rect.bottom > self.max_y:
        #     self.rect.bottom = self.max_y
        #     self.spdy = -abs(self.spdy)
        
        if self.rect.left < 0:
            self.rect.left = 0
            self.spdx = abs(self.spdx)
        if self.rect.right > self.max_x:
            self.rect.right = self.max_x
            self.spdx = -abs(self.spdx)
    
    def move(self):
        self.rect.x += self.spdx 
        self.rect.y += self.spdy
    
    def deload(self):
        if self.rect.top > self.max_y:
            self.kill()
    
    def update(self):
        self.checkBorder()
        self.deload()