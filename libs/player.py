import save
from classes import classes     # NOTE: Currently, the only affect class will have on the player is what abilities he will be able to use and also base stat levels. Should we do separate pixelart for each class?
from abilities import abilities

class Player:
    def __init__(self, player_class, chosen_save_game = ""): 
    
        # Instantiate player variables
        self.health = {}            # Self explanatory dictionary.
        self.mana = {}              # Also self explanatory.
        self.abilities = {}         # Dictionary of abilities, with the menu only displaying those currently usable by the player.
        self.stats = {}             # Dictionary of stats, including the three attack types and two defense types.
        self.inv = {}               # Need to implement, maybe in another class or a subclass?
        self.info = {}              # Dictionary of string descriptors for menus and such
    
        if save.exists(chosen_save_game):
            # Load previous save!
        else: # Should only run the first time. Afterwards, it should be loading from a savegame above.
            if not player_class in classes:
                config.log('Error: unknown class!', 'ERROR') # Make this a log function somewhere else?
                return
            self.health = classes[player_class]['health']
            self.mana = classes[player_class]['mana']
            self.abilities = abilities.get_abilities(player_class)
            self.stats = classes[player_class]['stats']
