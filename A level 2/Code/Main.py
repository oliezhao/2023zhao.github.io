
import pygame
from pygame import *

from Settings import *

from Entities import *
from Menus import *
from UI import *

class Game:
    def __init__(self) -> None:
        super().__init__()
        
        pygame.init()
        
    #initialises display and clock
        display.set_caption("A Level")
        self.screen = display.set_mode(resolution, RESIZABLE)
        self.clock = time.Clock()
        mouse.set_visible(False)
        
    #attributes
        self.pause = False
    
        #Main menu
        self.gamestate = "title_screen"
        self.main_menu = MainMenu()
        
        self.main_bg = image.load("Graphics\menus\main_menu_background.png").convert_alpha()
        self.main_bg = transform.scale(self.main_bg, (screenx, screeny))
        self.main_bg_rect = self.main_bg.get_rect(topleft = (0,0))
        
        #Game
        self.cursor_image = image.load("Graphics\sprites\cursor.png").convert_alpha()
        self.cursor_image = transform.scale(self.cursor_image, (5 * scale, 5* scale))
        
        
    #methods
    def run(self):        
        while True:
            keys = key.get_pressed()
            mouse_pos = mouse.get_pos()
            buttons = mouse.get_pressed()
            
            #Universal events
            for event in pygame.event.get():
                if event.type == QUIT: #Escape Closes game
                    quit()
                    exit()
            
            #Main Screen
            if self.gamestate == "title_screen":
                self.screen.blit(self.main_bg, self.main_bg_rect)
                if not(self.pause): self.main_menu.update()
                self.main_menu.draw()
                
                #Buttons
                if self.main_menu.play_button.clicked:
                    
                    self.gamestate = "game"
                    self.main_menu.kill()
                    
                    self.player = Player(0,0)
                
                if self.main_menu.settings_button.clicked:
                    pass
                
                if self.main_menu.quit_button.clicked:
                    quit()
                    exit()
                    
            #Game
            if self.gamestate == "game":
                
                self.player.update()
                
                self.screen.fill("White")
                self.screen.blit(self.player.image, self.player.rect)
                draw.rect(self.screen, "Green", self.player.hitbox, 2)
            
            #Cursor
            self.cursor_rect = self.cursor_image.get_rect(center = mouse_pos)
            self.screen.blit(self.cursor_image, self.cursor_rect)
            
            display.update()
            self.clock.tick(60)
            
if __name__ == "__main__":
    game = Game()
    game.run()
    