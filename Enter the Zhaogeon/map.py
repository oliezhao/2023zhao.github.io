import pygame
from pygame import *

from settings import *

from player import *
from cursor import *

class Map():
    def __init__(self):
        super().__init__()
        
        #debug
        self.debug = ""
        
        #spawning sprite of player
        self.player_sprite = "graphics/PS_nogun-8x12.png"
        
        #declaring player
        self.player = Player([0,0], 10, self.player_sprite)
        self.player_spritegroup = sprite.GroupSingle(self.player)
        
    def pc_direction(self, cursor_pos): 
        straight = False
        
        dx = cursor_pos[0] - self.player.rect.center[0]
        dy = cursor_pos[1] - self.player.rect.center[1]
        
        if dx != 0: self.debug = str(dy/dx)
        
        
        #if dy/dx is more than 1.7(32...) the angle between the mouse and the player is smaller than 30 degrees. Meaning the player should be looking straight
        if dx != 0 and abs(dy/dx) > 1.7: straight = True
        else: straight = False
        
        if straight == True:
            if dy >= 0: self.player_sprite = "graphics/PS_nogun-8x12.png" #player is facing south
            else: self.player_sprite = "graphics/PN_nogun-8x12.png"#player is facing north
        else:
            if dy >= 0:
                if dx > 0: self.player_sprite = "graphics/PSE_nogun-8x12.png" #player is facing south east
                else: self.player_sprite = "graphics/PSW_nogun-8x12.png" #player is facing south west
            else:
                if dx > 0: self.player_sprite = "graphics/PNE_nogun-8x12.png" #player is facing north east
                else: self.player_sprite = "graphics/PNW_nogun-8x12.png" #player is facing north west
    
    def update(self, cursor_pos):
        self.pc_direction(cursor_pos)
        self.player.update(self.player_sprite)
        
    def draw(self, surface):
        self.player_spritegroup.draw(surface)