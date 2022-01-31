import pygame
from pygame import *

from settings import MAP
from tile import *

class Level:
    def __init__(self):
        self.display_surface = display.get_surface
        self.visible_sprites = sprite.Group()
        self.obstacles_sprites = sprite.Group()
    
        self.create_map()
        
    def create_map(self):
        for row_index, row in enumerate(MAP):
            for col_index, col in enumerate(row):
                x = col_index * 200
                y = row_index * 200
                if col == "x":
                    Tile((x,y), [self.visible_sprites])
    
    def run(self):
        self.visible_sprites.draw(self.display_surface)