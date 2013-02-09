import pygame, config

initialized = False
imageDir = './images/'

def init(): # This is where the images are converted from indexes to actual images.
    images[001] = pygame.image.load(imageDir + 'grass.png')
    images[002] = pygame.image.load(imageDir + 'tree.png')
    initialized = True

def get(index):
    if images[index] == None:
        config.log(images[index] + ': No such image.', 'ERROR')
    return images[index]

images = {
    001: null,
    002: null
}
