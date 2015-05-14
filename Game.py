import pygame, sys, random
from Default import Default
from Player import Player
from HUD import Text
from HUD import Score
from Button import Button
from BackGround import BackGround
from Level import Level
from Block import Block
from HardBlock import HardBlock
from Enemy import Enemy
from Villagers import Villager
from PistolBullet import PistolBullet
from UziBullet import UziBullet
from ShotgunBullet import ShotgunBullet
from Sword import Sword
from Crosshair import Crosshair
#from Health import HealthBar
from AmmoHUD import Ammo


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
pistolBullets = pygame.sprite.Group()
uziBullets = pygame.sprite.Group()
shotgunBullets = pygame.sprite.Group()
defaults = pygame.sprite.Group()
hudItems = pygame.sprite.Group()
backgrounds = pygame.sprite.Group()
blocks = pygame.sprite.Group()
hardblocks = pygame.sprite.Group()
crosshairs = pygame.sprite.Group()
swords = pygame.sprite.Group()
#healthbars = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

Default.containers = (all, defaults)
Player.containers = (all, players)
BackGround.containers = (all, backgrounds)
Block.containers = (all, blocks)
HardBlock.containers = (all, hardblocks)
Score.containers = (all, hudItems)
PistolBullet.containers = (all, pistolBullets)
UziBullet.containers = (all, uziBullets)
ShotgunBullet.containers = (all, shotgunBullets)
Sword.containers = (all, swords)
Crosshair.containers = (all, crosshairs)
#HealthBar.containers = (all, healthbars)
Enemy.containers = (all, enemys)
Ammo.containers = (all, hudItems)



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
    
    
    
    
    level = Level(size, 50, 50)
    level.loadLevel("1")
    
    
    
    player = Player([width/2, height/2])
    #healthbar = HealthBar([115, -200])
    ammo = Ammo([100, 500])
    
    
    Enemys = []
    maxEnemy = 25
    Enemys += [Enemy("images/enemy/pr1.png", [0, 0], [200, 150])]
    
    
    
    #timer = Score([115, height - 25], " ", 36)
    #timerWait = 0
    #timerWaitMax = 6
    
    
    
    Crosshair("images/projectiles/target.png")
    pygame.mouse.set_visible(False)

    score = Score([width-125, height-25], "HI: ", 36)
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
                elif event.key == pygame.K_p:
                    sys.exit()
                elif event.key == pygame.K_k:
                    player.maxSpeed = 20
                elif event.key == pygame.K_l:
                    player.maxSpeed = 5
                elif event.key == pygame.K_j:
                    player.maxSpeed = 10
                elif event.key == pygame.K_y:
                    player.swordReloadMax = 15
                elif event.key == pygame.K_1:
                    player.changeGun("pistol")
                elif event.key == pygame.K_2:
                    player.changeGun("uzi")
                elif event.key == pygame.K_3:
                    player.changeGun("shotgun")
                elif event.key == pygame.K_4:
                    player.changeGun("sword")
                
                if event.key == pygame.K_RETURN :
                    if event.mod & pygame.KMOD_RALT or event.mod & pygame.KMOD_LALT:
                        if fullscreen:
                            pygame.display.set_mode(size)
                            fullscreen = True
                        else:
                            pygame.display.set_mode(size, pygame.FULLSCREEN)
                            fullscreen = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    player.shoot()
                if event.button == 3:
                    player.reload()
                    
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
                elif event.key == pygame.K_n:
                    player.swordReloadMax = 240
                    
            
        if len(enemys) < maxEnemy:
            if random.randint(0, 1 * 60) == 0:
                Enemy("images/enemy/pr1.png",
                                         [random.randint(0, 10), random.randint(0, 10)],
                                         [random.randint(100, width - 400), random.randint(100, height - 400)])
                     
                          
        #if timerWait < timerWaitMax:
        #timerWait += 1
        #else:
        #    timerWait = 0
        #    timer.increaseScore(.00001)
        
        playersHitEnemys = pygame.sprite.groupcollide(players, enemys, False, False)#True)
    
        playersHitHardBlocks = pygame.sprite.groupcollide(players, hardblocks, False, False)
        
        pistolBulletHitEnemys = pygame.sprite.groupcollide(pistolBullets, enemys, True, True)
        
        uziBulletHitEnemys = pygame.sprite.groupcollide(uziBullets, enemys, True, True)
        
        shotgunBulletHitEnemys = pygame.sprite.groupcollide(shotgunBullets, enemys, True, True)
        
        pistolBulletHitHardBlocks = pygame.sprite.groupcollide(pistolBullets, hardblocks, True, False)
        
        uziBulletHitHardBlocks = pygame.sprite.groupcollide(uziBullets, hardblocks, True, False)
        
        shotgunBulletHitHardBlocks = pygame.sprite.groupcollide(shotgunBullets, hardblocks, True, False)
        
        swordHitEnemys = pygame.sprite.groupcollide(swords, enemys, False, True)
        
        enemyHitHardBlocks = pygame.sprite.groupcollide(enemys, hardblocks, False, False)
        
        
        
        
        #enemyHitHealth = pygame.sprite.groupcollide(enemys, healthbars, False, False)
        
        for player in playersHitHardBlocks:
            for hardblock in playersHitHardBlocks[player]:
                player.collideHardBlock(hardblock)
                
        for enemy in enemyHitHardBlocks:
            for hardblock in enemyHitHardBlocks[enemy]:
                enemy.collideHardBlock(hardblock)
    
    
        '''for healthbar in enemyHitHealth:
            for healthbar in enemyHitHealth[healthbar]:
                player.modifyHealth(healthbar)
                
        
        for player in bulletHitEnemys:
            for enemy in bulletHitEnemys[bullet]:
                score.increaseScore(1)'''
                
        
        all.update(width, height, 
                   player.health, player.maxHealth,
                   player.currentAmmo, player.currentMaxAmmo, player.gun)
        
        
        
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        
        clock.tick(60)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
