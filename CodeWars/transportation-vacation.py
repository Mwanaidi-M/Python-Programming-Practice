"""
After a hard quarter in the office you decide to get some rest on a vacation. So you will book a flight
for yourself.

You will need a rental car in order for you to get around in your vacation. The manager of the car rental
makes you some good offers.

Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total.
Alternatively, if you rent the car for 3 or more days, you get $20 off your total.

Write a code that gives out the total amount for different days(d).
"""


def rental_car_cost(days):
    day_cost = 40
    total_cost = (day_cost * days)

    if days >= 7:
        total_cost = (day_cost * days) - 50
    elif days >= 3:
        total_cost = (day_cost * days) - 20

    return total_cost


print(rental_car_cost(1))
print(rental_car_cost(4))
print(rental_car_cost(7))
print(rental_car_cost(8))
