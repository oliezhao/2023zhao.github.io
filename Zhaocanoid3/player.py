import pygame
from pygame import *
import laser

class Player(sprite.Sprite):
    def __init__(self, windowsize, color, spdlmt):
        super().__init__()
        
        #-- player image
        self.image = Surface((windowsize[0]/5, windowsize[1]/100))
        self.rect = self.image.get_rect(midtop = (windowsize[0]/2, windowsize[1] * (9/10)))
        self.image.fill(color)
    
        #-- parameters
        self.velocity = 0
        self.max_x = windowsize[0]
        self.spdlmt = spdlmt
        
        #-- laser
        self.laser_spritegroup = sprite.Group()
        self.laser_ready = False
        self.laser_time = 0
        self.laser_cooldown = 600
        
    def newAttributes(self):
        self.width = self.rect.right - self.rect.left
    
    def input(self):
        keys = key.get_pressed()
        
        #'' accelrates when press (d OR a) and not touching window. adds friction when directional keys are not pressed
        if keys[K_d] and self.rect.right < self.max_x:
            self.velocity += 1
        if not(keys[K_d]) and self.velocity > 0:
            self.velocity -= 1
        if keys[K_a] and self.rect.left > 0:
            self.velocity -= 1
        if not(keys[K_a]) and self.velocity < 0:
            self.velocity += 1
        self.move()
        
    def move(self):
        
        #'' bounce mechanics and border control
        if self.rect.left < 0:
            self.rect.left = 0
            self.velocity = abs(self.velocity) - 1
        if self.rect.right > self.max_x:
            self.rect.right = self.max_x
            self.velocity = -(abs(self.velocity) - 1)
            
        #'' checks self.velocity is within range
        if self.velocity > self.spdlmt:
            self.velocity = self.spdlmt
        if self.velocity < -self.spdlmt:
            self.velocity = -self.spdlmt
        
        self.rect.x += self.velocity
    
    def shootLaser(self):
        current_time = time.get_ticks()
        if self.laser_ready:
            self.laser_ready = False
            self.laser_time = time.get_ticks()
            self.newLaser()
            print("shoot laser")
        elif current_time - self.laser_time >= self.laser_cooldown:
            self.laser_ready = True
    
    def newLaser(self):
        self.laser = laser.Laser('Red', self.width, self.rect.midtop, 10)
        self.laser_spritegroup.add(self.laser)
        
    def update(self):
        self.newAttributes()
        self.input()
        self.shootLaser()
        if self.laser_spritegroup:
            for self.laser in self.laser_spritegroup:
                self.laser.update()
    