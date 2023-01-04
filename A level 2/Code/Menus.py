import pygame

from pygame import *
from UI import *

class Menu(sprite.Sprite): #Creates a menu for
    def __init__(self, w, h) -> None:
        super().__init__()
        
        self.image = Surface(( round(w * scale), round(h * scale))) # Creates a rectangle Surface to act as menu Surface
        self.image.set_alpha(200) #Lowers Opacity
        self.rect = self.image.get_rect(topleft = (0,0)) #Inital value at top left. Position change after declaration

        self.buttons = sprite.Group()
        
        self.button_in_contact = sprite.GroupSingle()
    
    def update(self):
        mouse_pos = mouse.get_pos()
        
        for button in self.buttons:
            if button.rect.collidepoint(mouse_pos):
                self.button_in_contact.add(button)
            else:
                self.button_in_contact.remove(button)
    
# class Main_Menu(sprite.Sprite):
#     def __init__(self) -> None:
#         super().__init__()
        
#         self.debug_msg = ""
        
#         #Background
#         self.image = image.load("graphics/menus/main_menu_background.png").convert_alpha() #Sets background image
#         self.image = transform.scale(self.image, (256 * scale, 144 * scale)) #Sets background image to size of window
#         self.rect = self.image.get_rect(topleft = (0,0)) #Sets background position
        
#         #Menu
#         self.menu = Menu(100, 80) #Spawn a menu 100x100 pixel wide (scaled).
#         self.menu.rect.x += (10 * scale) #Creates a gap between edge of screen and menu
#         self.menu.rect.centery = self.rect.centery + (25 * scale) #Initally at topleft corner, moves it to the left center of window
#             #Menu's Buttons
#         self.play_button = Button("Play", 20)
#         self.play_button.rect.top = self.menu.rect.top + (5 * scale)
        
#         self.options_button = Button("Options", 20)
#         self.options_button.rect.top = self.play_button.rect.bottom + (5*scale)
        
#         self.quit_button = Button("Quit", 20)
#         self.quit_button.rect.top = self.options_button.rect.bottom + (5*scale)
        
#         self.menu.buttons.add(self.play_button, self.options_button, self.quit_button) #Add Menu's Buttons to SG (menu buttons SpriteGroup declared in Menu class of UI.py)
        
#         #Aligns all buttons in menu SG to center
#         for button in self.menu.buttons:
#             button.rect.centerx = self.menu.rect.centerx
        
#     def draw(self):
#         screen = display.get_surface() #Gets screen as window surface
#         mouse_pos = mouse.get_pos() #Gets mouse position for: highlighting buttons.
        
#         #Draw Order
#         #Background
#         #Menus
#         #Buttons
#         #Button Highlights
        
#         screen.blit(self.image, self.rect) #Draws Background... Draws Main_Menu.image into window surface. Main_Menu.rect.topleft should always be (0,0)
#         screen.blit(self.menu.image, self.menu.rect)
#         #self.menus_SG.draw(screen) #Draws Menus.. Draws Spritegroup, menus added into SG in def __init
        

#         self.menu.buttons.draw(screen)
    
#         for button in self.menu.button_in_contact: #Highlights all Buttons
#             button.highlight()
                
#     def update(self):
#         buttons = mouse.get_pressed()
        
#         self.menu.update()
        
#         if self.menu.button_in_contact:
#             if buttons[0]:
#                 self.menu.button_in_contact.sprite.clicked = True
#             else:
#                 self.menu.button_in_contact.sprite.clicked = False
            
        self.draw()

class Option_Menu(sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        screen = display.get_surface()
        
        self.menu = Menu(150, 100)
        self.menu.rect.center = screen.get_rect().center
        
        self.resume_button = Button("Resume", 20)
        self.resume_button.rect.top = self.menu.rect.top + (5 * scale)
        
        self.resolution_button = Button("Resolution", 20)
        self.resolution_button.rect.top = self.resume_button.rect.bottom + (5 * scale)
        
        self.return_to_main_menu_botton = Button("Return To Main Menu", 20)
        self.return_to_main_menu_botton.rect.top = self.resolution_button.rect.bottom + (5 * scale)
        
        self.quit_button = Button("Quit", 20)
        self.quit_button.rect.top = self.return_to_main_menu_botton.rect.bottom + (5 * scale)
        
        self.menu.buttons.add(self.resume_button, self.resolution_button, self.return_to_main_menu_botton, self.quit_button)
        
        for button in self.menu.buttons:
            button.rect.centerx = self.menu.rect.centerx
        
    def draw(self):
        screen = display.get_surface()
        
        screen.blit(self.menu.image, self.menu.rect)
        self.menu.buttons.draw(screen)
        
        for button in self.menu.button_in_contact:
            button.highlight()
        
    def update(self):
        buttons = mouse.get_pressed()
        
        self.menu.update()
        
        if self.menu.button_in_contact:
            if buttons[0]:
                self.menu.button_in_contact.sprite.clicked = True
            else:
                self.menu.button_in_contact.sprite.clicked = False
                
        self.draw()
