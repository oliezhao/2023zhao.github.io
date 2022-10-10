import pygame

pygame.init()
font = pygame.font.Font(None,30)

def debug(info, position = (200,200)):
    screen = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, 'Red')
    debug_rect = debug_surf.get_rect(topleft = position)
    pygame.draw.rect(screen, 'Black', debug_rect)
    screen.blit(debug_surf, debug_rect)