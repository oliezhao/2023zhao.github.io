import pygame, sys
from pygame import *

from settings import *
from level import *

class Game:
    def __init__(self):
        init()
        self.screen = display.set_mode((WIDTH,HEIGHT))
        self.caption = display.set_caption("Enter the Zhaogeon")
        self.clock = time.Clock()
        
        self.level = Level()
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    quit()
                    sys.exit()
                
            self.screen.fill("BLACK")
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()