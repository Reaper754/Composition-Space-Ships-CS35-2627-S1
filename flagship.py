from components import Health
from components import Shields
from components import Engines
from components import Weapons

class Flagship:
    def __init__(self):
        self.spaceship_class = "Flagship"
        self.health = Health(120, 120)
        self.shields = Shields(100, 100)
        self.engines = Engines(0)
        self.weapons = Weapons("Plasma Turrets", 50, "Ion Torpedoes", 100)
        self.speed = 1

    def stats(self):
        print(f"Ship stats:\n Class: {self.spaceship_class} \n Health: {self.health.value} \n Shields: {self.shields.value} \n Engines: {self.engines.power} \n Primary Weapon: {self.weapons.primary}\n Secondary Weapon {self.weapons.secondary} ")