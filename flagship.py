from components import Health
from components import Shields
from components import Engines
from components import Weapons

class Flagship:
    def __init__(self):
        self.spaceship_class = "Flagship"
        self.toughness = 5
        self.speed = 1
        self.shield_strength = 2
        self.health = Health()
        self.shields = Shields()
        self.engines = Engines()
        self.weapons = Weapons("Plasma Turrets", "Ion Torpedoes")