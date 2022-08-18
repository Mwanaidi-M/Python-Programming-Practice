def zero_fuel(distance_to_pump, mpg, fuel_left):
    """
    You were camping with your friends far away from home, but when it's time to go back,
    you realize that your fuel is running out and the nearest pump is 50 miles away! You
    know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.

    Considering these factors, this function tells you if it is possible to get to the pump or not.

    Function should return true if it is possible and false if not.
    Args:
        distance_to_pump: <int>
        mpg: <int>
        fuel_left: <int>

    Returns:
        <bool>
    """
    # get the general distance based on given fuel and miles per gallon
    dist = fuel_left * mpg

    # check if the given distance_to_pum is less than or equal to general distance; return True else False
    return True if distance_to_pump <= dist else False
