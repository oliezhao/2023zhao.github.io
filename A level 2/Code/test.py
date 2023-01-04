from pygame import *
import pygame 

class Game:
    def __init__(self) -> None:
        super().__init__()
        
        pygame.init()
        
    #initialises display and clock
        display.set_caption("A Level")
        self.screen = display.set_mode((1000,500))
        self.clock = time.Clock()

    #attributes
        self.black_menu = image.load("graphics/menus/menu_background.png").convert_alpha()
        self.black_menu = transform.scale(self.black_menu, (250,250))
        self.black_menu = Surface((250,250))
        self.black_menu.set_alpha(220)
        self.bm_rect = self.black_menu.get_rect(topleft = (0,0))
        
        self.red_box = Surface((100,100))
        self.red_box_rect = self.red_box.get_rect(topleft = (0,0))
        self.red_box.fill("Red")
        
    #methods    
    def run(self):
        while True:
            keys = key.get_pressed()
            
            #Quit Conditions
            for event in pygame.event.get():
                if event.type == QUIT or keys[K_ESCAPE]: #Escape Closes game
                    quit()
                    exit()
            
            self.screen.fill("#D38DD5")
            self.screen.blit(self.black_menu, self.bm_rect)
            
            mouse_pos = mouse.get_pos()
            self.red_box_rect.center = mouse_pos
            
            self.black_menu.blit(self.red_box, self.red_box_rect)
            
            display.update()
            self.clock.tick(60)
            
if __name__ == "__main__":
    game = Game()
    game.run()