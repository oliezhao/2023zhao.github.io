from pygame import *

from Settings import *

class Button(sprite.Sprite):
    def __init__(self, text: str) -> None:
        super().__init__()
        
        self.font = font.Font(None, round(20 * scale))
        self.image = self.font.render(text, True, "white")
        self.rect = self.image.get_rect(topleft = (0,0))
        self.clicked = False
        
    def highlight(self):
        
        screen = display.get_surface()
        draw.rect(screen, "white", self.rect, 2)
        
class Menu(sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
    
        self.image = Surface((1, 1))
        self.image.set_alpha(200)
        self.rect = self.image.get_rect(topleft = (0, 0))

        self.buttons = sprite.Group()
        self.button_in_contact = sprite.GroupSingle()
    
    def calcu_height(self):
        height = 5 * scale
        for button in self.buttons:
            button.rect.top = height
            height = button.rect.bottom + (5 * scale)
       
        return height
    
    def resize(self, w, h):
        w = w * scale
        h = h
        self.image = transform.scale(self.image, (w, h))
    
    def align_buttons(self, alignment: str):
        
        last_edge = self.rect.top
        
        for button in self.buttons:
            if alignment == "center":
                button.rect.centerx = self.rect.centerx
            if alignment == "left":
                button.rect.x = self.rect.x + (5 * scale)

            button.rect.top = last_edge + 5 * scale
            last_edge = button.rect.bottom
        
    def draw(self):
        screen = display.get_surface()
        
        screen.blit(self.image, self.rect)
        self.buttons.draw(screen)
        for button in self.button_in_contact:
            self.button_in_contact.sprite.highlight()
    
    def update(self):       
        mouse_pos = mouse.get_pos()
        mouse_buttons = mouse.get_pressed()
        
        for button in self.buttons:
            if button.rect.collidepoint(mouse_pos):
                self.button_in_contact.add(button)
            else:
                self.button_in_contact.remove(button)

        if self.button_in_contact:
            if mouse_buttons[0]:
                self.button_in_contact.sprite.clicked = True
            else:
                self.button_in_contact.sprite.clicked = False
        
class MainMenu(Menu):
    def __init__(self) -> None:
        super().__init__()

        self.play_button = Button("Play")
        self.settings_button = Button("Settings")
        self.quit_button = Button("Quit")
        self.buttons.add(self.play_button, self.settings_button, self.quit_button)
        
        height = self.calcu_height()
        self.resize(100, height)
        
        x = 5 * scale
        y = 70 * scale
        
        self.rect = self.image.get_rect(topleft = (x, y))
        
        self.align_buttons("center")
        
class PauseMenu(Menu):
    def __init__(self) -> None:
        super().__init__()
        
        self.resume_button = Button("Resume")
        self.settings_button = Button("Settings")
        self.return_to_menu_button = ("Return To Menu")
        self.quit_button = ("Quit")
        self.buttons.add(self.resume_button, self.settings_button, self.quit_button)
        
        height = self.calcu_height()
        self.resize(height, height)
        
        x = screenx/2
        y = screeny/2
        
        self.rect = self.image.get_rect(center = (x, y))
        
        self.align_buttons("center")

    def update(self):
        pass
    
class SettingsMenu(Menu):
    def __init__(self) -> None:
        super().__init__()
        
        
        
        