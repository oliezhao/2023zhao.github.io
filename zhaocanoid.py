import pygame
from pygame import *

screenx = 600
screeny = 800

pyrspdlmt = 15
balspdlmt = 5

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = Surface((80,10))
        self.color = self.image.fill('White')
        self.rect = self.image.get_rect(midtop = (screenx/2, screeny * 4/5))
        self.offset = 0
    
    def input(self):
        keys = pygame.key.get_pressed()
        
        if self.rect.right < screenx:
            if keys[K_d]: 
                self.offset += 1
            if not(keys[K_d]) and self.offset > 0: 
                self.offset -= 1
            if self.offset > pyrspdlmt: 
                self.offset = pyrspdlmt
        elif self.offset > 0:
            self.offset *= -1

        if self.rect.left > 0:
            if keys[K_a]: 
                self.offset -= 1
            if not(keys[K_a]) and self.offset < 0: 
                self.offset += 1
            if self.offset < -pyrspdlmt: 
                self.offset = -pyrspdlmt
        elif self.offset < 0:
            self.offset *= -1

    def move(self):
        self.rect.x += self.offset
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screenx:
            self.rect.right = screenx
            
    def update(self):
        self.input()
        self.move()

    def variables(self):
        return self.rect
    
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = Surface((10,10))
        self.colour = self.image.fill('Blue')
        self.rect = self.image.get_rect(center = (screenx/2, screeny/2))
        self.offsetx = 5
        self.offsety = 5
        
    def bounce(self):
        if not(self.rect.left > 0 and self.rect.right < screenx):
            self.offsetx *= -1
        if not(self.rect.top > 0):
            self.offsety *= -1
        print("bounce")
    
    def move(self):
        self.rect.x += self.offsetx
        self.rect.y += self.offsety
    
    def deload(self):
        if self.rect.bottom >= screeny:
            self.kill()
        
    def update(self):
        self.move()
        self.deload()
        
class Block(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = Surface(())
        self.rect = self.image.get_rect(topleft = (0,0))
        self.health = 4
    
def collision():
    ball_collision_list = pygame.sprite.spritecollide[player.sprite, balls, False, False]
    for ball in ball_collision_list:
        ball.bounce()

init()
screen = display.set_mode((screenx, screeny))
display.set_caption('Arkanoid')
clock = time.Clock()

text_font = pygame.font.Font('fonts/pixelart.ttf', 50)

player = pygame.sprite.GroupSingle()
player.add(Player())

balls = pygame.sprite.Group()
balls.add(Ball())

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_TAB:
                balls.add(Ball())
    
    keys = pygame.key.get_pressed()
    mpos = pygame.mouse.get_pos
    
    player.update()
    balls.update()

    screen.fill('Black')
    player.draw(screen)
    balls.draw(screen)
    
    display.update()
    clock.tick(60)