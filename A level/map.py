from pygame import *
from common import *

from tile import *
from camera import *
from player import *
from enemy import *

from math import cos, sin

class Map():
    def __init__(self) -> None:
        super().__init__()

        self.tile_sg_l1 = sprite.Group()
        self.tile_sg_l2 = sprite.Group()
        self.tiles = sprite.Group()
        self.nonpsprites= sprite.Group()
        self.sprites = sprite.Group()
        self.player_spritegroup = sprite.GroupSingle()
        self.bullets = sprite.Group()
        self.enemies = sprite.Group()

        self.hitboxes = sprite.Group()

        self.player = Player((0,0))
        self.sprites.add(self.player)

        self.camera = Camera()
        self.sprites.add(self.camera)

        self.loadmap(testlevel)

        self.debugmsg = ""

    def loadmap(self, map):
        
        for row_i, row in enumerate(map):
            for column_i, object in enumerate(row):
                if object != -1:
                    if object == 38:
                        self.player.rect.topleft = ((column_i * 16 * scale, row_i * 16 * scale))
                        self.player_spritegroup.add(self.player)
                    else:
                        tile = Tile(object, (column_i * round(16 * scale), row_i * round(16 * scale)))
                        if object != 48:
                            self.tile_sg_l2.add(tile)
                            self.hitboxes.add(tile.hitbox)
                        else:
                            self.tile_sg_l1.add(tile)
                            self.hitboxes.add(tile.hitbox)


    def withinbonds(self, direction):
        if not(self.camera.rect.colliderect(self.player.rect)):
            if direction == "x":
                if self.player.move_direction.x > 0:
                    self.player.rect.left = self.camera.rect.right - 1
                if self.player.move_direction.x < 0:
                    self.player.rect.right = self.camera.rect.left + 1
            
            if direction == "y":
                if self.player.move_direction.y > 0:
                    self.player.rect.bottom = self.camera.rect.top + 1
                if self.player.move_direction.y < 0:
                    self.player.rect.top = self.camera.rect.bottom - 1

            return False
        else:
            return True
    
    def wall_collision(self, direction):
        hitboxes_in_contact = sprite.spritecollide(self.player, self.hitboxes, False)
        if hitboxes_in_contact:
            for hitbox in hitboxes_in_contact:
                if direction == "x":
                    if self.player.move_direction.x > 0:
                        self.player.rect.right = hitbox.rect.left
                    if self.player.move_direction.x <0:
                        self.player.rect.left = hitbox.rect.right
                if direction == "y":
                    if self.player.move_direction.y > 0:
                        self.player.rect.top = hitbox.rect.bottom
                    if self.player.move_direction.y < 0:
                        self.player.rect.bottom = hitbox.rect.top

            return True


    def draw(self):
        screen = display.get_surface()
        self.tile_sg_l1.draw(screen)
        self.player_spritegroup.draw(screen)
        self.player.bullets.draw(screen)
        self.tile_sg_l2.draw(screen)
        
        draw.rect(screen, "Green", self.player.rect, 2)
        draw.rect(screen, "Red", self.camera.rect, 2)
        for hitbox in self.hitboxes:
            draw.rect(screen, "Blue", hitbox.rect, 2)
    def move(self):

        self.player.move("x")
        for bullet in self.bullets:
            bullet.move("x")
        if not(self.wall_collision("x")) and not(self.withinbonds("x")):
            for sprite in self.nonpsprites:
                sprite.rect.x -= round(self.player.velocity.x)
        self.withinbonds("x")

        self.player.move("y")
        for bullet in self.bullets:
            bullet.move("y")

        if not(self.wall_collision("y")) and not(self.withinbonds("y")):  
            for sprite in self.nonpsprites:
                sprite.rect.y += round(self.player.velocity.y)
        self.withinbonds("y")
    
    def update(self):

        #--Sprite Group
        for hitbox in self.hitboxes:
            self.nonpsprites.add(hitbox)
            self.sprites.add(hitbox)

        for tile in self.tile_sg_l1:
            self.tiles.add(tile)

        for tile in self.tile_sg_l2:
            self.tiles.add(tile)

        for bullet in self.player.bullets:
            self.bullets.add(bullet)
            print(bullet)

        for bullet in self.bullets:
            self.nonpsprites.add(bullet)
            self.sprites.add(bullet)

        for tile in self.tiles:
            self.nonpsprites.add(tile)
            self.sprites.add(tile)

        for enemy in self.enemies:
            self.nonpsprites.add(tile)
            self.sprites.add(tile)
        
        #---Logic
        self.player_spritegroup.update()
        self.bullets.update()
        
        for bullet in self.bullets:
            if sprite.spritecollide(bullet, self.hitboxes, False):
                bullet.kill()
            
            
        self.move()

        #---Draw
        self.draw()

        self.debugmsg = str(self.player.bullets) + str(self.bullets)