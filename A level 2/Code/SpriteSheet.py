from pygame import *
import json

from Settings import *

class SpriteSheet():
    def __init__(self, file_name: str):
        super().__init__()
        
        file_name = "Graphics\spritesheets\\" + file_name
        self.spritesheet = image.load(file_name).convert_alpha()
        self.json_file = file_name.replace("png", "json")
        
        with open(self.json_file) as json_file:
            self.meta_data = json.load(json_file)
    
    def get_image(self, x, y, w, h):
        sprite = Surface((w,h))
        sprite.set_colorkey(0,0)
        sprite.blit(self.spritesheet, (0,0), (x, y, w, h))
        sprite = transform.scale(sprite, (w * scale, h *scale))
        return sprite
        
    def parse_sprite(self, image_name: str):
        sprite = self.meta_data["frames"][image_name + ".png"]["frame"]
        x, y, w ,h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        return self.get_image(x, y, w, h)