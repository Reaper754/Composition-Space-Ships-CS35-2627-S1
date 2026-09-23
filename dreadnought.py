from components import Health
from components import Shields
from components import Engines
from components import Weapons

class Dreadnought:
    def __init__(self):
        self.spaceship_class = "Dreadnought"
        self.toughness = 3
        self.speed = 1.5
        self.shield_strength = 1
        self.health = Health()
        self.shields = Shields()
        self.engines = Engines()
        self.weapons = Weapons("Laser Beams", "Rockets")