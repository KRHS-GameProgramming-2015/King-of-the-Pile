import sys, pygame, math, random
from Button import *



class Menu():
    def __init__(self, images):
        self.images = []
        for image in images:
            #print image
            self.images += [pygame.image.load(image)]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.originalImage = self.image
        self.width, self.height = self.image.get_size() 
        self.playing = False


    def update():
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
            elif event.type == pygame.KEYUP:
                pass
                
    def play(self, mLocation):
        pass
        
    def quitGame(self, mLocation):
        pass
        

        
        mLocation = pygame.mouse.get_pos()
        
        
        
        
        
        
