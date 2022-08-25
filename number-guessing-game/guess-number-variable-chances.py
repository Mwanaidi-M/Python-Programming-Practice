import random


# variable to hold the chances a player uses
player_chances = 0

# get player's number guess
player_choice = ""


def get_comp_number(start_val, stop_val):
    """
    Function to generate a random number for the computer within a given range.
    Args:
        start_val: <int>
        stop_val: <int>

    Returns:
        comp_number: <int>
    """

    comp_number = random.randint(start_val, stop_val)

    return comp_number


number_random = get_comp_number(1, 100)

print(number_random)

# start a loop to run the program
while True:
    # prompt player for their guess
    player_choice = int(input("Guess the randomly generated number from 1 to 100: \t"))

    # increment the chance by 1
    player_chances += 1

    # give player hints whether the guess is greater or smaller than the computer guess
    if player_choice > number_random:
        print(f"My number is less than {player_choice}.\n")

    elif player_choice < number_random:
        print(f"My number is greater than {player_choice}.\n")

    # if the player's guess is correct, show player success message, chances they took & break the loop
    else:
        print(f"\nYay! You got it right. The random number is indeed {player_choice} \U0001F973.")
        print(f"It took you {player_chances} attempts to guess this number.")
        break

