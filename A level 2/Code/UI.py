from pygame import *

from Settings import *
from SpriteSheet import *

import random

#---Debug
def debug(text):
    font_ = font.Font(None, round(10 * scale))
    text = font_.render(text, True, "White")
    rect = text.get_rect(topleft = (0,0))
    
    screen = display.get_surface()
    draw.rect(screen, "Black", rect)
    screen.blit(text, rect)

def draw_text(text, x, y, size: int = 10):
    text = str(text)
    font_ = font.Font(None, round(size * scale))
    text = font_.render(text, True, "Black")
    rect = text.get_rect(center = (x, y))
    
    screen = display.get_surface()
    screen.blit(text, rect)

def draw_image(image, x ,y):
    rect = image.get_rect(center = (x, y))
    screen = display.get_surface()
    screen.blit(image, rect)
      
#---Menus
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
        self.image.set_alpha(150)
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
        
    def draw_buttons(self):
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
        
class MainMenu(Menu):
    def __init__(self) -> None:
        super().__init__()

        self.play_button = Button("Play")
        self.level_select_button = Button("Select Level")
        self.settings_button = Button("Settings")
        self.quit_button = Button("Quit")
        self.buttons.add(self.play_button, self.level_select_button, self.settings_button, self.quit_button)
        
        height = self.calcu_height()
        self.resize(100, height)
        
        x = 5 * scale
        y = 60 * scale
        
        self.rect = self.image.get_rect(topleft = (x, y))
        
        self.align_buttons("center")

class LevelSelectMenu(Menu):
    def __init__(self) -> None:
        super().__init__()
        self.test_level_button = Button("Test Level")

        self.buttons.add(self.test_level_button)
        
        height = self.calcu_height()
        self.resize(100, height)
        
        x = screenx/2
        y = screeny/2
        
        self.rect = self.image.get_rect(center = (x, y))
        
        self.align_buttons("center")
        
class PauseMenu(Menu):
    def __init__(self) -> None:
        super().__init__()
        
        self.resume_button = Button("Resume")
        self.settings_button = Button("Settings")
        self.return_to_menu_button = Button("Return To Menu")
        self.quit_button = Button("Quit")
        self.buttons.add(self.resume_button, self.settings_button, self.return_to_menu_button, self.quit_button)
        
        height = self.calcu_height()
        self.resize(120, height)
        
        x = 0
        y = screeny/2
        
        self.rect = self.image.get_rect(midleft = (x, y))
        
        self.align_buttons("left")
    
class SettingsMenu(Menu):
    def __init__(self) -> None:
        super().__init__()
        pass
    
#---UI
class PlayerUI(sprite.Sprite):
    def __init__(self, player_health) -> None:
        super().__init__()
        
        self.spritesheet = SpriteSheet("UI_spritesheet.png")
        self.book = self.spritesheet.parse_sprite("closed_book")
        self.book_rect = self.book.get_rect(topleft = (0,0))
        
        self.player_health = player_health
        
        self.last_edge = 0
        self.hearts = sprite.Group()
        
        self.calc_hearts()
        
    def calc_hearts(self): #adds appropriate number of hearts to self.hearts
        
        y = self.book_rect.centery
        
        no_of_H = int(self.player_health/2) #number of hearts

        if self.player_health % 2 == 0: #half heart. bool determines
            hh = False
        else:
            hh = True
        
        self.last_edge = round(self.book_rect.right + (3 * scale))
        for num in range(0,no_of_H):
            heart = Heart("full", self.last_edge, y)
            self.hearts.add(heart)
            self.last_edge = round(heart.rect.right + (3 * scale))
            
        if hh:
            heart = Heart("half", self.last_edge, y)
            self.hearts.add(heart)
    
    def remove_half_heart(self):
        last_heart = self.hearts.sprites()[-1]
        if last_heart.type == "half":
            last_heart.kill()
        
        if last_heart.type == "full":
            last_heart.type = "half"
    
    def add_half_heart(self):
        pass
    
    def draw(self):
        screen = display.get_surface()
        
        screen.blit(self.book, self.book_rect) # draws book
        self.hearts.draw(screen)
    
    def update_health(self, player_health): #dont always update, only when UI changes
        
        if self.player_health > player_health:
            diff = self.player_health - player_health
            for num in range(0,diff):
                if self.hearts: self.remove_half_heart()

        if self.player_health < player_health:
            diff = player_health - self.player_health
            for num in range(0, diff):
                self.add_half_heart()
        
        self.player_health = player_health
        
        for heart in self.hearts:
            heart.update()
            
    def update_book(self, player_gun):
        if player_gun:
            self.book = self.spritesheet.parse_sprite("open_book")
        else:
            self.book = self.spritesheet.parse_sprite("closed_book")
            
class Heart(sprite.Sprite):
    def __init__(self, type: str, x, y) -> None:
        super().__init__()
        
        self.value = str(random.randint(1,3))
        self.type = type
        
        self.spritesheet = SpriteSheet("UI_spritesheet.png")
        self.set_type()
        self.image = self.spritesheet.parse_sprite(self.filename)
        self.rect = self.image.get_rect(midleft = (x, y))
    
    def set_type(self):
        if self.type == "full": self.filename = "heart2_" + self.value
        if self.type == "half": self.filename = "heart1_" + self.value
    
    def update(self):
        self.set_type()
        self.image = self.spritesheet.parse_sprite(self.filename)
