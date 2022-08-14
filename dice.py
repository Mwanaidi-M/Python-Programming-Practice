import random


class Die:
    """ Make a class Die with one attribute called sides, which has a default
        value of 6. Write a method called roll_die() that prints a random number
        between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times.
        Make a 10-sided die and a 20-sided die. Roll each die 10 times.
    """

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return random.randint(1, self.sides)


die1 = Die()
results = []
for die_round in range(10):
    res = die1.roll_die()
    results.append(res)

print(f"Casting dice with 6-sides results: {results}")


die2 = Die(10)
results = []
for die_round in range(10):
    res = die2.roll_die()
    results.append(res)

print(f"\nCasting dice with 10-sides results: {results}")

die3 = Die(20)
results = []
for die_round in range(10):
    res = die3.roll_die()
    results.append(res)

print(f"\nCasting dice with 20-sides results: {results}")
