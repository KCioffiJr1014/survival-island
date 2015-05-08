import pygame,math,sys,random


class Ammo(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self, self.containers)
        
        self.shotgunAmmoimages = [pygame.image.load("images/ammo/shot0.png"),
                            pygame.image.load("images/ammo/shot1.png"),
                            pygame.image.load("images/ammo/shot2.png"),
                            pygame.image.load("images/ammo/shot3.png"),
                            pygame.image.load("images/ammo/shot4.png"),
                            pygame.image.load("images/ammo/shot5.png"),
                            pygame.image.load("images/ammo/shot6.png"),
                            pygame.image.load("images/ammo/shot7.png"),
                            pygame.image.load("images/ammo/shot8.png")]
                            
        self.uziAmmoimages = [pygame.image.load("images/ammo/uzi0.png"),
                            pygame.image.load("images/ammo/uzi1.png"),
                            pygame.image.load("images/ammo/uzi2.png"),
                            pygame.image.load("images/ammo/uzi3.png"),
                            pygame.image.load("images/ammo/uzi4.png"),
                            pygame.image.load("images/ammo/uzi5.png"),
                            pygame.image.load("images/ammo/uzi6.png"),
                            pygame.image.load("images/ammo/uzi7.png"),
                            pygame.image.load("images/ammo/uzi8.png"),
                            pygame.image.load("images/ammo/uzi9.png"),
                            pygame.image.load("images/ammo/uzi10.png"),
                            pygame.image.load("images/ammo/uzi11.png"),
                            pygame.image.load("images/ammo/uzi12.png"),
                            pygame.image.load("images/ammo/uzi13.png"),
                            pygame.image.load("images/ammo/uzi14.png"),
                            pygame.image.load("images/ammo/uzi15.png"),
                            pygame.image.load("images/ammo/uzi16.png"),
                            pygame.image.load("images/ammo/uzi17.png"),
                            pygame.image.load("images/ammo/uzi18.png"),
                            pygame.image.load("images/ammo/uzi19.png"),
                            pygame.image.load("images/ammo/uzi20.png")]
                            
        self.images = self.shotgunAmmoimages
        self.maxFrame = len(self.images)-1
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
        ammo = args[5]
        maxAmmo = args[6]
        gun = args[7]
        self.maxFrame = len(self.images)-1
        
        percentAmmo = float(ammo)/float(maxAmmo)
        print percentAmmo, ">>>>>>", gun, ammo, maxAmmo
        if gun == "shotgun":
            self.images = self.shotgunAmmoimages
            self.frame = ammo
        elif gun == "uzi":
            self.images = self.uziAmmoimages
            self.frame = ammo
        self.image = self.images[self.frame]
        
        
                    
