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
        self.mass += other.mass/8
        #print self.mass,self
        self.image = pygame.transform.scale(self.originalImage, (self.mass, self.mass)) 
        self.rect = self.image.get_rect(center = self.rect.center)
        self.searchRect.inflate_ip((self.rect.width * 2)- self.searchRect.width, (self.rect.height * 2)- self.searchRect.height)
        #print self.rect.size, self.searchRect.size
        self.radius = self.rect.width/3
        self.searchRadius = self.searchRect.width/2
        self.accx = self.accControlx/(self.mass/50)
        self.accy = self.accControly/(self.mass/50)
        if self.mass > 200:
            self.accx = self.accControlx/(200/50)
            self.accy = self.accControly/(200/50)
            
    def search(self, other):
        if self.searchRect.right > other.searchRect.left and self.searchRect.left < other.searchRect.right:
            if self.searchRect.bottom > other.searchRect.top and self.searchRect.top < other.searchRect.bottom:
                if self.searchRadius + other.searchRadius > self.distanceTo(other.rect.center):
                    return True
        return False
