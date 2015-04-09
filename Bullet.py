import math,sys,pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, angle):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load()
        self.rect = self.image.get_rect()
        self.angle = angle
        rot_image = pygame.transform.rotate(self.baseImage, self.angle)
        rot_rect = self.rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect)
        self.image = rot_image
        self.place(player.rect.center)    
        self.living = True
        
        
    def move(self):
            self.rect = self.rect.move(self.speed)
        
    def place(self, pt):
        self.rect.center = pt
        
    def update(*args):
        self = args[0]
        width = args[1]
        height = args[2]
        self.move()
        self.animate()
        
    def distance(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
        
    def animate(self):
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
        self.place(player.rect.center)
        
        
        
    
        
        
