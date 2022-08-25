def list_capital_indexes(strng):
    """
    Function that takes a single parameter, which is a string. The function should return a list of all the
    indexes in the string that have capital letters.

    For example, calling list_capital_indexes("HeLlO") should return the list [0, 2, 4].
    Args:
        strng:

    Returns:
        capital_list: <list>
    """

    # create empty list to hold the index values
    capital_list = []

    # loop through the length of the string and if the letter at the specified index == the letter at the
    # index in uppercase then add that index to the list
    for st_index in range(len(strng)):
        if strng[st_index] == strng[st_index].upper():
            capital_list.append(st_index)

    return capital_list


print(list_capital_indexes("HeLlO"))
