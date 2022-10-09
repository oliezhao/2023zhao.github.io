import pygame
from pygame import *

from settings import *
from debug import debug

from player import *
from cursor import *

from map import *

class Game:
    def __init__(self):
        super().__init__()
        display.set_caption("Dogwater")
        self.screen = display.set_mode(windowsize)
        self.clock = time.Clock()
    
        #declaring UI features
        self.cursor = Cursor()
        self.UI_spritelist = sprite.Group()
        
        #declareing map
        self.map = Map()
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    quit()
                    exit()
                    
            #game logic
            self.cursor.update()
            self.map.update(self.cursor.rect.center)
            
            #display order
            self.screen.fill('black')
            self.map.draw(self.screen)
            self.UI_spritelist.draw(self.screen)

            #debug is always drawn last
            debug(self.map.debug)
            display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    game = Game()
    game.run()
    
#notes to self
# when scale images, screenx * image.x/256 or screeny * image.y/144