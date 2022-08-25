# The goal of this challenge is to analyze a string to check if it contains two of the
# same letter in a row. For example, the string "hello" has l twice in a row, while the
# string "nono" does not have two identical letters in a row.

def double_lett(strng):
    """
     Function that takes a single parameter,a string. The function must return True if there
     are two identical letters in a row in the string, and False otherwise.
    Args:
        strng: <str>
    Returns:
        ans: <bool>
    """

    # loop through the length of the string -1(to avoid Index range error
    for indx in range(len(strng) - 1):
        # check if same letters follow each other, return True
        if strng[indx] == strng[indx+1]:
            return True
    return False


print(double_lett("hello"))
print(double_lett("nono"))
