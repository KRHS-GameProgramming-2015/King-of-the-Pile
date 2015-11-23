import sys, pygame, math
from Ball import Ball

class PlayerBall(Ball):
    def __init__(self, image, maxSpeed, pos = [0,0]):
        Ball.__init__(self, [image], [0,0], pos)
        self.maxSpeedx = maxSpeed[0]
        self.maxSpeedy = maxSpeed[1]
        self.targetx = self.rect.centerx
        self.targety = self.rect.centery
  
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
    
    def go(self, direction):
        count = 0
        count1 = 0
        count2 = 0
        count3 = 0
        if direction == "up":
            self.speedy = -self.maxSpeedy - count
            count +=1
        elif direction == "down":
            self.speedy = self.maxSpeedy + count1
            count1 +=1
        if direction == "right":
            self.speedx = self.maxSpeedx + count2
            count2 +=1
        elif direction == "left":
            self.speedx = -self.maxSpeedx - count3
            count3 +=1
        
        if direction == "stop up":
            self.speedy = 0
            count = 0
        elif direction == "stop down":
            self.speedy = 0
            count1 = 0
        if direction == "stop right":
            self.speedx = 0
            count2 = 0
        elif direction == "stop left":
            self.speedx = 0
            count3 = 0
            
    def move(self):
        if self.rect.centerx > self.targetx:
            self.speedx = -self.maxSpeedx
        elif self.rect.centerx < self.targetx:
            self.speedx = self.maxSpeedx
        else:
            self.speedx = 0
        
        if self.rect.centery > self.targety:
            self.speedy = -self.maxSpeedy
        elif self.rect.centery < self.targety:
            self.speedy = self.maxSpeedy
        else:
            self.speedy = 0
        
        Ball.move(self)
    
    def follow(self, mLocation):
        self.targetx = mLocation[0]
        self.targety = mLocation[1]
            
            
            
