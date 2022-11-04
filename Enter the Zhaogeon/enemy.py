from pygame import *
from settings import *
from math import atan2, sin, cos

from bullet import *

class Enemy(sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        
        self.image = image.load("graphics/ER-8x12.png").convert_alpha()
        self.image = transform.scale(self.image, (8 * (screenx/256), 12 * (screeny/144)))
        self.rect = self.image.get_rect(topleft = pos)
        
        self.shoot_cooldown = -300
        self.bullet_spritegroup = sprite.Group()

    def angle_calc(self, player_pos):
        dx = player_pos[0] - self.rect.x
        dy = player_pos[1] - self.rect.y

        angle = atan2(dy, dx)
        return angle
    
    def shoot(self, player_pos):
        time_ = time.get_ticks()
        if time_ - self.shoot_cooldown >= 300:
            self.shoot_cooldown = time_
            self.bullet = Bullet("enemy", 5, self.rect.center, self.angle_calc(player_pos))
            self.bullet_spritegroup.add(self.bullet)