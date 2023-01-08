from pygame import *
from math import sin, cos

from SpriteSheet import *

class Bullet(sprite.Sprite):
    def __init__(self, id, speed, angle, lifetime, damage):
        super().__init__()
        
        self.clock = 0
        self.lifetime = lifetime
        self.speed = speed
        self.angle = angle
        
        self.spritesheet = SpriteSheet("bullet_spritesheet.png")
        self.image = self.spritesheet.parse_sprite(id)
        
        self.damage = damage
        
    def spawn(self, x, y):
        self.rect = self.image.get_rect(center = (x, y))
    
    def move(self, direction):
        if direction == "x": self.rect.x += round(self.speed * cos(self.angle))
        if direction == "y": self.rect.y -= round(self.speed * sin(self.angle))
        
    def update(self):
        self.clock += 1
        
        self.move("x")
        self.move("y")
        
        if self.clock >= self.lifetime:
            self.kill()