def formatted_number(number):
    """
    Given an integer, number, print the following values for each integer 1 from number to :
    1. Decimal
    2. Octal
    3. Hexadecimal (capitalized)
    4. Binary
    The four values must be printed on a single line in the order specified
    above for each i from 1 to number. Each value should be space-padded to match the width
    of the binary value of number and the values should be separated by a single space.
    Args:
        number: int
    Returns:
    """

    width = len(bin(number)[2:])
    for num in range(1, number + 1):
        print(f'{num:{width}d} {num:{width}o} {num:{width}X} {num:{width}b}')


formatted_number(17)
