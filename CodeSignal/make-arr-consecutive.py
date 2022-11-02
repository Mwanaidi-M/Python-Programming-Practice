"""
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday,
each statue having an non-negative integer size. Since he likes to make things perfect,
he wants to arrange them from smallest to largest so that each statue will be bigger than
the previous one exactly by 1. He may need some additional statues to be able to accomplish
that. Help him figure out the minimum number of additional statues needed.

Example:

For statues = [6, 2, 3, 8], the output should be solution(statues) = 3.
Ratiorg needs statues of sizes 4, 5 and 7.
"""


def solution(n):
    # get minimum & maximum value in array n
    min_val = min(n)
    max_val = max(n) + 1

    # initialize a counter to count how many values are needed
    count = 0

    # create new array to hold complete array
    new_arr = []

    for num in range(min_val, max_val):
        # append all values in the given range to the new array
        new_arr.append(num)

    for num in new_arr:
        # check if value in new array is in old array; if not increase count by 1
        if num not in n:
            count += 1

    print(new_arr)
    return count
