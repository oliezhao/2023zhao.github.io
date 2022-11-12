from pygame import *
from common import *

class Cursor(sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = image.load("graphics/sprites/cursor-9x9.png").convert_alpha()
        self.image = transform.scale(self.image, (6 * scale, 6 * scale)).convert_alpha()
        self.rect = self.image.get_rect(center = mouse.get_pos())
    
    def update(self):
        self.rect.center = mouse.get_pos()
        
class Button(sprite.Sprite):
    def __init__(self, text, color, size, pos, alignment):
        super().__init__()
        
        font_file = "graphics/Bold.otf"

        self.font = font.Font(None , size)

        self.image = self.font.render(text, True, color)
        if alignment == "topleft": self.rect = self.image.get_rect(topleft = pos)
        if alignment == "center": self.rect = self.image.get_rect(center = pos)
    
    def highlight(self):
        screen = display.get_surface()
        draw.rect(screen, "White", self.rect, 2, 6)

class MainMenu(sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.debugmsg = ""
        
        self.font = font.Font(None, 50)
        self.bg_image = image.load("graphics/main_menu.png").convert_alpha()
        self.bg_image = transform.scale(self.bg_image, (256 * scale, 144 * scale))

        self.button_in_contact = sprite.GroupSingle()
        self.button_spritelist = sprite.Group()
        self.UI_spritelist = sprite.Group()#is drawn in self.draw
        
        self.play_button = Button("Play", "White", int(20 * scale) , (screenx * 0.5, screeny * 0.5), "center")
        self.option_button = Button("Options", "White", int(20 * scale) , (screenx * 0.5, screeny * 0.625), "center")
        self.quit_button = Button("Quit", "White", int(20 * scale) , (screenx * 0.5, screeny * 0.750), "center")
        self.button_spritelist.add(self.play_button)
        self.button_spritelist.add(self.option_button)
        self.button_spritelist.add(self.quit_button)

    def input(self):
        mouse_pos = mouse.get_pos()
        
        for button in self.button_spritelist:
            if button.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                self.button_in_contact.add(button)
            else:
                self.button_in_contact.remove(button)
    
    def draw(self):
        screen = display.get_surface()
        
        screen.blit(self.bg_image, (0,0))
        self.UI_spritelist.draw(screen)
        for button in self.button_in_contact:
            button.highlight()
        
    def update(self):

        for button in self.button_spritelist: self.UI_spritelist.add(button)
        self.input()
        self.draw()

class Pause_Menu(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = Surface((150 * scale, 100 * scale))
        self.rect = self.image.get_rect(center = (screenx/2, screeny/2))

        self.button_spritelist = sprite.Group()
        self.button_in_contact = sprite.GroupSingle()

        self.resume_button = Button("Resume", "White", int(20 * scale), (screenx/2, screeny * 0.375), "center")
        self.options_button = Button("Options", "White", int(20 * scale) , (screenx/2, screeny * 0.5), "center")
        self.exit_to_menu_button = Button("Exit To Menu", "White", int(20 * scale) , (screenx/2, screeny * 0.625), "center")
        self.quit_button = Button("Quit", "White", int(20 * scale) , (screenx/2, screeny * 0.750), "center")
    
        self.button_spritelist.add(self.resume_button)
        self.button_spritelist.add(self.options_button)
        self.button_spritelist.add(self.exit_to_menu_button)
        self.button_spritelist.add(self.quit_button)

    def input(self):
        mouse_pos = mouse.get_pos()

        for button in self.button_spritelist:
            if button.rect.collidepoint((mouse_pos[0], mouse_pos[1])):
                self.button_in_contact.add(button)
            else:
                self.button_in_contact.remove(button)

    def draw(self):
        
        screen = display.get_surface()
        
        self.image.fill("Black")
        screen.blit(self.image, self.rect)
        self.button_spritelist.draw(screen)
        for button in self.button_in_contact: button.highlight()


    def update(self):
        self.input()
        self.draw()