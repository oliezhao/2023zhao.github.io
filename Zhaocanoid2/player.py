import pygame
from pygame import *
from laser import Laser

class Player(sprite.Sprite):
    def __init__(self, screenx, screeny):
        super().__init__()
        
        self.screenx = screenx
        self.screeny = screeny
        
        self.x = screenx/5
        self.y = screeny/100
        
        self.image = Surface((self.x, self.y))
        self.image.fill('White')
        self.rect = self.image.get_rect(midtop = (screenx/2, screeny * 9/10))
        
        self.health = 0
        self.spdlmt = 15
        self.velocity = 0
        
        self.laser_time = 0
        self.laser_cooldown = 200
        self.laser_ready = True
        self.laser_sound = mixer.Sound('sounds/laser7.wav')
        
        self.laser_spritelist = sprite.Group()
        
    def input(self):
        keys = key.get_pressed()
        
        if keys[K_d] and self.rect.right < self.screenx:
            self.velocity += 1
        if keys[K_a] and self.rect.left > 0:
            self.velocity -= 1
        if not(keys[K_d]) and self.velocity > 0:
            self.velocity -= 1
        if not(keys[K_a]) and self.velocity < 0:
            self.velocity += 1
        
        if keys[K_SPACE] and self.laser_ready:
            self.shoot_laser()
            self.laser_time = time.get_ticks()
            self.laser_ready = False
            
    
    def move(self):
        
        if self.velocity > self.spdlmt:
            self.velocity = self.spdlmt
        if self.velocity < -self.spdlmt:
            self.velocity = - self.spdlmt
        
        self.rect.x += self.velocity
        
        if self.rect.left < 0:
            self.rect.left = 0
            self.velocity *= -1
        if self.rect.right > self.screenx:
            self.rect.right = self.screenx
            self.velocity *= -1

    def laser_recharge(self):
        if not self.laser_ready:
            current_time = time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.laser_ready = True
    
    def shoot_laser(self):
        self.laser_sound.play()
        self.laser_spritelist.add(Laser(self.x, self.y, self.rect.midtop))
    
    def update(self):
        self.input()
        self.laser_recharge()
        self.laser_spritelist.update()
        self.move()