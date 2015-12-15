import sys, pygame, math, random
from BgColor import *
from Ball import *
from Player import *
from Predator import *
pygame.init()

clock = pygame.time.Clock()

screenModes = pygame.display.list_modes()

width = screenModes[0][0]
height = screenModes[0][1]
size = width, height


r = 255
g = 255
b = 255

bgColor = BgColor()
#bgColor = r,g,b = 0,0,0

screen = pygame.display.set_mode(size, pygame.FULLSCREEN)



balls = []
ballTimer = 0
ballTimerMax = 2 * 60
predatorTimer = 0
predatorTimerMax = .8 * 60

player = PlayerBall(["PlayerBall/ball.png"],[10,10],[width/2, height/2])
predators = [PredatorBall(["PredatorBall/predator1.png"],[10,10],[width/2, height/2]),
             PredatorBall(["PredatorBall/predator1.png"],[10,10],[width/2, height/2]),
             PredatorBall(["PredatorBall/predator1.png"],[10,10],[width/2, height/2]),
             PredatorBall(["PredatorBall/predator1.png"],[10,10],[width/2, height/2]),
             PredatorBall(["PredatorBall/predator1.png"],[10,10],[width/2, height/2]),
             PredatorBall(["PredatorBall/predator1.png"],[10,10],[width/2, height/2]),
             PredatorBall(["PredatorBall/predator1.png"],[10,10],[width/2, height/2]),
             PredatorBall(["PredatorBall/predator1.png"],[10,10],[width/2, height/2]),
             PredatorBall(["PredatorBall/predator1.png"],[10,10],[width/2, height/2]),
             PredatorBall(["PredatorBall/predator1.png"],[10,10],[width/2, height/2]),
             PredatorBall(["PredatorBall/predator1.png"],[10,10],[width/2, height/2]),
             PredatorBall(["PredatorBall/predator1.png"],[10,10],[width/2, height/2]),
             PredatorBall(["PredatorBall/predator1.png"],[10,10],[width/2, height/2]),
             PredatorBall(["PredatorBall/predator1.png"],[10,10],[width/2, height/2]),
             PredatorBall(["PredatorBall/predator1.png"],[10,10],[width/2, height/2]),
             PredatorBall(["PredatorBall/predator1.png"],[10,10],[width/2, height/2])]
             
foodMax = 10 * len(predators)
ballTimerMax = 1 * 60 / len(predators)
ballImages = ["Ball/Food.png"]#,
              #"Ball/Food-fire.png",
              #"Ball/Food-icy.png",
              #"Ball/Food-ocean.png"]

count = 0
while count < foodMax:

    ballTimer = 0
    ballSpeed = [0,0]
        
    ballPos = [random.randint(50, width-100),
                 random.randint(50, height-100)]

    ballImage = ballImages[random.randint(0, len(ballImages)-1)]
    balls += [Ball([ballImage],
                   ballSpeed,
                   20,
                   ballPos)]
    count += 1

fullscreen = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
        elif event.type == pygame.KEYUP:
            pass
    
    mLocation = pygame.mouse.get_pos()
    player.follow(mLocation)
    
    predatorTimer += 1
    if predatorTimer >= predatorTimerMax:
            predatorTimer = 0
            for predator in predators:
                predator.follow([random.randint(50, width-100),
                                 random.randint(50, height-100)])
    
    ballTimer += 1
    if ballTimer >= ballTimerMax and len(balls) < foodMax:
        ballTimer = 0
        ballSpeed = [0,0]
            
        ballPos = [random.randint(50, width-100),
                 random.randint(50, height-100)]
        ballImage = ballImages[random.randint(0, len(ballImages)-1)]
        balls += [Ball([ballImage],
               ballSpeed,
               20,
               ballPos)]
        #print len(balls), clock.get_fps()
    
    player.update(size)
    for predator in predators:
        predator.update(size)
    
    for ball in balls:
        ball.update(size)
    
    for first in balls:
        if player.collideBall(first):
            first.die()
            player.grow(first)
        
        for predator in predators:
            if predator.collideBall(first):
                first.die()
                predator.grow(first)
    
    for predator in predators:
        if player.canEatOther(predator):
            print "predator dies"
            predator.die()
            player.grow(predator)
        elif predator.canEatOther(player):
            print "player dies"
            player.die()
            
	#for predator in predators:
		#for second in predators:
			#if not second == predator:
				#if predator.canEatOther(second):
					#second.die()
					#predator.grow(second)
				#if second.canEatOther(predator):
					#predator.die()
					#second.grow(predator)
                       
    for ball in balls:
        if not ball.living:
            balls.remove(ball)
            
    for predator in predators:
        if not predator.living:
            predators.remove(predator)
            
    

    
    bgColor.fade()
    screen.fill(bgColor.color())
    
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    for predator in predators:
        screen.blit(predator.image, predator.rect)
    screen.blit(player.image, player.rect)
    
    pygame.display.flip()
    

        
    clock.tick(60)
