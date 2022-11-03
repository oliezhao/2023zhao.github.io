from asyncio import constants
from pygame import *
from settings import *
from math import sqrt

#Objects of Player created in Map
class Player(sprite.Sprite):
    def __init__(self, position, speed, spawn_sprite):
        super().__init__()

        self.sprite = spawn_sprite

        self.image = image.load(self.sprite).convert_alpha()
        self.image = transform.scale(self.image, (screenx * 8/256, screeny * 12/144))
        self.rect = self.image.get_rect(topleft = position)

        self.health = 6

        self.const_speed = speed
        self.speed = Vector2(0,0) #i increment the player position by these values
        
        self.face_direction = "" #string value to calculates what direction the player is facing
        self.move_direction = Vector2(0,0) #indicates the direction and ratio of movement speed relative to constatn speed
        
        self.states = [] #array that stores 
        self.invinc = False

        self.cursor =  Cursor()

        self.clock = 0
        self.roll_timer = 0
        self.roll_cooldown_timer = -1000

    def input_detect(self):
        keys = key.get_pressed()
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
            
            if keys[K_SPACE] and self.move_direction != (0,0) and self.clock - self.roll_cooldown_timer >= 200:
                self.roll_cooldown_timer = self.clock
                self.states.append("rolling")
                self.states.append("nodmg")
                self.roll_timer = self.clock
                self.invinc = True
                self.states.append("rolling")
    
        if "rolling" in self.states:#if player is rolling
            print(self.clock - self.roll_cooldown_timer)
            if "nodmg" not in self.states:#give nodmg status ONCE
                self.states.append("nodmg")
            
            if self.clock - self.roll_timer >= 240: #applies slower speed for last 5 frames or 0.08 seconds of roll
                self.move_direction.x *= 0.5
                self.move_direction.y *= 0.5

            if self.clock - self.roll_timer >= 320:#rolling lasts for 20 frames or 0.32 seconds
                self.roll_cooldown_timer = self.clock#starts roll cooldown timer to ensure no rool spaming
                self.states.remove("rolling") #remove rooling status
                self.states.remove("nodmg") #remove no damage status

    def apply_states(self, effect):
        if effect == "rolling": #if appling rolling status
            
            

                
                

    def speed_calc(self):

        #if the player is moving diagonally, reduce speed of both axis by 30% to maintain constaint
        if self.move_direction.x and self.move_direction.y != 0:
            
            self.speed.x = int( self.move_direction.x * sqrt((self.const_speed**2)/2) )
            self.speed.y = int( self.move_direction.y * sqrt((self.const_speed**2)/2) )

        else:

            self.speed.x = self.const_speed * self.move_direction.x
            self.speed.y = self.const_speed * self.move_direction.y



    def face_direction_calc(self, cursor_pos):
        #takes in cursor_pos through Map from Main
        #calcualtes the angle between cursor and player to determine which way the player is facing
        #if player-cursor angle is less then 30 degrees i.e dy.dx > 1.7 or root(3)
        
        straight = False
        
        dx = cursor_pos[0] - self.rect.center[0]
        dy = cursor_pos[1] - self.rect.center[1]
        
        #if dy/dx is more than 1.7(32...) the angle between the mouse and the player is smaller than 30 degrees. Meaning the player should be looking straight
        #dx cannot be 0 as it will crash game
        if dx != 0 and abs(dy/dx) > 1.7: straight = True
        else: straight = False
        
        if straight == True:
            if dy >= 0: self.face_direction = "S" #player is facing south
            else: self.face_direction = "N" #player is facing north
        else:
            if dy >= 0:
                if dx > 0: self.face_direction = "SE" #player is facing south east
                else: self.face_direction = "SW" #player is facing south west
            else:
                if dx > 0: self.face_direction = "NE" #player is facing north east
                else: self.face_direction = "NW"#player is facing north west
    
        #instead of directly changing the player sprite to an image. Change a new variable, self.face_direction and have animate() calculate which sprite to display

    def animate(self):
        if "rolling" not in self.states:
            if self.face_direction == "N": self.sprite = "graphics/PN_nogun-8x12.png"
            if self.face_direction == "NW":self.sprite = "graphics/PNW_nogun-8x12.png"
            if self.face_direction == "NE":self.sprite = "graphics/PNE_nogun-8x12.png"
            if self.face_direction == "S": self.sprite = "graphics/PS_nogun-8x12.png"
            if self.face_direction == "SE":self.sprite = "graphics/PSE_nogun-8x12.png"
            if self.face_direction == "SW":self.sprite = "graphics/PSW_nogun-8x12.png"

            self.image = image.load(self.sprite).convert_alpha()
            self.image = transform.scale(self.image, (screenx * 8/256, screeny * 12/144))
        
        if "rolling" in self.states:
            self.image.fill("White")

        
    def update(self, cursor_pos):
        #cursor pos should be same as get.mouse_pos()
        self.clock = time.get_ticks()



        self.input_detect()
        
        
        self.face_direction_calc(cursor_pos)
        self.speed_calc()
        
        for state in self.states:
             self.apply_states(state)

        self.animate()
        
        
            