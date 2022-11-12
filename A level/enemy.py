from pygame import *

from common import *
from bullet import *

class Enemy(sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = image.load("graphics/EL-8x12.png").convert_alpha()
        self.image = transform.scale(self.image, (8 * scale, 12 * scale))
        self.rect = self.image.get_rect(topleft = pos)

        self.clock = time.get_ticks()

        self.shoot_timer = -50

        self.bullets = sprite.Group()

    def look(self, player_rect_center):
        if player_rect_center > self.rect.center:
            self.image = image.load("graphics/ER-8x12.png").convert_alpha()
        if player_rect_center < self.rect.center:
            self.image = image.load("graphics/EL-8x12.png").convert_alpha()

        self.rect = self.image.get_rect(self.image, (8* scale, 12 * scale))

    def shoot(self, player_rect_center):
        self.shoot_timer = self.clock
        self.bullet = Bullet(self.rect.center)
        self.bullet.move(2, get_angle(self.rect.center, player_rect_center))
        self.bullets.add(self.bullet)
    
    def update(self, player_rect_center):
        self.look(player_rect_center)#
        if self.clock - self.shoot_timer > 50:
            self.shoot(player_rect_center)
        