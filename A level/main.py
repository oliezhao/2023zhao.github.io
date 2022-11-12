from pygame import *
import pygame

from common import *
from debug import *
from map import *
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
        
        self.gamestate ="main_menu"
        self.pause = False
        self.UI_spritegroup = sprite.Group()

        self.main_menu = MainMenu()
        self.pause_menu = Pause_Menu()

        
    def run(self):
        
        #---GAME LOOP---
        while True: #loops indefinately
            
            keys = key.get_pressed()
            buttons = mouse.get_pressed()

            for event in pygame.event.get():
                if (event.type == QUIT) or (keys[K_LALT] and keys[K_F4]): #if (windows is closed) or (alt+f4 is pressed)
                     quit() #game closes
                     exit()
                
                if self.gamestate == "main_menu":
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        if self.main_menu.play_button in self.main_menu.button_in_contact:
                            self.map = Map()
                            self.gamestate = "game"
                        if self.main_menu.quit_button in self.main_menu.button_in_contact:
                            quit()
                            exit()

                if self.gamestate == "game":
                    if  keys[K_ESCAPE]:
                        self.gamestate = "pause_menu" 
                
                if self.gamestate == "pause_menu":
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        if self.pause_menu.resume_button in self.pause_menu.button_in_contact:
                            self.gamestate = "game"
                        if self.pause_menu.exit_to_menu_button in self.pause_menu.button_in_contact:
                            self.gamestate = "main_menu"
                        if self.pause_menu.quit_button in self.pause_menu.button_in_contact:
                            quit()
                            exit()

            #---MAIN MENU---
            if self.gamestate == "main_menu":
                
                self.main_menu.update()#updates main_menu
                    #Adds all main_menu.buttons in main_menu.UI_srpitelist
                    #Detects input on main menu
                    #Draws elements
                        #1. Background
                        #2. All sprites in main_menu.UI_spritelist
                        #3. Highlight buttons mouse is hovering over
                    #Empties main_menu.buttons_in_contact spritelist
                
                debug(self.screen, self.main_menu.debugmsg, (0,0))
            
            #---GAME ---
            if self.gamestate == "game":

                self.screen.fill("#DCC7DC")
                self.map.update()
                debug(self.screen, self.map.debugmsg, (0,0) )
            
            #--Pause Menu
            if self.gamestate == "pause_menu":
                self.screen.fill("#DCC7DC")
                self.map.draw()

                self.pause_menu.update()

                debug(self.screen, self.gamestate, (0,0))
            
            #debug(self.screen, self.gamestate, (0,0))
            #Cursor
            self.cursor_spritegroup.update()
            self.cursor_spritegroup.draw(self.screen)

            #Display and Clock
            display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()