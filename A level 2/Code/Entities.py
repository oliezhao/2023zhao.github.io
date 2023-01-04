from pygame import *
import json
from math import atan2, degrees

from Settings import *
from SpriteSheet import *

from Gun import *

class Entities(sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.id = ""  
        self.facedirection = ""
        self.state = "idle"
        self.frame = 1
        
        self.clock = 0
        
        self.health = 0
        self.statuses = []
        self.cont_speed = 0
        self.direction = Vector2(0,0)
        
        self.guns = sprite.Group()
        self.gun = sprite.GroupSingle()

    def hurt(self, damage):
        self.health -= damage
    
    def shoot(self, target):
        self.gun.sprite.shoot()
    
    def load_image(self):
        self.image_name = self.id + self.facedirection + "/" + self.state + "_" + str(self.frame) 
        self.image = self.spritesheet.parse_sprite(self.image_name)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect(center = self.hitbox.center)
    
    def move(self, direction: str):
        pass
    
class Player(Entities):
    def __init__(self, x ,y):
        super().__init__()
        
        self.id = "P"
        
        self.spritesheet = SpriteSheet("player_spritesheet.png")        
        
        self.hitbox = Surface( (round(8 * scale), round(12 * scale)) )
        self.hitbox = self.hitbox.get_rect(center = (x, y))
        
        self.rolling = False
        self.roll_timer = -999
        
        self.move_direction = Vector2(0,0)
        self.speed = 1 * scale
        
    def inputs(self):
        keys = key.get_pressed()
        
        if not(self.rolling):
            if (keys[K_w] and keys[K_s]) or not(keys[K_w] or keys[K_s]):
                self.move_direction.y = 0
            else:
                if keys[K_w]: self.move_direction.y = 1
                if keys[K_s]: self.move_direction.y = -1
        
            if (keys[K_a] and keys[K_d]) or not(keys[K_a] or keys[K_d]):
                self.move_direction.x = 0
            else:
                if keys[K_a]: self.move_direction.x = -1
                if keys[K_d]: self.move_direction.x = 1
        
            if keys[K_SPACE] and self.move_direction != (0,0):
                
                self.roll_timer = self.clock
                
                if self.move_direction.y == 0:
                    if self.move_direction.x == 1: self.facedirection = "E"
                    if self.move_direction.x == -1: self.facedirection = "W"
                if self.move_direction.y == 1:
                    if self.move_direction.x == 0: self.facedirection = "N"
                    if self.move_direction.x == 1: self.facedirection = "NE"
                    if self.move_direction.x == -1: self.facedirection = "NW"
                if self.move_direction.y == -1:
                    if self.move_direction.x == 0: self.facedirection = "S"
                    if self.move_direction.x == 1: self.facedirection = "SE"
                    if self.move_direction.x == -1: self.facedirection = "SW"
                
                self.rolling = True
        
    def animate(self):
        mouse_pos = mouse.get_pos()
        
        pca = get_angle(self.hitbox.center, mouse_pos)
        
        if not(self.rolling):
            if pca > 0 and pca < 60: self.facedirection = "NE"
            if pca > 60 and pca < 120: self.facedirection = "N"
            if pca > 120 and pca < 180: self.facedirection = "NW"
            if pca < 0 and pca > -60: self.facedirection = "SE"
            if pca < -60 and pca > -120: self.facedirection = "S"
            if pca < -120 and pca > -180: self.facedirection = "SW"

        if self.rolling:
            self.state = "roll"
            
            if self.clock - self.roll_timer < 4: self.frame = 1
            elif self.clock - self.roll_timer < 8: self.frame = 2
            elif self.clock - self.roll_timer < 12: self.frame = 3
            elif self.clock - self.roll_timer < 30: self.frame = 4
            else:
                self.rolling = False
                self.state = "idle"
                self.frame = 1
    
    def move(self):
        self.hitbox.y -= round(self.speed * self.move_direction.y)
        self.hitbox.x += round(self.speed * self.move_direction.x)
        
    def update(self):
        self.inputs()
        self.move()
        self.animate()
        self.load_image()
        
        self.clock += 1
