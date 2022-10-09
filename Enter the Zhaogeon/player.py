from pygame import *
from settings import *

class Player(sprite.Sprite):
    def __init__(self, position, speed, spawn_sprite):
        super().__init__()

        self.image = image.load(spawn_sprite).convert_alpha()
        self.image = transform.scale(self.image, (screenx * 8/256, screeny * 12/144))
        self.rect = self.image.get_rect(topleft = position)
        self.speed = speed
        self.direction = math.Vector2(0,0)
        
        self.cursor =  Cursor()

    def move(self):
        keys = key.get_pressed()
        #checks if keys are being pressed
        if keys:
            #if both, or none of the "x-axis keys" are being pressed the player does not move
            if (not(keys[K_a] or keys[K_d])) or (keys[K_a] and keys[K_d]): self.direction.x = 0
            else:
                if keys[K_d]: self.direction.x = 1
                if keys[K_a]: self.direction.x = -1
            
            #same logic applied to the y axis
            if (not(keys[K_w] or keys[K_s])) or (keys[K_w] and keys[K_s]): self.direction.y = 0
            else:
                if keys[K_w]: self.direction.y = 1
                if keys[K_s]: self.direction.y = -1
                
            #if the player is moving diagonally, reduce speed of both axis by 30% to maintain constaint
            if self.direction.x and self.direction.y != 0:
                self.direction.x *= 0.7
                self.direction.y *= 0.7
            
            self.rect.x += self.speed * self.direction.x
            self.rect.y -= self.speed * self.direction.y
            
        else:
            self.direction = (0,0)

    def animate(self, sprite):
        self.image = image.load(sprite).convert_alpha()
        self.image = transform.scale(self.image, (screenx * 8/256, screeny * 12/144))
        
    def update(self, sprite):
        self.animate(sprite)
        self.move()
        
            