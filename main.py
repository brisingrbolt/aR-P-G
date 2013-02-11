## Temp placeholder file until start on libs
import sys, pygame
sys.path.insert(0, 'libs') # Add libs to the path
from maps import GridFromMap
from pygame.locals import *

screen = pygame.display.set_mode((320,320))
grid = GridFromMap('map')
grid.display(screen)
pygame.display.update()

clock = pygame.time.Clock()
pressed = {}
pressed['up'] = False
pressed['down'] = False
pressed['left'] = False
pressed['right'] = False

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
            grid.move('up')
        if pressed['down']:
            grid.move('down')
        if pressed['left']:
            grid.move('left')
        if pressed['right']:
            grid.move('right')

        screen.fill((0, 0, 0))
        grid.display(screen)
        pygame.display.update()
        clock.tick(12)
