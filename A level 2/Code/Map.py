from pygame import *
import csv, os

from SpriteSheet import *

test_level = { 
              "tiles": "Maps/test_level_Tile_Layer.csv", 
              "entites": "Maps/test_level_Objects.csv"
              }

def import_csv_layout(path):
    level = []
    with open(path) as map:
        data = csv.reader(map, delimiter = ",")
        for row in data:
            level.append(row)
    return level
    
class Map(sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        
        self.level = import_csv_layout(test_level["tiles"])
        self.tiles = sprite.Group()
        self.hitboxes = sprite.Group()
        
        self.load_map()

        self.move_direciton = Vector2(0,0)
        self.speed = scale
    
    def input(self):
        keys = key.get_pressed()
        if keys[K_UP]: self.move_direciton.y = -1
        elif keys[K_DOWN]: self.move_direciton.y = 1
        else: self.move_direciton.y = 0
        
        if keys[K_RIGHT]: self.move_direciton.x = -1
        elif keys[K_LEFT]: self.move_direciton.x = 1
        else: self.move_direciton.x = 0
        
    def move(self, speed, direction):
        for tile in self.tiles:
            tile.rect.x -= round(speed * direction.x)
            tile.rect.y += round(speed * direction.y)
    
    def load_map(self):
        for row_i, row in enumerate(self.level):
            for col_i, value in enumerate(row):
                if value != "-1":
                    if len(value) == 1:
                        print("stuff")
                        value = "0" + value
                    y = int(value[0])
                    x = int(value[1])
                    tile = Tile(x, y, col_i, row_i)
                    if value != "34":
                        if value == "30":
                            tile.add_hitbox("half")
                        else:
                            tile.add_hitbox("full")
                    self.tiles.add(tile)
    
    def update(self):
        self.input()
        self.move()
        
class Tile(sprite.Sprite):
    def __init__(self, x, y, row_i, col_i) -> None:
        super().__init__()
        
        self.spritesheet = Tile_SpriteSheet("test_level_spritesheet.png")
        self.image = self.spritesheet.get_image(x, y)
        self.rect = self.image.get_rect(topleft = (row_i * 16 * scale, col_i * 16 * scale))
        
    def add_hitbox(self, type: str):
        if type == "full": rect = Surface((round(16 * scale), round(16 * scale))).get_rect()
        if type == "half": rect = Surface((round(16 * scale), round(8 * scale))).get_rect()
        self.hitbox = rect
        
print(import_csv_layout(test_level["tiles"]))