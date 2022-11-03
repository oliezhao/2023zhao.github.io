from pygame import *

from settings import *
from level import *

from player import *
from wall import *
from cursor import *
from camera import *

from debug import *
#the map is created in Main
class Map():
    def __init__(self):
        super().__init__()
        
        #spawning sprite of player
        self.player_spawn_sprite = "graphics/PS_nogun-8x12.png"
        self.worldshift = Vector2(0,0)
        
        #camra
        self.camera = Camra()
        self.camera_spritegroup = sprite.GroupSingle(self.camera)
        
        #declaring player
        self.player_speed = int(screenx/200)
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

    def collision_detect(self, direction):#returns true when player collids with wall, returns false when player is not colliding with wall
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

    def camera_detect(self, direction):#returns a value if player is outside camera hitbox, returns false is player is within.
        
        if not(sprite.collide_rect(self.player, self.camera)): #if player is not colliding with camera hitbox
            if direction == "x":
                if self.player.rect.right < self.camera.rect.left: #detects if the player is to the left or right of the camera hitbox
                    return "pc"
                elif self.player.rect.left > self.camera.rect.right: 
                    return "cp"

            if direction == "y":
                if self.player.rect.top > self.camera.rect.bottom: #player is underneath camera hitbox
                    return "c/p"
                elif self.player.rect.bottom < self.camera.rect.top:  #player is above cameraiu hitbox
                    return "p/c"
                    
        else: #if player is colliding with camera hitbox
            return False

                    
    def move(self):

        #should probably split into different functions

        #moves player first so that he can be teleported to correct position later

        #moves player first so game can tell where he would be and correct to be where he should be

        #---X AXIS MOVEMENT
        self.player.rect.x += self.player.speed.x #moves players

        if not(self.collision_detect("x")) and self.camera_detect("x"):#if the player is not colliding with wall AND player is out of camera hitbox move all walls
            for wall in self.wall_spritegroup:
                wall.rect.x -= self.player.speed.x

        if self.camera_detect("x") == "pc": self.player.rect.right = self.camera.rect.left + 1
        if self.camera_detect("x") == "cp": self.player.rect.left = self.camera.rect.right - 1


        #-----Y AXIS MOVEMENT
        self.player.rect.y += self.player.speed.y

        if not(self.collision_detect("y")) and self.camera_detect("y"):#if the player is not colliding with wall AND player is out of camera hitbox move all walls
            for wall in self.wall_spritegroup:
                wall.rect.y -= self.player.speed.y

        if self.camera_detect("y") == "p/c": self.player.rect.bottom = self.camera.rect.top + 1
        if self.camera_detect("y") == "c/p": self.player.rect.top = self.camera.rect.bottom - 1


    
    def update(self, cursor_pos):
        #passes cursor position to player
        self.move()
        self.player.update(cursor_pos)
        
        
    def draw(self, surface):
        surface.blit(self.camera.hitbox, self.camera.rect)
        self.wall_spritegroup.draw(surface)
        self.player_spritegroup.draw(surface)
        