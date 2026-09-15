# Composition: Build a Fleet of Spaceships

Create a program that models several different spaceships built from reusable component objects. Instead of putting all spaceship data and behaviour directly inside each ship class, create smaller component classes and use those objects as parts of different spaceships. This follows the composition slides’ focus on “has-a” relationships, reusable components, and modular design. 

Requirements:

* Create at least three reusable component classes, such as `Engine`, `Shield`, `Weapon`, `CargoHold`, or another appropriate spaceship component.
* Each component class must contain at least one property and one method related to its responsibility. For example, an `Engine` might store its speed and have a method that activates it.
* Create at least three different spaceship classes, such as `Fighter`, `Cruiser`, `CargoShip`, or `Dreadnought`.
* Each spaceship class must create and store at least two component objects as properties. Different spaceship classes should be able to reuse the same component classes with different values.
* At least one component class must be reused by three different spaceship classes. For example, `Fighter`, `Cruiser`, and `CargoShip` could all contain an `Engine`, but each could create an engine with different specifications.
* Give each spaceship class at least one method that coordinates the behaviour of its components rather than duplicating the component's code.
* Create at least one object from each spaceship class and demonstrate how their different combinations of components give the ships different capabilities.

The important relationship is that each spaceship **has** component objects inside it. The same component classes should be reusable when building different kinds of spaceships, rather than rewriting similar functionality separately inside every spaceship class.

---

## File Structure

```text
spaceship_fleet/
│
├── components.py
├── ship_type_1.py
├── ship_type_2.py
├── ship_type_3.py
└── main.py
```

Students should replace `ship_type_1.py`, `ship_type_2.py`, and `ship_type_3.py` with filenames that match the spaceship classes they design.

For example, a student could choose:

```text
spaceship_fleet/
│
├── components.py
├── interceptor.py
├── exploration_ship.py
├── carrier.py
└── main.py
```

* `components.py`

  * Contains all reusable spaceship component classes.
  * Examples could include engines, shields, weapons, cargo systems, sensors, or other components designed by the student.
  * Components should be designed so they can be reused by multiple spaceship classes where appropriate.

* Each spaceship file

  * Contains one spaceship class designed by the student.
  * Each spaceship class should create and store its required component objects.
  * Each spaceship class should contain methods that coordinate the behaviour of its components.
  * Each spaceship class must be placed in its own `.py` file.

* `main.py`

  * Imports each spaceship class.
  * Creates at least one object from each spaceship class.
  * Demonstrates how the different ships use their components.
  * Shows that component classes can be reused across different types of spaceships.
  * All code used to run and test the finished program should be placed here.

---

## Assessment

| Assessment Item                    | Criteria                                                                                                                                                               |  Marks |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -----: |
| ☐ Component Classes                | Creates at least three component classes. Each component contains at least one property and one method related to its responsibility.                                  |      4 |
| ☐ Spaceship Classes                | Creates at least three different spaceship classes, such as a `Fighter`, `Cruiser`, `CargoShip`, or `Dreadnought`.                                                     |      3 |
| ☐ Components Inside Spaceships     | Each spaceship creates and stores at least two component objects as properties.                                                                                        |      4 |
| ☐ Reusable Components              | At least one component class is used by all three spaceship classes, with different values or configurations where appropriate.                                        |      3 |
| ☐ Coordinating Component Behaviour | Each spaceship class contains at least one method that uses or coordinates one or more of its component objects rather than recreating that component's functionality. |      3 |
| ☐ Different Ship Configurations    | The different spaceship classes use their components in meaningfully different combinations or configurations that reflect the purpose of each ship.                   |      2 |
| ☐ Complete Working Program         | Creates at least one object from each spaceship class and successfully demonstrates the functionality of its components without errors.                                |      1 |
|                                    | **Total**                                                                                                                                                              | **20** |

