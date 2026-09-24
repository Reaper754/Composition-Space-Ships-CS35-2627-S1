class Health:
    def __init__(self, health):
        self.value = health

    def damage(self, amount):
        self.value -= amount
        if self.value <= 0:
            print("The ship has been destroyed.")
        else:
            print(f"The ship now has {self.value} health left.")


class Shields:
    def __init__(self, shield):
        self.value = shield

    def damage(self, amount):
        self.value -= amount
        if self.value <= 0:
            print("The shields are down.")
        else:
            print(f"The ship now has {self.value} shields left.")

class Engines:
    def __init__(self, power):
        self.power = power

    def full_power(self):
        self.power *= 100
        print(f"The ship is now moving at {self.power} knots.")

    def half_power(self):
        self.power *= 50
        print(f"The ship is now moving at {self.power} knots.")

    def stop(self):
        self.power *= 0
        print(f"The ship is now stationary.")

    def reverse(self):
        self.power *= 25
        print(f"The ship is now moving at {self.power} knots in reverse.")

class Weapons:
    def __init__(self, primary_weapon, primary_damage, secondary_weapon, secondary_damage):
        self.primary = primary_weapon
        self.primary_damage = primary_damage
        self.secondary = secondary_weapon
        self.secondary_damage = secondary_damage

    def shoot_p(self):
        print(f"Primary weapon did {self.primary_damage} to target.")

    def shoot_s(self):
        print(f"Secondary weapon did {self.secondary_damage} to target.")