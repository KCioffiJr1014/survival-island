import pygame, sys, random
from Default import Default
from Player import Player
from HUD import Text
from HUD import Score
from Button import Button
from BackGround import BackGround
from Level import Level
from Block import Block

pygame.init()

clock = pygame.time.Clock()

width = 800 
height = 600
size = width, height


bgColor = r,g,b = 0, 0, 10

screen = pygame.display.set_mode(size)

bgImage = pygame.image.load("maps/sand.PNG").convert()
bgRect = bgImage.get_rect()

players = pygame.sprite.Group()
defaults = pygame.sprite.Group()
hudItems = pygame.sprite.Group()
backgrounds = pygame.sprite.Group()
blocks = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

Default.containers = (all, defaults)
Player.containers = (all, players)
BackGround.containers = (all, backgrounds)
Block.containers = (all, blocks)
Score.containers = (all, hudItems)



run = False

startButton = Button([width/2, height-300], 
				     "images/start.png", 
				     "images/start.png")

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
					
		bgColor = r,g,b
		screen.fill(bgColor)
		screen.blit(bgImage, bgRect)
		screen.blit(startButton.image, startButton.rect)
		pygame.display.flip()
		clock.tick(60)
		
	BackGround("maps/sand.PNG")
	
	player = Player([width/2, height/2])
	
	
	level = Level(size, 50)
	level.loadLevel("1")

	timer = Score([80, height - 25], "Time: ", 36)
	timerWait = 0
	timerWaitMax = 6

	score = Score([width-80, height-25], "Score: ", 36)
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w or event.key == pygame.K_UP:
					player.go("up")
				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					player.go("right")
				if event.key == pygame.K_s or event.key == pygame.K_DOWN:
					player.go("down")
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					player.go("left")
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_w or event.key == pygame.K_UP:
					player.go("stop up")
				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					player.go("stop right")
				if event.key == pygame.K_s or event.key == pygame.K_DOWN:
					player.go("stop down")
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					player.go("stop left")
			
		'''if len(Terrorists) < 10:
			if random.randint(0, 1*60) == 0:
				Ball("images/Ball/ball.png",
						  [random.randint(0,10), random.randint(0,10)],
						  [random.randint(100, width-100), random.randint(100, height-100)])
		'''				  
						  
		if timerWait < timerWaitMax:
			timerWait += 1
		else:
			timerWait = 0
			timer.increaseScore(.1)
		
		#playersHitTerrorists = pygame.sprite.groupcollide(players, terrorists, False, True)
		#defaultsHitDefaults = pygame.sprite.groupcollide(terrorists, villagers, False, False)
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
		
		
		
		
		
		
		
		
		
		
		
		
		
		
