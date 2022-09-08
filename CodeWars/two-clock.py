def past(h, m, s):
    """
    Clock shows h hours, m minutes and s seconds after midnight.
    Your task is to write a function which returns the time since midnight in milliseconds.
    Example:
    h = 0
    m = 1
    s = 1
    result = 61000
    """
    milsec = 0

    # convert hours to seconds
    h = h * 3600
    # convert minutes to seconds
    m = m * 60
    # add the seconds then multiply by 1000
    milsec = (h + m + s) * 1000

    return milsec


print(past(0, 1, 1))
