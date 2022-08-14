def swap_case():
    """given a string, your task is to swap cases. i.e convert all lowercase letters to uppercase letters and vice versa.


    Returns:
        str: string input from the user.
    """
    # take input from the user
    txt = input('Your string:\t')

    # python string has a swapcase() method to convert lowercase letters to uppercase letters and vice versa
    return txt.swapcase()


print(swap_case())
