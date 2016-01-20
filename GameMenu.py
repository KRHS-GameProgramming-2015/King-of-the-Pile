import sys, pygame, math, random
from KingOTP import *

pygame.init()

clock = pygame.time.Clock()

screenModes = pygame.display.list_modes()
screenWidth = screenModes[0][0]
screenHeight = screenModes[0][1]
screenSize = screenWidth, screenHeight
screen = pygame.display.set_mode(screenSize, pygame.FULLSCREEN)

