import datetime


def birthday_time():
    """
    Function to calculate how many days are left to/passed from one's birthday.
    Returns:
        bday_days: <class 'datetime.timedelta'>
    """
    # ask user to enter their birth month and day number
    bday_month_day = list(map(int, input("Enter your birthday Month and Day. E.g. 8 12:\t").split()))

    # get the single values for the month and day
    bday_month, bday_day = bday_month_day

    # get today's date
    current_day = datetime.date.today()

    # get current year
    current_year = current_day.year

    # convert given data to birthday date
    bday = datetime.date(current_year, bday_month, bday_day)

    # day difference
    remainder_days = bday - current_day

    # f"Today: {current_day}\nBirthday: {bday}"
    return f"Your birthday is {remainder_days.days} days away."


# print(birthday_time())


def get_future_date(num_days):
    """
    Function to calculate a future point in time.
    Args:
        num_days: <int>

    Returns:
        fut_date: <class 'datetime.timedelta'>
    """

    day_today = datetime.datetime.now()

    fut_date = day_today + datetime.timedelta(days=num_days)

    return f"The date after {num_days} days will be {fut_date.date()}"


print(get_future_date(75))


def get_past_date(num_days):
    """
    Function to calculate the date num_days ago.
    Args:
        num_days: <int>

    Returns:
        past_date: <class 'datetime.timedelta'>
    """

    date_today = datetime.date.today()

    past_date = date_today - datetime.timedelta(days=num_days)

    return f"The date {num_days} days ago was {past_date}"


print(get_past_date(75))
