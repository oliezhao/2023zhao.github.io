from pygame import *
from settings import *
from tile import *
from player import *

class Level:
    def __init__(self):
        
        self.display_surface = display.get_surface()
        #spirit group setup
        self.visable_sprites = sprite.Group()
        self.obstacle_sprites = sprite.Group()
        self.create_map()
    
    def create_map(self):
         for row_index, row in enumerate(map):
             for column_index, value in enumerate(row):
                 x = column_index * tilesize
                 y = row_index * tilesize
                 if value == "p":
                     Player((x,y),[self.visable_sprites])
        
    def run(self):
        pass