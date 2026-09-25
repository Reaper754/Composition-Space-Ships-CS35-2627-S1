from components import Health
from components import Shields
from components import Engines
from components import Weapons

class Dreadnought:
    def __init__(self):
        self.spaceship_class = "Dreadnought"
        self.health = Health(100, 100)
        self.shields = Shields(110, 110)
        self.engines = Engines(0)
        self.weapons = Weapons("Laser Beams", 150, "Rockets", 200)
        self.speeed = 2

    def stats(self):
        print(f"Ship stats:\n Class: {self.spaceship_class} \n Health: {self.health.value} \n Shields: {self.shields.value} \n Engines: {self.engines.power} \n Primary Weapon: {self.weapons.primary}\n Secondary Weapon {self.weapons.secondary} ")