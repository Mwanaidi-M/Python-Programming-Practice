def to_alternating_case(string):
    """
    Function that transforms each lowercase letter to uppercase and each uppercase letter to lowercase.
    Args:
        string: <str>
    Returns:
        alt_string: <str>
    """

    print(string.swapcase())


to_alternating_case("hello world")
to_alternating_case("HeLLo WoRLD")
