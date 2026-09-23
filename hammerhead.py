from components import Health
from components import Shields
from components import Engines
from components import Weapons

class Hammerhead:
    def __init__(self):
        self.spaceship_class = "Hammerhead"
        self.toughness = 10
        self.speed = 2
        self.shield_strength = 0
        self.health = Health()
        self.shields = Shields()
        self.engines = Engines()
        self.weapons = Weapons("Ram", "Anti-Aircraft Turrets")