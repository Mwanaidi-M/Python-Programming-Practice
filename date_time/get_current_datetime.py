import datetime


def get_now():
    """
    Function to retrieve the current date and time.
    Returns:
        curr_datetime: <str>
    """

    curr_datetime = datetime.datetime.now().strftime("%b %d %Y \n%H:%M:%S %p")

    return curr_datetime


print(get_now())
