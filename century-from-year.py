
def solution(year):
    """
    Given a year, return the century it is in. The first century spans from the year 1 up
    to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

    Example:
    For year = 1905, the output should be solution(year) = 20
    For year = 1700, the output should be solution(year) = 17

    """
    # check if the year is divisible by 100 and return the floor division result
    if year % 100 == 0:
        century = year // 100

    # otherwise, add 1 to the floor division value
    else:
        century = (year // 100) + 1

    return century
