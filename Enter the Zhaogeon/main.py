import pygame
from pygame import *

from settings import *
from debug import debug

from player import *
from map import *
from cursor import *
from level import level1
class Game:
    def __init__(self):
        super().__init__()
        display.set_caption("Dogwater")
        self.screen = display.set_mode(windowsize)
        self.clock = time.Clock()

        
        #--Object Creation--
        #decalres an Instance of Cursor
        self.cursor = Cursor()
        self.UI_spritelist = sprite.Group(self.cursor)
        
        #declares an Instance of Map
        #an Instance of Player is declared in Map
        self.map = Map()
        
        self.gamestate = "main menu"

        self.main_menu_image = image.load("graphics/main_menu.png").convert_alpha()
        self.main_menu_image = transform.scale(self.main_menu_image, (screenx, screeny))

        self.victory_image = image.load("graphics/congradulations.png").convert_alpha()
        self.victory_image = transform.scale(self.victory_image, (screenx, screeny))

        self.defeat_image = image.load("graphics/defeat.png").convert_alpha()
        self.defeat_image = transform.scale(self.victory_image, (screenx, screeny))

    def run(self):
        
        #--GAME LOOP--
        while True:
            
            #detect keys pressed every loop
            keys = key.get_pressed()
            buttons = mouse.get_pressed()
            for event in pygame.event.get():
                #quits game if window is closed or escape key is pressed
                if event.type == QUIT or keys[K_ESCAPE]:
                    quit()
                    exit()
            if self.gamestate == "main menu" and buttons[0]:
                self.gamestate = "game"
            if self.gamestate == "game":
                if not(self.map.enemy_spritegroup):
                    self.gamestate = "victory"
                if not(self.map.player_spritegroup):
                    self.gamestate = "defeat"

            if (self.gamestate == "victory" or self.gamestate == "defeat") and keys[K_r]:
                for sprite in self.map.notp_spritegroup:
                        sprite.kill()
                self.map.loadmap(level1)
                self.gamestate = "game"
        
            #--Game Logic
            
            #moves cursor sprite to mouse location
            self.cursor.update()
    
            #runs player.update
            self.map.update(self.cursor.rect.center)
            
            #--Display order
            self.screen.fill('black')
            self.map.draw(self.screen)
            self.UI_spritelist.draw(self.screen)
            
            #debug is always drawn last
            # string = ""
            # if not(self.map.camera_detect): string += "Out of bounds, "
            # wall_in_contact = sprite.spritecollide(self.map.player, self.map.wall_spritegroup, False)
            # if wall_in_contact: 
            #     string += "Collision with Wall, "
            
            string = str(self.map.player.status)

            if self.gamestate == "game":
                #runs player.update
                self.map.update(self.cursor.rect.center)
                
                #--Display order
                self.screen.fill("#ffe4e1")
                self.map.draw(self.screen)
            
                #debug is always drawn last
                # string = ""
                # if not(self.map.camera_detect): string += "Out of bounds, "
                # wall_in_contact = sprite.spritecollide(self.map.player, self.map.wall_spritegroup, False)
                # if wall_in_contact: 
                #     string += "Collision with Wall, "
                
                string = str(self.map.bullet_spritegroup)

                debug(string) #debug is always drawn last

            if self.gamestate == "victory":
                self.screen.blit(self.victory_image, (0,0))

            if self.gamestate == "defeat":
                self.screen.blit(self.defeat_image, (0,0))

            self.UI_spritelist.draw(self.screen)

            display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    mouse.set_visible(False)
    game = Game()
    game.run()
    
#notes to self
# when scale images, screenx * image.x/256 or screeny * image.y/144a
#the entire screen displays 256 pixels across and 144 pixels high