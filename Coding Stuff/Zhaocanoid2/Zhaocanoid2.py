import pygame, sys
from pygame import *
from player import Player
import block

class Game:
    def __init__(self):
        
        self.x = screenx
        self.y = screeny
        
        self.player = Player(screenx, screeny)
        self.player_spritelist = sprite.GroupSingle()
        self.player_spritelist.add(self.player)
        
        self.blocks = sprite.Group()
        self.createBlocks()
        
    def createBlocks(self):
        print(screeny/10, screenx/10)
        for row in range(1, int(screeny/2), int(screeny/20)):
            for col in range(1, int(screenx), int(screenx/10)):
                print(row, col)
                square = block.Block(screenx/10 - 2, screeny/20 - 2, col, row)
                self.blocks.add(square)
        
    def run(self):
        
        self.player.update()
        self.player_spritelist.draw(screen)
        self.player.laser_spritelist.draw(screen)
        self.blocks.draw(screen)
     
class Ball(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = Surface((screenx/60, screenx/60))
        self.image.fill("Blue")
        self.rect = self.image.get_rect(midbottom = (game.player.rect.midtop))
        self.spdlmt = 10
        self.velox = 0
        self.veloy = self.spdlmt
        
        self.sound = mixer.Sound('sounds/jumpsound.mp3')
    
    def calc(self):
        player_width = game.player.rect.right - game.player.rect.left
        midpoint = player_width/2
        collision_point = self.rect.midbottom[0] - game.player.rect.left
        if collision_point <= 0: 
            self.velox = -abs(self.spdlmt)
        elif collision_point >= player_width:
            self.velox = abs(self.spdlmt)  
        else:  
            if collision_point < midpoint:
                self.velox = self.spdlmt * (1 - (collision_point/midpoint))
                self.velox = -abs(self.velox)
            elif collision_point > midpoint:
                self.velox = self.spdlmt * (1 - (collision_point/midpoint))
                self.velox = abs(self.velox)
        
        self.veloy = -(self.spdlmt**2 - self.velox**2)**(1/2)
        
    def check(self):
        if self.rect.left < 0:
            self.velox = abs(self.velox)
        if self.rect.right > screenx:
            self.velox = -abs(self.velox)
            
        if self.rect.top < 0:
            self.veloy = abs(self.veloy)
        
        if self.rect.colliderect(game.player.rect):
            if self.rect.bottom >= game.player.rect.top:
                self.rect.bottom = game.player.rect.top + 1
                self.sound.play()
                self.calc()
                self.veloy = -abs(self.veloy)

    def move(self):
        self.check()
        self.rect.x += self.velox
        self.rect.y += self.veloy
        
    def update(self):
        self.move()

if __name__ == '__main__':
    screenx = 600
    screeny = int((4/3) * screenx) 

    init()
    screen = display.set_mode((screenx, screeny))
    display.set_caption("Zhaocanoid")
    clock = time.Clock()

    game = Game()
    
    ball_spritelist = sprite.Group()
    ball_spritelist.add(Ball())
        
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_TAB:
                    ball_spritelist.add(Ball())
                    print(game.player.laser_spritelist)

        keys = key.get_pressed()
        mpos = mouse.get_pos()

        ball_spritelist.update()
        
        screen.fill((20,20,30))
        game.run()
        ball_spritelist.draw(screen)

        display.update()
        clock.tick(60)