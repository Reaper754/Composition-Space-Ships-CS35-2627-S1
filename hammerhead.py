from components import Health
from components import Shields
from components import Engines
from components import Weapons

class Hammerhead:
    def __init__(self):
        self.spaceship_class = "Hammerhead"
        self.health = Health(300)
        self.shields = Shields(0)
        self.engines = Engines(3)
        self.weapons = Weapons("Ram", 400, "Anti-Aircraft Turrets", 20)