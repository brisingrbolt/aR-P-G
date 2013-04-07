import save, pygame, config
from cloak import Cloak
## from abilities import abilities

class Player:
    FRAME_DISPLAY_TIMES = 4 ## Should be a multiple of two
    
    frames = {};
    current_frame = 0;
    frame_display_count = 1;
    direction = 'down';
    def __init__(self, chosen_save_game = None): 
    
        # Instantiate player variables
        self.health = {}              # Self explanatory dictionary.
        self.mana = {}                # Also self explanatory.
        self.abilities = {}           # Dictionary of abilities, with the menu only displaying those currently usable
                                      # by the player.
        self.stats = {}               # Dictionary of stats, including the three attack types and two defense types.
        self.inv = {}                 # Need to implement, maybe in another class or a subclass?
        self.info = {}                # Dictionary of string descriptors for menus and such
        self.cloak = Cloak('mctague') # This is where the character's current cloak (form) is stored.
        self.cloaks = {}              # Plural of above. Dictionary to hold unlocked forms for image and special move
                                      # objects.
   
        # Load class attributes
        #self.health = classes[]['health']
        #self.mana = classes[]['mana']

    def initialize_frames(self):
        self.frames = self.cloak.get_frames()

    def set_direction(self, direction):
        self.direction = direction
        self.current_frame = 1;

    def get_next_frame(self):
        out = self.frames[self.direction][self.current_frame-1]
        if self.frame_display_count is not self.FRAME_DISPLAY_TIMES:
            self.frame_display_count += 1
            return out
        if self.current_frame < len(self.frames[self.direction]):
            self.current_frame += 1
        else:
            self.current_frame = 1
        self.frame_display_count = 1
        return out

    def get_current_frame(self):
        return self.frames[self.direction][self.current_frame-1]

    def set_cloak(self, cloak_name):
        self.cloak = self.cloaks[name]

    def add_cloak(self, cloak):
        self.cloak[name] = cloak.get_name()

    def load_cloak(self, name):
        self.stats = self.cloaks[name].get_stats_for_level(self.level)
        self.abilities = self.cloaks[name].get_abilities_for_level(self.level)
