from pygame import *
from common import *

from UI import *

class MainMenu(sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.debugmsg = ""
        
        self.font = font.Font(None, 50)
        self.bg_image = image.load("graphics/main_menu.png").convert_alpha()
        self.bg_image = transform.scale(self.bg_image, (256 * scale, 144 * scale))
        
        self.buttons_in_contact = sprite.Group()
        self.button_spritelist = sprite.Group()
        self.UI_spritelist = sprite.Group()#is drawn in self.draw
        
        self.playbutton = Button("Play", "White", int(20 * scale) , (screenx/2, screeny * 0.5), "graphics/Bold.otf")
        self.optionbutton = Button("Options", "White", int(20 * scale) , (screenx/2, screeny * 0.625), "graphics/Bold.otf")
        self.quitbutton = Button("Quit", "White", int(20 * scale) , (screenx/2, screeny * 0.750), "graphics/Bold.otf")
        self.button_spritelist.add(self.playbutton)
        self.button_spritelist.add(self.optionbutton)
        self.button_spritelist.add(self.quitbutton)
        
        self.play = False
    
    def input(self):
        mouse_pos = mouse.get_pos()
        mouse_keys = mouse.get_pressed()
        events = event.get()
        
        for button in self.button_spritelist:
            if button.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                if button == self.playbutton and mouse_keys[0]: 
                    self.play = True
                if button == self.quitbutton and mouse_keys[0]:
                    quit()
                    exit()
                    
                self.buttons_in_contact.add(button)
                
    def highlight(self, screen):
        mouse_pos = mouse.get_pos()

        for button in self.buttons_in_contact:
            draw.rect(screen, "White", button.rect, 2)
    
    def draw(self):
        screen = display.get_surface()
        
        screen.blit(self.bg_image, (0,0))
        self.UI_spritelist.draw(screen)
        self.highlight(screen)
        
    def update(self):
        
        self.UI_spritelist.add(self.button_spritelist)

        self.input()
        
        self.draw()
        
        self.buttons_in_contact.empty()
        
        self.debugmsg = (str(self.UI_spritelist) + "/" + str(self.button_spritelist))