def divisors(num):
    """
    Count the number of divisors of a positive integer n.

    Examples (input --> output):
    4 --> 3 (1, 2, 4)
    5 --> 2 (1, 5)
    12 --> 6 (1, 2, 3, 4, 6, 12)
    30 --> 8 (1, 2, 3, 5, 6, 10, 15, 30)
    """

    # create list of numbers that are divisible by num
    list_divisors = [val for val in range(1, num + 1) if num % val == 0]

    # return the length of the list
    return len(list_divisors)