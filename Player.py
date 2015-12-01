import sys, pygame, math
from Ball import Ball

class PlayerBall(Ball):
    def __init__(self, images, maxSpeed, pos = [0,0], mass = 5):
        Ball.__init__(self, images, [0,0], mass, pos)
        self.maxSpeedx = maxSpeed[0]
        self.maxSpeedy = maxSpeed[1]
        self.realSpeedx = self.speedx
        self.realSpeedy = self.speedy
        self.accx = .1 # Higher number means less acceleration effect ie follows mouse movments more closly any number greater than 1 causes more jitter 
        self.accy = .1
        #self.viscosityX = 4
        #self.viscosityY = 4
        self.accx = self.accx/(mass/5)
        self.accy = self.accy/(mass/5)
        self.mass = mass
  
    def collideScreen(self, size):
        width = size[0]
        height = size[1]
        
        if not self.didBounceX:
            if self.rect.left < 0 or self.rect.right > width:
                self.speedx = -self.speedx
                self.didBounceX = True
                self.move()
                self.speedx = 0
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy = -self.speedy
                selfdidBounceY = True
                self.move()
                self.speedy = 0
                
    def collideBall(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if self.radius + other.radius > self.distanceTo(other.rect.center):
                    return True
        return False
    
    def go(self, direction, mLocation):
        if direction == "up":
            self.realSpeedy += -self.accy
            self.speedy = int(round(self.realSpeedy))
        elif direction == "down":
            self.realSpeedy += self.accy
            self.speedy = int(round(self.realSpeedy))
            
        if direction == "right":
            self.realSpeedx += self.accx
            self.speedx = int(round(self.realSpeedx))
        elif direction == "left":
            self.realSpeedx += -self.accx
            self.speedx = int(round(self.realSpeedx))
            
        self.speedx += (mLocation[0] - self.rect.centerx)/8 * self.accx
        self.speedy += (mLocation[1] - self.rect.centery)/8 * self.accy
            
    #def move(self):
        #if self.rect.centerx > self.targetx:
            #self.speedx = -self.maxSpeedx
        #elif self.rect.centerx < self.targetx:
            #self.speedx = self.maxSpeedx
        #else:
            #self.speedx = 0
        
        #if self.rect.centery > self.targety:
            #self.speedy = -self.maxSpeedy
        #elif self.rect.centery < self.targety:
            #self.speedy = self.maxSpeedy
        #else:
            #self.speedy = 0
        
        #Ball.move(self)
    
    def follow(self, mLocation):
        if self.rect.centerx > mLocation[0]:
            self.go("left", mLocation)
            
        if self.rect.centerx < mLocation[0]:
            self.go("right", mLocation)
            
        if self.rect.centery < mLocation[1]:
            self.go("down", mLocation)\
            
        if self.rect.centery > mLocation[1]:
            self.go("up", mLocation)
            
        #print self.rect.centerx, self.rect.centery
            
            
            
