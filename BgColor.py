class BgColor():
    def __init__(self, r=0, g=0, b=0):
        self.r = r = 255
        self.g = g
        self.b = b
        self.fadeTimer = 0
        self.fadeTimerMax = .25 *60
        
    def color(self):
        return self.r, self.g, self.b
    
    def increaseColor(self, r=False, g=False, b=False, amount=1):
        if r:
            self.r += amount
        
        if g:
            self.g += amount
        
        if b:
            self.b += amount
            
        if self.r >= 255:
            self.r = 255
            
        if self.g >= 255:
            self.g = 255
            
        if self.b >= 255:
            self.b = 255 
        
        if self.r < 0:
            self.r = 0
            
        if self.g < 0:
            self.g = 0
            
        if self.b < 0:
            self.b = 0 
        
    def fade(self, amount = 1, fadeTime = .25*60):
        
        if self.fadeTimer < 65:
            self.increaseColor(0,1,0,4)
 
        elif self.fadeTimer < 98 and self.fadeTimer >= 65:
            self.increaseColor(1,0,0,-8)
 
        elif self.fadeTimer < 163 and self.fadeTimer > 98:
            self.increaseColor(0,1,0,-4)
            self.increaseColor(0,0,1,4)
  
        elif  self.fadeTimer < 229 and self.fadeTimer > 163:
            self.increaseColor(1,0,0,4)
 
        elif self.fadeTimer < 263 and self.fadeTimer > 229:
            self.increaseColor(0,0,1,-8)
 
        elif self.fadeTimer > 264:
            self.fadeTimer = 0
 
        self.fadeTimer += 1
