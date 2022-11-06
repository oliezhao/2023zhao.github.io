from pygame import *

from setting import *
from common import *

class Player(sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.hitbox = Surface((8 * scale, 12 * scale))
        self.rect = self.hitbox.get_rect(topleft = pos)

        self.clock = 0
        #---timers
        self.timer = 0
        self.roll_timer = -100
        
        self.row = 1
        self.column = 1
    
        self.speed_constant = 5
    
        self.speed = self.speed_constant
        self.move_direction = Vector2(0,0)#---the vector direction of the character. 0 = not movement. 1 or -1 means moving.
        self.velocity = Vector2(0,0)#--- adds to player.rect to move player
        
        self.debugmsg = ""
        
        self.health = 6
        self.states = []
        
    def input(self):
        keys = key.get_pressed()
        buttons = mouse.get_pressed()
        
        #---movement---
        if "rolling" not in self.states:
            if not(keys[K_a] or keys[K_d]) or keys[K_a] and keys[K_d]: #if player is pressing both x-axis buttons,
                self.move_direction.x = 0 #player does not move
            else:
                if keys[K_d]: self.move_direction.x = 1 #player is moving to the right (pos x axis)
                if keys[K_a]: self.move_direction.x = -1 #player is moving to the left (neg x axis)
            
            if (not(keys[K_w] or keys[K_s])) or (keys[K_w] and keys[K_s]): #if both y-axis buttons are pressed
                    self.move_direction.y = 0 # no movement in y axis
            else:
                if keys[K_w]: self.move_direction.y = 1 #player is moving up (neg y axis)
                if keys[K_s]: self.move_direction.y = -1 #player is moving down (pos y axis)

        #---roll--
        if "rolling" not in self.states:
            if self.move_direction.xy != (0,0) and keys[K_SPACE]:
                self.apply_status("rolling")
            
    def velo_calc(self): #assigns values to self.velocity
        if abs(self.move_direction.x) == 1 and abs(self.move_direction.y) == 1:
            self.move_direction.x *= 0.7
            self.move_direction.y *= 0.7

        self.velocity.x = self.move_direction.x * self.speed
        self.velocity.y = self.move_direction.y * self.speed       
    
    def apply_status(self, status):
        if status == "rolling":
            
            self.roll_timer = self.clock
            
            self.states.append("rolling")
            self.states.append("nodmg")

            self.speed *= 0.5
    
    def timer_check(self):
        if "rolling" in self.states:
            if self.clock - self.roll_timer == 12:
                self.speed = self.speed_constant
            if self.clock - self.roll_timer == 30:
                self.speed = self.speed_constant * 0.5
                self.states.remove("nodmg")
            if self.clock - self.roll_timer == 48:
                self.states.remove("rolling")
                self.speed = self.speed_constant

    def animate(self):
        
        pca = get_angle(self.rect, mouse.get_pos())
        
        if "rolling" not in self.states:
            self.row = 1
            
            if pca >= 120 and pca < 180: self.column = 1
            if pca >= 60 and pca < 120: self.column = 2
            if pca >= 0 and pca < 60: self.column = 3
            if pca < -120 and pca >= -180: self.column = 4
            if pca < -60 and pca >= -120: self.column = 5
            if pca < 0 and pca >= -60: self.column = 6
        
        if "rolling" in self.states:
            
            if self.move_direction.y > 0:
                if self.move_direction.x < 0: self.column = 1
                if self.move_direction.x == 0: self.column = 2
                if self.move_direction.x > 0: self.column = 3
            if self.move_direction.y < 0:
                if self.move_direction.x < 0: self.column = 4
                if self.move_direction.x == 0: self.column = 5
                if self.move_direction.x > 0: self.column = 6
            
            if self.clock - self.roll_timer < 4: self.row = 2
            elif self.clock - self.roll_timer < 8: self.row = 3
            elif self.clock - self.roll_timer < 12: self.row = 4
            elif self.clock - self.roll_timer < 30: 
                if self.move_direction.y == 0:
                    if self.move_direction.x > 0: self.column = 8
                    if self.move_direction.x < 0: self.column = 7 
                self.row = 5
            else:
                self.row = 6
                self.column = 1
        
    def load_image(self, row, column):
        self.image = spritesheet_loader("graphics/spritesheets/PlayerSS.png", row, column, 1)
        self.image_rect = self.image.get_rect(topleft = self.rect.topleft)
        
    def print(self, string):
        print(string)
    
    def move(self, direction):
        if direction == "x": self.rect.x += self.velocity.x
        if direction == "y": self.rect.y -= self.velocity.y
    
    def update(self):
        self.clock += 1
        
        self.debugmsg = str(self.velocity) + str(self.states)
                
        self.input()
        self.velo_calc()
        self.timer_check()
        
        self.move("x")
        self.move("y")
        self.animate()
        self.load_image(self.row, self. column)
        
        