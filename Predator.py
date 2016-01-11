import sys, pygame, math
from Player import PlayerBall

class PredatorBall(PlayerBall):
    def __init__(self, images, maxSpeed, pos = [0,0], mass = 50):
        PlayerBall.__init__(self, images, maxSpeed, pos, mass)
        self.predatorTimer = 0
        self.predatorTimerMax = 1 * 60
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
            
    def follow(self, mLocation):
        
        mx = mLocation[0]
        my = mLocation[1]
        mx = abs(mx)
        my = abs(my)
        m = [mx,my]
        
        
        #print "[",mx,",",my,"]"
        
        if self.rect.centerx > mx:
            self.go("left", m)
            
        if self.rect.centerx < mx:
            self.go("right", m)
            
        if self.rect.centery < my:
            self.go("down", m)
            
        if self.rect.centery > my:
            self.go("up", m)
            
    def search(self, other):
        #print self.searchRadius, self.searchRect.size, self.mass
        if self.searchRect.right > other.rect.left and self.searchRect.left < other.rect.right:
            if self.searchRect.bottom > other.rect.top and self.searchRect.top < other.rect.bottom:
                if self.searchRadius + other.radius > self.distanceTo(other.rect.center):
                    if self.mass - 10 > other.mass:
                        #print "following"
                        return True
        
        return False
