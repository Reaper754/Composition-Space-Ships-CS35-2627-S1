from components import Health
from components import Shields
from components import Engines
from components import Weapons

class Dreadnought:
    def __init__(self):
        self.spaceship_class = "Dreadnought"
        self.health = Health(100)
        self.shields = Shields(110)
        self.engines = Engines(2)
        self.weapons = Weapons("Laser Beams", 150, "Rockets", 200)