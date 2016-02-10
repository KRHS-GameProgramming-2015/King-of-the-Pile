import sys, pygame, math, random
from BgColor import *
from Ball import *
from Player import *
from Predator import *
from Food import *
from PoisonFood import *
from GameMenu import *
from Button import *
pygame.init()
clock = pygame.time.Clock()

screenModes = pygame.display.list_modes()
screenWidth = screenModes[0][0]
screenHeight = screenModes[0][1]
screenSize = screenWidth, screenHeight
screen = pygame.display.set_mode(screenSize)#, pygame.FULLSCREEN)
print screenSize
originalScreenSize = [1680, 1050]

r = 255
g = 255
b = 255

bgColor = BgColor()
#bgColor = r,g,b = 0,0,0



balls = []
ballTimer = 0
ballTimerMax = 0 * 60
#predatorTimer = 0
#predatorTimerMax = 1 * 60



fullscreen = False

predatorRespawn= False

#superlevel = 0

sizeCap = 5000

menu = Menu(["Menu/MenuScreen.png"])
wonMenu = Menu(["Menu/winScreen.png"])
loseMenu = Menu(["Menu/loseScreen.png"])
playButton = Button(["Menu/Start.png"],[screenWidth/3.36,screenHeight/1.14])
quitButton = Button(["Menu/Quit.png"],[screenWidth/1.57,screenHeight/1.14])
winPlayButton = Button(["Menu/winPlayAgain.png"],[screenWidth/2.1,screenHeight/1.14])
winQuitButton = Button(["Menu/winQuit.png"],[screenWidth/1.05,screenHeight/1.05])
losePlayButton = Button(["Menu/losePlayAgain.png"],[screenWidth/1.98,screenHeight/1.56])
loseQuitButton = Button(["Menu/LoseQuit.png"],[screenWidth/2,screenHeight/1.05])

#menu.image = pygame.transform.scale(menu.originalImage, screenSize) 
#menu.rect = menu.image.get_rect(center = menu.rect.center)
#wonMenu.image = pygame.transform.scale(wonMenu.originalImage, screenSize) 
#wonMenu.rect = wonMenu.image.get_rect(center = wonMenu.rect.center)
#loseMenu.image = pygame.transform.scale(loseMenu.originalImage, screenSize) 
#loseMenu.rect = loseMenu.image.get_rect(center = loseMenu.rect.center)

#playButton.image = pygame.transform.scale(playButton.originalImage, (screenSize[0]/originalScreenSize[0],screenSize[1]/originalScreenSize[1])) 
#playButton.rect = playButton.image.get_rect(center = playButton.rect.center)
#quitButton.image = pygame.transform.scale(quitButton.originalImage, (screenSize[0]/originalScreenSize[0],screenSize[1]/originalScreenSize[1])) 
#quitButton.rect = quitButton.image.get_rect(center = quitButton.rect.center)
#winPlayButton.image = pygame.transform.scale(winPlayButton.originalImage, (screenSize[0]/originalScreenSize[0],screenSize[1]/originalScreenSize[1])) 
#winPlayButton.rect = winPlayButton.image.get_rect(center = winPlayButton.rect.center)
#winQuitButton.image = pygame.transform.scale(winQuitButton.originalImage, (screenSize[0]/originalScreenSize[0],screenSize[1]/originalScreenSize[1])) 
#winQuitButton.rect = winQuitButton.image.get_rect(center = winQuitButton.rect.center)
#losePlayButton.image = pygame.transform.scale(losePlayButton.originalImage, (screenSize[0]/originalScreenSize[0],screenSize[1]/originalScreenSize[1])) 
#losePlayButton.rect = losePlayButton.image.get_rect(center = losePlayButton.rect.center)
#loseQuitButton.image = pygame.transform.scale(loseQuitButton.originalImage, (screenSize[0]/originalScreenSize[0],screenSize[1]/originalScreenSize[1])) 
#loseQuitButton.rect = loseQuitButton.image.get_rect(center = loseQuitButton.rect.center)


mode = "menu"


