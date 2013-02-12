import pygame, config

initialized = False
imageDir = './images/'

def init(): # This is where the images are converted from indexes to actual images.
    images[1] = pygame.image.load(imageDir + 'grass.png')
    images[2] = pygame.image.load(imageDir + 'placeholder.png')
    initialized = True

def get(index):
    if not index > 0:
        return None
    if images[index] == None:
        config.log(images[index] + ': No such image.', 'ERROR')
    return images[index]

images = {
    1: None,
    2: None
}
