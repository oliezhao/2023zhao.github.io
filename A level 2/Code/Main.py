
from pygame import *

from Settings import *

from Entities import *
from Gun import *
from Menus import *
from UI import *
from Map import *

import copy

class Game:
    def __init__(self) -> None:
        super().__init__()
        pygame.init()
        
    #initialises display and clock
        display.set_caption("A Levels")
        self.screen = display.set_mode(resolution, RESIZABLE)
        self.clock = time.Clock()
        mouse.set_visible(False)
        
    #---Attributes
        self.show_debug = False #toggles debug menu on/off
        self.pause = False #used to stop updating game
    
        #--title Screen
        self.gamestate = "title_screen" #used to change gamestates
        
        self.main_bg = image.load("Graphics\menus\main_menu_background.png").convert_alpha() #title_screen background (name wrong atm, change later maybe)
        self.main_bg = transform.scale(self.main_bg, (screenx, screeny)) #scales the screen to size of window
        self.main_bg_rect = self.main_bg.get_rect(topleft = (0,0))
        
        #--game
        self.cursor_image = image.load("Graphics\sprites\cursor.png").convert_alpha() #cursor image
        self.cursor_image = transform.scale(self.cursor_image, (5 * scale, 5* scale))
        self.cursor_rect = self.cursor_image.get_rect(topleft = (0,0)) #at topleft of screen initally, moved before display
        
        self.killcount = 0
        
        self.enemies = sprite.Group()
        
        #--menus
        self.main_menu = MainMenu() #title_screens has a "main_menu"
        self.level_select_menu = LevelSelectMenu()
        self.pause_menu = PauseMenu()
        
        
        self.menu = sprite.GroupSingle(self.main_menu)
        self.menus = sprite.Group(self.main_menu)
        
        #--guns
        self.guns = sprite.Group() #only guns on map / not ones held by player
        
        #--bullets
        self.player_bullets = sprite.Group()
        self.enemy_bullets = sprite.Group()
        self.bullets = sprite.Group()
        
        self.current_map = Map()
        
        self.non_player_spritegroups = [self.enemies, self.bullets, self.guns, self.current_map.tiles]

        
    def unclick(self, menu):
        for button in menu.buttons:
            button.clicked = False

    def run(self): #methods  
        while True:
            keys = key.get_pressed()
            mouse_pos = mouse.get_pos()
            buttons = mouse.get_pressed()
            
            for e in event.get(): #events
                if e.type == QUIT: #Escape Closes game
                    quit()
                    exit()
                
                if 1 == 1: #universal inputs
                    if self.menu:
                        if self.menu.sprite.button_in_contact:
                            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                                self.menu.sprite.button_in_contact.sprite.clicked = True
                    
                    if e.type == KEYDOWN and e.key == K_BACKQUOTE: #debug menu is universal, debug message changes per gamestate
                        if self.show_debug: #toggles debug
                            self.show_debug = False
                        else:
                            self.show_debug = True
                
                if self.gamestate == "game": #game inputs
                    if e.type == KEYDOWN and e.key == K_ESCAPE: #pause menu
                        self.pause = True
                        self.menus.add(self.pause_menu)
                        self.menu.add(self.pause_menu)
                    
                    #map guns
                    if self.guns:
                        for gun in self.guns:
                            if sprite.collide_rect(self.player, gun): #gun pickup
                                gun.highlight = True
                                if e.type == KEYDOWN and e.key == K_e:
                                    self.guns.remove(gun)
                                    for player_gun in self.player.guns:
                                        if gun.id == player_gun.id:
                                            print("yep")
                                            player_gun.ammo += 10
                                        else:
                                            print("nope")
                                            self.player.pickup_gun(gun)
                            else:
                                gun.highlight = False
                    
                    #player gun
                    if self.player.gun:
                        for gun in self.player.gun:
                            if e.type == KEYDOWN:
                                if e.key == K_x:
                                    self.guns.add(self.player.drop_weapon())
                                if e.key == K_r:
                                    gun.reloading = True
                                    gun.reload_timer = gun.clock
                                
                            #onetap shooting
                            if "rolling" not in self.player.statuses:
                                if gun.type == "SemiAuto":
                                    if e.type == MOUSEBUTTONDOWN and e.button == 1:
                                        self.player.shoot()
                                if gun.type == "Shotgun":
                                    pass
                
                if self.gamestate == "level_select": #level selevt inputs
                    if e.type == KEYDOWN and e.key == K_ESCAPE:
                        self.gamestate = "title_screen"
                        self.menus.remove(self.level_select_menu)
                        self.menus.add(self.main_menu)
                        self.menu.add(self.main_menu)
                    
            if self.gamestate == "title_screen": #---Title Screen
                
                if 1 == 1: #--draw
                    self.screen.blit(self.main_bg, self.main_bg_rect)
                
                if 1 == 1: #--main menu buttons
                    if self.main_menu.play_button.clicked: #change gamestate so effects only happen once (prevents multiple instances of Objects being created)
                        
                        self.gamestate = "game"
                        self.menus.remove(self.main_menu)
                        self.menu.empty()
                        
                        self.player = Player(screenx/2, screeny/2)
                        self.enemy_1 = Enemy(screenx/2, screeny/2, Five_Pointer(reload_time = 50, cooldown = 30))
                        self.enemies.add(self.enemy_1)
                        
                        self.player.guns.add(Five_Pointer())

                        self.player.guns.add(Rubber_Repeater())
                        
                        self.guns.add()

                        self.player_UI = PlayerUI(self.player.health)
                    
                    if self.main_menu.level_select_button.clicked:
                        self.gamestate = "level_select"
                        
                        self.menus.remove(self.main_menu)
                        self.menus.add(self.level_select_menu)
                        self.menu.add(self.level_select_menu)
                        
                    if self.main_menu.settings_button.clicked:
                        pass

                    if self.main_menu.quit_button.clicked:
                        quit()
                        exit()
                
                if 1 == 1: #--debug message
                    string = str(self.cursor_rect.center) + ", " + str(mouse_pos)
                    if self.show_debug: debug(string)
            
            if self.gamestate == "level_select": #Level select
                self.screen.fill("#D38DD5")

            if self.level_select_menu.test_level_button.clicked:
                self.menus.remove(self.level_select_menu)
                self.menu.empty()
                self.current_map = Map()
                self.gamestate == "game"
                
            if self.gamestate == "game": #---Game
                
                if not(self.pause): #--Updates
                    
                    if 1 == 1:#Player update
                        self.player.update() #updates mouse position
                        self.player.gun.update() #updates current held gun
                        
                        if self.player.gun: 
                            self.player_bullets.add(self.player.gun.sprite.bullets)
                             
                        self.bullets.add(self.player_bullets)
                    
                    if 1 == 1:#Enemy update
                        for enemy in self.enemies:
                            enemy.update(self.player.hitbox.center)
                            enemy.gun.update()
                            if enemy.gun:
                                self.enemy_bullets.add(enemy.gun.sprite.bullets)
                        self.bullets.add(self.enemy_bullets)
                    
                    if 1 == 1:#Bullet update
                        self.bullets.update()
                        
                        for enemy in self.enemies:
                            bullet_hit = sprite.spritecollide(enemy, self.player_bullets, False)
                            for bullet in bullet_hit:
                                enemy.hurt(bullet.damage)
                                bullet.kill()
                            if enemy.health <= 0:
                                self.guns.add(enemy.drop_weapon())
                                enemy.kill()
                                self.killcount += 1
                                
                        bullet_hit = sprite.spritecollide(self.player, self.enemy_bullets, False)
                        for bullet in bullet_hit:
                            if "nodmg" not in self.player.statuses: 
                                self.player.hurt(bullet.damage)
                                bullet.kill()
                        
                    if 1 == 1:#Other update
                        self.player_UI.update_health(self.player.health)
                        self.player_UI.update_book(self.player.gun)
                    
                    # for spritegroup in self.non_player_spritegroups:
                    #     for sprite in spritegroup:
                    #         sprite.rect.x -= round(self.player.speed * self.player.move_direction)
                    #         sprite.rect.y += round(self.player.speed * self.player.move_direction)
                            
                if 1 == 1: #--Draws
                    self.screen.fill("Black")
                    
                    self.current_map.tiles.draw(self.screen) #map draw
                    
                    #player draw
                    if 1 == 1:
                        if self.player.facedirection == "N" or self.player.facedirection == "NW" or self.player.facedirection == "SW": #conditional draw order: if player is facing these directions, draw gun b4 player. Else, draw in reverse order
                            self.player.draw_gun()
                            self.screen.blit(self.player.image, self.player.rect)
                        else:
                            self.screen.blit(self.player.image, self.player.rect)
                            self.player.draw_gun()
                    
                    #enemy draw
                    for enemy in self.enemies: 
                        enemy.draw()
                        enemy.draw_gun()
                    
                    #gun draw
                    for gun in self.guns:
                        gun.draw()
                    
                    #bullets draw
                    if 1 == 1:
                        self.bullets.draw(self.screen)

                    #UI draw
                    if 1 == 1:
                        for enemy in self.enemies:
                            draw_text(enemy.health, enemy.hitbox.centerx, enemy.hitbox.top - scale)
                        
                        draw_text(self.player.health, self.player.hitbox.centerx , self.player.hitbox.top - scale)
                        
                        self.player_UI.draw()#draw UI goes here
                        
                        if self.player.gun: 
                            draw_image(transform.rotate(self.player.gun.sprite.image_cont, 90), 23 * scale, 13 * scale)
                            draw_text(self.player.gun.sprite.clip, 10 * scale, 13 * scale)
                            draw_text(self.player.gun.sprite.ammo, 13 * scale, 17 * scale, size = 5)
                        
                    #Hitboxes draw
                    if 0 == 1:
                        draw.rect(self.screen, "Green", self.player.hitbox, 2)
                        if self.player.gun: draw.rect(self.screen, "Blue", self.player.gun.sprite.rect, 2)
                        for enemy in self.enemies: draw.rect(self.screen, "Red", enemy.hitbox, 2)
                        for gun in self.guns: draw.rect(self.screen, "Blue", gun.rect, 2)
                        for bullet in self.bullets: draw.rect(self.screen, "Purple", bullet.rect, 2)

                if self.pause: #--pause menu
                    #-pause menu buttons
                    if self.pause_menu.resume_button.clicked:
                        self.pause = False
                        
                        self.menus.remove(self.pause_menu)
                        self.menu.empty()
                        
                    if self.pause_menu.return_to_menu_button.clicked:
                        self.pause = False
                        self.gamestate = "title_screen"
                        
                        self.player.kill() #move this into map.despawn method
                        for gun in self.player.guns:
                            gun.kill()
                        for gun in self.guns:
                            gun.kill()
                        for enemy in self.enemies:
                            enemy.kill()
                        for bullet in self.bullets:
                            bullet.kill()
                        
                        self.menus.remove(self.pause_menu)
                        self.menus.add(self.main_menu)
                        self.menu.add(self.main_menu)

                    if self.pause_menu.quit_button.clicked:
                        quit()
                        exit()
                  
                #--debug
                string = self.enemy_1.debug_msg
                if self.show_debug: debug(string)
            
            if self.menus: #---Menu Handler
                menu = self.menu.sprite
                
                if self.menu:
                    menu.update()
                                
                self.menus.draw(self.screen)
                for menu in self.menus:
                    menu.draw_buttons()
            
            self.unclick(self.main_menu)
            self.unclick(self.pause_menu)
            self.unclick(self.level_select_menu)
            
            #---Cursor
            if 0 == 0:
                self.cursor_rect = self.cursor_image.get_rect(center = mouse_pos)
                self.screen.blit(self.cursor_image, self.cursor_rect)
            
            display.update()
            self.clock.tick(60)
            
if __name__ == "__main__":
    game = Game()
    game.run()