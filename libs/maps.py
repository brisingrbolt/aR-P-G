import pygame, os.path, images

class Grid(): ## Is it necessary to subclass this? Will investigate later
    def __init__(self):
        self.tiles = {}
        self.x = None
        self.y = None

class GridFromMap(Grid):
    def __init__(self, mapName):
        self.loaded = False

    def loadFromMap(self, mapName, mapDir = '../maps/'):
        if not images.initialized: images.init()

        # Check to make sure the file exists
        if not os.path.exists(mapDir + mapName):
            config.log(mapname + ': Map not found!', 'ERROR')
            return 
        
        # Actually load the file
        mapFile = open(mapDir + mapName, 'r')

        # Try reading the first line for width NOTE: This might change when multiple layers are implemented
        line = mapFile.readline()
        self.x = len(line.replace('\n', '').split())
        config.log('Map width: ' + self.x)
        f.seek(0)

        # Try reading number of lines for height NOTE: See above
        for i, l in enumerate(f):
            pass
        self.y = i + 1
        config.log('Map height: ' + self.y)
        f.seek(0)

        # Check to make sure all tiles actually exist?

        # Initalize tile dictionary
        x, y = 1, 1
        for i in range(x):
            for e in range(y):
                self.tiles[(x,y)] = {}
                self.tiles[(x,y)] = None
                self.tiles[(x,y)]['coords'] = (((x-1)tileSize),((y-1)*tileSize)) # NOTE: May need to change this, so that the maps scroll properly. In other words, starting location needs to be determined based on the player's location within the map.
                y += 1
            y = 1
            x += 1
        
        # Read in map data and fill self.tiles with image references, one layer for now
        
        self.loaded = True

    def display(self, screen, location):
        pass
