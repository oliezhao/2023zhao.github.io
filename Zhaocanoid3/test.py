import pygame
from pygame import *

init()
display.set_caption("Zhaocanoid")
screen = display.set_mode((800,800))
clock = time.Clock()

shape = ['XXXXXXXXXXXXXXX',
         'XXXXXXXXXXXXXXX',
         'XXXXXXXXXXXXXXX',
         'XXXXX     XXXXX',
]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
            exit()
            
    keys = key.get_pressed()
    screen.fill(('Black'))
    
    for row_index, row in enumerate(shape):
        for column_index, column in enumerate(row):
            width = 800/len(row)
            height = 200/len(shape)
            square = Surface((width - 2, height - 2))
            square.fill("White")
            square_rect = square.get_rect(topleft = (column_index * width + 1, row_index * height + 1))
            if column == "X":
                screen.blit(square, square_rect)

    display.update()
    clock.tick(60)