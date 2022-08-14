def invert(lst):
    """
    Given a set of numbers, return the additive inverse of each. Each positive becomes negatives,
    and the negatives become positives. For Example:

    invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
    invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
    invert([]) == []

    :param lst: list
    :return: list
    """

    if len(lst) == 0:
        return lst
    else:
        return [-num for num in lst if num == num]
