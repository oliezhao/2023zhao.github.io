from pygame import *

from SpriteSheet import *
from Bullets import *


class Gun(sprite.Sprite):
    def __init__(self, gun: str, bullet_speed: int = 10, bullet_lifespan: int = 100, cooldown: int = 10, damage: int = 1, magazine_cap: int = 10, reload_time: int = 10, x = -100, y = -100) -> None:
        super().__init__()
        
        self.clock = 0
        
        self.image_cont = SpriteSheet("gun_spritesheet.png").parse_sprite(gun)
        self.hitbox = self.image_cont.get_rect(center = (x ,y))
        self.image = self.image_cont
        self.rect = self.image.get_rect(center = (x, y))
        self.angle = 0
        
        self.highlight = False

        self.bullet_lifetime = bullet_lifespan
        self.bullets = sprite.Group()
        self.bullet_speed = bullet_speed
        
        self.cooldown = cooldown
        self.last_shot = -cooldown
        
        self.clip = magazine_cap
        self.ammo = 100
        self.magazine_cap = magazine_cap
        self.reloading = False
        self.reload_time = reload_time
        self.reload_timer = -reload_time
        
        self.damage = damage
    
    def reload(self):
        if self.clock - self.reload_timer > self.reload_time:
            self.reloading = False
            mixer.music.pause()
            mixer.music.load("Sound\gun_reloaded.wav")
            mixer.music.play()
            diff = self.magazine_cap - self.clip
            if diff > self.ammo: diff = self.ammo
            self.clip += diff
            self.ammo -= diff
        if self.ammo <= 0:
            self.reloading = False
        
    def shoot(self, id, angle, center):
        if self.clock - self.last_shot >= self.cooldown and not(self.reloading):
            if self.clip == 0:
                mixer.music.load('Sound\gun_empty.wav')
                mixer.music.play()
                self.reloading = True
                self.reload_timer = self.clock
            else:
                self.clip -= 1
                self.last_shot = self.clock
                bullet = Bullet(id, self.bullet_speed, angle, self.bullet_lifetime, self.damage)
                bullet.spawn(center[0], center[1])
                self.bullets.add(bullet)
            
    def recoil(self):
        pass
        
    def rotate(self, angle):
        self.image= self.image_cont
        self.angle = angle
        
        if self.angle > 90 or self.angle < -90:
            self.image = transform.flip(self.image, False, True)
        
        self.image = transform.rotate(self.image, self.angle).convert_alpha()
    
    def draw(self):
        screen = display.get_surface()
        screen.blit(self.image, self.rect)
        if self.highlight == True:
            draw.rect(screen, "Blue", self.rect, 2)
    
    def update(self):
        if self.reloading and self.ammo != 0:
            self.reload()
        
        self.clock += 1

class Five_Pointer(Gun):
    def __init__(self, gun: str = "pistol", bullet_speed: int = 10, bullet_lifespan: int = 75, cooldown: int = 15, damage: int = 1, magazine_cap: int = 5, reload_time: int = 20) -> None:
        super().__init__(gun , bullet_speed, bullet_lifespan, cooldown, damage, magazine_cap, reload_time)

        self.id = 1
        self.type = "SemiAuto"
        
class Rubber_Repeater(Gun):
    def __init__(self, gun: str = "assult_rifle", bullet_speed: int = 10, bullet_lifespan: int = 100, cooldown: int = 10, damage: int = 1, magazine_cap: int = 10, reload_time: int = 10, x=0, y=0) -> None:
        super().__init__(gun, bullet_speed, bullet_lifespan, cooldown, damage, magazine_cap, reload_time, x, y)
        
        self.id = 2
        self.type = "Auto"
        
