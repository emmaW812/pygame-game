import pygame

from pygame.locals import *

class Fruits():
    def __init__(self, pos, fruit, space, mapper):
        super().__init__()
        self.fruit = fruit #int 0 to 9
        self.radius = RADII[self.fruit]
        



pygame.init()
HEIGHT = 500
WIDTH = 500
GRAVITY = -9.8
FramePerSec = pygame.time.Clock()
RADII = [17, 25, 32, 38, 50, 63, 75, 87, 100, 115, 135]
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
import pygame.examples.aliens as aliens

print("asdfasdf")
