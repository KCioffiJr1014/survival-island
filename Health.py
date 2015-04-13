import pygame,math,sys,random

class HealthBar(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images = []
        self.images += [pygame.image.load("images/health/0%.png")]
        self.images += [pygame.image.load("images/health/5%.png")]
        self.images += [pygame.image.load("images/health/10%.png")]
        self.images += [pygame.image.load("images/health/15%.png")]
        self.images += [pygame.image.load("images/health/20%.png")]
        self.images += [pygame.image.load("images/health/25%.png")]
        self.images += [pygame.image.load("images/health/30%.png")]
        self.images += [pygame.image.load("images/health/35%.png")]
        self.images += [pygame.image.load("images/health/40%.png")]
        self.images += [pygame.image.load("images/health/45%.png")]
        self.images += [pygame.image.load("images/health/55%.png")]
        self.images += [pygame.image.load("images/health/60%.png")]
        self.images += [pygame.image.load("images/health/65%.png")]
        self.images += [pygame.image.load("images/health/70%.png")]
        self.images += [pygame.image.load("images/health/75%.png")]
        self.images += [pygame.image.load("images/health/80%.png")]
        self.images += [pygame.image.load("images/health/85%.png")]
        self.images += [pygame.image.load("images/health/90%.png")]
        self.images += [pygame.image.load("images/health/95%.png")]
        self.images += [pygame.image.load("images/health/100%1.png")]
        self.maxFrame = len(self.images)-1
#        self.surface = pygame.transform.scale(self.faces,(100,25))
        self.frame = self.maxFrame
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = position
        #if pygame.mixer:
        #    self.healthSound = pygame.mixer.Sound("health.wav")
        
       
    def  __str__(self):
        return "I'm a Health Bar " + str(self.rect.center) + str(self.speed) + str(self.living)
     
    def health_bar(self):
        pass
            
    def update(self, life, maxLife):
        percentLife = float(life)/float(maxLife)
        if percentLife > .95:
            self.frame = 19
            print percentLife
        elif percentLife > .90:
            self.frame = 18
            print percentLife
        elif percentLife > .85:
            self.frame = 17
            print percentLife
        elif percentLife > .80:
            self.frame = 16
            print percentLife
        elif percentLife > .75:
            self.frame = 15
            print percentLife
        elif percentLife > .70:
            self.frame = 14
            print percentLife
        elif percentLife > .65:
            self.frame = 13
            print percentLife
        elif percentLife > .60:
            self.frame = 12
            print percentLife
        elif percentLife > .50:
            self.frame = 11
            print percentLife
        elif percentLife > .45:
            self.frame = 10
            print percentLife
        elif percentLife > .40:
            self.frame = 9
            print percentLife
        elif percentLife > .35:
            self.frame = 8
            print percentLife
        elif percentLife > .30:
            self.frame = 7
            print percentLife
        elif percentLife > .25:
            self.frame = 6
            print percentLife
        elif percentLife > .20:
            self.frame = 5
            print percentLife
        elif percentLife > .15:
            self.frame = 4
            print percentLife
        elif percentLife > .10:
            self.frame = 3
            print percentLife
        elif percentLife > .5:
            self.frame = 2
            print percentLife
        elif percentLife > .1:
            self.frame = 1
            print percentLife
        else:
            self.frame = 0
            print percentLife
            self.living = False
        self.image = self.images[self.frame]
