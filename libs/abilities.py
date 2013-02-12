def get_abilities(player_class):
    out = {}
    for ability in abilities:
        if player_class in abilities[ability]['classes']:
            out[ability] = abilities[ability]
    return out

abilites = {
    'Fireball': {
        'classes': [
            'mage',
            'warrior'
        ],
        'bonus': {
            'magic': 3
        },
        'level': 1,
        'description': 'A flaming ball of fire.'
    },
    'Icy Breath': {
        'classes': [
            'mage'
        ],
        'bonus': {
            'magic': 5
        },
        'level': 3,
        'description': 'A freezing breath of ice.'
    },
    'Shield Bash': {
        'classes': [
            'warrior',
            'ranger'
        ],
        'bonus': {
            'melee': 3
        },
        'level': 1,
        'description': 'Bash the enemy with your shield.'
    },
    'Heated Metal': {
        'classes': [
            'warrior'
        ],
        'bonus': {
            'melee': 5
        },
        'level': 3,
        'description': 'Strike the enemy with your sword aflame.'
    },
    'Elven Arrow': {
        'classes': [
            'ranger'
        ],
        'bonus': {
            'ranged': 5
        },
        'level': 3
    },
    'Rapid Shot': {
        'classes': [
            'ranger'
            'mage'
        ],
        'bonus': {
            'ranged': 2,
            'magic': 2,
            'melee': 2 
        },
        'level': 1
    }
}
