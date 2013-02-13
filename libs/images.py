import pygame
import config

initialized = False
image_dir = './images/'
loaded_tileset = ''

def initialize(tileset): # This is where the images are converted from indexes to actual images.
    global loaded_tileset
    clear()
    if tileset not in tilesets:
        config.log('No such tileset: ' + tileset, 'ERROR')
        return
    for tile in tilesets[tileset]['tiles']:
        images[tile] = pygame.image.load(image_dir + tilesets[tileset]['tiles'][tile])

    loaded_tileset = tileset
    tilesets[tileset]['initialized'] = True

def isInitialized(tileset):
    return tilesets[tileset]['initialized']

def clear():
    global loaded_tileset
    images = {}
    loaded_tileset = ''
    for tileset in tilesets:
        tilesets[tileset]['initialized'] = False

def get(index):
    global loaded_tileset
    if not loaded_tileset:
        config.log('No tileset loaded.', 'ERROR')
        return None
    if not index > 0:
        return None
    if tilesets[loaded_tileset]['tiles'][index] is None:
        config.log(images[loaded_tileset]['tiles'][index] + ': No such image.', 'ERROR')
    return images[index]

tilesets = {
    'greenland': {
        'tiles': {
            1: 'grass.png',
            2: 'oak-tree-topleft.png',
            3: 'oak-tree-topright.png',
            4: 'oak-tree-botleft.png',
            5: 'oak-tree-botright.png',
            6: 'placeholder.png',
        },
        'initialized': False
    }
}

images = {}
