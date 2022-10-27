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
        display.set_caption("A Levels") 
        self.screen = display.set_mode(windowsize)
        self.clock = time.Clock()

        self.cursor = Cursor() #Creates an Instane of Cursor
        self.UI_spritelist = sprite.Group(self.cursor) #Adds self.cursor to UI_spritelist
        #All cordinates of cursor should be taken from self.cursor.rect. This allows manipulation of cursor by enemies.
        #Enemy can trap cursor. Create a barrier in which the cursor cannot enter e.c.t
        
        self.map = Map() #Creates an Instance of Map
        
    def run(self):
        
        #--GAME LOOP--
        while True:
            
            keys = key.get_pressed() #Creates array

            for event in pygame.event.get():

                if (event.type == QUIT) or (keys[K_ESCAPE]): #Exit conditions for game
                    quit()
                    exit()
                    
            #--Game Logic
            
            #1. Update cursor
            #Player Instance created and updated in map because player is only spawned when map is loaded. I.e on main menu player isnt displayed or updated. Also makes pausing game easier as i only need to stop updating Map
            #Enemy Instance will also be created an updated on map
            #2. Update Map - player on map needs cursor info to calculate which 

            self.cursor.update() #Updates cursor
            #Sets self.cursor.rect.center to mouse cordinates)
            self.map.update(self.cursor.rect.center) #Updates map
            #Updates player on map
            #Moves map
                #moves player
                #calculates if player is within camera range
                    #if he is nothing happens
                    #if he isn't tellport him back within ranges

            #--Display order

            self.screen.fill('black') #Background
            self.map.draw() #Draws map
            self.UI_spritelist.draw(self.screen) # Draws UI

            #Debug BS
            string = ""
            
            string += str(self.map.player.speed.xy)
            
            if not(sprite.collide_rect(self.map.player, self.map.camera)): string += "Out of bounds, " #displays when player out of camera bounds
            wall_in_contact = sprite.spritecollide(self.map.player, self.map.wall_spritegroup, False)
            
            if wall_in_contact: #displays when player collides with wall
                string += "Collision with Wall, "
            
            
            debug(string) #debug is always drawn last

            display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    mouse.set_visible(False) #Hides Mouse
    game = Game()
    game.run()
    
#notes to self
# when scale images, screenx * image.x/256 or screeny * image.y/144
#the entire screen displays 256 pixels across and 144 pixels high