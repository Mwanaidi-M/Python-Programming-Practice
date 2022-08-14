import random

"""
Make a list or tuple containing a series of 10 numbers and five letters. Randomly select four 
numbers or letters from the list and print a message saying that any ticket matching these 
four numbers or letters wins a prize.

You can use a loop to see how hard it might be to win the kind of lottery you just modeled. 
Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your 
ticket wins. Print a message reporting how many times the loop had to run to give you a winning ticket.
"""


def get_winning_ticket():
    """ Function to generate the winning lotto combination. """
    winning_lotto = []

    # while the list doesn't have 4 xters,
    while len(winning_lotto) < 4:
        # generate a random value
        match_obj = random.choice(lottery_numbers)

        # to avoid adding duplicates, only add to the list as long as the value isn't already in the list.
        if match_obj not in winning_lotto:
            winning_lotto.append(match_obj)

    return winning_lotto


def make_my_ticket():
    """ Function to generate a user's ticket randomly using the same method for get_winning_ticket() """
    my_ticket = []

    while len(my_ticket) < 4:
        match_obj = random.choice(lottery_numbers)

        if match_obj not in my_ticket:
            my_ticket.append(match_obj)

    return my_ticket


def check_ticket(winning_tkt, your_tkt):
    """ Check your ticket against the winning tickt to see if you have a winner. """

    # check if the value in the winning lotto is in the user's ticket
    for value in your_tkt:
        if value not in winning_tkt:
            return False

    return True


# out list of numbers & letters
lottery_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 'f', 'g', 'h', 'i', 'j']

winner = get_winning_ticket()

# personal_ticket = make_my_ticket()

# print(f"The winning combination is {winner}")
# print(f"My own ticket: {personal_ticket}")
#
# print(check_ticket(winner,personal_ticket))

rounds_played = 0
won = False

# setting a value for the number of tries so the loop doesn't run forever
max_tries = 1_000_000

while not won:
    personal_ticket = make_my_ticket()
    ticket_winner = check_ticket(winner, personal_ticket)

    rounds_played += 1

    if rounds_played >= max_tries:
        break

if won:
    print(f"We have a winner.\nYour ticket:{personal_ticket}\nWinning ticket:{winner}")

else:
    print(f"You tried {rounds_played} times but no luck.")
    print(f"\nYour ticket:{personal_ticket}\nWinning ticket:{winner}")
