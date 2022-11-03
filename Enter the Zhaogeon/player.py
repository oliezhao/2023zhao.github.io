from asyncio import constants
from pygame import *
from settings import *

from math import sqrt
from math import atan2

from bullet import *


#Objects of Player created in Map
class Player(sprite.Sprite):
    def __init__(self, position, speed, spawn_sprite):
        super().__init__()

        self.sprite = spawn_sprite

        self.image = image.load(self.sprite).convert_alpha()
        self.image = transform.scale(self.image, (screenx * 8/256, screeny * 12/144))
        self.rect = self.image.get_rect(topleft = position)

        self.health = [2,2,2,2]

        self.const_speed = speed
        self.speed = Vector2(0,0)
        
        self.face_direction = ""
        self.move_direction = Vector2(0,0)
        
        self.states = []
        #self.state = "" #change to array so player can have multiple states
        self.invinc = False

        self.cursor =  Cursor()

        self.roll_timer = 0
        self.roll_cooldown_timer = -1000
        self.shoot_cooldown_timer = -1000
    
        self.bullet_spritegroup = sprite.Group()
    
    # def damage(self):
    #     last_heart = self.health[self.health.__len__ - 1]
    #     last_heart - 1
    #     if last_heart <= 0:
    #         self.health.pop()


    def input_detect(self):
        time_ = time.get_ticks()
        keys = key.get_pressed()
        mouse_ = mouse.get_pressed()     

        if "rolling" not in self.states:#if player is not rolling
            if not(keys[K_a] or keys[K_d]) or keys[K_a] and keys[K_d]: #if player is pressing both x-axis buttons,
                self.move_direction.x = 0 #player does not move
            else:
                if keys[K_d]: self.move_direction.x = 1 #player is moving to the right (pos x axis)
                if keys[K_a]: self.move_direction.x = -1 #player is moving to the left (neg x axis)
            
            if (not(keys[K_w] or keys[K_s])) or (keys[K_w] and keys[K_s]): #if both y-axis buttons are pressed
                    self.move_direction.y = 0 # no movement in y axis
            else:
                if keys[K_w]: self.move_direction.y = -1 #player is moving up (neg y axis)
                if keys[K_s]: self.move_direction.y = 1 #player is moving down (pos y axis)
            
            if (keys[K_SPACE]) and self.move_direction != 0:
                self.roll_timer = time_
                self.invinc = True
                self.states.append("rolling")

            if mouse_[0] and time_ - self.shoot_cooldown_timer >= 300:
                self.shoot_cooldown_timer = time_
                self.bullet = Bullet("player", 10, self.rect.center, self.angle_calc(mouse.get_pos()))
                self.bullet_spritegroup.add(self.bullet)

        if "rolling" in self.states:
            if "nodmg" not in self.states:
                self.states.append("nodmg")
            
            if time_ - self.roll_timer >= 480:
                self.move_direction.x *= 0.9
                self.move_direction.y *= 0.9
                self.states.remove("nodmg")

            if time_ - self.roll_timer >= 800:
                self.roll_cooldown_timer = time_
                self.states.remove("rolling")


    def speed_calc(self):

        #if the player is moving diagonally, reduce speed of both axis by 30% to maintain constaint
        if self.move_direction.x and self.move_direction.y != 0:
            
            self.speed.x = int(self.move_direction.x * sqrt((self.const_speed**2)/2))
            self.speed.y = int(self.move_direction.y * sqrt((self.const_speed**2)/2))

        else:
            self.speed.x = self.const_speed * self.move_direction.x
            self.speed.y = self.const_speed * self.move_direction.y
    
    def angle_calc(self, cursor_pos):
        dx = cursor_pos[0] - self.rect.center[0]
        dy = cursor_pos[1] - self.rect.center[1]
        
        angle = atan2(dy, dx)
        return angle

    def face_direction_calc(self, cursor_pos):
        #takes in cursor_pos through Map from Main
        #calcualtes the angle between cursor and player to determine which way the player is facing
        #if player-cursor angle is less then 30 degrees i.e dy.dx > 1.7 or root(3)
        
        straight = False
        
        dx = cursor_pos[0] - self.rect.center[0]
        dy = cursor_pos[1] - self.rect.center[1]
        
        if dx != 0: self.angle = dy/dx
        else: self.angle = 0

        #if dy/dx is more than 1.7(32...) the angle between the mouse and the player is smaller than 30 degrees. Meaning the player should be looking straight
        #dx cannot be 0 as it will crash game
        if abs(self.angle) > 1.7: straight = True
        else: straight = False
        
        if straight == True:
            if dy >= 0: self.face_direction = "S" #player is facing south
            else: self.face_direction = "N" #player is facing north
        elif straight == False:
            if dy >= 0:
                if dx > 0: self.face_direction = "SE" #player is facing south east
                else: self.face_direction = "SW" #player is facing south west
            else:
                if dx > 0: self.face_direction = "NE" #player is facing north east
                else: self.face_direction = "NW"#player is facing north west
    
        #instead of directly changing the player sprite to an image. Change a new variable, self.face_direction and have animate() calculate which sprite to display

    def animate(self):
        
        if self.face_direction == "N": 
            self.sprite = "graphics/PN_nogun-8x12.png"
        if self.face_direction == "NW":
            self.sprite = "graphics/PNW_nogun-8x12.png"
        if self.face_direction == "NE":
            self.sprite = "graphics/PNE_nogun-8x12.png"
        if self.face_direction == "S": 
            self.sprite = "graphics/PS_nogun-8x12.png"
        if self.face_direction == "SE":
            self.sprite = "graphics/PSE_nogun-8x12.png"
        if self.face_direction == "SW":
            self.sprite = "graphics/PSW_nogun-8x12.png"
        
        if self.move_direction.x > 0:
            if self.move_direction.y == 0: rotation = -90
            if self.move_direction.y > 0: rotation = -135
            if self.move_direction.y < 0: rotation =-45
        elif self.move_direction.x < 0:
            if self.move_direction.y == 0: rotation = 90
            if self.move_direction.y > 0: rotation = 135
            if self.move_direction.y < 0: rotation = 45
        else:
            if self.move_direction.y > 0: rotation = 180
            if self.move_direction.y < 0: rotation = 0

        self.image = image.load(self.sprite).convert_alpha()
        self.image = transform.scale(self.image, (screenx * 8/256, screeny * 12/144))
        
        if "rolling" in self.states:
            self.image = transform.rotate(self.image, rotation)

        self.rect = self.image.get_rect(center = self.rect.center)

        
    def update(self, cursor_pos):
        #cursor pos should be same as get.mouse_pos()

        self.input_detect()
        self.face_direction_calc(cursor_pos)
        self.speed_calc()

        self.animate()
        
        
            