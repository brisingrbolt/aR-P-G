import pygame, os.path, images, config

class Grid(): ## Is it necessary to subclass this? Will investigate later
    def __init__(self):
        pass

class GridFromMap(Grid):
    def __init__(self, mapName):
        self.tiles = {}
        self.width = None
        self.height = None
        self.tileSize = 32
        self.loaded = False

        self.loadFromMap(mapName)

    def loadFromMap(self, mapName, mapDir = 'maps/'):
        if not images.initialized: images.init()

        # Check to make sure the file exists
        if not os.path.exists(mapDir + mapName):
            config.log(mapName + ': Map not found!', 'ERROR')
            return 
        
        # Actually load the file
        mapFile = open(mapDir + mapName, 'r')

        # Try reading the first line for width NOTE: This might change when multiple layers are implemented
        line = mapFile.readline()
        self.width = len(line.replace('\n', '').split())
        config.log('Map width: ' + str(self.width))
        mapFile.seek(0)

        # Try reading number of lines for height NOTE: See above
        for i, l in enumerate(mapFile):
            pass
        self.height = i + 1
        config.log('Map height: ' + str(self.height))
        mapFile.seek(0)

        # Check to make sure all tiles actually exist?

        # Initalize tile dictionary
        x, y = 1, 1
        for i in range(self.width):
            for e in range(self.height):
                self.tiles[(x,y)] = {}
                self.tiles[(x,y)]['coords'] = (((x-1)*self.tileSize),((y-1)*self.tileSize)) # NOTE: May need to change this, so that the maps scroll properly. In other words, starting location needs to be determined based on the player's location within the map.
                y += 1
            y = 1
            x += 1
        
        # Read in map data and fill self.tiles with image references, one layer for now
        x, y = 1, 1
        for line in mapFile.readlines():
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

    def display(self, screen, location = None):
        if not self.loaded:
            config.log('Grid is not loaded!', 'ERROR')
            return
        for tile in self.tiles:
            for i in range(3):
                image = images.get(self.tiles[tile][i+1])
                if not image == None: screen.blit(image, self.tiles[tile]['coords'])
                
        config.log('Grid drawn to screen')

    def move(self, direction):
        if not self.loaded:
            config.log('Grid is not loaded!', 'ERROR')
            return
        if direction == 'up':
            for tile in self.tiles:
                newCoords = ( (self.tiles[tile]['coords'][0]), (self.tiles[tile]['coords'][1] + 4) )
                self.tiles[tile]['coords'] = newCoords
        if direction == 'down':
            for tile in self.tiles:
                newCoords = ( (self.tiles[tile]['coords'][0]), (self.tiles[tile]['coords'][1] - 4) )
                self.tiles[tile]['coords'] = newCoords
        if direction == 'left':
            for tile in self.tiles:
                newCoords = ( (self.tiles[tile]['coords'][0] + 4), (self.tiles[tile]['coords'][1]) )
                self.tiles[tile]['coords'] = newCoords
        if direction == 'right':
            for tile in self.tiles:
                newCoords = ( (self.tiles[tile]['coords'][0] - 4), (self.tiles[tile]['coords'][1]) )
                self.tiles[tile]['coords'] = newCoords
