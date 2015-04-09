import pygame, sys, math

class Crosshair(pygame.sprite.Sprite):
	def __init__(self, image, speed = [0,0], pos = [0,0]):
            pygame.sprite.Sprite.__init__(self, self.containers)
            self.image = pygame.image.load(image)
            self.baseImage = pygame.image.load("images/projectiles/target.PNG")
            self.rect = self.image.get_rect()
            self.speed = [self.speedx, self.speedy]
            self.place(pos)
            self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
            mousePos = pygame.mouse.get_pos()
            mousePosPlayerX = mousePos[0] - self.rect.center[0]
            mousePosPlayerY = mousePos[1] - self.rect.center[1]
            
