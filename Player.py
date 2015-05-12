import pygame, sys, math
from PistolBullet import PistolBullet
from UziBullet import UziBullet
from ShotgunBullet import ShotgunBullet
from Sword import Sword
from Crosshair import Crosshair
from Health import HealthBar
from AmmoHUD import Ammo

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
                        
        self.swordImages = [pygame.image.load("images/player/k1.png")]
            
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
        '''mousePos = pygame.mouse.get_pos()
        mousePosPlayerX = mousePos[0] - self.rect.center[0]
        mousePosPlayerY = mousePos[1] - self.rect.center[1]
        self.angle = ((math.atan2(mousePosPlayerY, mousePosPlayerX))/math.pi)*180
        self.angle = -self.angle'''
        self.pistolimage = pygame.image.load("images/player/ppist.PNG")
        self.uziimage = pygame.image.load("images/player/puzi.PNG")
        self.shotgunimage = pygame.image.load("images/player/pshot.PNG")
        self.gun = "pistol"
        self.shooting = False
        self.reloading = False
        self.shootDelay = 0
        self.gunReload = 0
        
        self.maxPistolAmmo = 12
        self.pistolAmmo = 12
        self.pistolReloadMax = 30
        self.pistolDelayMax = 2
        self.pistolDamage = 15
        
        self.maxUziAmmo = 20
        self.uziAmmo = 20
        self.uziReloadMax = 60
        self.uziDelayMax = 4
        self.uzidamage = 25
        
        self.maxShotgunAmmo = 8
        self.shotgunAmmo = 8
        self.shotgundamage = 5
        self.shotgunReloadMax = 120
        self.shotgunDelayMax = 12
        self.shotgunDamage = 50
        
        self.maxSwordAmmo = 1
        self.swordAmmo = 1
        self.sworddamage = 5
        self.swordReloadMax = 240
        self.swordDelayMax = 8
        self.swordDamage = 50
        
        
        self.currentAmmo = self.pistolAmmo
        self.currentMaxAmmo = self.maxPistolAmmo
        
        self.health = 200
        self.maxHealth = 200
        self.nodamage = 0
        self.living = True
        
    
    def update(*args):
        self = args[0]
        width = args[1]
        height = args[2]
        self.move()
        self.animate()
        self.changed = False
        if self.shooting:
            print self.shooting
            if ((self.gun == "pistol" and self.shootDelay < self.pistolDelayMax)
                or (self.gun == "uzi" and self.shootDelay < self.uziDelayMax)
                or (self.gun == "shotgun" and self.shootDelay < self.shotgunDelayMax)
                or (self.gun == "sword" and self.shootDelay < self.swordDelayMax)):
                    self.shootDelay += 1
            else:
                self.shootDelay = 0
                self.shooting = False
        if self.reloading:
            print self.gunReload
            if ((self.gun == "pistol" and self.gunReload < self.pistolReloadMax)
                or (self.gun == "uzi" and self.gunReload < self.uziReloadMax)
                or (self.gun == "shotgun" and self.gunReload < self.shotgunReloadMax)
                or (self.gun == "sword" and self.gunReload < self.swordReloadMax)):
                    self.gunReload += 1
            else:
                self.gunReload = 0
                self.reloading = False
                
        
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
    
    def collideHardBlock(self, block):
        self.speedx = -self.speedx
        self.speedy = -self.speedy
        self.move()
        self.speedx = 0
        self.speedy = 0
    
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
            
    def collideWall(self, width, height):
        if not self.didBounceX:
            #print "trying to hit Wall"
            if self.rect.left < 0 or self.rect.right > width:
                self.speedx = 0
                self.didBounceX = True
                #print "hit xWall"
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy = 0
                self.didBounceY = True

    def shoot(self, option=None):
        if option == None and not self.shooting and not self.reloading:
            if self.gun == "pistol":
                if self.pistolAmmo > 0:
                    self.pistolAmmo -= 1
                    self.currentAmmo = self.pistolAmmo
                    self.shootDelay = 1
                    self.shooting = True
                    return PistolBullet(self.rect.center, self.angle)
            elif self.gun == "uzi":
                if self.uziAmmo > 0:
                    self.uziAmmo -= 1
                    self.currentAmmo = self.uziAmmo
                    self.shootDelay = 1
                    self.shooting = True
                    return UziBullet(self.rect.center, self.angle)
            elif self.gun == "shotgun":
                if self.shotgunAmmo > 0:
                    self.shotgunAmmo -= 1
                    self.currentAmmo = self.shotgunAmmo
                    self.shootDelay = 1
                    self.shooting = True
                    return ShotgunBullet(self.rect.center, self.angle)
            elif self.gun == "sword":
                if self.swordAmmo > 0:
                    self.swordAmmo -= 1
                    self.currentAmmo = self.swordAmmo
                    self.shootDelay = 1
                    self.shooting = True
                    return Sword(self.rect.center, self.angle)
            
            
    def changeGun(self, kind):
        if not self.shooting and not self.reloading:
            if kind == "pistol":
                self.gun = "pistol"
                self.images = self.pistolImages
                self.currentAmmo = self.pistolAmmo
                self.currentMaxAmmo = self.maxPistolAmmo
            elif kind == "uzi":
                self.gun = "uzi"
                self.images = self.uziImages
                self.currentAmmo = self.uziAmmo
                self.currentMaxAmmo = self.maxUziAmmo
            elif kind == "shotgun":
                self.gun = "shotgun"
                self.images = self.shotgunImages
                self.currentAmmo = self.shotgunAmmo
                self.currentMaxAmmo = self.maxShotgunAmmo
            elif kind == "sword":
                self.gun = "sword"
                self.images = self.swordImages
                self.currentAmmo = self.swordAmmo
                self.currentMaxAmmo = self.maxSwordAmmo
            self.maxFrame = len(self.images) - 1
            self.frame = 0
        
    def reload(self):
        if self.gun == "pistol":
            self.gunReload = 1
            self.reloading = True
            self.pistolAmmo = self.maxPistolAmmo
        elif self.gun == "uzi":
            self.gunReload = 1
            self.reloading = True
            self.uziAmmo = self.maxUziAmmo
        elif self.gun == "shotgun":
            self.gunReload = 1
            self.reloading = True
            self.shotgunAmmo = self.maxShotgunAmmo
        elif self.gun == "sword":
            self.gunReload = 1
            self.reloading = True
            self.swordAmmo = self.maxSwordAmmo
        
