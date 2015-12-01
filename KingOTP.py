import sys, pygame, math, random
from BgColor import *
from Ball import *
from Player import *
#from Predator import *
pygame.init()

clock = pygame.time.Clock()

width = 1366 
height = 768
size = width, height

r = 255
g = 255
b = 255

bgColor = BgColor()
#bgColor = r,g,b = 0,0,0

screen = pygame.display.set_mode(size, pygame.FULLSCREEN )

balls = []
ballTimer = 0
ballTimerMax = 1 * 60

player = PlayerBall(["playerBall/ball.png"],[10,10],[width/2, height/2])



count = 0
while count < 4:

    ballTimer = 0
    ballSpeed = [random.randint(-5, 5),
                 random.randint(-5, 5)]
    if ballSpeed[0] == 0:
        ballSpeed[0] = 1
    if ballSpeed[1] == 0:
        ballSpeed[1] = 1
        
    ballPos = [random.randint(100, width-100),
                 random.randint(100, height-100)]
    #ballImage = ballImages[random.randint(0, len(ballImages)-1)]
    balls += [Ball(["Ball/ball.png",
                    "Ball/balla.png",
                    "Ball/ballb.png",
                    "Ball/ballc.png"],
                   ballSpeed,
                   5,
                   ballPos)]
    count += 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.go("up")
            elif event.key == pygame.K_DOWN:
                player.go("down")
            elif event.key == pygame.K_LEFT:
                player.go("left")
            elif event.key == pygame.K_RIGHT:
                player.go("right")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.go("stop up")
            elif event.key == pygame.K_DOWN:
                player.go("stop down")
            elif event.key == pygame.K_LEFT:
                player.go("stop left")
            elif event.key == pygame.K_RIGHT:
                player.go("stop right")
    
    mLocation = pygame.mouse.get_pos()
    player.follow(mLocation)
    
    ballTimer += 1
    if ballTimer >= ballTimerMax:
        ballTimer = 0
        ballSpeed = [random.randint(-5, 5),
                     random.randint(-5, 5)]
        if ballSpeed[0] == 0:
            ballSpeed[0] = 1
        if ballSpeed[1] == 0:
            ballSpeed[1] = 1
            
        ballPos = [random.randint(100, width-100),
                     random.randint(100, height-100)]
        balls += [Ball(["Ball/ball.png",
						"Ball/balla.png",
						"Ball/ballb.png",
						"Ball/ballc.png"],
                       ballSpeed,
					   5,
                       ballPos)]
        #print len(balls), clock.get_fps()
    
    player.update(size)
    
    for ball in balls:
        ball.update(size)
    
    for first in balls:
        if player.collideBall(first):
             first.die()
        else:
            for second in balls:
                if first != second:
                    first.collideBall(second)
                    
    for ball in balls:
        if not ball.living:
            balls.remove(ball)
                    
    
    bgColor.fade()
    screen.fill(bgColor.color())
    
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    screen.blit(player.image, player.rect)
    pygame.display.flip()
    
    if len(balls) == 0:
        count = 0
        while count <100:
            print "YOU WON!!!"
            count += 1
        sys.exit()
        
    clock.tick(60)
