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
                'hero-up-4.png',
                'hero-up-5.png'
            ],
            'down': [
                'hero-down-1.png',
                'hero-down-1.png',
                'hero-down-1.png',
                'hero-down-1.png',
                'hero-down-1.png'
            ],
            'left': [
                'hero-west-1.png',
                'hero-west-2.png',
                'hero-west-3.png',
                'hero-west-4.png',
                'hero-west-3.png'
            ],
            'right': [
                'hero-east-1.png',
                'hero-east-2.png',
                'hero-east-3.png',
                'hero-east-4.png',
                'hero-east-3.png'
            ]
        }
    }
}
