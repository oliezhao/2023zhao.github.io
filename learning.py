import pygame
from pygame.constants import K_END, K_ESCAPE, K_r

#-- variables
screenx = 700
screeny = 800

pyerpaddelx = screenx/10
pyerpaddely = screeny/100
p_offsetx = 0

ballx = pyerpaddelx/10
bally = ballx
offsetx = 6
offsety = 6
offset = [[1,1],]

k_d = False
k_a = False
Kup = False

points = 0

menu = True
playing = False
death = False

#-- set up
pygame.init()
screen = pygame.display.set_mode((screenx,screeny))
clock = pygame.time.Clock()
pygame.display.set_caption("test")

pixelart_font = pygame.font.Font('fonts/pixelart.TTF',25)

#-- surfaces

ball_surface = pygame.Surface((ballx,bally))
ball_surface.fill('BLUE')
ball_hitbox = ball_surface.get_rect(center = (screenx/2, screeny/2))
ball_list = [ball_surface.get_rect(center = (screenx/2, screeny/2))]
print(len(ball_list))
print(offset)

pyerpaddel_surface = pygame.Surface((pyerpaddelx,pyerpaddely))
pyerpaddel_surface = pygame.transform.rotozoom(pyerpaddel_surface, 0, 1)
pyerpaddel_surface.fill('WHITE')
pyerpaddel_hitbox = pyerpaddel_surface.get_rect(center = (screenx/2,screeny - (screeny/10)))

timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer, 5000)

#--functions--
def gamestate():
    global menu, playing, death
    if menu and keys[pygame.K_s]:
        ball_hitbox.center = [screenx/2,screeny/2]
        menu = False
        playing = True
        death = False
        
    if playing and not(ball_list):
        playing = False
        death = True
        
    if death and keys[K_r]:
        ball_hitbox.center = [screenx/2,screeny/2]
        playing = True
        death = False
        
    if keys[K_ESCAPE]:
        ball_hitbox.center = [screenx/2,screeny/2]
        menu = True
        playing = False
        death = False

def score():
    global points
    if pyerpaddel_hitbox.colliderect(ball_hitbox):
        points += 100
    return str(points)

def moveBall(ball_list):
    if ball_list:
        global ball_hitbox, offsetx, offsety
        for ball in range(len(ball_list)):
            if ball_list[ball].left <= 0 or ball_list[ball].right >= screenx:
                offset[ball][0] *= -1
            if ball_list[ball].top <= 0 or pyerpaddel_hitbox.colliderect(ball_list[ball]):
                offset[ball][1] *= -1
            ball_list[ball].x += offset[ball][0]
            ball_list[ball].y += offset[ball][1]
            screen.blit(ball_surface, ball_list[ball])
                
        ball_list = [ball for ball in ball_list if ball.y < screeny]   
            
        return ball_list
    else: return []
    
def movePaddel():
    global p_offsetx
    if pyerpaddel_hitbox.right > screenx:  
        pyerpaddel_hitbox.right = screenx
        p_offsetx = 0
    else:
        if keys[pygame.K_d]: 
            p_offsetx += 1
        if not(keys[pygame.K_d]) and p_offsetx > 0:
            p_offsetx -= 1
    pyerpaddel_hitbox.x += p_offsetx
    
    if pyerpaddel_hitbox.left < 0:
        pyerpaddel_hitbox.left = 0
        p_offsetx = 0
    else:
        if keys[pygame.K_a]: 
            p_offsetx -= 1
        if not(keys[pygame.K_a]) and p_offsetx < 0:
            p_offsetx += 1

def text(text, x, y):
    global text_surface, text_hb
    text_surface = pixelart_font.render(text , False , 'WHITE')
    text_hb = text_surface.get_rect(topleft = (x, y))
        
#--main loop--
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == timer:
            ball_list.append(ball_surface.get_rect(center = (screenx/2, screeny/2)))
            offset.append([1,1])
            print(len(ball_list))
            print(offset)
    
    keys = pygame.key.get_pressed()
    mpos = pygame.mouse.get_pos()
    
    gamestate()
    
    if menu:
        screen.fill('Blue')
        text('Menu', screenx/2, screeny/2)
        screen.blit(text_surface, text_hb)
    if playing:
        text(score(), 10, 10)
        screen.fill("black")
        screen.blit(pyerpaddel_surface, pyerpaddel_hitbox)    
        screen.blit(text_surface, text_hb)
        movePaddel()
        ball_list = moveBall(ball_list)
    if death:
        text("gameover", screenx/2, screeny/2)
        screen.fill('Red')
        text_hb.center = [screenx/2, screeny/2]
        screen.blit(text_surface, text_hb)
    
    pygame.display.update()
    clock.tick(60)