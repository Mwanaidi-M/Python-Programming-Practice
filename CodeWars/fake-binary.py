def bin_fake(string):
    """
    Given a string of digits, you should replace any digit below 5 with '0' and any digit
    5 and above with '1'. Return the resulting string.
    Args:
        string: str
    Returns: str
    """

    new_str = ['0' if int(st) < 5 else '1' for st in string]

    return ''.join(new_str)


print(bin_fake('45385593107843568'))
