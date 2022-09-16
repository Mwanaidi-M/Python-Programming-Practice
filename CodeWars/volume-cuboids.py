from functools import reduce


def find_difference(a, b):
    """
    Create a program that will take two lists of integers, a and b.
    Each list will consist of 3 positive integers above 0, representing the dimensions of
    cuboids a and b. You must find the difference of the cuboids' volumes regardless of
    which is bigger.
    """
    # get the volume of list a & b
    va = reduce(lambda n1, n2: n1 * n2, a)
    vb = reduce(lambda n1, n2: n1 * n2, b)

    # return the absolute value of the difference
    return abs(va-vb)