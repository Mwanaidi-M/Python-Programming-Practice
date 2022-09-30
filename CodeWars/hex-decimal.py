def hex_to_dec(s):
    """
    Complete the function which converts hex number (given as a string) to a decimal number.
    """

    # convert the hex value by passing it into the int function with the base value (16) as the 2nd argument.
    decimal_val = int(s, 16)
    return decimal_val
