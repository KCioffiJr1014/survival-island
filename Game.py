import pygame, sys, random
from Default import Default
from Player import Player
from HUD import Text
from HUD import Score
from Button import Button
from BackGround import BackGround
from Level import Level
from Block import Block
from Enemy import Enemy
from Villagers import Villager
from Pistol import Pistol
from Bullet import Bullet
from Crosshair import Crosshair
from Health import HealthBar

pygame.init()

clock = pygame.time.Clock()

width = 800
height = 600
fullscreen = 0
altFlag = False
size = width, height


bgColor = r,g,b = 0, 0, 10

screen = pygame.display.set_mode(size)

bgImage = pygame.image.load("images/startscreen.PNG").convert()
bgRect = bgImage.get_rect()

players = pygame.sprite.Group()
enemys = pygame.sprite.Group()
pistols = pygame.sprite.Group()
defaults = pygame.sprite.Group()
hudItems = pygame.sprite.Group()
backgrounds = pygame.sprite.Group()
blocks = pygame.sprite.Group()
bullets = pygame.sprite.Group()
crosshairs = pygame.sprite.Group()
healthbars = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

Default.containers = (all, defaults)
Player.containers = (all, players)
BackGround.containers = (all, backgrounds)
Block.containers = (all, blocks)
Score.containers = (all, hudItems)
Pistol.containers = (all, pistols)
Bullet.containers = (all, bullets)
Crosshair.containers = (all, crosshairs)
HealthBar.containers = (all, healthbars)



run = False

startButton = Button([width/4, height/1.5], 
                     "images/start.png", 
                     "images/start.png")
                     
startButton2 = Button([width/1.4, height/1.5],
                    "images/quit.png",
                    "images/quit.png")
                    
projectiles = []

while True:
    while not run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                startButton.click(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                if startButton.release(event.pos):
                    run = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                startButton2.click(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                if startButton2.release(event.pos):
                    running = False
                    sys.exit()
                    
        bgColor = r,g,b
        screen.fill(bgColor)
        fullscreen = False
        screen.blit(bgImage, bgRect)
        screen.blit(startButton.image, startButton.rect)
        screen.blit(startButton2.image, startButton2.rect)
        pygame.display.flip()
        clock.tick(60)
        
    BackGround("maps/black.PNG")
    
    
    
    
    level = Level(size, 50)
    level.loadLevel("1")
    
    
    
    player = Player([width/2, height/2])
    healthbar = HealthBar([width - 75, 75])  #DEFAULT: 100 MODED: 200
    
    
    timer = Score([115, height - 25], "USELESS FOR NOW: ", 36)
    timerWait = 0
    timerWaitMax = 6
    
    
    
    Crosshair("images/projectiles/target.png")
    pygame.mouse.set_visible(False)

    score = Score([width-125, height-25], "USELESS FOR NOW: ", 36)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.go("up")
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.go("right")
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.go("down")
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.go("left")
                if event.key == pygame.K_RETURN :
                    print event.mod, pygame.KMOD_RALT
                if event.mod & pygame.KMOD_RALT: #Binary and with KMOD_RIGHT to filter out other mod keys
                    if fullscreen:
                        pygame.display.set_mode(size)
                        fullscreen = True
                    else:
                        pygame.display.set_mode(size, pygame.FULLSCREEN)
                        fullscreen = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    #print "1"
                    b = player.shoot()
                    #print len(bullets)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.go("stop up")
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.go("stop right")
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.go("stop down")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.go("stop left")
                elif (event.key == pygame.MOUSEBUTTONUP):
                    player.shoot("stop")
                elif (event.key == pygame.K_RALT or event.key == pygame.K_LALT):
                    altFlag = False
            
        '''if len(Enemys) < 10:
            if random.randint(0, 1*60) == 0:
                Enemy("images/Ball/ball.png",
                          [random.randint(0,10), random.randint(0,10)],
                          [random.randint(100, width-100), random.randint(100, height-100)])
        '''               
                          
        if timerWait < timerWaitMax:
            timerWait += 1
        else:
            timerWait = 0
            timer.increaseScore(.1)
        
        #playersHitEnemys = pygame.sprite.groupcollide(players, enemys, False, True)
        
        #defaultsHitDefaults = pygame.sprite.groupcollide(enemys, villagers, False, False)
        '''
        for player in playersHitBalls:
            for ball in playersHitBalls[player]:
                score.increaseScore(1)
                
        for bully in ballsHitBalls:
            for victem in ballsHitBalls[bully]:
                bully.collideBall(victem)
        '''
        all.update(width, height)
        
     
        
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        
        clock.tick(60)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
