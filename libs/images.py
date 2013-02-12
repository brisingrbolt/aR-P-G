import pygame
import config

initialized = False
image_dir = './images/'

def init(): # This is where the images are converted from indexes to actual images.
    images[1] = pygame.image.load(image_dir + 'grass.png')
    images[2] = pygame.image.load(image_dir + 'placeholder.png')
    initialized = True

def get(index):
    if not index > 0:
        return None
    if images[index] is None:
        config.log(images[index] + ': No such image.', 'ERROR')
    return images[index]

images = {
    1: None,
    2: None
}
