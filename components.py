class Health:
    def __init__(self):
        self.value = 100

class Shields:
    def __init__(self):
        self.value = 100

class Engines:
    def __init__(self):
        self.power = 0

class Weapons:
    def __init__(self, primary_weapon, secondary_weapon):
        self.primary = primary_weapon
        self.secondary = secondary_weapon