import sys, pygame, math, random
from BgColor import *
from Ball import *
from Player import *
#from Predator import *
pygame.init()

clock = pygame.time.Clock()

screenModes = pygame.display.list_modes()

width = screenModes[0][0]
height = screenModes[0][1]
size = width, height
print size

r = 255
g = 255
b = 255

bgColor = BgColor()
#bgColor = r,g,b = 0,0,0

screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

balls = []
ballTimer = 0
ballTimerMax = 1 * 60

player = PlayerBall(["playerBall/ball.png"],[10,10],[width/2, height/2])

ballImages = ["Ball/Food.png",
              "Ball/Food-fire.png",
              "Ball/Food-icy.png",
              "Ball/Food-ocean.png"]

count = 0
while count < 4:

    ballTimer = 0
    ballSpeed = [0,0]
        
    ballPos = [random.randint(0, width),
                 random.randint(0, height)]

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
    
    ballTimer += 1
    if ballTimer >= ballTimerMax:
        ballTimer = 0
        ballSpeed = [0,0]
            
        ballPos = [random.randint(0, width),
                 random.randint(0, height)]
        ballImage = ballImages[random.randint(0, len(ballImages)-1)]
        balls += [Ball([ballImage],
               ballSpeed,
               20,
               ballPos)]
        #print len(balls), clock.get_fps()
    
    player.update(size)
    
    for ball in balls:
        ball.update(size)
    
    for first in balls:
        if player.collideBall(first):
            first.die()
            player.grow(first)
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
    

        
    clock.tick(60)
