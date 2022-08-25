# The calendar module allows you to output calendars and provides additional useful functions for them.
import calendar


def find_day():
    """
    You are given a date, a single line of input containing the space separated month, day and year,
    respectively, in MM DD YY format. Your task is to find what the day is on that date.
    Output the correct day in capital letters.

    Returns:
    actual_day: <str>

    """

    # get date from user in one line separated by space
    user_date = list(map(int, input().split(' ')))

    # set the variables for month, day, name
    month, day, year = user_date

    # get the list of days from calendar.day_name
    list_days = list(calendar.day_name)

    # get the day number from the given input
    day_number = calendar.weekday(year, month, day)

    # use day_number as index position from the list_days then convert it to upper_case
    actual_day = list_days[day_number].upper()

    print(actual_day)


find_day()