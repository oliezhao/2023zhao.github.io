import pygame
from pygame import *
import player
import ball

class Game:
    def __init__(self):
        super().__init__()
        
        #-- Player
        self.player = player.Player(windowsize, 'White', 15)
        self.player_spritegroup = sprite.GroupSingle(self.player)
        
        #-- Ball
        self.ball = ball.Ball(windowsize, 'Blue', self.player.rect.midtop, 5)
        self.ball_spritegroup = sprite.Group()
        self.ball_spritegroup.add(self.ball)
        print(self.ball.rect.midbottom, self.player.rect.midtop)
    
    def addBall(self):
        self.ball = ball.Ball(windowsize, 'Blue', self.player.rect.midtop, 5)
        self.ball_spritegroup.add(self.ball)
    
    def ball_HITS_player(self):
        if self.ball.rect.colliderect(self.player.rect):
            
            #-- setting ball a bit below player so collision is detected again if ball.spdy = 0
            self.ball.rect.bottom = self.player.rect.top + 1
            
            #-- variables
            player_midpoint = self.player.width/2
            collsion_point = self.ball.rect.midbottom[0] - self.player.rect.left
            
            #if ball hits player on the edge ball.spdx is max and ball.spy = 0
            if collsion_point < 0:
                self.ball.spdx = -self.ball.spd
            elif collsion_point > self.player.width:
                self.ball.spdx = self.ball.spd
            #ball.spdx = ball.spd * ratio "distance from midpoint:midpoint" - player.velocity  *did sm werid math thing so if its above midpoint ball.spdx is postitive and vice versa
            else:
                self.ball.spdx = self.ball.spd * ((collsion_point/player_midpoint) - 1) - self.player.velocity/2
            #-- ball.spdy must be negative, use trignomitry to keep ball.spd constant
            self.ball.spdy = -abs((self.ball.spd**2 - self.ball.spdx**2)**(1/2))
            
            print(self.ball.spd, self.ball.spdx, self.ball.spdy)
            
        self.ball.move()

        
    def run(self):
        #-- updates
        self.player.update()
        for self.ball in self.ball_spritegroup:
            self.ball.update()
            self.ball_HITS_player()
        
        #-- draws
        self.ball_spritegroup.draw(screen)
        self.player_spritegroup.draw(screen)

if __name__ == "__main__":

    windowsize = [600,800]
    background_color = (20,20,30)


    init()
    display.set_caption("Zhaocanoid")
    screen = display.set_mode(windowsize)
    clock = time.Clock()

    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_TAB:
                    game.addBall()
                
        keys = key.get_pressed()
        
        if keys[K_TAB]:
            game.addBall()
        
        screen.fill((background_color))
        game.run()

        display.update()
        clock.tick(60)