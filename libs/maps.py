import pygame
import os.path
import images
import config

class Map():
    def __init__(self, map_name):
        self.tiles = {}
        self.width = None
        self.height = None
        self.tile_size = 32
        self.loaded = False
        self.moving = False
        self.clock = pygame.time.Clock()

        self.load_from_map(map_name)

    def load_from_map(self, map_name, map_dir = 'maps/'):
        # Check to make sure the file exists
        if not os.path.exists(map_dir + map_name):
            config.log_e('Map not found: ' + map_name)
            return 
        
        # Actually load the file
        map_file = open(map_dir + map_name, 'r')

        line = map_file.readline()
        while not line.startswith('tileset'):
            line = map_file.readline()
        line = line.replace('\n', '')
        tileset = line.split()[-1]

        images.initialize(tileset)

        # Try reading the first line of map for width
        self.read_to_map_start(map_file)

        line = map_file.readline()
        self.width = len(line.replace('\n', '').split())
        config.log_d('Map width: ' + str(self.width))

        self.read_to_map_start(map_file)

        # Try reading number of lines for height
        for i, l in enumerate(map_file):
            pass
        self.height = i + 1
        config.log_d('Map height: ' + str(self.height))

        self.read_to_map_start(map_file)

        # TODO: Check to make sure all tiles actually exist?

        # Initalize tile dictionary
        x, y = 1, 1
        for i in range(self.width):
            for e in range(self.height):
                self.tiles[(x,y)] = {}
                self.tiles[(x,y)]['coords'] = (((x-1) * self.tile_size), ((y-1) * self.tile_size)) # NOTE: May need to change this, so that the maps scroll properly. In other words, starting location needs to be determined based on the player's location within the map.
                y += 1
            y = 1
            x += 1
        
        # Read in map data and fill self.tiles with image references, one layer for now
        x, y = 1, 1
        for line in map_file.readlines():
            line = line.replace('\n', '')
            for tile in line.split():
                layers = tile.split(',')
                self.tiles[(x,y)][1] = int(layers[0])
                self.tiles[(x,y)][2] = int(layers[1])
                self.tiles[(x,y)][3] = int(layers[2])
                x += 1
            x = 1
            y += 1

        # This grid is now loaded!
        self.loaded = True
    
    def read_to_map_start(self, _file): # Start at beginning of file and read lines until the line starts with BEGIN
        _file.seek(0)
        line = _file.readline()
        while not line.startswith('BEGIN'):
            line = _file.readline()
        return _file

    def display(self, screen, location = None):
        if not self.loaded:
            config.log_e('Grid is not loaded!')
            return
        for tile in self.tiles:
            for i in range(3):
                image = images.get(self.tiles[tile][i+1])
                if image is not None: screen.blit(image, self.tiles[tile]['coords'])

    def move(self, direction, distance = 4):
        if not self.loaded:
            config.log_e('Grid is not loaded!')
            return
        if direction is 'up':
            for tile in self.tiles:
                new_coords = ((self.tiles[tile]['coords'][0]), (self.tiles[tile]['coords'][1] + distance))
                self.tiles[tile]['coords'] = new_coords
        if direction is 'down':
            for tile in self.tiles:
                new_coords = ((self.tiles[tile]['coords'][0]), (self.tiles[tile]['coords'][1] - distance))
                self.tiles[tile]['coords'] = new_coords
        if direction is 'left':
            for tile in self.tiles:
                new_coords = ((self.tiles[tile]['coords'][0] + distance), (self.tiles[tile]['coords'][1]))
                self.tiles[tile]['coords'] = new_coords
        if direction is 'right':
            for tile in self.tiles:
                new_coords = ((self.tiles[tile]['coords'][0] - distance), (self.tiles[tile]['coords'][1]))
                self.tiles[tile]['coords'] = new_coords
