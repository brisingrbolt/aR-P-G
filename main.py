## Temp placeholder file until start on libs
import sys
import pygame
sys.path.insert(0, 'libs')   # Add libs to the path
from maps import GridFromMap
from pygame.locals import *
from player import *

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
x_size = 9
y_size = 9
screen = pygame.display.set_mode((x_size * TILE_SIZE,y_size * TILE_SIZE))
player_coords = (x_size / 2 * TILE_SIZE, y_size / 2 * TILE_SIZE)
grid = GridFromMap('map')
grid.display(screen)
pygame.display.update()

p = Player()
p.initialize_frames()

def game():
    while 1:  
        for event in pygame.event.get():
            if event.type is KEYDOWN:
                if event.key in [K_UP, K_k]:
                    pressed["up"] = True
                    p.set_direction("up")
                elif event.key in [K_DOWN, K_j]:
                    pressed["down"] = True
                    p.set_direction("down")
                elif event.key in [K_LEFT, K_h]:
                    pressed["left"] = True
                    p.set_direction("left")
                elif event.key in [K_RIGHT, K_l]:
                    pressed["right"] = True
                    p.set_direction("right")
                elif event.key is K_ESCAPE:
                    print "Exit"
                    sys.exit()
            elif event.type is KEYUP:
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
        refresh_display(True)
        clock.tick(12)

def refresh_display(animate_player = False):
    screen.fill((0, 0, 0))
    grid.display(screen)
    if animate_player:
        screen.blit(p.get_next_frame(), player_coords)
    else:
        screen.blit(p.get_current_frame(), player_coords)
    pygame.display.update()
