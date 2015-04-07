import math,sys,pygame

class Pistol(pygame.sprite.Sprite):
    def __init__(self,player):
        self.facing = player.facing
      
        if self.facing == "up":
            self.image = pygame.image.load("rsc/Projectiles/gustu.png")
            self.speed = [0, -5]
        elif self.facing == "down":
            self.image = pygame.image.load("rsc/Projectiles/gustd.png")
            self.speed = [0, 5]
        elif self.facing == "right":
            self.image = pygame.image.load("rsc/Projectiles/gustr.png")
            self.speed = [5, 0]
        elif self.facing == "left":
            self.image = pygame.image.load("rsc/Projectiles/gustl.png")
            self.speed = [-5, 0]
        self.rect = self.image.get_rect()
        self.damage = 20
        self.place(player.rect.center)
        self.radius = 20
        self.move()
        self.living = True
      
    def move(self):
        self.rect = self.rect.move(self.speed)
    
    def collideWall(self, width, height):
        if self.rect.left < 0 or self.rect.right > width:
            self.speedx = 0
            #print "hit xWall"
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speedy = 0
    
    def collidePistol(self, other):
		if self != other:
			if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
				if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
					if (self.radius + other.radius) > self.distance(other.rect.center):
						self.living = False
                        
   
                        
    def place(self, pt):
        self.rect.center = pt
        
    def update(self, width, height):
        #self.speed = [self.speedx, self.speedy]
        self.move()
        
    def distance(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
        
    def animate(self):
        if self.waitCount < self.maxWait:
            self.waitCount += 1
        else:
            self.waitCount = 0
            self.facingChanged = True
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
        
        if self.changed:    
            if self.facing == "up":
                self.images = self.upImages
            elif self.facing == "down":
                self.images = self.downImages
            elif self.facing == "right":
                self.images = self.rightImages
            elif self.facing == "left":
                self.images = self.leftImages
            
            self.image = self.images[self.frame]
