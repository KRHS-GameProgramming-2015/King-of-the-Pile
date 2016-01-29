import sys, pygame, math, random

class Button():
    def __init__(self, images, pos=[0,0]):
        self.images = []
        for image in images:
            #print image
            self.images += [pygame.image.load(image)]
        self.image = self.images[0]
        self.rect = self.image.get_rect(center = pos)
        self.originalImage = self.image
        self.width, self.height = self.image.get_size() 
        self.cliked = False
        
    def click(self, pt):
        if self.rect.right > pt[0] and self.rect.left < pt[0]:
            if self.rect.bottom > pt[1] and self.rect.top < pt[1]:
                self.clicked = True
                return True
        return False
        
    def release(self, pt):
        if self.rect.right > pt[0] and self.rect.left < pt[0]:
            if self.rect.bottom > pt[1] and self.rect.top < pt[1]:
                self.clicked = False
                return True
        return False
