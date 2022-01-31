from pygame import *
import pygame

init()
font_ = pygame.font.Font(None,30)

def debug(info):
    display_surface = display.get_surface()
    debug_surf = font_.render(str(info), True, "WHITE")
    debug_rect = debug_surf.get_rect(topleft = (10,10))
    draw.rect(display_surface, "BLACK", debug_rect)
    display_surface.blit(debug_surf, debug_rect)