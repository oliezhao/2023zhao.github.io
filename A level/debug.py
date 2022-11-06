from pygame import *
import pygame

init()
font_ = pygame.font.Font(None, 30)

def debug(surface, text, pos):
    debug_text = font_.render(str(text), True, "White")
    debug_rect = debug_text.get_rect(topleft = pos)
    
    draw.rect(surface, "Black", debug_rect)
    surface.blit(debug_text, debug_rect)
