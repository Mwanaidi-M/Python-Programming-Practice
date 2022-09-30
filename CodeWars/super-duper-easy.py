def problem(a):
    """
    Make a function that returns the value multiplied by 50 and increased by 6.
    If the value entered is a string it should return "Error".
    """
    try:
        msg = int(a * 50 + 6)

    except Exception as exc:
        msg = "Error"

    return msg

    # ALTERNATIVE METHOD
    # return "Error" if a == str(a) else a * 50 + 6


print(problem(1.2))
