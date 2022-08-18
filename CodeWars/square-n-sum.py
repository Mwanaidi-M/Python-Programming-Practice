def square_sum(numbers):
    """
    Complete the square sum function so that it squares each number passed into
    it and then sums the results together.

    For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
    Args:
        numbers: <list>

    Returns:
        result: <int>
    """

    # create a list of the power of the values then return their sum
    result = sum([pow(val, 2) for val in numbers])

    return result
