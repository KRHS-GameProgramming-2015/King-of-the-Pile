import sys, pygame, math

class Ball():
    def __init__(self, images, speed, mass, pos=[0,0]):
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        
        #print images
        self.images = []
        for image in images:
            #print image
            self.images += [pygame.image.load(image)]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.originalImage = self.image
        self.width,self.height = self.image.get_size() 
        self.radius = self.rect.width/2 - 2
        
        self.frame = 0
        self.maxFrame = len(self.images)-1
        self.timer = 0
        self.timerMax = .25* 60
        
        self.didBounceX = False
        self.didBounceY = False
        
        self.rect = self.rect.move(pos)
        
        self.living = True
        
        self.mass = mass
        

    def grow(self):
		self.image = pygame.transform.scale(self.originalImage, (self.mass, self.mass)) 
		self.rect = self.image.get_rect(center = self.rect.center)    
    

    def die(self):
        
        self.living = False

    def update(self, size):
        self.move()
        self.grow()
        self.collideScreen(size)      
    
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        self.didBounceX = False
        self.didBounceY = False

    def collideScreen(self, size):
        width = size[0]
        height = size[1]
        
        if not self.didBounceX:
            if self.rect.left < 0 or self.rect.right > width:
                self.speedx = -self.speedx
                self.didBounceX = True
                self.move()
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy = -self.speedy
                selfdidBounceY = True
                self.move()

        
    def collideBall(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if self.radius + other.radius > self.distanceTo(other.rect.center):
                    if not self.didBounceX:
                        if ((self.rect.center[0] < other.rect.center[0] and self.speedx > 0) or
                            (self.rect.center[0] > other.rect.center[0] and self.speedx < 0)):
                            self.speedx = -self.speedx
                            self.didBounceX = True
                            self.move()
                    if not self.didBounceY:
                        if ((self.rect.center[1] < other.rect.center[1] and self.speedy > 0) or
                            (self.rect.center[1] > other.rect.center[1] and self.speedy < 0)):
                            self.speedy = -self.speedy
                            self.didBounceY = True
                            self.move()
                    
        
    def distanceTo(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt((x1-x2)**2+(y1-y2)**2)
