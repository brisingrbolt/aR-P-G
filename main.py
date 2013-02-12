## Temp placeholder file until start on libs
import sys
import pygame
sys.path.insert(0, 'libs')   # Add libs to the path
from maps import GridFromMap
from pygame.locals import *

# Constants
TILE_SIZE = 32
INCREMENT_DISTANCE = 4  # By how much the coordinates change every frame.

# Runtime variables
clock = pygame.time.Clock()
pressed = {}
pressed['up'] = False
pressed['down'] = False
pressed['left'] = False
pressed['right'] = False

# Resource variables
screen = pygame.display.set_mode((288,288))
grid = GridFromMap('map')
grid.display(screen)
pygame.display.update()

def game():
    while 1:  
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key in [K_UP, K_k]:
                    pressed["up"] = True
                elif event.key in [K_DOWN, K_j]:
                    pressed["down"] = True
                elif event.key in [K_LEFT, K_h]:
                    pressed["left"] = True
                elif event.key in [K_RIGHT, K_l]:
                    pressed["right"] = True
                elif event.key == K_ESCAPE:
                    print "Exit"
                    sys.exit()
            elif event.type == KEYUP:
                if event.key in [K_UP, K_k]:
                    pressed["up"] = False
                elif event.key in [K_DOWN, K_j]:
                    pressed["down"] = False
                elif event.key in [K_LEFT, K_h]:
                    pressed["left"] = False
                elif event.key in [K_RIGHT, K_l]:
                    pressed["right"] = False

        if pressed['up']:
            move('up')
        if pressed['down']:
            move('down')
        if pressed['left']:
            move('left')
        if pressed['right']:
            move('right')

        refresh_display()
        clock.tick(12)

def move(direction):
    iterations = TILE_SIZE / INCREMENT_DISTANCE
    
    for i in range(iterations):
        grid.move(direction, INCREMENT_DISTANCE)
        refresh_display()
        clock.tick(12)

def refresh_display():
    screen.fill((0, 0, 0))
    grid.display(screen)
    pygame.display.update()
