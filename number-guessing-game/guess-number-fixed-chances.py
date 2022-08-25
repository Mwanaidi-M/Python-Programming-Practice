import random

# give the player a fixed number of chances to guess the number
player_chances = 5

# initialize the players input to an empty string
player_choice = ""


def get_comp_number(start_range, stop_range):
    """ Get a random number from the computer within the given range. """
    comp_number = random.randint(start_range, stop_range)

    return comp_number


# get a random number between 1 & 100
random_num = get_comp_number(1, 100)

# start a loop to prompt the player for a number
while True:
    # get the player's number & reduce their chances by 1 for every input.
    player_choice = int(input("Enter your guess: \t"))
    player_chances -= 1

    # give hints to the player if their number is less or greater than the random number
    if player_choice > random_num:
        print(f"The number is less than {player_choice}\n")
    elif player_choice < random_num:
        print(f"The number is greater than {player_choice}\n")
    else:
        # if they give the correct input, show a success message and exit the loop/stop program
        print(f"Yay! You got it right. The random number is indeed {player_choice} \U0001F973")
        break

    # if the player's chances are greater than 0, show them how many chances they have left,
    # else if chances are up, exit the loop and tell player what the random number is.
    if player_chances > 0:
        print(f"Number of chances left: {player_chances}.\n")
    elif player_chances == 0:
        print(f"\nThe random number was: {random_num}")
        break

