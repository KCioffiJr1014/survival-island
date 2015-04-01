import pygame, math

class Block(pygame.sprite.Sprite):
	def __init__(self, image, pos = [0,0]):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()
		self.place(pos)
		self.living = True
		
	def place(self, pos):
		self.rect.topleft = pos
		
	def update(*args):
		self = args[0]
		
		
		
		
		
		
		
		
		
		
		
		
		
		
