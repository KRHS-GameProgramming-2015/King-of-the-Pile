import sys, pygame, math, random
from BgColor import *
from Ball import *
from Player import *
from Predator import *
from Food import *
from PoisonFood import *
pygame.init()

clock = pygame.time.Clock()

screenModes = pygame.display.list_modes()

screenWidth = screenModes[0][0]
screenHeight = screenModes[0][1]
screenSize = screenWidth, screenHeight


r = 255
g = 255
b = 255

bgColor = BgColor()
#bgColor = r,g,b = 0,0,0

screen = pygame.display.set_mode(screenSize, pygame.FULLSCREEN)

balls = []
ballTimer = 0
ballTimerMax = 2 * 60
predatorTimer = 0
predatorTimerMax = 1 * 60

player = PlayerBall(["PlayerBall/ball.png"],[10,10],[screenWidth/2-1024, screenHeight/2-1024])
predators = [PredatorBall(["PredatorBall/predator1.png"],[10,10],[screenWidth/2-512, screenHeight/2-512]),#]
             PredatorBall(["PredatorBall/predator1.png"],[10,10],[screenWidth/2-512, screenHeight/2-512]),
             PredatorBall(["PredatorBall/predator1.png"],[10,10],[screenWidth/2-512, screenHeight/2-512]),
             PredatorBall(["PredatorBall/predator1.png"],[10,10],[screenWidth/2-512, screenHeight/2-512])]#,
             #PredatorBall(["PredatorBall/predator1.png"],[10,10],[screenWidth/2-512, screenHeight/2-512]),
             #PredatorBall(["PredatorBall/predator1.png"],[10,10],[screenWidth/2-512, screenHeight/2-512]),
             #PredatorBall(["PredatorBall/predator1.png"],[10,10],[screenWidth/2-512, screenHeight/2-512]),
             #PredatorBall(["PredatorBall/predator1.png"],[10,10],[screenWidth/2-512, screenHeight/2-512]),
             #PredatorBall(["PredatorBall/predator1.png"],[10,10],[screenWidth/2-512, screenHeight/2-512]),
             #PredatorBall(["PredatorBall/predator1.png"],[10,10],[screenWidth/2-512, screenHeight/2-512]),
             #PredatorBall(["PredatorBall/predator1.png"],[10,10],[screenWidth/2-512, screenHeight/2-512]),
             #PredatorBall(["PredatorBall/predator1.png"],[10,10],[screenWidth/2-512, screenHeight/2-512]),
             #PredatorBall(["PredatorBall/predator1.png"],[10,10],[screenWidth/2-512, screenHeight/2-512]),
             #PredatorBall(["PredatorBall/predator1.png"],[10,10],[screenWidth/2-512, screenHeight/2-512]),
             #PredatorBall(["PredatorBall/predator1.png"],[10,10],[screenWidth/2-512, screenHeight/2-512]),
             #PredatorBall(["PredatorBall/predator1.png"],[10,10],[screenWidth/2-512, screenHeight/2-512])]
             
foodMax = 10 * len(predators)
ballTimerMax = 1 * 60 / len(predators)

count = 0
while count < foodMax:

    ballTimer = 0
        
    ballPos = [random.randint(50-512, screenWidth-100-512),
                 random.randint(50-512, screenHeight-100-512)]

    balls += [Food(ballPos)]
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
    

    ballTimer += 1
    if ballTimer >= ballTimerMax and len(balls) < foodMax:
        ballTimer = 0
        
        ballPos = [random.randint(50-512, screenWidth-100-512),
                 random.randint(50-512, screenHeight-100-512)]#screenWidth/2-512, screenHeight/2-512
        
        if random.randint(1,5)==1:
            balls += [PoisonFood(ballPos)]
        else:
            balls += [Food(ballPos)]
    
    player.update(screenSize)
    for predator in predators:
        predator.update(screenSize)
        if predator.search(player):
            predator.follow([player.rect.centerx, player.rect.centery])
        else:
            predatorTimer += 1
            if predatorTimer >= predatorTimerMax:
                predatorTimer = 0
                for predator in predators:
                    #print "pred location", predator,(predator.rect.centerx, predator.rect.centery)
                    predator.follow([random.randint(50-512, screenWidth-100-512),
                                     random.randint(50-512, screenHeight-100-512)])
    
    for ball in balls:
        ball.update(screenSize)
    
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

            predator.die()
            player.grow(predator)
        elif predator.canEatOther(player):
            
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
        if ball.age > 15 * 60:
            ball.living = False
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
