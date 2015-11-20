import sys, pygame, math
pygame.init()


def distance(pt1, pt2):
    x1 = pt1[0]
    y1 = pt1[1]
    x2 = pt2[0]
    y2 = pt2[1]
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

clock = pygame.time.Clock()

width = 800 
height = 600
size = width, height

speed1x = 5
speed1y = 5
speed1 = [speed1x, speed1y]

speed2x = 3
speed2y = 3
speed2 = [speed2x, speed2y]

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)

ball1 = pygame.image.load("ball1.png")
ball1rect = ball1.get_rect()
ball1radius = ball1rect.width/2 - 2
ball2 = pygame.image.load("ball2.png")
ball2rect = ball2.get_rect()
ball2radius = ball2rect.width/2 - 2 
ball2rect = ball2rect.move([200,200])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
            
    ball1rect = ball1rect.move(speed1)
    if ball1rect.left < 0 or ball1rect.right > width:
        speed1[0] = -speed1[0]
    if ball1rect.top < 0 or ball1rect.bottom > height:
        speed1[1] = -speed1[1]
        
    ball2rect = ball2rect.move(speed2)
    if ball2rect.left < 0 or ball2rect.right > width:
        speed2[0] = -speed2[0]
    if ball2rect.top < 0 or ball2rect.bottom > height:
        speed2[1] = -speed2[1]
        
    if ball1rect.right > ball2rect.left and ball1rect.left < ball2rect.right:
        if ball1rect.bottom > ball2rect.top and ball1rect.top < ball2rect.bottom:
            if ball1radius + ball2radius > distance(ball1rect.center, ball2rect.center):
                if ball1rect.center[0] < ball2rect.center[0] and speed1[0] > 0:
                    speed1[0] = -speed1[0]
                if ball2rect.center[0] < ball1rect.center[0] and speed2[0] > 0:
                    speed1[1] = -speed1[1]
                if ball1rect.center[1] < ball2rect.center[1] and speed1[1] > 0:
                    speed2[0] = -speed2[0]
                if ball2rect.center[1] < ball2rect.center[1] and speed2[1] > 0:
                    speed2[1] = -speed2[1]
    
    bgColor = r,g,b
    screen.fill(bgColor)
    screen.blit(ball1, ball1rect)
    screen.blit(ball2, ball2rect)
    pygame.display.flip()
    clock.tick(60)
