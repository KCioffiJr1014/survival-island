import pygame, sys, math

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(image)
        self.baseImage = pygame.image.load("images/projectiles/target.PNG")             
        mousePos = pygame.mouse.get_pos()
        self.rect = self.image.get_rect(center = mousePos)

    def update(*args):
        self = args[0]
        mousePos = pygame.mouse.get_pos()
        #print mousePos, self.rect.center
        self.rect.center = mousePos
        
