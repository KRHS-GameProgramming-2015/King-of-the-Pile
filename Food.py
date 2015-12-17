import sys, pygame, math
from Ball import Ball

class Food(Ball):
    def __init__(self, pos):
        image = "Ball/Food.png"
        mass = 20
        Ball.__init__(self, [image], [0, 0], mass, pos)
