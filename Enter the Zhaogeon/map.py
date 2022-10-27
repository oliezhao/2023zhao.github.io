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
                        return "pw" #player is moving right into the wall
                        self.player.rect.right = wall.rect.left #the player's right is teleported to the walls left
                    elif self.player.move_direction.x < 0: #if the player is moving left
                        return "wp" #player is moving left int othe wall
                        self.player.rect.left = wall.rect.right #the player's left is teleported to the walls right
                    else:
                        return False

                if direction == "y": #if checking for y axis
                    if self.player.move_direction.y > 0: #if player is moving down
                        return "p/w" #player is moving down into the wall
                        self.player.rect.bottom = wall.rect.top #players bottom is teleported to the walls top
                    elif self.player.move_direction.y < 0: #if player is moving up
                        return "w/p" #player is moving up into the wall
                        self.player.rect.top = wall.rect.bottom #players top is teleported to walls bottom
                    else:
                        return False

    def camera_detect(self, direction):

        if not(sprite.collide_rect(self.player, self.camera)):
            for wall in self.wall_spritegroup:
                if direction == "x":
                    if self.player.rect.right < self.camera.rect.left: #detects if the player is to the left or right of the camera hitbox
                        return "pc" #player is the left of camera
                        self.player.rect.right = self.camera.rect.left + 1#teleports player back to the according side of the camera hitbox
                    elif self.player.rect.left > self.camera.rect.right: 
                        return "cp" #player is right of camera
                        self.player.rect.left = self.camera.rect.right - 1

                    wall.rect.x -= self.player.speed.x

                if direction == "y":
                    if self.player.rect.top > self.camera.rect.bottom: #detects if the player is to the top or bottom of the camera
                        return "c/p" #player is below wall
                        self.player.rect.top = self.camera.rect.bottom - 1#teleports the player to the according side of the camera hitbox
                    elif self.player.rect.bottom < self.camera.rect.top: 
                        return "p/c" #player is above wall
                        self.player.rect.bottom = self.camera.rect.top + 1
                    
                    wall.rect.y -= self.player.speed.y
    def move(self):

        #should probably split into different functions

        #moves player first so that he can be teleported to correct position later

        #issue teleports player to wall after camera. causes player to be out of bounds when he shouldnt be. fix teleport player to camera b4 wall
        #move all instances of player/map movement to move function. modify calc funtions to only return values
        
        #x axis
        self.player.rect.x += self.player.speed.x #moves players
        
        if self.collision_detect("x"):
        if self.camera_detect("y"): 
        
        #if not(self.collision_detect("x")): self.camera_detect("x")
        
        #y axis
        self.player.rect.y += self.player.speed.y
        
        if self.collision_detect("y"):
        if self.camera_detect("y"):
        if not(self.collision_detect("y")): self.camera_detect("y")

            if self.player.rect.right < self.camra.rect.left: 
                self.player.rect.right = self.camra.rect.left + 1
            elif self.player.rect.left > self.camra.rect.right: 
                self.player.rect.left = self.camra.rect.right - 1
                
            if self.player.rect.top > self.camra.rect.bottom: 
                self.player.rect.top = self.camra.rect.bottom - 1
            elif self.player.rect.bottom < self.camra.rect.top: 
                self.player.rect.bottom = self.camra.rect.top + 1
                
            for self.wall in self.wall_spritegroup:
                self.wall.rect.x -= self.player.speed.x
                self.wall.rect.y -= self.player.speed.y
        else:
            self.worldshift.x = 0
            self.worldshift.y = 0
    
    def update(self, cursor_pos):
        #passes cursor position to player
        print(self.player.speed)
        self.move()
        self.player.update(cursor_pos)
        
        
    def draw(self, surface):
        surface.blit(self.camra.hitbox, self.camra.rect)
        self.wall_spritegroup.draw(surface)
        self.player_spritegroup.draw(surface)
        