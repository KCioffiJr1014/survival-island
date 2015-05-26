import pygame, sys

class Jump(pygame.sprite.Sprite):
    def __init__(self, pos, size = [150,150]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        
        
        self.pistoljumpImages =
        
        
        
        self.uzijumpImages =
        
        
        
        self.shotgumjumpImages = 
        
        
        
        
        
        
        
        
        
        
        self.images = self.pistolImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.waitCount = 0
        self.maxWait = 60*.25
        self.baseImage = self.images[self.frame]
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = pos)
        self.pistolimage = pygame.image.load("images/player/ppist.PNG")
        self.uziimage = pygame.image.load("images/player/puzi.PNG")
        self.shotgunimage = pygame.image.load("images/player/pshot.PNG")
        self.jump = "pistol"
        self.jumping = False
        
        
        
        
        def update(*args):
        self = args[0]
        width = args[1]
        height = args[2]
        self.move()
        self.animate()
