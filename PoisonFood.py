import sys, pygame, math
from Ball import Ball

class PoisonFood(Ball):
    def __init__(self, pos):
        image = "Ball/poison-Food.png"
        mass = -50
        Ball.__init__(self, [image], [0, 0], mass, pos)
