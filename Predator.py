import sys, pygame, math
from Player import PlayerBall

class PredatorBall(PlayerBall):
    def __init__(self, images, maxSpeed, pos = [0,0], mass = 50):
        PlayerBall.__init__(self, images, maxSpeed, pos, mass)

    def die(self):
        self.living = False
        print "pred dies"
        
    def grow(self, other):
        self.mass += other.mass/8
        #print self.mass,self
        self.image = pygame.transform.scale(self.originalImage, (self.mass, self.mass)) 
        self.rect = self.image.get_rect(center = self.rect.center)
        self.radius = self.rect.width/3
        self.accx = self.accControlx/(self.mass/50)
        self.accy = self.accControly/(self.mass/50)
        if self.mass > 200:
            self.accx = self.accControlx/(200/50)
            self.accy = self.accControly/(200/50)
