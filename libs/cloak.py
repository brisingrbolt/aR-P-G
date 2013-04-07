import pygame

class Cloak:
    def __init__(self, name):
        self.stats = {}
        self.name = name
        self.abilities = {}
        self.images = cloaks[name]['images']
        pass

    def get_stats_for_level(self, level):
        pass

    def get_abilities_for_level(self, level):
        pass

    def get_frames(self):
        out = self.images
        for direction in out:
            index = 0
            for frame in out[direction]:
                out[direction][index] = pygame.image.load("images/" + frame)
                index += 1
        return out

cloaks = {
    'mctague': {
        'images': {
            'up': [
                'hero-up-1.png',
                'hero-up-2.png',
                'hero-up-3.png',
                'hero-up-4.png'
            ],
            'down': [
                'hero-down-1.png',
                'hero-down-2.png',
                'hero-down-3.png',
                'hero-down-4.png'
            ],
            'left': [
                'hero-left-1.png',
                'hero-left-2.png',
                'hero-left-3.png',
                'hero-left-4.png'
            ],
            'right': [
                'hero-right-1.png',
                'hero-right-2.png',
                'hero-right-3.png',
                'hero-right-4.png'
            ]
        }
    }
}
