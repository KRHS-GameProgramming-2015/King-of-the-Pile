import sys, pygame, math
from Player import PlayerBall

class PredatorBall(PlayerBall):
    def __init__(self, images, maxSpeed, pos = [0,0], mass = 50):
        PlayerBall.__init__(self, images, maxSpeed, pos, mass)

	def die(self):
		sys.exit()
