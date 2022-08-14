def find_runner_up():
    """Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
        You are given 'n' scores. Store them in a list and find the score of the runner-up.
    """
    # get the number of scores to be input
    size = int(input('Your runner up score size:\t'))

    # get the input as int in one line then split them using 'map' function then store the values in a set to remove
    # duplicates
    scores = set(map(int, input().split()))

    # save the scores as a list in a new variable
    runner_up = list(scores)
    print(scores)

    # sort the list
    runner_up.sort()

    # get the runner-up value(second-last) using negative indexing
    print(runner_up[-2])


find_runner_up()