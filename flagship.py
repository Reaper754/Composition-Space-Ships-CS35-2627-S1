from components import Health
from components import Shields
from components import Engines
from components import Weapons

class Flagship:
    def __init__(self):
        self.spaceship_class = "Flagship"
        self.health = Health(120)
        self.shields = Shields(100)
        self.engines = Engines(1)
        self.weapons = Weapons("Plasma Turrets", 50, "Ion Torpedoes", 100)