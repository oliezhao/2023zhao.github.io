from pygame import *
import pygame

from common import *
from debug import *
from main_menu import *
from player import *
from UI import *

class Game:
    def __init__(self):
        super().__init__()
        
        display.set_caption("A Level")
        self.screen = display.set_mode(screen_resolution)
        self.clock = time.Clock()
        
        
        mouse.set_visible(False)
        self.cursor = Cursor()
        self.cursor_spritegroup = sprite.Group(self.cursor)
        
        self.gamestate ="main menu"   
        self.UI_spritegroup = sprite.Group()
        
        self.player = Player([0, 0])
        self.player_spritegroup = sprite.GroupSingle(self.player)

        self.main_menu = MainMenu()
        

        
    def run(self):
        
        #---GAME LOOP---
        while True: #loops indefinately
            keys = key.get_pressed()
            
            for event in pygame.event.get():
                if (event.type == QUIT) or (keys[K_LALT] and keys[K_F4]): #if (windows is closed) or (alt+f4 is pressed)
                     quit() #game closes
                     exit()
            
            #---MAIN MENU---
            if self.gamestate == "main menu":
                
                self.main_menu.update()#updates main_menu
                    #Adds all main_menu.buttons in main_menu.UI_srpitelist
                    #Detects input on main menu
                    #Draws elements
                        #1. Background
                        #2. All sprites in main_menu.UI_spritelist
                        #3. Highlight buttons mouse is hovering over
                    #Empties main_menu.buttons_in_contact spritelist
                
                if self.main_menu.play == True: #When play button is pressed
                    self.gamestate = "game" #change gamestate
                
                debug(self.screen, self.main_menu.debugmsg, (0,0))
            
            #---GAME ---
            if self.gamestate == "game":#GAME
                self.screen.fill("White")
                
                self.player.update()#updates player
                    #increment self.clock by 1
                    #detect inputs
                        #applies
                    #calculates velocity
                    
                    
                self.player_spritegroup.draw(self.screen)
                
                #---HIT BOX SHOW
                draw.rect(self.screen, "Green", self.player.rect, 2)
                
                debug(self.screen, self.player.debugmsg, (0,0) )
            
            #Cursor
            self.cursor_spritegroup.update()
            self.cursor_spritegroup.draw(self.screen)
            
            #Display and Clock
            display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()