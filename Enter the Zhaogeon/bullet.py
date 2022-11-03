from pygame import *
from settings import *
from math import cos, sin


class Bullet(sprite.Sprite):
    def __init__(self, person, speed, pos, angle):
        super().__init__()

        if person == "player": self.image = image.load("graphics/bullet-5x5.png").convert_alpha()
        if person == "enemy":  self.image = image.load("graphics/Ebullet-5x5.png").convert_alpha()
        self.image = transform.scale(self.image, (screenx * 5/256, screeny * 5/144))
        self.rect = self.image.get_rect(center = pos)
        
        self.speed = speed
        self.angle = angle
        self.move_direction = Vector2(0,0)

    def update(self, direction):
        if direction == "x": self.rect.x += round(self.speed*cos(self.angle))
        if direction == "y": self.rect.y += round(self.speed*sin(self.angle))
