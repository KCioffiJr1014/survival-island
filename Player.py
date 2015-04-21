import pygame, sys, math
from PistolBullet import PistolBullet
from UziBullet import UziBullet
from ShotgunBullet import ShotgunBullet
from Crosshair import Crosshair
from Health import HealthBar

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, size = [100,100]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        
        self.pistolImages = [pygame.image.load("images/player/ppist.PNG"),
                        pygame.image.load("images/player/ppist2.PNG"),
                        pygame.image.load("images/player/ppist3.PNG"),
                        pygame.image.load("images/player/ppist2.PNG"),
                        pygame.image.load("images/player/ppist.PNG"),
                        pygame.image.load("images/player/ppist4.PNG"),
                        pygame.image.load("images/player/ppist5.PNG"),
                        pygame.image.load("images/player/ppist4.PNG")]
        self.shotgunImages = [pygame.image.load("images/player/pshot.PNG")]
        self.uziImages =   [pygame.image.load("images/player/puzi.PNG"),
                            pygame.image.load("images/player/puzi2.PNG"),
                            pygame.image.load("images/player/puzi3.PNG"),
                            pygame.image.load("images/player/puzi2.PNG"),
                            pygame.image.load("images/player/puzi.PNG"),
                            pygame.image.load("images/player/puzi4.PNG"),
                            pygame.image.load("images/player/puzi5.PNG"),
                            pygame.image.load("images/player/puzi4.PNG")]
            
        self.images = self.pistolImages
        self.changed = False
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.waitCount = 0
        self.maxWait = 60*.25
        self.baseImage = self.images[self.frame]
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = pos)
        self.maxSpeed = 10
        self.speedx = 0
        self.speedy = 0
        self.pistolimage = pygame.image.load("images/player/ppist.PNG")
        self.uziimage = pygame.image.load("images/player/puzi.PNG")
        self.shotgunimage = pygame.image.load("images/player/pshot.PNG")
        self.gun = "pistol"
        
        self.maxPistolCount = 100000000
        self.pistolCoolDownMax = 50
        self.pistoldelay = 5
        self.maxUziCount = 100000000
        self.uziCoolDown = 0
        self.uziCoolDownMax = 50
        self.uzidelay = 5
        self.damage = 40
        self.health = 250
        self.maxHealth = 250
        self.nodamage = 0
        self.living = True
        
    
    def update(*args):
        self = args[0]
        width = args[1]
        height = args[2]
        self.move()
        self.animate()
        self.changed = False
        
    def attack(self, atk):
        if atk == "pistol" and self.pistolCoolDown == 0:
            self.pistoling = True
            self.pistolCoolDown = self.pistolCoolDownMax
            return [Pistol(self)]
        return []
        if atk == "uzi" and self.uziCoolDown == 0:
            self.uziing = True
            self.uziCoolDown = self.uziCoolDownMax
            return [Uzi(self)]
        return []
        if atk == "shotgun" and self.uziCoolDown == 0:
            self.uziing = True
            self.uziCoolDown = self.uziCoolDownMax
            return [Uzi(self)]
        return []
        
        
        
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
        
    def animate(self):
        if self.waitCount < self.maxWait:
            self.waitCount += 1
        else:
            self.waitCount = 0
            self.changed = True
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
        
        self.baseImage = self.images[self.frame]    
        mousePos = pygame.mouse.get_pos()
        mousePosPlayerX = mousePos[0] - self.rect.center[0]
        mousePosPlayerY = mousePos[1] - self.rect.center[1]
        self.angle = ((math.atan2(mousePosPlayerY, mousePosPlayerX))/math.pi)*180
        self.angle = -self.angle
        rot_image = pygame.transform.rotate(self.baseImage, self.angle)
        rot_rect = self.rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect)
        self.image = rot_image
        
    
    def go(self, direction):
        if direction == "up":
            self.speedy = -self.maxSpeed
        elif direction == "stop up":
            self.speedy = 0
        elif direction == "down":
            self.speedy = self.maxSpeed
        elif direction == "stop down":
            self.speedy = 0
            
        if direction == "right":
            self.speedx = self.maxSpeed
        elif direction == "stop right":
            self.speedx = 0
        elif direction == "left":
            self.speedx = -self.maxSpeed
        elif direction == "stop left":
            self.speedx = 0
            
    def modifyHealth (self, amount):
        self.health == amount
        if self.health <= 0:
            self.health = 0
            self.living = False
        elif self.health >= self.maxHealth:
            self.health = self.maxHealth

    def shoot(self, option=None):
        if option == None:
            if self.gun == "pistol":
                return PistolBullet(self.rect.center, self.angle)
            elif self.gun == "uzi":
                return UziBullet(self.rect.center, self.angle)
            elif self.gun == "shotgun":
                return ShotgunBullet(self.rect.center, self.angle)
            
            
    def changeGun(self, kind):
        if kind == "pistol":
            self.gun = "pistol"
            self.images = self.pistolImages
        elif kind == "uzi":
            self.gun = "uzi"
            self.images = self.uziImages
        elif kind == "shotgun":
            self.gun = "shotgun"
            self.images = self.shotgunImages
        self.maxFrame = len(self.images) - 1
        self.frame = 0


