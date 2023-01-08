from pygame import *
import pygame 
from math import *

def debug(text):
    font_ = font.Font(None, round(30))
    text = font_.render(text, True, "White")
    rect = text.get_rect(topleft = (0,0))
    
    screen = display.get_surface()
    draw.rect(screen, "Black", rect)
    screen.blit(text, rect)

class Object(sprite.Sprite):
    def __init__(self, coords, color: str) -> None:
        super().__init__()
        
        self.image = Surface((200,200))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = coords)
        
class Game:
    def __init__(self) -> None:
        super().__init__()
        
        pygame.init()
        
    #initialises display and clock
        display.set_caption("A Level")
        self.screen = display.set_mode((1000,500))
        self.clock = time.Clock()

    #attributes

        self.select = 1


        self.sub_SG_1 = sprite.Group()
        self.sub_SG_2 = sprite.Group()
        self.main_SG = sprite.Group(self.sub_SG_1, self.sub_SG_2)
    
    #methods    
    def run(self):
        while True:
            keys = key.get_pressed()
            mouse_pos = mouse.get_pos()
            
            #Quit Conditions
            for event in pygame.event.get():
                if event.type == QUIT or keys[K_ESCAPE]: #Escape Closes game
                    quit()
                    exit()
                
                if event.type == KEYDOWN and event.key == K_q:
                    print("switch")
                    if self.select == 1: 
                        self.select = 2
                        print(self.select)
                    else: 
                        self.select = 1
                        print(self.select)
                
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.select == 1:
                            object = Object(mouse_pos, "Red")
                            self.sub_SG_1.add(object)
                            # self.main_SG.add(object)
                        else:
                            object = Object(mouse_pos, "Blue")
                            self.sub_SG_2.add(object)
                            # self.main_SG.add(object)
                    if event.button == 3:
                        print("delete")
                        for object in self.main_SG:
                            if object.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                                object.kill()
                
                           
            #Update
            if 1 == 1:
                # self.main_SG.add(self.sub_SG_1)
                # self.main_SG.add(self.sub_SG_2)
                
                main_string = ""
                
                for sprite in self.main_SG.sprites():
                    main_string = str(sprite)
                
                string = str(self.select) + ", " + str(self.main_SG) + ", " + str(self.sub_SG_1) + ", " + str(self.sub_SG_2)
                
                print(str(sin(7)))
                
            #Draw
            if 1 == 1:
                self.screen.fill("#D38DD5")
                self.main_SG.draw(self.screen)
                debug(string)
                
            display.update()
            self.clock.tick(60)
            
if __name__ == "__main__":
    game = Game()
    game.run()