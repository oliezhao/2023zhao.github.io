from pygame import *
from settings import *
from math import atan2, sin, cos
import random


from bullet import *

class Enemy(sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        
        self.image = image.load("graphics/ER-8x12.png").convert_alpha()
        self.image = transform.scale(self.image, (8 * (screenx/256), 12 * (screeny/144)))
        self.rect = self.image.get_rect(topleft = pos)
        
        self.shoot_cooldown = -300
        self.bullet_spritegroup = sprite.Group()

        self.time = 0

    def angle_calc(self, player_pos):
        dx = player_pos[0] - self.rect.x
        dy = player_pos[1] - self.rect.y
    
        angle = atan2(dy, dx)

        if dx > 0: self.image = self.image = image.load("graphics/ER-8x12.png").convert_alpha()

        return angle
    
    def animate(self, player_pos):
        if abs(self.angle_calc(player_pos)) < 1.6:
            self.image = image.load("graphics/ER-8x12.png").convert_alpha()
        if abs(self.angle_calc(player_pos)) > 1.6:
            self.image = image.load("graphics/EL-8x12.png").convert_alpha()

        self.image = transform.scale(self.image, (8 * (screenx/256), 12 * (screeny/144)))
        self.rect = self.image.get_rect(center = self.rect.center)

    def shoot(self, player_pos):
        if self.time - self.shoot_cooldown >= 500:
            self.shoot_cooldown = self.time
            self.bullet = Bullet("enemy", 5, self.rect.center, self.angle_calc(player_pos))
            self.bullet_spritegroup.add(self.bullet)

    def update(self, player_pos):
        print("update")
        self.time = time.get_ticks()
        self.animate(player_pos)
        self.shoot(player_pos)