## Temp placeholder file until start on libs
import sys
import pygame
sys.path.insert(0, 'libs')   # Add libs to the path
from maps import Map
from pygame.locals import *
from player import *

# Constants
TILE_SIZE = 32
INCREMENT_DISTANCE = 4  # By how much the coordinates change every frame.

# Runtime variables
clock = pygame.time.Clock()

# Resource variables
FPS = 16
x_size = 9 # Should always be odd, so that the player is in the dead middle
y_size = 9
screen = pygame.display.set_mode((x_size * TILE_SIZE,y_size * TILE_SIZE))
player_coords = (x_size / 2 * TILE_SIZE, y_size / 2 * TILE_SIZE)
grid = Map('map')
grid.display(screen)
pygame.display.update()

p = Player()
p.initialize_frames()

pressed = {}
pressed['up'] = False
pressed['down'] = False
pressed['left'] = False
pressed['right'] = False

locked = False

def game():
    global direction
    while True:
        locked = should_be_locked()
        if not locked:
            for event in pygame.event.get():
                moving = False
                if event.type is KEYDOWN:
                    if event.key in [K_UP, K_k]:
                        p.set_direction("up")
                        pressed['up'] = True
                    if event.key in [K_DOWN, K_j]:
                        p.set_direction("down")
                        pressed['down'] = True
                    if event.key in [K_LEFT, K_h]:
                        p.set_direction("left")
                        pressed['left'] = True
                    if event.key in [K_RIGHT, K_l]:
                        p.set_direction("right")
                        pressed['right'] = True
                    if event.key is K_ESCAPE:
                        print "Exit"
                        pygame.quit()
                elif event.type is KEYUP:
                    if event.key in [K_UP, K_k]:
                        pressed['up'] = False
                    if event.key in [K_DOWN, K_j]:
                        pressed['down'] = False
                    if event.key in [K_LEFT, K_h]:
                        pressed['left'] = False
                    if event.key in [K_RIGHT, K_l]:
                        pressed['right'] = False

            a_key_pressed = False
            for key in pressed:
                if pressed[key]:
                    a_key_pressed = True        
            moving = a_key_pressed ## TODO: This is where logic for whether or not the map should be moving will be.

        refresh_display(moving)
        clock.tick(FPS)

def move(direction):
    iterations = TILE_SIZE / INCREMENT_DISTANCE
    
    for i in range(iterations):
        grid.move(p.direction, INCREMENT_DISTANCE)
        refresh_display(True)
        clock.tick(FPS)

def should_be_locked():
    ## Any tile will do here
    if grid.tiles[(1,1)]['coords'][0] % TILE_SIZE == 0 and \
       grid.tiles[(1,1)]['coords'][1] % TILE_SIZE == 0:
        return False
    else:
        return True

def refresh_display(animate_player = False):
    screen.fill((0, 0, 0))
    grid.display(screen)
    if animate_player:
        grid.move(p.direction, INCREMENT_DISTANCE)
        screen.blit(p.get_next_frame(), player_coords)
    else:
        screen.blit(p.get_current_frame(), player_coords)
    pygame.display.update()
