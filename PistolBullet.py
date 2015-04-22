import math,sys,pygame

class PistolBullet(pygame.sprite.Sprite):
    def __init__(self, pos, angle):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.baseImage = pygame.image.load("images/projectiles/bullet.PNG")
        
        self.rect = self.baseImage.get_rect()
        self.angle = angle
        rot_image = pygame.transform.rotate(self.baseImage, self.angle)
        rot_rect = self.rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect)
        self.image = rot_image 
        x = pos[0] + (math.cos(math.radians(self.angle - 35)) * math.sqrt(3529))
        y = pos[1] + (-math.sin(math.radians(self.angle - 35)) * math.sqrt(3529))
        print angle, pos, [x,y]
        self.place([x,y])    
        self.living = True
        self.speedx = math.cos(math.radians(self.angle))*11
        self.speedy = -math.sin(math.radians(self.angle))*11
        self.speed = [self.speedx, self.speedy] 
       
        
    def move(self):
        self.rect = self.rect.move(self.speed)
        
    def place(self, pt):
        self.rect.center = pt
        
    def update(*args):
        self = args[0]
        width = args[1]
        height = args[2]
        self.move()
        
    def distance(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
        
        
    
        
        
    
        
        
        
    
        
        
