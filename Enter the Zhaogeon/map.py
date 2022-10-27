from pygame import *

from settings import *
from level import *

from player import *
from wall import *
from cursor import *
from camra import *

#the map is created in Main
class Map():
    def __init__(self):
        super().__init__()
        
        #spawning sprite of player
        self.player_spawn_sprite = "graphics/PS_nogun-8x12.png"
        self.worldshift = Vector2(0,0)
        
        #camra
        self.camra = Camra()
        self.camra_spritegroup = sprite.GroupSingle(self.camra)
        
        #declaring player
        self.player_speed = 7
        self.player_spritegroup = sprite.GroupSingle()
        
        #wall
        self.wall_spritegroup = sprite.Group()
        
        
        self.loadmap(level1)
        
    def loadmap(self, level):
        size = int( 15 * (screenx/256) )
        for row_i, row in enumerate(level):
            for collum_i, object in enumerate(row):
                if object == 1:
                    self.wall = Wall([collum_i * size, row_i * size])
                    self.wall_spritegroup.add(self.wall)
                if object == 2:
                    self.player = Player([collum_i * size, row_i *size], self.player_speed, self.player_spawn_sprite)
                    self.player_spritegroup.add(self.player)

    def move(self):

        self.player.rect.x += self.player.speed.x #moves players
        if not(self.collision_detect("x")): self.camera_detect("x")

    
    def update(self, cursor_pos):
        #passes cursor position to player
        print(self.player.speed)
        self.move()
        self.player.update(cursor_pos)
        
        
    def draw(self, surface):
        surface.blit(self.camra.hitbox, self.camra.rect)
        self.wall_spritegroup.draw(surface)
        self.player_spritegroup.draw(surface)
        