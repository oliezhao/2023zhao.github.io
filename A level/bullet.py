from pygame import *

from common import *
from math import cos, sin, radians

class Bullet(sprite.Sprite):
    def __init__(self, group, pos):
        super().__init__()

        self.group = group

        self.image = image.load("graphics/bullet-5x5.png")
        
        if group == "enemy":
            self.image = image.load("graphics/Ebullet-5x5.png")
        
        self.image = transform.scale(self.image, (5 * scale, 5* scale))

        self.rect = self.image.get_rect(center = pos)

        self.angle = 0
        self.speed = 0
        self.velocity = Vector2(0,0)
        
    def stop(self):
        self.speed = 0

    def set_trajectory(self, speed, angle):
        self.angle = radians(angle)
        self.speed = speed * scale
    
    def velo_calc(self):
        self.velocity.x = round(self.speed * cos(self.angle))
        self.velocity.y = round(self.speed * sin(self.angle))
        
    def move(self, direction):
        if direction == "x": self.rect.x += self.velocity.x
        if direction == "y": self.rect.y -= self.velocity.y
        
    def update(self):
        self.velo_calc()