def words_reverse(string):
    """
    Complete the function that accepts a string parameter, and reverses each word in the string.
    All spaces in the string should be retained.

    Examples
    "This is an example!" ==> "sihT si na !elpmaxe"
    "double  spaces"      ==> "elbuod  secaps"
    Args:
        string: str

    Returns: str
    """

    arr_str = [st[::-1] for st in string.split(' ')]

    return ' '.join(arr_str)


print(words_reverse("This is an example!"))
print(words_reverse("double  spaces"))
