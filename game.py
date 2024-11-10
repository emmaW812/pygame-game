import pygame
from pygame.locals import *

pygame.init()
HEIGHT = 500
WIDTH = 500
GRAVITY = -9.8
FramePerSec = pygame.time.Clock()
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

