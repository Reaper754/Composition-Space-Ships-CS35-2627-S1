from flagship import Flagship
from dreadnought import Dreadnought
from hammerhead import Hammerhead

flagship = Flagship()
dreadnought = Dreadnought()
hammerhead = Hammerhead()

select = """Choose your Spaceship:
1 for Flagship | 2 for Dreadnought | 3 for Hammerhead | 4 for exit\n"""

message = """Enter an input: 
| Shoot | Damage | Engines | Repair | Stats |\n"""

option_shoot = """Which weapon do you want to fire:
Primary | Secondary\n """

damage = "How much damage does the ship take: "

shield_damage = "How much damage do the shields sustain: "

throttle = """Which speed should the ship go:
Full Speed | Half Speed | Stopped | Reverse """

fix = "How much does the ship repair:"

while True:
    try:
        ship = int(input(select))
        if ship == 1:
            print("type exit to quite.")
            user_input = input(message).strip().lower()
            if user_input == "shoot":
                fire_type = input(option_shoot).strip().lower()
                if fire_type == "primary":
                    flagship.weapons.shoot_p()
                elif fire_type == "secondary":
                    flagship.weapons.shoot_s()
            if user_input == "damage":
                if flagship.shields.value > 0:
                    print("Shields are still up.")
                    amount = int(input(shield_damage))
                    flagship.shields.damage(amount)
                else:
                    amount = int(input(damage))
                    flagship.health.damage(amount)
            if user_input == "engines":
                    speed = input(throttle).strip().lower()
                    if speed == "full speed":
                        flagship.engines.power = flagship.speed
                        flagship.engines.full_power()
                    elif speed == "half speed":
                        flagship.engines.power = flagship.speed
                        flagship.engines.half_power()
                    elif speed == "stopped":
                        flagship.engines.power = flagship.speed
                    elif speed == "reverse":
                        flagship.engines.power = flagship.speed
                        flagship.engines.reverse()
            if user_input == "repair":
                amount = int(input(fix))
                if flagship.shields.value <= 0 and flagship.health.value < flagship.health.max:
                    flagship.health.value = amount
                    if flagship.health.value > flagship.health.max:
                        flagship.health.value = flagship.health.max
                if flagship.shields.value <= 0 and flagship.health.value == flagship.health.max:
                    flagship.shields.value = amount
                    if flagship.shields.value > flagship.shields.max:
                        flagship.shields.value = flagship.shields.max
            if user_input == "stats":
                flagship.stats()
            else:
                if user_input == "exit":
                    break
                print("Invalid command.")
        elif ship == 2:
            print("type exit to quite.")
            user_input = input(message).strip().lower()
            if user_input == "shoot":
                fire_type = int(input(option_shoot))
                if fire_type == 1:
                    dreadnought.weapons.shoot_p()
                elif fire_type == 2:
                    dreadnought.weapons.shoot_s()
            if user_input == "damage":
                if dreadnought.shields.value > 0:
                    print("Shields are still up.")
                    amount = int(input(shield_damage))
                    dreadnought.shields.damage(amount)
                else:
                    amount = int(input(damage))
                    dreadnought.health.damage(amount)
            if user_input == "engines":
                    speed = input(throttle).strip().lower()
                    if speed == "full speed":
                        dreadnought.engines.power = flagship.speed
                        dreadnought.engines.full_power()
                    elif speed == "half speed":
                        dreadnought.engines.power = flagship.speed
                        dreadnought.engines.half_power()
                    elif speed == "stopped":
                        dreadnought.engines.power = flagship.speed
                    elif speed == "reverse":
                        dreadnought.engines.power = flagship.speed
                        dreadnought.engines.reverse()
            if user_input == "repair":
                amount = int(input(fix))
                if dreadnought.shields.value <= 0 and dreadnought.health.value < dreadnought.health.max:
                    dreadnought.health.value = amount
                    if dreadnought.health.value > dreadnought.health.max:
                        dreadnought.health.value = dreadnought.health.max
                if dreadnought.shields.value <= 0 and dreadnought.health.value == dreadnought.health.max:
                    dreadnought.shields.value = amount
                    if dreadnought.shields.value > dreadnought.shields.max:
                        dreadnought.shields.value = dreadnought.shields.max
            if user_input == "stats":
                dreadnought.stats()
            else:
                if user_input == "exit":
                    break
                print("Invalid command.")
        elif ship == 3:
            print("type exit to quite.")
            user_input = input(message).strip().lower()
            if user_input == "shoot":
                fire_type = int(input(option_shoot))
                if fire_type == 1:
                    hammerhead.weapons.shoot_p()
                    hammerhead.health.value -= 50
                    print(f"{hammerhead.spaceship_class} is now at {hammerhead.health.value}.")
                elif fire_type == 2:
                    hammerhead.weapons.shoot_s()
            if user_input == "damage":
                if hammerhead.shields.value > 0:
                    print("Shields are still up.")
                    amount = int(input(shield_damage))
                    hammerhead.shields.damage(amount)
                else:
                    amount = int(input(damage))
                    hammerhead.health.damage(amount)
            if user_input == "engines":
                    speed = input(throttle).strip().lower()
                    if speed == "full speed":
                        hammerhead.engines.power = flagship.speed
                        hammerhead.engines.full_power()
                    elif speed == "half speed":
                        hammerhead.engines.power = flagship.speed
                        hammerhead.engines.half_power()
                    elif speed == "stopped":
                        hammerhead.engines.power = flagship.speed
                    elif speed == "reverse":
                        hammerhead.engines.power = flagship.speed
                        hammerhead.engines.reverse()
            if user_input == "repair":
                amount = int(input(fix))
                if hammerhead.shields.value <= 0 and hammerhead.health.value < hammerhead.health.max:
                    hammerhead.health.value = amount
                    if hammerhead.health.value > hammerhead.health.max:
                        hammerhead.health.value = hammerhead.health.max
                if hammerhead.shields.value <= 0 and hammerhead.health.value == dreadnought.health.max:
                    hammerhead.shields.value = amount
                    if hammerhead.shields.value > hammerhead.shields.max:
                        hammerhead.shields.value = hammerhead.shields.max
            if user_input == "stats":
                hammerhead.stats()
            else:
                if user_input == "exit":
                    break
                print("Invalid command.")
        else:
            if ship == 4:
                break
            print("Invalid command.")
    except ValueError:
        print("Invalid input")
