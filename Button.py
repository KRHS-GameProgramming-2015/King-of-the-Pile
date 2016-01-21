import sys, pygame, math, random

class Button():
    def __init__(self, images, pos=[0,0]):
        self.images = []
        for image in images:
            #print image
            self.images += [pygame.image.load(image)]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.originalImage = self.image
        self.width, self.height = self.image.get_size() 
