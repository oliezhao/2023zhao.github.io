from pygame import *
import pygame

from settings import *
from level import *

class Game:
    def __init__(self):
        
        init
        self.screen = display.set_mode((width,height))
        self.clock = time.Clock()
        self.caption = display.set_caption("Enter the Zhaogeon")
        
        self.level = Level()
        
    def run(self):
        keys = key.get_pressed() 
        
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    quit()
                    exit()
                    
                # exit game if esc is pressed
                
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        quit()
                        exit()

            self.screen.fill("black")
            self.level.run()
            display.update()
            self.clock.tick(fps)

            
if __name__ == "__main__":
    game = Game()
    game.run()