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
        self.objects = import_csv_layout(test_level["entites"])
        self.tiles = sprite.Group()
        self.hitboxes = []
        
        self.load_map()

        self.move_direciton = Vector2(0,0)
        self.speed = scale
    
    def load_objects(self):
        for row_i, row in enumerate(self.objects):
            for col_i, value in enumerate(row):
                if value == "1":
                    pass
        pass
                
    def load_map(self):
        for row_i, row in enumerate(self.level):
            for col_i, value in enumerate(row):
                if value != "-1":
                    if len(value) == 1:
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
    
    def deload_map(self):
        for tile in self.tiles:
            tile.kill()
    
    def update(self):
        print("tiles")
        for tile in self.tiles:
            print("yesss")
            if tile.hitbox:
                print("yes")
                tile.hitbox_to_rect()
        
class Tile(sprite.Sprite):
    def __init__(self, x, y, row_i, col_i) -> None:
        super().__init__()
        
        self.spritesheet = Tile_SpriteSheet("test_level_spritesheet.png")
        self.image = self.spritesheet.get_image(x, y)
        self.rect = self.image.get_rect(topleft = (row_i * 16 * scale, col_i * 16 * scale))
        self.hitbox = sprite.GroupSingle()
        
    def add_hitbox(self, type: str):
        if type == "full": self.hitbox.add(Hitbox(self.rect.left, self.rect.top, 16, 16))
        if type == "half": self.hitbox.add(Hitbox(self.rect.left, self.rect.top, 16, 8))
    
    def hitbox_to_rect(self):
        if self.hitbox: 
            print("yes")
            self.hitbox.sprite.rect.topleft = self.rect.topleft

class Hitbox(sprite.Sprite):
    def __init__(self, x, y, w, h) -> None:
        super().__init__()
        
        self.surface = Surface((round(w * scale), round(h * scale)))
        self.rect = self.surface.get_rect(topleft = (x, y))