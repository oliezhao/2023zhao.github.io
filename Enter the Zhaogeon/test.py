from pygame import *
import pygame

class Object():
    def __init__(self,color, size, pos):
        super().__init__()
        self.image = Surface(size)
        self.image.fill("Red")
        self.rect = self.image.get_rect(topleft = (pos))
    
    def move(self):
        self.rect.center = mouse.get_pos()
        
class Game():
    def __init__(self):
        super().__init__()
        display.set_caption("test")
        self.screen = display.set_mode((1000,1000))
        self.clock = time.Clock()

        self.square = Object("Red", (100,100), (0,0))
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    quit()
                    exit()
            
            
            self.square.move()
            
            self.screen.fill("Black")
            self.screen.blit(self.square.image, self.square.rect)
            print(self.square.rect.center[0])
            display.update()
            self.clock.tick(60)

            



if __name__ == '__main__':
    game = Game()
    game.run()
