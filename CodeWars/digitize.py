def digitize(num):
    """
    Given a random non-negative number, you have to return the digits of this number within
    an array in reverse order.

    Example(Input => Output):
    348597 => [7,9,5,8,4,3]
    0 => [0]
    Args:
        num: int

    Returns: list
    """

    # create a list of the numbers by converting the whole number to a string then convert
    # the digits into integers. Reverse the list afterwards
    # number = [int(n) for n in str(num)]
    # number.reverse()
    #
    # return number

    # found another alternative way
    return list(map(int, str(num)[::-1]))


print(digitize(348597))