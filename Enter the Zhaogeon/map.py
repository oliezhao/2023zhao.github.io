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

    def collision_detect(self, direction):

        walls_in_contact = sprite.spritecollide(self.player, self.wall_spritegroup, False) #Creates a list of all walls in collision with player
        if walls_in_contact: #if the list is not empty
            for wall in walls_in_contact: #checks for very wall in contact
                if direction == "x": #if checking for the x axis
                    if self.player.move_direction.x > 0: #if player is moving right
                        self.player.rect.right = wall.rect.left #the player's right is teleported to the walls left
                        return True
                    elif self.player.move_direction.x < 0: #if the player is moving left
                        self.player.rect.left = wall.rect.right #the player's left is teleported to the walls right
                        return  True
                    else:
                        return False

                if direction == "y": #if checking for y axis
                    if self.player.move_direction.y > 0: #if player is moving down
                        self.player.rect.bottom = wall.rect.top #players bottom is teleported to the walls top
                        return True
                    elif self.player.move_direction.y < 0: #if player is moving up
                        self.player.rect.top = wall.rect.bottom #players top is teleported to walls bottom
                        return True
                    else:
                        return False

    def camera_detect(self, direction):

        # if not(sprite.collide_rect(self.player, self.camera)): #if player is out of bounds with camera

        #     if self.player.rect.right < self.camera.rect.left: #detects if the player is to the left or right of the camera hitbox
        #         self.player.rect.right = self.camera.rect.left + 1#teleports player back to the according side of the camera hitbox
        #     elif self.player.rect.left > self.camera.rect.right: 
        #         self.player.rect.left = self.camera.rect.right - 1
                
        #     if self.player.rect.top > self.camera.rect.bottom: #detects if the player is to the top or bottom of the camera
        #         self.player.rect.top = self.camera.rect.bottom - 1#teleports the player to the according side of the camera hitbox
        #     elif self.player.rect.bottom < self.camera.rect.top: 
        #         self.player.rect.bottom = self.camera.rect.top + 1
                
        #     for self.wall in self.wall_spritegroup: #change to "for element in self.nonplayer_spritegroup" at later date
        #         self.wall.rect.x -= self.player.speed.x #because player is being teleport back to camera hitbox, all assets move in oppsite direcction of player, with player speed to simulate player movement
        #         self.wall.rect.y -= self.player.speed.y
        
        if not(sprite.collide_rect(self.player, self.camera)):
            for wall in self.wall_spritegroup:
                if direction == "x":
                    if self.player.rect.right < self.camera.rect.left: #detects if the player is to the left or right of the camera hitbox
                        self.player.rect.right = self.camera.rect.left + 1#teleports player back to the according side of the camera hitbox
                    elif self.player.rect.left > self.camera.rect.right: 
                        self.player.rect.left = self.camera.rect.right - 1

                    wall.rect.x -= self.player.speed.x

                if direction == "y":
                    if self.player.rect.top > self.camera.rect.bottom: #detects if the player is to the top or bottom of the camera
                        self.player.rect.top = self.camera.rect.bottom - 1#teleports the player to the according side of the camera hitbox
                    elif self.player.rect.bottom < self.camera.rect.top: 
                        self.player.rect.bottom = self.camera.rect.top + 1
                    
                    wall.rect.y -= self.player.speed.y
    def move(self):

        self.player.rect.x += self.player.speed.x #moves players
        if not(self.collision_detect("x")): self.camera_detect("x")

        
        self.player.rect.y += self.player.speed.y
        if not(self.collision_detect("y")): self.camera_detect("y")

    def update(self, cursor_pos):
        #passes cursor position to player
        print(self.player.speed)
        self.move()
        self.player.update(cursor_pos)
        
        
    def draw(self, surface):
        surface.blit(self.camra.hitbox, self.camra.rect)
        self.wall_spritegroup.draw(surface)
        self.player_spritegroup.draw(surface)
        