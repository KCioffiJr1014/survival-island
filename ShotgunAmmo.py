import pygame,math,sys,random

class ShotgunAmmo(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images = []
        self.images += [pygame.image.load("images/ammo/shot1.png")]
        self.images += [pygame.image.load("images/ammo/shot2.png")]
        self.images += [pygame.image.load("images/ammo/shot3.png")]
        self.images += [pygame.image.load("images/ammo/shot4.png")]
        self.images += [pygame.image.load("images/ammo/shot5.png")]
        self.images += [pygame.image.load("images/ammo/shot6.png")]
        self.images += [pygame.image.load("images/ammo/shot7.png")]
        self.images += [pygame.image.load("images/ammo/shot8.png")]
        self.maxFrame = len(self.images)-1
#        self.surface = pygame.transform.scale(self.faces,(100,25))
        self.frame = self.maxFrame
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = position
        #if pygame.mixer:
        #    self.healthSound = pygame.mixer.Sound("health.wav")
        
       
    def  __str__(self):
        return "I'm a Health Bar " + str(self.rect.center) + str(self.speed) + str(self.ammoing)
     
            
    def update(*args):
        self = args[0]
        width = args[1]
        height = args[2]
        ammo = args[3]
        maxAmmo = args[4]
        
        percentAmmo = float(ammo)/float(maxAmmo)
        if percentAmmo > .95:
            self.frame = 5
        elif percentAmmo > .75:
            self.frame = 4
        elif percentAmmo > .50:
            self.frame = 3
        elif percentAmmo > .25:
            self.frame = 2
        elif percentAmmo > .0:
            self.frame = 1
        else:
            self.frame = 0
            self.living = False
        self.image = self.images[self.frame]
