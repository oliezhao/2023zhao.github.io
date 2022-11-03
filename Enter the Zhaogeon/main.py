import pygame
from pygame import *

from settings import *
from debug import debug

from player import *
from map import *
from cursor import *

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
        
    def run(self):
        
        #--GAME LOOP--
        while True:
            
            #detect keys pressed every loop
            keys = key.get_pressed()
            
            for event in pygame.event.get():
                #quits game if window is closed or escape key is pressed
                if event.type == QUIT or keys[K_ESCAPE]:
                    quit()
                    exit()
                    
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
            
            #debug(time.get_ticks()) #debug is always drawn last

            display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    mouse.set_visible(False)
    game = Game()
    game.run()
    
#notes to self
# when scale images, screenx * image.x/256 or screeny * image.y/144
#the entire screen displays 256 pixels across and 144 pixels high