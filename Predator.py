import sys, pygame, math
from Player import PlayerBall

class PredatorBall(PlayerBall):
    def __init__(self, images, maxSpeed, pos = [0,0], mass = 50):
        PlayerBall.__init__(self, images, maxSpeed, pos, mass)
        #print self.rect.size, self.searchRect.size

    def die(self):
        self.living = False
        print "pred dies"
        
    def grow(self, other):
        self.mass += abs(other.mass)/8
        #print self.mass,self
        self.image = pygame.transform.scale(self.originalImage, (abs(self.mass), abs(self.mass))) 
        self.rect = self.image.get_rect(center = self.rect.center)
        self.searchRect = self.rect.inflate(300,300)
        self.searchRadius = self.searchRect.width/2
        #print self.rect.size, self.searchRect.size
        self.radius = self.rect.width/3
        self.searchRadius = self.searchRect.width/2
        self.accx = self.accControlx/(abs(self.mass)/50)
        self.accy = self.accControly/(abs(self.mass)/50)
        if self.mass > 200:
            self.accx = self.accControlx/(200/50)
            self.accy = self.accControly/(200/50)
            
    def search(self, other):
        #print self.searchRadius, self.searchRect.size, self.mass
        if self.searchRect.right > other.rect.left and self.searchRect.left < other.rect.right:
            if self.searchRect.bottom > other.rect.top and self.searchRect.top < other.rect.bottom:
                if self.searchRadius + other.radius > self.distanceTo(other.rect.center):
                    return True
        
        return False
