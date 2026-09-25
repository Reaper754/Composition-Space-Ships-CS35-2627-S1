from components import Health
from components import Shields
from components import Engines
from components import Weapons

class Hammerhead:
    def __init__(self):
        self.spaceship_class = "Hammerhead"
        self.health = Health(300, 300)
        self.shields = Shields(0, 0)
        self.engines = Engines(0)
        self.weapons = Weapons("Ram", 400, "Anti-Aircraft Turrets", 20)
        self.speed = 3

    def stats(self):
        print(f"Ship stats:\n Class: {self.spaceship_class} \n Health: {self.health.value} \n Shields: {self.shields.value} \n Engines: {self.engines.power} \n Primary Weapon: {self.weapons.primary}\n Secondary Weapon {self.weapons.secondary} ")