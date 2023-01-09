from pygame import *
import json
from math import sin, cos, degrees
import random

from Settings import *
from SpriteSheet import *

class Entities(sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.hitbox = Surface( (round(1 * scale), round(1 * scale)) )
        
        self.debug_msg = ""
        
        self.id = ""  
        self.facedirection = ""
        self.angle = 0
        self.state = "idle"
        self.frame = 1
        
        self.clock = 0
        
        self.health = 0
        self.statuses = []
        self.cont_speed = 0
        self.move_angle = 0
        self.move_direction = Vector2(0, 0)
        
        self.guns = sprite.Group()
        self.gun = sprite.GroupSingle()

    def move_direction_calc(self):

        self.move_direction.x = cos(self.move_angle)
        self.move_direction.y = sin(self.move_angle)
            
    def hurt(self, damage):
        self.health -= damage
    
    def shoot(self):
        self.gun.sprite.shoot(self.id, self.angle, self.hitbox.center)
    
    def pickup_gun(self, gun):
        if gun not in self.guns:
            gun.pickedup = True 
            self.guns.add(gun)
            self.gun.add(gun)
    
    def drop_weapon(self):
        gun = self.gun.sprite
        gun.pickedup = False
        self.gun.empty()
        self.guns.remove(gun)
        
        return(gun)
        
    def equip_gun(self, num):
        last_gun = len(self.guns) - 1
        if num <= last_gun:
            self.gun.sprite = self.guns.sprites()[num]
    
    def hold_gun(self):
        gun = self.gun.sprite
        
        if self.facedirection == "W": 
            gun.rect.midright = self.hitbox.center
        if self.facedirection == "E": 
            gun.rect.midleft = self.hitbox.center
            
    def draw_gun(self):
        if self.gun and "rolling" not in self.statuses:
            screen = display.get_surface()
            screen.blit(self.gun.sprite.image, self.gun.sprite.rect)

    def load_image(self):
        
        gun = ""
        if self.gun and "rolling" not in self.statuses: gun = "g_"
        self.image_name = self.id + self.facedirection + "/" + gun + self.state + "_" + str(self.frame) 
        self.image = self.spritesheet.parse_sprite(self.image_name)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect(center = self.hitbox.center)

        if self.gun: self.hold_gun()
        
    def move(self, direction: str):
        if direction == "x": self.hitbox.x += round(self.speed * self.move_direction.x)
        if direction == "y": self.hitbox.y -= round(self.speed * self.move_direction.y)
    
    def animate(self):
        
        angle = round(degrees(self.angle))
        if -90 < angle < 90: 
            self.facedirection = "E"
        else: self.facedirection = "W"

        if self.gun:
            if self.gun.sprite.angle != angle:
                self.gun.sprite.rotate(angle)
        
    def draw(self):
        screen = display.get_surface()
        screen.blit(self.image, self.rect)
    
class Player(Entities):
    def __init__(self, x ,y):
        super().__init__()
        
        self.id = "P"
        
        self.facedirection = "N"
        
        self.spritesheet = SpriteSheet("player_spritesheet.png")        
        
        self.hitbox = Surface( (round(8 * scale), round(12 * scale)) )
        self.hitbox = self.hitbox.get_rect(center = (x, y))

        self.health = 6
        
        self.speed_cont = 1 * scale
        self.speed = self.speed_cont

    def move_direction_calc(self):
        x = self.move_direction.x
        y = self.move_direction.y
        
        if x != 0 and y != 0:
            if x > 0: self.move_direction.x = 0.7
            else: self.move_direction.x = -0.7
            if y > 0: self.move_direction.y = 0.7
            else: self.move_direction.y = -0.7

    def inputs(self):
        keys = key.get_pressed()
        buttons = mouse.get_pressed()
        
        if "rolling" not in self.statuses:
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
                
                self.statuses.append("rolling")

            if self.gun and buttons[0]:
                for gun in self.gun:
                    if gun.type == "Auto":
                        self.shoot()
            
            #Hotbar
            if keys[K_1]: self.equip_gun(0)
            if keys[K_2]: self.equip_gun(1)
            if keys[K_3]: self.equip_gun(2)
            if keys[K_4]: self.equip_gun(3)
            if keys[K_5]: self.equip_gun(4)
            if keys[K_6]: self.equip_gun(5)
            if keys[K_7]: self.equip_gun(6)
            if keys[K_8]: self.equip_gun(7)
            if keys[K_9]: self.equip_gun(8)
            if keys[K_0]: self.equip_gun(9)
    
    def hold_gun(self): #moves gun "attachment point" based on player face direction. ran at end of self.load_image()
        gun = self.gun.sprite
        
        gun.rect.midleft = self.hitbox.center
        
        if self.facedirection == "N": gun.rect.bottom = self.hitbox.centery #if looking up
        elif self.facedirection == "S": gun.rect.top = self.hitbox.centery #if looking down
        else: gun.rect.centery = self.hitbox.centery #if looking straight
        
        if "W" in self.facedirection: 
            gun.rect.right = self.hitbox.centerx #if looking left    
            if "N" not in self.facedirection: gun.rect.right = self.hitbox.centerx - (3 * scale) #werird conditions... makes rotating gun look better imo
            else: gun.rect.bottom = self.hitbox.centery + (2 * scale)
        if "E" in self.facedirection: gun.rect.left = self.hitbox.centerx #if looking right      
        
    def apply_status(self):
        
        if "rolling" in self.statuses:
            
            if self.clock - self.roll_timer < 4: 
                self.speed = self.speed_cont * 0.5
            elif self.clock - self.roll_timer < 32: 
                self.speed = self.speed_cont * 1.5
            elif self.clock - self.roll_timer <44: 
                self.speed = self.speed_cont * 0.5
            else:
                self.speed = self.speed_cont
                
            if self.frame > 0:
                if "nodmg" not in self.statuses: self.statuses.append("nodmg")
            if self.frame > 4:
                if "nodmg" in self.statuses: self.statuses.remove("nodmg")
        
    def animate(self):
        
        angle = round(degrees(self.angle))
        
        if "rolling" not in self.statuses:
            if angle > 0 and angle < 60: self.facedirection = "NE"
            if angle > 60 and angle < 120: self.facedirection = "N"
            if angle > 120 and angle < 180: self.facedirection = "NW"
            if angle < 0 and angle > -60: self.facedirection = "SE"
            if angle < -60 and angle > -120: self.facedirection = "S"
            if angle < -120 and angle > -180: self.facedirection = "SW"

        if "rolling" in self.statuses:
            self.state = "roll"
            
            if self.clock - self.roll_timer < 4: self.frame = 1 #Windup frams
            elif self.clock - self.roll_timer < 8: self.frame = 2
            elif self.clock - self.roll_timer < 12: self.frame = 3
            elif self.clock - self.roll_timer < 36: self.frame = 4 #Fly frames
            elif self.clock - self.roll_timer <48: self.frame = 5 #Recovery frames
            else:
                self.statuses.remove("rolling")
                self.state = "idle"
                self.frame = 1
        
        if self.gun:
            if self.gun.sprite.angle != angle:
                self.gun.sprite.rotate(angle)

    def move(self, direction):
        if direction == "x": self.hitbox.x += round(self.speed * self.move_direction.x)
        if direction == "y": self.hitbox.y -= round(self.speed * self.move_direction.y)
    
    def update(self): 
        
        mouse_pos = mouse.get_pos()
        self.angle = get_angle(self.hitbox.center, mouse_pos)
        
        self.inputs()
        self.move_direction_calc()
        self.apply_status()
        
        self.animate()
        self.load_image()
        
        self.debug_msg = str(self.speed) + ", " + str(self.move_direction)
        if self.gun: 
            if self.gun.sprite.bullets: 
                self.debug_msg += ", gunbullets" + str(self.gun.sprite.bullets)
        #self.debug_msg += str(self.gun) + ", " + str(self.guns) 
        
        self.clock += 1
        
class Enemy(Entities):
    def __init__(self, x, y, weapon):
        super().__init__()
        
        self.id = "E"
        
        self.facedirection = "W"
    
        self.spritesheet = SpriteSheet("enemy_spritesheet.png")
        
        self.hitbox = Surface((round(8 * scale), round(12 * scale)))
        self.hitbox = self.hitbox.get_rect(center = (x, y))
        
        self.health = 2

        self.gun.add(weapon)
        
        self.cont_speed = 0.75 * scale
        self.speed = self.cont_speed

        self.timer_1 = 0 #rename later... used to decide move anticlockwise or clockwise to the player
        self.rand_val_1 = 1 #random value used to decide move anticlockwise or clockwise to the player between 1,2
    
    def run_timers(self):
        if self.clock - self.timer_1 >= 50:
            self.timer_1 = self.clock
            self.rand_val_1 = random.randint(1,2)
            
    def shoot(self):
        if self.gun.sprite.clip > 0:
            self.gun.sprite.shoot(self.id, self.angle, self.hitbox.center)
        elif self.gun.sprite.reloading == False:
            self.gun.sprite.reloading = True
            self.gun.sprite.reload_timer = self.gun.sprite.clock
    
    def decide(self, target): #enemy AI decisions
        distance = get_distance(self.hitbox.center, target)
        
        if distance < 60:
            self.move_angle = self.angle - 3.14
            self.speed = self.cont_speed * 0.5
            if distance < 40:
                self.speed = 0.75 * self.cont_speed
                self.facedirection = self.move_angle
        
        elif distance > 80:
            self.move_angle = self.angle
            self.speed = self.cont_speed
        
        else:
            if self.rand_val_1 == 1: self.move_angle = self.angle + 1.57    
            if self.rand_val_1 == 2: self.move_angle = self.angle - 1.57

        self.move_direction_calc()
        
        self.move("x")
        self.move("y")
        
        if 40 < distance < 80:
            self.shoot()
    
    def update(self, target):
        self.angle = get_angle(self.hitbox.center, target)

        self.run_timers()
        
        self.decide(target)
        
        self.animate()
        self.load_image()
        
        self.clock += 1
        
        self.debug_msg = str(get_distance(self.hitbox.center, target))