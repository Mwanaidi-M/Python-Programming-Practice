# ROCK-PAPER-SCISSORS
from random import choice

game_choices = ['rock', 'paper', 'scissors']


def get_computer_choice():
    """
    Function to get the computer's choice from the R-P-S choices at random.

    :return: comp_choice <str>
    """
    comp_choice = choice(game_choices)

    # print(f"Computer Chose: {comp_choice}.")

    return comp_choice


def get_player_choice():
    """
    Function to get the user's choice input.
    The choice selected should be case-insensitive.

    :return: user_choice <str>
    """

    user_choice = ''

    while user_choice.lower() not in game_choices:
        user_choice = input("\nInput weapon name:\t")

    user_choice = user_choice.lower()

    # print(f"You have selected: {user_choice}")

    return user_choice


def game():
    """
    Function to play the R-P-S game 5 times to keep score
    Rules are:
    - Rock wins against scissors
    - paper wins against rock
    - scissors wins against paper
    """

    comp_score = player_score = 0

    msg = " Rock / Paper / Scissors. Choose your weapon. "

    print(f"{msg:-^100}")

    for round_played in range(5):
        computer = get_computer_choice()
        player = get_player_choice()

        if computer == player:
            print(f"It's a tie!")

        elif computer == 'rock' and player == 'paper':
            print(f"\nYou win! Paper beats Rock!")
            player_score += 1

        elif computer == 'rock' and player == 'scissors':
            print(f"\nYou loose! Rock beats Scissors!")
            comp_score += 1

        elif computer == 'paper' and player == 'rock':
            print(f"\nYou loose! Paper beats Rock!")
            comp_score += 1

        elif computer == 'paper' and player == 'scissors':
            print(f"\nYou win! Scissors beats Paper!")
            player_score += 1

        elif computer == 'scissors' and player == 'paper':
            print(f"\nYou loose! Scissors beats Paper!")
            comp_score += 1

        elif computer == 'scissors' and player == 'rock':
            print(f"\nYou win! Rock beats scissors!")
            player_score += 1

        print(f"The computer selected: {computer}")
        print(f"You selected: {player}")

    print(f"\nComp Score: {comp_score}\nPlayer Score: {player_score}")


game()
# print(get_computer_choice())
# print(get_player_choice())
