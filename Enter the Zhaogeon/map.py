from pygame import *

from settings import *
from level import *

from player import *
from wall import *
from cursor import *
from camera import *

#the map is created in Main
class Map():
    def __init__(self):
        super().__init__()
    
        self.player_spawn_sprite = "graphics/PS_nogun-8x12.png" #the sprite the player spawns with
        self.worldshift = Vector2(0,0) #used to self very element on screen
        
        #camra
        self.camera = Camera()
        self.camra_spritegroup = sprite.GroupSingle(self.camera)
        
        #declaring player
        self.player_speed = 7
        self.player_spritegroup = sprite.GroupSingle()
        
        #wall
        self.wall_spritegroup = sprite.Group()
        
        self.display_sprites = sprite.Group()
        self.all_sprites = sprite.Group(self.camra_spritegroup)

        self.loadmap(level1)
        
    def loadmap(self, level):
        size = int( 24 * (screenx/256) ) # size of wall tile (it is a square)
        for row_i, row in enumerate(level):
            for collum_i, object in enumerate(row):
                if object == 1:
                    self.wall = Wall(size, [collum_i * size, row_i * size])#positions the Wall on screen in position of its order in the 2d array * its size (for both sides/axis)
                    self.wall_spritegroup.add(self.wall)#adds the wall into the wall spritegroup
                    self.all_sprites.add(self.wall)#adds the wall into the all_sprites spritegroup
                if object == 2:
                    self.player = Player([collum_i * size, row_i *size], self.player_speed, self.player_spawn_sprite)#spawns player in position of its position in array * size of wall. With its speed and spawning sprite
                    self.player_spritegroup.add(self.player)#
                    self.all_sprites.add(self.player)#adds player 

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

        #should probably split into different functions

        #moves player first so that he can be teleported to correct position later

        #issue teleports player to wall after camera. causes player to be out of bounds when he shouldnt be. fix teleport player to camera b4 wall
        #move all instances of player/map movement to move function. modify calc funtions to only return values
        
        #x axis
        self.player.rect.x += self.player.speed.x #moves players
        if not(self.collision_detect("x")): self.camera_detect("x")
        
        #y axis
        self.player.rect.y += self.player.speed.y
        if not(self.collision_detect("y")): self.camera_detect("y")

        #self.player.speed is calculated in Player Class, ran in update through player.update (which rans player.speed_calcu)
    
    def update(self, cursor_pos):
        
        #move method needs player info to be calculated first

        self.player.update(cursor_pos) #player updates does all the calculations of the player
        self.move() #moves all sprites on map accordingly
        
    def draw(self):
        screen = display.get_surface()
        screen.blit(self.camera.hitbox, self.camera.rect)
        self.wall_spritegroup.draw(screen)
        self.player_spritegroup.draw(screen)
        