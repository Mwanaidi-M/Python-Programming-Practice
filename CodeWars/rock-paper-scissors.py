"""
You have to return which player won! In case of a draw return Draw!.
- Scissor beats Paper
- Paper beats Rock
- Rock beats Scissors

Examples(Input1, Input2 --> Output):

"scissors", "paper" --> "Player 1 won!"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!"
"""


def rps(p1, p2):
    msg = ''
    if (p1 == 'scissors' and p2 == 'rock') or (p1 == 'rock' and p2 == 'paper') or (p1 == 'paper' and p2 == 'scissors'):
        msg = 'Player 2 won!'
    elif (p1 == 'scissors' and p2 == 'paper') or (p1 == 'paper' and p2 == 'rock') or (p1 == 'rock' and p2 == 'scissors'):
        msg = 'Player 1 won!'
    elif p1 == p2:
        msg = 'Draw!'

    return msg


print(rps('scissors', 'rock'))
print(rps('rock', 'rock'))
print(rps('rock', 'scissors'))