while True:
    print mode
    


    while mode == "menu":    
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pt = pygame.mouse.get_pos()
        
                if quitButton.click(pt):
                    print "Good Bye"
                    sys.exit()
                if playButton.click(pt):
                    menu.playing = True
                    mode = "game"
                    player = PlayerBall(["PlayerBall/ball.png"],[10,10],[screenWidth/2-1024, screenHeight/2-1024])
                    predators = [PredatorBall(["PredatorBall/predator1.png"],[10,10],[random.randint(50-512, screenWidth-100-512),random.randint(50-512, screenHeight-100-512)])]
                                 #PredatorBall(["PredatorBall/predator1.png"],[10,10],[random.randint(50-512, screenWidth-100-512),random.randint(50-512, screenHeight-100-512)]),
                                 #PredatorBall(["PredatorBall/predator1.png"],[10,10],[random.randint(50-512, screenWidth-100-512),random.randint(50-512, screenHeight-100-512)]),
                                 #PredatorBall(["PredatorBall/predator1.png"],[10,10],[random.randint(50-512, screenWidth-100-512),random.randint(50-512, screenHeight-100-512)])]#,
                                 #PredatorBall(["PredatorBall/predator1.png"],[10,10],[random.randint(50-512, screenWidth-100-512),random.randint(50-512, screenHeight-100-512)]),
                                 #PredatorBall(["PredatorBall/predator1.png"],[10,10],[random.randint(50-512, screenWidth-100-512),random.randint(50-512, screenHeight-100-512)]),
                                 #PredatorBall(["PredatorBall/predator1.png"],[10,10],[random.randint(50-512, screenWidth-100-512),random.randint(50-512, screenHeight-100-512)]),
                                 #PredatorBall(["PredatorBall/predator1.png"],[10,10],[random.randint(50-512, screenWidth-100-512),random.randint(50-512, screenHeight-100-512)]),
                                 #PredatorBall(["PredatorBall/predator1.png"],[10,10],[random.randint(50-512, screenWidth-100-512),random.randint(50-512, screenHeight-100-512)]),
                                 #PredatorBall(["PredatorBall/predator1.png"],[10,10],[random.randint(50-512, screenWidth-100-512),random.randint(50-512, screenHeight-100-512)]),
                                 #PredatorBall(["PredatorBall/predator1.png"],[10,10],[random.randint(50-512, screenWidth-100-512),random.randint(50-512, screenHeight-100-512)]),
                                 #PredatorBall(["PredatorBall/predator1.png"],[10,10],[random.randint(50-512, screenWidth-100-512),random.randint(50-512, screenHeight-100-512)]),
                                 #PredatorBall(["PredatorBall/predator1.png"],[10,10],[random.randint(50-512, screenWidth-100-512),random.randint(50-512, screenHeight-100-512)]),
                                 #PredatorBall(["PredatorBall/predator1.png"],[10,10],[random.randint(50-512, screenWidth-100-512),random.randint(50-512, screenHeight-100-512)]),
                                 #PredatorBall(["PredatorBall/predator1.png"],[10,10],[random.randint(50-512, screenWidth-100-512),random.randint(50-512, screenHeight-100-512)])]
                                 
                    foodMax = 12 * len(predators)
                    

                    count = 0
                    while count < foodMax:

                        ballTimer = 0
                            
                        ballPos = [random.randint(50-512, screenWidth-100-512),
                                     random.randint(50-512, screenHeight-100-512)]

                        balls += [Food(ballPos)]
                        count += 1

                    foodMax = 12 * len(predators)
                    level = 1
                        
        screen.blit(menu.image, menu.rect)
        screen.blit(playButton.image, playButton.rect)
        screen.blit(quitButton.image, quitButton.rect)
    
        pygame.display.flip()
        clock.tick(60)   
            
    
    
    while mode == "game":
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
        
        foodMax = 12 * len(predators)
        if foodMax > 12*4:
            foodMax = 12*2
        #print foodMax, ballTimerMax
        
        if len(predators) <= 0:
            predatorRespawn = True
            #print predatorRespawn
            iteration = 0
            
        if predatorRespawn == True and ballTimer >= ballTimerMax:
            
            
            #print player.mass
            predators += [PredatorBall(["PredatorBall/predator1.png"],
                                      [10,10],
                                      [random.randint(50-512, screenWidth-100-512),random.randint(50-512, screenHeight-100-512)],
                                      random.randint(player.mass/3 , math.floor(player.mass/1.2)))]
            iteration += 1
            
            #print iteration, predatorRespawn
            
            if iteration >= level:
                level += 1
                predatorRespawn = False

        
        if ballTimer >= ballTimerMax and len(balls) < foodMax:
            ballTimer = 0
            
            ballPos = [random.randint(50-512, screenWidth-100-512),
                     random.randint(50-512, screenHeight-100-512)]#screenWidth/2-512, screenHeight/2-512
            
            if random.randint(1,6)==1:
                balls += [PoisonFood(ballPos)]
            else:
                balls += [Food(ballPos)]
        
        player.update(screenSize)
        for predator in predators:
            predator.update(screenSize)
            predator.predatorTimer += 1
            predator.follow(predator.followLocation)
            if predator.search(player):
                predator.followLocation=[player.rect.centerx, player.rect.centery]
                predator.amFollowing = True
            else:
                if predator.predatorTimer >= predator.predatorTimerMax:
                    for ball in balls:
                        if predator.search(ball) and predator.amFollowing == False:
                            predator.followLocation=[ball.rect.centerx, ball.rect.centery]
                            predator.amFollowing = True
                            #print predator, "following", ball
                            predator.predatorTimer = 0
                        elif predator.predatorTimer >= predator.predatorTimerMax * 6:
                            predator.predatorTimer = 0
                            #print "pred location", predator,(predator.rect.centerx, predator.rect.centery)
                            predator.followLocation=([random.randint(50-512, screenWidth-100-512),
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
                mode = "lost"
                
        for predator in predators:
            for second in predators:
                if not second == predator:
                    if predator.canEatOther(second):
                        second.die()
                        predator.grow(second)
                    if second.canEatOther(predator):
                        predator.die()
                        second.grow(predator)
                           
        for ball in balls:
            if ball.mass >= sizeCap:
                ball.mass = sizeCap-1 
            if ball.age > 15 * 60:
                ball.living = False
            if not ball.living:
                balls.remove(ball)
                
        for predator in predators:
            if predator.mass >= sizeCap:
                predator.mass = sizeCap-1 
            if not predator.living:
                predators.remove(predator)
                
        if level >= 8:
            print "........................................................"
            print ":                                                      :"
            print ":                                                      :"
            print ":                    YOU WON!!!                        :"
            print ":                                                      :"
            print ":                                                      :"
            print "........................................................"
            mode = "won"
                
        
            
        if player.mass >= sizeCap:
            
            i=0
            while i<100:
                print " "
                i+=1
            print "........................................................"
            print ":                                                      :"
            print ":                                                      :"
            print ":                    YOU WON!!!                        :"
            print ":                                                      :"
            print ":                                                      :"
            print "........................................................"
            mode = "won"
        

        
        bgColor.fade()
        screen.fill(bgColor.color())
        
        for ball in balls:
            screen.blit(ball.image, ball.rect)
        for predator in predators:
            screen.blit(predator.image, predator.rect)
        screen.blit(player.image, player.rect)
    
    
        #if mode == "won":
            #superlevel += 1

    
        pygame.display.flip()
    
    

        
        clock.tick(60)
        
    while mode == "won":
    
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pt = pygame.mouse.get_pos()
        
                if winQuitButton.click(pt):
                    print "Good Bye"
                    sys.exit()
                if winPlayButton.click(pt):
                    print "Win button play clicked"
                    menu.playing = True
                    mode = "game"
                    player = PlayerBall(["PlayerBall/ball.png"],[10,10],[screenWidth/2-1024, screenHeight/2-1024])
                    #level = superlevel
                    foodMax = 12 * len(predators)
                    

                    count = 0
                    while count < foodMax:

                        ballTimer = 0
                            
                        ballPos = [random.randint(50-512, screenWidth-100-512),
                                     random.randint(50-512, screenHeight-100-512)]

                        balls += [Food(ballPos)]
                        count += 1

                    foodMax = 12 * len(predators)
                    level = 1
        
        screen.blit(wonMenu.image, wonMenu.rect)
        screen.blit(winPlayButton.image, winPlayButton.rect)
        screen.blit(winQuitButton.image, winQuitButton.rect)
    
        pygame.display.flip()
        clock.tick(60)   
    
    while mode == "lost":
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pt = pygame.mouse.get_pos()
                #print menu.playing
                if loseQuitButton.click(pt):
                    print "Good Bye"
                    sys.exit()
                if losePlayButton.click(pt):
                    print " lose button play clicked"
                    menu.playing = True
                    mode = "game"
                    player = PlayerBall(["PlayerBall/ball.png"],[10,10],[screenWidth/2-1024, screenHeight/2-1024])
                    predators = [PredatorBall(["PredatorBall/predator1.png"],[10,10],[random.randint(50-512, screenWidth-100-512),random.randint(50-512, screenHeight-100-512)])]
                                 #PredatorBall(["PredatorBall/predator1.png"],[10,10],[random.randint(50-512, screenWidth-100-512),random.randint(50-512, screenHeight-100-512)]),
                                 #PredatorBall(["PredatorBall/predator1.png"],[10,10],[random.randint(50-512, screenWidth-100-512),random.randint(50-512, screenHeight-100-512)]),
                                 #PredatorBall(["PredatorBall/predator1.png"],[10,10],[random.randint(50-512, screenWidth-100-512),random.randint(50-512, screenHeight-100-512)])]#,
                                 #PredatorBall(["PredatorBall/predator1.png"],[10,10],[random.randint(50-512, screenWidth-100-512),random.randint(50-512, screenHeight-100-512)]),
                                 #PredatorBall(["PredatorBall/predator1.png"],[10,10],[random.randint(50-512, screenWidth-100-512),random.randint(50-512, screenHeight-100-512)]),
                                 #PredatorBall(["PredatorBall/predator1.png"],[10,10],[random.randint(50-512, screenWidth-100-512),random.randint(50-512, screenHeight-100-512)]),
                                 #PredatorBall(["PredatorBall/predator1.png"],[10,10],[random.randint(50-512, screenWidth-100-512),random.randint(50-512, screenHeight-100-512)]),
                                 #PredatorBall(["PredatorBall/predator1.png"],[10,10],[random.randint(50-512, screenWidth-100-512),random.randint(50-512, screenHeight-100-512)]),
                                 #PredatorBall(["PredatorBall/predator1.png"],[10,10],[random.randint(50-512, screenWidth-100-512),random.randint(50-512, screenHeight-100-512)]),
                                 #PredatorBall(["PredatorBall/predator1.png"],[10,10],[random.randint(50-512, screenWidth-100-512),random.randint(50-512, screenHeight-100-512)]),
                                 #PredatorBall(["PredatorBall/predator1.png"],[10,10],[random.randint(50-512, screenWidth-100-512),random.randint(50-512, screenHeight-100-512)]),
                                 #PredatorBall(["PredatorBall/predator1.png"],[10,10],[random.randint(50-512, screenWidth-100-512),random.randint(50-512, screenHeight-100-512)]),
                                 #PredatorBall(["PredatorBall/predator1.png"],[10,10],[random.randint(50-512, screenWidth-100-512),random.randint(50-512, screenHeight-100-512)]),
                                 #PredatorBall(["PredatorBall/predator1.png"],[10,10],[random.randint(50-512, screenWidth-100-512),random.randint(50-512, screenHeight-100-512)])]
                                 
                    foodMax = 12 * len(predators)
                    

                    count = 0
                    while count < foodMax:

                        ballTimer = 0
                            
                        ballPos = [random.randint(50-512, screenWidth-100-512),
                                     random.randint(50-512, screenHeight-100-512)]

                        balls += [Food(ballPos)]
                        count += 1

                    foodMax = 12 * len(predators)
                    level = 1
        
        screen.blit(loseMenu.image, loseMenu.rect)
        screen.blit(losePlayButton.image, losePlayButton.rect)
        screen.blit(loseQuitButton.image, loseQuitButton.rect)
    
        pygame.display.flip()
        clock.tick(60)   
