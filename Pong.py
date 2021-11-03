import pygame
import random

CD = True

#colours
BLACK = (0,0,0)
WHITE = (255,255,255)

#define
src_x = 1000
src_y = 800
src_size = (src_x, src_y)

b_x = 10
b_y = 10
bpx = (src_x - b_x)/2
bpy = (src_y - b_y)/2
bpx_ofset = -9
bpy_ofset = -2

p_x = 10
p_y = 100
ppy1 = (src_y - p_y)/2
ppy2 = (src_y - p_y)/2

screen = pygame.display.set_mode(src_size)
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
done = False
pygame.init()


#functions
def maths():
    #coords for centre of the ball
    global bcy
    global bcx
    #coords for centre of paddel
    global pcy1
    global pcy2

    pcy1 = ppy1 + (p_y/2)
    pcy2 = ppy2 + (p_y/2)

def display():
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, [0, ppy1, p_x, p_y])
    pygame.draw.rect(screen, WHITE, [src_x - p_x, ppy2, p_x, p_y])
    pygame.draw.rect(screen, WHITE, [bpx,bpy,b_x,b_y])

def moveBall():
    global bpx
    global bpy
    global bpx_ofset
    global bpy_ofset
    if (bpx <= border) or (bpx >= src_x - p_x - border):
        bpx_ofset = -bpx_ofset
    bpx += bpx_ofset

    if bpy <= 0 or bpy >= src_y - b_y:
        bpy_ofset = -bpy_ofset
    bpy += bpy_ofset

def ColliDect():
    global CD
    if bpx <= p_x:
        if (bpy > ppy1 - b_y) and (bpy < ppy1 + b_y):
            print("in1")
            CD = True
        else:
            print("out1")
            CD = False
    elif bpx >= src_x - p_x - b_x:
        if (bpy > ppy2 - b_y) and (bpy < ppy2 + b_y):
            print("in2")
            CD = True
        else:
            print("out2")
            CD = False

def playerMouseControll():
    global ppy1
    mousepos = pygame.mouse.get_pos()
    mpy = mousepos[1]
    #print(mpy)
    if mpy < src_y - p_y:
        ppy1 = int(mpy)
    else:
        ppy1 = src_y - p_y

#def AI():


##main code
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    

    ColliDect()

    #margin of ball bounce (x-axis)
    if CD == True:
        border = b_x
    elif CD == False:
        border = 0
 

    playerMouseControll()
    moveBall()
    display()

    pygame.display.flip()
    clock.tick(60)

pygame.quit
